-- Share of invoice IDs marked as cancellations by month. This is a diagnostic
-- for cancellation/credit activity, not proof a complete customer order failed.
SELECT
    strftime('%Y-%m', invoice_date) AS sales_month,
    COUNT(DISTINCT CASE WHEN is_cancellation = 0 THEN invoice_no END) AS non_cancellation_invoices,
    COUNT(DISTINCT CASE WHEN is_cancellation = 1 THEN invoice_no END) AS cancellation_invoices,
    ROUND(1.0 * COUNT(DISTINCT CASE WHEN is_cancellation = 1 THEN invoice_no END)
      / NULLIF(COUNT(DISTINCT invoice_no), 0), 4) AS cancellation_share_of_invoices
FROM transactions
GROUP BY sales_month
ORDER BY sales_month;
