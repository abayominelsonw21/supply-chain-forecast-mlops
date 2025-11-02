Supply Chain Demand Forecast (In-Progress)
📦 Supply Chain Inventory Demand Forecast (MLOps Project)
🎯 Project Status: Week 1 - Data Engineering Foundation COMPLETE
This project demonstrates the ability to build a production-ready MLOps pipeline designed to forecast retail demand, minimizing inventory risks for a multi-location business.

🛠️ Architecture & Technology Stack (The MLOps Standard)
This project is built using a modern, scalable, and 100% free/open-source stack, showcasing modular software engineering principles.
Component	Tool / Technology	Role in Project
Orchestration	Apache Airflow (Local via Docker)	Schedules daily data processing and automated model retraining tasks.
Data Versioning	DVC (Data Version Control)	Tracks all raw and processed data files (e.g., the 421k sales records) outside of Git.
Data Processing	Python (Pandas)	Performs ETL (Extract, Transform, Load) and high-speed feature engineering.
Experiment Tracking	MLflow	Will be used in Week 2 to log, compare, and register model artifacts.
Model Serving	FastAPI + Docker	Will serve the final forecast predictions via a low-latency API.

📈 Data Engineering Deliverable (Week 1)
Goal: Create a singular, cleaned, and enriched feature table ready for direct model consumption.

1. Data Source & Ingestion
Source: Walmart Recruiting - Store Sales Forecasting (Kaggle Competition Data).

Method: Raw data files (train.csv, features.csv, stores.csv) were merged via Pandas Left Join on the common keys (Store, Date, IsHoliday).

Result: A master DataFrame containing 421,570 records was created.

2. Feature Engineering Highlights (DS Skill)
All features have been calculated and saved to the processed layer:

✅ Time-Series Features: Calculated Lag-1, Lag-4, and 4-Week Rolling Mean of Weekly_Sales (crucial for accurate forecasting).

✅ Contextual Features: Handled missing promotional data by imputing NaNs with 0 (MarkDown1-5) and created One-Hot Encoding for Store Type (A, B, C).

✅ Data Integrity: The raw and processed data versions are fully tracked by DVC.


➡️ Next Steps (Week 2 Focus)
The upcoming sprint focuses on turning this data artifact into a deployed AI system:

Modeling: Train and register the final XGBoost/Prophet model using MLflow.

Deployment: Write the Dockerfile and Airflow DAG to automate the training/serving workflow.

Visualization: Build the Streamlit dashboard front-end.
