-- Monthly fulfilled-order sales. Excludes cancellation invoices and non-positive
-- quantities/prices; revenue is line-level quantity * unit price in GBP.
SELECT
    strftime('%Y-%m', invoice_date) AS sales_month,
    ROUND(SUM(quantity * unit_price), 2) AS gross_sales_gbp,
    COUNT(DISTINCT invoice_no) AS invoices,
    COUNT(DISTINCT customer_id) AS customers
FROM transactions
WHERE is_cancellation = 0
  AND quantity > 0
  AND unit_price > 0
GROUP BY sales_month
ORDER BY sales_month;
