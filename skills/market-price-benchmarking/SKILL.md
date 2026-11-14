---
name: "market-price-benchmarking"
description: "Benchmark fair market price and buy timing before negotiating."
license: "MIT"
---

# Market-Price Benchmarking

You can't spot a deal without knowing the going rate.

## 1. Establish the going rate
- Gather recent comparable prices before judging any listing; anchor to data, not the seller's number.
- Know the range: what's cheap, fair and overpriced for this exact item.

## 2. Comparable, or not comparable

Include a price as a comparable only when all four hold:
- **Item:** same model, variant and spec. A bigger capacity, a later revision or a bundled extra is a different item until you price the difference explicitly.
- **Condition:** the band is stated (new, used-graded, for parts), not inferred from the photo.
- **Recency:** sold inside a stated window, default 90 days. Record the date of every point.
- **Market:** same country and currency as the buyer, or a conversion with its date stated.

Record every excluded listing with its reason. Unsold asking prices are not comparables: they measure the seller's hope, not the clearing price.

## 3. Normalise to landed cost
- Convert each point to the buyer's landed cost: price + tax + shipping + fees + mandatory extras, in one currency with the FX date stated.
- Adjust for condition with an explicit rule (a stated percentage, or a paired new/used point) and name the rule. Keep the raw price beside the adjusted one so the adjustment is auditable.

## 4. Aggregate robustly
- Report count, median and spread. At five comparables or more, report the interquartile range; below five, report the median and the full min-max and say so.
- Read the spread as the fair band: where quartiles are reported, below the 25th is cheap and above the 75th is overpriced; with a min-max, only points inside the range are normal. One outlier must not move the median.
- Fewer than three comparables is insufficient evidence, not a benchmark.

## 5. Worked example

Item: used 2021 road bike, buyer in the UK, GBP, 90-day window.

| # | Point | Raw | Landed | Included? |
|---|---|---|---|---|
| 1 | sold, same model, used-good, Leeds, 3 weeks ago | 850 | 850 | yes |
| 2 | sold, same model, used-good, Bristol, 6 weeks ago | 900 | 900 | yes |
| 3 | sold, same model, used-excellent, London, 2 weeks ago | 1,100 | 990 | yes, condition rule: -10% to used-good |
| 4 | sold, same model, for-parts, 5 weeks ago | 300 | 300 | no, condition band |
| 5 | live listing, same model, unsold | 1,450 | 1,450 | no, asking price |
| 6 | sold, 2023 model, Manchester | 1,600 | 1,600 | no, different item |
| 7 | sold, same model, Berlin, 4 weeks ago | 800 EUR | no GBP conversion date recorded | no, other market, no FX date |

Benchmark: n=3, median 900, range 850-990 (under five points, so min-max is reported).

Judgement against it: a listing at 950 sits inside the band, so fair. A listing at 1,450 is 61% above the median and matches an asking price, so overpriced and not evidence of value. A listing materially below the lowest comparable with no stated fault is a scam signal to check, not a bargain.

Insufficient-evidence outcome: drop point 1 and only 900 and 990 remain. n=2, so the output is "insufficient evidence: two comparables, widen the window or the region before judging", not a price.

## 6. Time the buy
- Prices move with season, cycle and release timing; buy when the curve favours you if you can wait.
- A patient buyer beats an urgent one on price.

## 7. Judge the listing against the benchmark
- Flag both overpriced and suspiciously-cheap (scam signal) against the benchmark.

## 8. Accept or reject

- Accept a benchmark only when it names the item, condition band, window, market, count, median and spread, and lists every excluded point with its reason.
- Reject any judgement built on asking prices, on a single point, or on another market without a stated conversion and date.
- Reject a recommendation that does not name what would change it (window, region, condition rule).

## Voice
Benchmark-first. Refuse calling something a deal without a comparable-price reference.
