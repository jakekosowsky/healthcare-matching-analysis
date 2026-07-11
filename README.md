# Improving Access to Mental-Health Care

A personal analytics project about a practical access problem: after someone asks for mental-health support, what helps them successfully connect with a provider and reach a first session?

The analysis follows the matching funnel from request to provider acceptance to completed care. It examines where people fall out of that process and how the experience differs across session preferences, acquisition channels, and time.

## Questions explored

- Where is the largest drop in the request-to-session funnel?
- Do video and in-person requests produce different outcomes?
- Did match-to-session conversion change materially over the six-month analysis period?
- Which acquisition channels were associated with successful first sessions?

## Quick answers

**The largest loss occurred after provider acceptance.** Across 47,664 client requests, 75.2% received an acceptance but only 11.8% reached a first session. Among accepted requests, 15.5% ultimately reached a session. The main access problem in this sample was therefore not simply getting a provider to accept—it was converting that acceptance into completed care.

**Video requests converted much more often than in-person requests.** A first session occurred for 16.3% of video requests versus 5.5% of in-person requests. The difference remained after acceptance: 20.0% of accepted video requests reached a session, compared with 8.5% of accepted in-person requests. Video requests also had a higher acceptance rate, 80.7% versus 63.8%.

**Session conversion was relatively stable from July through December 2021.** Monthly request-to-session conversion stayed between 10.7% and 12.6%, even as monthly request volume ranged from roughly 6,400 to 10,000. Acceptance improved to 81.1% in December, but that increase did not produce a comparable jump in completed sessions.

**Partnership and provider-originated requests converted at higher observed rates, but the comparison is directional.** Partnership requests reached a session 40.5% of the time and provider-originated requests 20.6%, versus 11.7% for direct-to-consumer requests. Those two higher-performing groups contained only 121 and 107 requests, compared with more than 47,000 direct-to-consumer requests, so the gap should not be treated as a definitive causal result.

## Repository structure

```text
src/
  build_funnel.py              client-level funnel construction
analysis/
  conversion_over_time.py      monthly access and conversion trends
  session_preferences.py       video and in-person comparisons
  acquisition_channels.py      source-level conversion analysis
  provider_capacity.py         provider-level exploratory diagnostics
notebooks/
  matching_analysis.ipynb
```

## Privacy

No client- or provider-level source data is published. The repository shows the analytical logic and aggregate findings without exposing the underlying records. Results describe this dataset and should not be interpreted as causal estimates.

## Tools

Python · pandas · NumPy · Matplotlib · funnel analysis · cohort analysis
