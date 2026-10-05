# Retail Growth: Findings and First Actions

**Decision:** Which customers and markets should a small online retailer prioritize to grow repeat revenue, and what cancellation activity should it investigate?

## Readout

Prioritize retention among high-value, identifiable customers, and treat the quieter high-frequency group as a reactivation test. The UK is the clear core market in this dataset. Before acting on either customer or cancellation patterns, improve customer-ID coverage and verify what a `C` invoice represents in the business process.

## Evidence

- **Sales rose slightly while invoice volume fell.** Comparing the same complete January–November periods, positive sales increased from **£9.01M in 2010 to £9.18M in 2011 (+1.9%)**, while non-cancellation invoice count fell from **18,435 to 17,582 (-4.6%)**. Mean positive sales per invoice increased from **£489 to £522**; median invoice value increased much less, from **£301 to £305**. The gap between mean and median makes larger invoices a plausible contributor; this comparison does not identify why invoice volume changed.
- **A small high-value segment accounts for over half of identified sales.** The RFM “Champions” group contains **647 customers (11.0% of the 5,878 identified customers)** and represents **£9.33M (53.7%)** of their positive sales. The group’s median is 16 eligible invoices and 8 days since its latest purchase as of the snapshot on 10 December 2011.
- **A reactivation test has a defined target.** The quartile-based “At risk” group contains **888 customers (15.1%)**, with **£2.18M (12.6%)** in historical positive sales, a median of 5 eligible invoices, and median recency of 243.5 days. The £2.18M is past sales, not recoverable revenue or a forecast.
- **Sales are concentrated in the UK.** The UK accounts for **£17.41M (85.0%)** of **£20.48M** in positive, non-cancellation line sales. Country sales alone are an unsafe expansion score: EIRE’s £659k comes from 5 identified customers, consistent with a small number of high-volume accounts.
- **Customer attribution is incomplete.** **235,151 of 1,033,036 loaded rows (22.8%)** have no customer ID. Those rows represent **£3.10M (15.1%)** of positive sales, so customer and cohort results cover an incomplete but revenue-weighted portion of transactions.
- **Cancellation markers need operational interpretation.** **8,292 of 53,628 distinct invoice IDs (15.5%)** begin with `C`. The monthly share ranges from 12.2% to 18.4% in months with more than 100 invoice IDs. These are source-flagged cancellation/credit invoices divided by all invoice IDs, not a verified rate of complete customer orders being cancelled.

## What to do next

1. **Test reactivation with a holdout.** If a current customer file has comparable RFM signals, test a small message or offer against a randomized holdout among high-frequency, less-recent customers. Compare incremental repeat-invoice rate and contribution margin over a fixed window; do not treat the historical £2.18M as expected uplift.
2. **Protect the high-value base.** Review service and retention options for the Champions segment, with a holdout or phased rollout to measure incremental value and cost. The concentration makes retention important, and it also makes results sensitive to a few large buyers.
3. **Fix the attribution gap.** Trace when customer IDs are absent and whether the gap can be reduced in current transaction capture. Keep anonymous sales in overall sales reporting; exclude them only from customer-level measures.
4. **Keep the UK core stable while testing expansion.** If international growth is a live priority, compare customer count, repeat rate, invoice value, fulfilment cost, and margin for candidate markets. The current data shows sales concentration, not market-level profitability.
5. **Reconcile `C` invoices to source transactions.** Check whether each marker is a full cancellation, a partial line reversal, a return, or another credit event before changing operations.

## Scope and method

Source: [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii), a historical dataset from one UK-based online retailer covering 1 December 2009 through 9 December 2011. The UCI description notes that many customers are wholesalers. The dataset is distributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); attribution: Chen, D. (2012), DOI [10.24432/C5CG6D](https://doi.org/10.24432/C5CG6D).

The source workbook had 1,067,371 rows. Preparation removed 34,335 exact duplicate rows and retained rows with missing customer IDs. Positive sales equal `quantity * unit_price` for non-cancellation rows where quantity and price are both positive; values are GBP. This is a gross line-sales measure, not profit or margin. Invoice count refers to distinct invoice IDs, not confirmed checkout orders.

RFM uses identified customers with at least one eligible invoice. Recency is measured against 10 December 2011; frequency is distinct eligible invoice count; monetary value is positive line sales. Scores use dataset-relative quartiles, with lower recency days scored higher. “Champions” have R, F, and M scores of at least 4; “At risk” have R at most 2 and F at least 3. Names are prioritization heuristics, not validated behavioral states or predictions.

The comparison uses January–November in 2010 and 2011 because December 2011 is only observed through the 9th. This is a one-retailer observational dataset, so the analysis supports historical description and test design, not causal claims or current market forecasts. The executed calculations and plots are in [the analysis notebook](../notebooks/01_retail_growth_analysis.ipynb); data preparation and reusable queries are in [`src/`](../src/) and [`sql/`](../sql/).
