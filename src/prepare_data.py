"""Validate UCI Online Retail II data and load transaction rows into SQLite."""
from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "online_retail_II.xlsx"
DB = ROOT / "data" / "processed" / "retail.db"

RENAME = {
    "Invoice": "invoice_no", "StockCode": "stock_code", "Description": "description",
    "Quantity": "quantity", "InvoiceDate": "invoice_date", "Price": "unit_price",
    "Customer ID": "customer_id", "Country": "country",
}

def main():
    if not SOURCE.exists():
        raise FileNotFoundError(f"Download the UCI source file to {SOURCE}")
    frames = pd.read_excel(SOURCE, sheet_name=None, engine="openpyxl")
    data = pd.concat(frames.values(), ignore_index=True).rename(columns=RENAME)
    required = set(RENAME.values())
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Unexpected source schema; missing columns: {sorted(missing)}")

    data["invoice_no"] = data["invoice_no"].astype("string").str.strip()
    data["invoice_date"] = pd.to_datetime(data["invoice_date"], errors="coerce")
    data["customer_id"] = pd.to_numeric(data["customer_id"], errors="coerce").astype("Int64")
    data["quantity"] = pd.to_numeric(data["quantity"], errors="coerce")
    data["unit_price"] = pd.to_numeric(data["unit_price"], errors="coerce")
    data["is_cancellation"] = data["invoice_no"].str.upper().str.startswith("C", na=False).astype("int8")
    data["line_value_gbp"] = data["quantity"] * data["unit_price"]

    raw_rows = len(data)
    missing_transaction_rows = int(data[["invoice_no", "invoice_date", "quantity", "unit_price"]].isna().any(axis=1).sum())
    data = data.dropna(subset=["invoice_no", "invoice_date", "quantity", "unit_price"])
    exact_duplicate_rows = int(data.duplicated().sum())
    data = data.drop_duplicates()
    DB.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB) as conn:
        data.to_sql("transactions", conn, if_exists="replace", index=False, chunksize=50_000)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_invoice_date ON transactions(invoice_date)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_customer ON transactions(customer_id)")
    print(f"Raw rows: {raw_rows:,}; rows loaded: {len(data):,}")
    print(f"Rows removed for missing transaction fields: {missing_transaction_rows:,}; exact duplicate rows removed: {exact_duplicate_rows:,}")
    print(f"Date range: {data.invoice_date.min()} to {data.invoice_date.max()}")
    print(f"Customers with IDs: {data.customer_id.nunique():,}; countries: {data.country.nunique():,}")
    print(f"SQLite database: {DB}")

if __name__ == "__main__":
    main()
