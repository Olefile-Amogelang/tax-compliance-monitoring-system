# Tax Compliance Monitoring System

## Overview
This project simulates a tax compliance monitoring system used to identify underreporting and assess taxpayer risk using automated data pipelines.

## Features
- Data ingestion from multiple sources
- Compliance checks (late filing & underreporting detection)
- Risk scoring system
- Data storage using SQLite
- Interactive dashboard using Streamlit

## Tech Stack
- Python
- Pandas
- SQLite
- Streamlit

## Use Case
This system demonstrates how revenue authorities can leverage data engineering and analytics to monitor compliance, detect anomalies, and improve decision-making.

## How to Run

```bash
pip install -r requirements.txt
python run_pipeline.py
python -m streamlit run dashboard/app.py
