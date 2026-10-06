# Executive Summary: Retail Growth Analytics

## Decision

Prioritize retention among high-value, identifiable customers; test reactivation among less-recent frequent buyers; and improve customer-ID capture before relying on customer-level reporting. Reconcile cancellation-marked invoices with the underlying business process before treating them as cancelled orders.

## What the data shows

The analysis covers a single UK-based online retailer from December 2009 to December 2011. Comparing the same complete January–November months, positive line sales rose from **£9.01M in 2010 to £9.18M in 2011 (+1.9%)**, while non-cancellation invoice IDs fell from **18,435 to 17,582 (-4.6%)**. Mean invoice value increased from £489 to £522; median invoice value moved from £301 to £305.

Among **5,878 identified customers** with at least one eligible invoice, **4,255 (72.4%)** placed two or more. The RFM Champions segment includes **647 customers (11.0%)** and accounts for **£9.33M (53.7%)** of identified positive sales. The quartile-based At risk segment includes **888 customers (15.1%)** and has **£2.18M** in historical positive sales. This historical amount is not recoverable revenue or a forecast.

Geography is highly concentrated: the UK contributes **£17.41M (85.0%)** of £20.48M positive sales. Meanwhile, **235,151 loaded rows (22.8%)** have no customer ID and account for **£3.10M (15.1%)** in positive sales. Customer analysis therefore describes an incomplete, revenue-weighted subset.

There are **8,292 cancellation-marked invoice IDs among 53,628 distinct IDs (15.5%)**. The marker may represent cancellation, return, partial reversal, or another credit event. It should be reconciled to source transactions before it is interpreted as a whole-order cancellation rate.

## Recommended tests

1. **Retention:** test a service or retention treatment with a holdout among high-value customers; compare incremental repeat-invoice rate and contribution margin.
2. **Reactivation:** test a targeted message or offer among less-recent, frequent customers against a randomized holdout. Do not use historical segment sales as expected uplift.
3. **Attribution:** investigate when customer IDs are missing; retain anonymous sales in topline reporting and exclude them only from customer-level measures.
4. **Market evaluation:** keep the UK core in view and compare candidate markets on customer count, repeat rate, invoice value, fulfilment cost, and margin before expansion decisions.
5. **Cancellation reconciliation:** sample `C` invoice IDs and classify full cancellations, partial reversals, returns, and other credits.

## Interpretation limits

This is descriptive analysis of one historical retailer, not a causal study or a current market forecast. Positive sales are gross line sales, not profit or margin. Invoice IDs are not guaranteed to represent distinct checkout orders. RFM labels are dataset-relative prioritization heuristics, not predictions. Full definitions and methods are in [findings.md](findings.md), with calculations in the [analysis notebook](../notebooks/01_retail_growth_analysis.ipynb).
