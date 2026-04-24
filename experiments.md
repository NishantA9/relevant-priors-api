# Experiments

## Baseline
I started with a keyword overlap baseline between the current study description and prior study descriptions.

## Improved Rule-Based Approach
I normalized common abbreviations and compared important radiology terms such as modality and body region.

## What Worked
Matching anatomy/body region helped identify relevant prior studies even when the exact wording was different.

## What Failed
Exact string matching was too strict because radiology descriptions often use different wording for related exams.

## Next Improvements
I would improve the anatomy dictionary, tune thresholds using the public evaluation JSON, and train a lightweight classifier if more time were available.