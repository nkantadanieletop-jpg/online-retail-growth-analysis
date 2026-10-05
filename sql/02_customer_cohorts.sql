-- Customer first eligible invoice month and subsequent monthly invoice activity.
WITH valid_invoices AS (
    SELECT customer_id, invoice_no, date(invoice_date, 'start of month') AS invoice_month
    FROM transactions
    WHERE customer_id IS NOT NULL
      AND is_cancellation = 0
      AND quantity > 0
      AND unit_price > 0
    GROUP BY customer_id, invoice_no, invoice_month
), first_purchase AS (
    SELECT customer_id, MIN(invoice_month) AS cohort_month
    FROM valid_invoices
    GROUP BY customer_id
)
SELECT
    f.cohort_month,
    o.invoice_month,
    (CAST(strftime('%Y', o.invoice_month) AS INTEGER) - CAST(strftime('%Y', f.cohort_month) AS INTEGER)) * 12
      + CAST(strftime('%m', o.invoice_month) AS INTEGER) - CAST(strftime('%m', f.cohort_month) AS INTEGER) AS months_since_first_invoice,
    COUNT(DISTINCT o.customer_id) AS active_customers
FROM valid_invoices o
JOIN first_purchase f USING (customer_id)
GROUP BY f.cohort_month, o.invoice_month
ORDER BY f.cohort_month, o.invoice_month;
