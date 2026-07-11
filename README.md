# Improving Access to Mental-Health Care

A personal analytics project about a practical access problem: after someone asks for mental-health support, what helps them successfully connect with a provider and reach a first session?

The analysis follows the matching funnel from request to provider acceptance to completed care. It examines where people fall out of that process and how the experience differs across service preferences, acquisition channels, provider characteristics, and provider capacity.

## Questions explored

- How does match-to-session conversion change over time?
- Do people seeking video and in-person care experience different outcomes?
- Which referral or acquisition channels lead to successful first sessions?
- How do provider qualifications relate to conversion?
- Does growing provider workload make a successful match less likely?
- Where can the matching process be improved so more people receive care?

## Repository structure

```text
src/
  build_funnel.py              client-level funnel construction
analysis/
  conversion_over_time.py      monthly access and conversion trends
  session_preferences.py       video and in-person comparisons
  acquisition_channels.py      source-level conversion analysis
  provider_capacity.py         workload and provider diagnostics
notebooks/
  matching_analysis.ipynb
```

## Privacy

No client- or provider-level source data is published. The repository shows the analytical logic and reporting structure without exposing the underlying records.

## Tools

Python · pandas · NumPy · Matplotlib · funnel analysis · cohort analysis
