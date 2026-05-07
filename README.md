# ETL with Airflow 🚀

## Author
- **Name:** Mamadou Korka Diallo
- **GitHub:** SedarKorka
- **Date:** May 2026
- **Course:** Hands-On Introduction to Data Engineering - LinkedIn Learning

---

## Description
This project implements a complete ETL pipeline using Apache Airflow.
The goal is to automate the process of collecting, cleaning, and storing data from external sources.

---

## Technologies Used
| Technology | Version |
|---|---|
| Python | 3.12.1 |
| Apache Airflow | 2.9.2 |
| Pandas | Latest |
| SQLite | Built-in |
| GitHub Codespaces | Latest |

---

## Project Structure

    ETL-with-Airflow/
    ├── airflow/
    │   ├── dags/
    │   │   ├── one_task_dag.py
    │   │   ├── two_task_dag.py
    │   │   ├── extract_dag.py
    │   │   ├── transform_dag.py
    │   │   ├── load_dag.py
    │   │   ├── basic_etl_dag.py
    │   │   └── challenge_dag.py
    │   ├── airflow.cfg
    │   └── webserver_config.py
    ├── lab/
    │   ├── manual/
    │   ├── orchestrated/
    │   ├── end-to-end/
    │   └── challenge/
    └── README.md

---

## DAGs Description

### 1. one_task_dag
- First simple DAG
- Creates a text file with "Hello LinkedIn Learning"

### 2. two_task_dag
- DAG with 2 dependent tasks
- T0 >> T1

### 3. extract_dag
- Downloads domain list from IANA
- Uses BashOperator + wget

### 4. transform_dag
- Cleans data and adds date column
- Uses PythonOperator + Pandas

### 5. load_dag
- Loads data into SQLite database
- Uses BashOperator + sqlite3

### 6. basic_etl_dag
- Complete ETL pipeline
- extract_task >> transform_task >> load_task

### 7. challenge_dag
- S&P 500 companies analysis
- Counts companies per sector per day

---

## ETL Concepts

| Step | Description |
|---|---|
| **Extract** | Retrieve data from source system |
| **Transform** | Clean and prepare the data |
| **Load** | Store in final system |

---

## Installation

```bash
# 1 - Set AIRFLOW_HOME
export AIRFLOW_HOME="/workspaces/ETL-with-Airflow/airflow"

# 2 - Install Airflow
pip install "apache-airflow==2.9.2" \
--constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.2/constraints-3.12.txt"

# 3 - Initialize database
airflow db init

# 4 - Create admin user
airflow users create \
--username admin \
--password admin \
--firstname Admin \
--lastname User \
--role Admin \
--email admin@example.com

# 5 - Disable CSRF in webserver_config.py
WTF_CSRF_ENABLED = False

# 6 - Start Airflow
airflow webserver -D
airflow scheduler -D
```

---

## Usage

```bash
# Start Airflow
export AIRFLOW_HOME="/workspaces/ETL-with-Airflow/airflow"
airflow webserver -D
airflow scheduler -D

# Stop Airflow
pkill -f airflow

# List DAGs
airflow dags list

# Trigger a DAG
airflow dags trigger <dag_name>

# View database
sqlite3 lab/end-to-end/basic-etl-load-db.db
SELECT * FROM top_level_domains LIMIT 10;
```

---

## Issues Encountered

| Issue | Solution |
|---|---|
| Python 3.12 incompatible with Airflow 2.6.3 | Used Airflow 2.9.2 |
| Bad Request error in Codespaces | Updated base_url in airflow.cfg |
| datahub.io URL not available | Used data.iana.org instead |

---

## Important Notes
- Airflow 2.9.2 is required for Python 3.12
- CSRF must be disabled for Codespaces
- SQLite is for development only
- In production use PostgreSQL or MySQL
