# Empirical Socio-Technical Analysis of Real-World AI Incidents

## Overview
This repository contains an end-to-end data processing and empirical research pipeline that categorizes real-world AI failures using the **Human-Technology-Organization (HTO) Socio-Technical Framework**.

Using raw data from the **AI Incident Database (AIID)**, this project extracts, tags, and evaluates 1,607 documented incident records to understand why AI implementations fail in practice.

---

## Empirical Findings (N = 1,607)

| Socio-Technical Dimension | Incident Count | Percentage | Primary Indicators |
| :--- | :--- | :--- | :--- |
| **Human Oversight / Trust Breakdown** | **1,189** | **74.0%** | Operator error, automation bias, user mistrust, lack of training |
| **System Reliability / Technical Deficit** | **707** | **44.0%** | Model hallucinations, data leaks, system bugs, integration failures |
| **Governance / Organizational Deficit** | **436** | **27.1%** | Compliance non-conformance, shadow AI, missing corporate policy |
| **Cross-Dimensional Overlap** | **698** | **43.4%** | Incidents spanning 2 or more HTO dimensions simultaneously |

![HTO Distribution Chart](data/processed/hto_distribution_chart.png)

---

## Core Insight
While technical performance is often blamed for AI failure, empirical evidence shows that **74.0% of real-world AI incidents involve human factors and workflow integration failures**. Furthermore, 43.4% of breakdowns are multi-dimensional, requiring holistic socio-technical governance rather than simple model re-training.

---

## Macro Longitudinal Trends (OECD AIM Dataset: 2020–2026)

In addition to the qualitative HTO breakdown, a macro longitudinal analysis was conducted on the **OECD AI Incidents and Hazards Monitor (AIM)** dataset ($N = 16,737$ incidents across 79 months).

| Metric | 2020 Baseline | 2025 Peak | 2026 Trajectory (Jan–Jul) | Overall Shift |
| :--- | :--- | :--- | :--- | :--- |
| **Annual Incidents** | 900 | 4,571 | 4,030 (7 months) | **5.0x increase** |
| **Avg. Monthly Incidents** | 75.0 / month | 380.9 / month | 575.7 / month | **7.7x surge** |
| **Incident Rate per 1k AI Events** | 27.65 | 25.85 | 26.84 | **Stable proportion** |

![OECD Longitudinal Trends](data/processed/oecd_longitudinal_trends.png)

### Key Takeaways
1. **Accelerating Failure Frequency:** Monthly AI incident reports expanded 7.67x between 2020 and 2026, demonstrating that risk exposure scales alongside adoption velocity.
2. **Linear Growth Rate:** The constant incident intensity rate (~26 incidents per 1,000 AI news events) indicates that failure occurrence is systematically tied to deployment scale, reinforcing the necessity of automated socio-technical governance frameworks.

link - https://oecd.ai/en/incidents?search_terms=%5B%5D&and_condition=false&from_date=1900-08-11&to_date=2026-08-11&properties_config=%7B%22principles%22:%5B%5D,%22industries%22:%5B%5D,%22harm_types%22:%5B%5D,%22harm_levels%22:%5B%5D,%22harmed_entities%22:%5B%5D,%22business_functions%22:%5B%5D,%22ai_tasks%22:%5B%5D,%22autonomy_levels%22:%5B%5D,%22languages%22:%5B%5D%7D&order_by=date&num_results=20

---

## Repository Structure

```text
├── data/
│   ├── raw/                 <-- Raw AIID snapshot export (.xlsx)
│   └── processed/           <-- Tagged dataset (.csv) & generated chart (.png)
├── 01_ingest_incidents.py   <-- API data fetching script
├── 02_parse_and_code.py      <-- HTO categorization pipeline
└── 03_analyze_data.py       <-- Statistical evaluation & chart generation


## Getting Started

### Prerequisites
Clone this repository and ensure Python 3.9+ is installed. Install the required dependencies:

```bash
pip install pandas openpyxl matplotlib requests

## Execution Pipeline

1. Setup Data: Ensure the raw Excel export (AIID__Excel__Export-20260803.xlsx) is placed inside data/raw/ (or run python 01_ingest_incidents.py to fetch data via API).

link - https://incidentdatabase.ai/research/snapshots/

2. Process & Tag Dataset: Run the HTO classification pipeline to parse raw incident text and assign socio-technical tags: python 02_parse_and_code.py

3. Generate Analytics & Charts: Compute statistical distributions and output the visualization: python 03_analyze_data.py

4. Outputs will be saved directly to data/processed/ai_incidents_tagged.csv and data/processed/hto_distribution_chart.png.

--------------------------------------------------------

