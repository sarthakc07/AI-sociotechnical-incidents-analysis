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

2. Process & Tag Dataset: Run the HTO classification pipeline to parse raw incident text and assign socio-technical tags: python 02_parse_and_code.py

3. Generate Analytics & Charts: Compute statistical distributions and output the visualization: python 03_analyze_data.py

4. Outputs will be saved directly to data/processed/ai_incidents_tagged.csv and data/processed/hto_distribution_chart.png.
