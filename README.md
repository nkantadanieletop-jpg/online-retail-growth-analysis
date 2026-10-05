# Online Retail Growth Analysis

**Business question:** Which customer groups and markets should a small online retailer prioritize to grow repeat revenue, and what should it investigate about cancellation activity?

This portfolio project uses real, two-year transaction data to examine sales trends, repeat purchasing, customer cohorts, RFM segments, geographic concentration, and cancellation invoices. The work is designed to end with practical priorities a commercial team could test, backed by reproducible Python and SQL.

## Dataset

The [UCI Online Retail II dataset](https://archive.ics.uci.edu/dataset/502/online+retail+ii) contains 1,067,371 transaction lines from a UK-based non-store retailer between December 2009 and December 2011. It includes invoice, product, quantity, timestamp, unit price, customer ID, and country. The preparation step removed 34,335 exact duplicate rows and loaded 1,033,036 rows. Rows missing invoice, timestamp, quantity, or price are counted and reported by the script; missing customer IDs are retained for sales totals but excluded from customer analysis. Invoice numbers beginning with `C` identify cancellation activity. The dataset is available under CC BY 4.0; attribution: Chen, D. (2012), *Online Retail II*, UCI Machine Learning Repository, DOI: 10.24432/C5CG6D.

## Questions and measures

- How do fulfilled-order sales and order counts change over time?
- What share of identifiable customers place another order, and how quickly?
- Which acquisition-month cohorts remain active in later months?
- How concentrated are sales across countries and products?
- How does the share of invoice IDs flagged as cancellations vary by month?

Sales use positive-quantity, positive-price lines on non-cancellation invoices. The cancellation metric counts distinct invoice IDs beginning with `C`, divided by all distinct invoice IDs in the month; it is a diagnostic for cancellation or credit activity, not proof that a complete customer order was cancelled. Customer retention only includes rows with an identified customer ID. These definitions avoid treating anonymous transactions as known customers; they do not establish why a customer returned or why cancellation activity occurred.

## Set up

Requires Python 3.12 and Windows PowerShell. Because this workspace has a long path, keep the virtual environment in a short path under your Documents\Codex folder:

```powershell
$venv = Join-Path $env:USERPROFILE 'Documents\Codex\venvs\retail-growth'
New-Item -ItemType Directory -Force -Path (Split-Path $venv) | Out-Null
python -m venv $venv
& "$venv\Scripts\python.exe" -m pip install -r requirements.txt
```

Download `online_retail_II.xlsx` from the UCI dataset page above and place it in `data/raw/`. The source data is not committed to the repository. Then prepare the SQLite database and open the notebook:

```powershell
& "$venv\Scripts\python.exe" src/prepare_data.py
& "$venv\Scripts\python.exe" -m jupyterlab
```

Open `notebooks/01_retail_growth_analysis.ipynb`. The SQL files in `sql/` can be run against `data/processed/retail.db` using SQLite; Python's standard library includes the SQLite driver.

## Repository map

```text
data/raw/             Downloaded source file (ignored by Git)
data/processed/       Generated SQLite database (ignored by Git)
notebooks/            Analysis and charts
reports/              Final findings and figures
sql/                  Reusable business queries
src/                  Reproducible data preparation
```

## Findings so far

See [the findings note](reports/findings.md) for the period comparison, customer segments, commercial implications, and limitations. The executed notebook retains the underlying tables and charts.
