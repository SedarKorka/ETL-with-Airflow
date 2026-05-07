================================================================
              ETL WITH AIRFLOW - DATA ENGINEERING PROJECT
================================================================

AUTHOR  : Mamadou Korka Diallo (SedarKorka)
DATE    : May 2026
COURSE  : Hands-On Introduction to Data Engineering
          LinkedIn Learning

================================================================
                        DESCRIPTION
================================================================

This project implements a complete ETL (Extract, Transform, Load)
pipeline using Apache Airflow as the orchestration tool.

The main goal is to automate the process of collecting, cleaning,
and storing data from external sources.

================================================================
                    TECHNOLOGIES USED
================================================================

- Python            3.12.1
- Apache Airflow    2.9.2
- Pandas            (data manipulation)
- SQLite            (database)
- GitHub Codespaces (development environment)
- Bash              (system commands)

================================================================
                    PROJECT STRUCTURE
================================================================

ETL-with-Airflow/
│
├── airflow/
│   ├── dags/
│   │   ├── one_task_dag.py        # 1 task DAG
│   │   ├── two_task_dag.py        # 2 task DAG
│   │   ├── extract_dag.py         # Extract DAG
│   │   ├── transform_dag.py       # Transform DAG
│   │   ├── load_dag.py            # Load DAG
│   │   ├── basic_etl_dag.py       # Complete ETL DAG
│   │   └── challenge_dag.py       # S&P 500 Challenge
│   ├── airflow.cfg                # Airflow configuration
│   ├── airflow.db                 # Airflow database
│   └── webserver_config.py        # Webserver configuration
│
├── lab/
│   ├── manual/                    # Manual ETL work
│   │   ├── manual-extract-data.csv
│   │   ├── manually-transform-data.csv
│   │   ├── manual-load-db
│   │   ├── transform.py
│   │   └── load.py
│   │
│   ├── orchestrated/              # Airflow orchestrated work
│   │   ├── airflow-extract-data.csv
│   │   ├── airflow-transform-data.csv
│   │   └── airflow-load-db.db
│   │
│   ├── end-to-end/                # Complete ETL pipeline
│   │   ├── basic-etl-extract-data.csv
│   │   ├── basic-etl-transform-data.csv
│   │   └── basic-etl-load-db.db
│   │
│   └── challenge/                 # S&P 500 Challenge
│       ├── challenge-extract-data.csv
│       ├── challenge-transform-data.csv
│       └── challenge-load-db.db
│
└── README.txt                     # This file

================================================================
                        DAG DESCRIPTIONS
================================================================

1. ONE_TASK_DAG
   - First simple DAG
   - Creates a text file with "Hello LinkedIn Learning"
   - 1 task using BashOperator

2. TWO_TASK_DAG
   - DAG with 2 dependent tasks
   - T0 prints "First Airflow Task"
   - T1 waits for T0 then prints "Second Airflow Task"
   - Dependency : T0 >> T1

3. EXTRACT_DAG
   - Downloads internet domain list from IANA
   - Source : https://data.iana.org/TLD/tlds-alpha-by-domain.txt
   - Saves to airflow-extract-data.csv
   - Uses BashOperator + wget

4. TRANSFORM_DAG
   - Reads extracted data
   - Adds date column with today's date
   - Saves to airflow-transform-data.csv
   - Uses PythonOperator + Pandas

5. LOAD_DAG
   - Loads transformed data into SQLite
   - Uses BashOperator + sqlite3
   - Table : top_level_domains

6. BASIC_ETL_DAG
   - Complete ETL pipeline in 1 DAG
   - Combines Extract + Transform + Load
   - Dependencies : extract >> transform >> load
   - Source : IANA TLD list
   - Destination : SQLite basic-etl-load-db.db

7. CHALLENGE_DAG
   - S&P 500 Challenge
   - Extract  : Downloads list of 500 companies
   - Transform : Counts companies per sector + date
   - Load     : Stores in SQLite challenge-load-db.db
   - Source   : GitHub datasets/s-and-p-500-companies

================================================================
                        CONCEPTS LEARNED
================================================================

ETL (Extract, Transform, Load)
   Extract   : Retrieve data from a source system
   Transform : Clean and prepare the data
   Load      : Store in a final system

AIRFLOW
   DAG       : Directed Acyclic Graph - task plan
   Task      : A single step in the pipeline
   Operator  : Tool to execute a task
   Scheduler : Monitors and triggers DAGs
   Webserver : Airflow graphical interface

OPERATORS USED
   BashOperator   : Executes bash commands
   PythonOperator : Executes Python code

DEPENDENCIES
   A >> B      : B only starts when A is done
   A >> B >> C : Linear chain of tasks

================================================================
                        INSTALLATION
================================================================

PREREQUISITES :
   - GitHub Codespaces
   - Python 3.12
   - pip

STEPS :

1. Clone the repository
   git clone https://github.com/SedarKorka/ETL-with-Airflow

2. Open in GitHub Codespaces

3. Set AIRFLOW_HOME
   export AIRFLOW_HOME="/workspaces/ETL-with-Airflow/airflow"

4. Install Airflow
   pip install "apache-airflow==2.9.2" \
   --constraint "https://raw.githubusercontent.com/apache/airflow/\
   constraints-2.9.2/constraints-3.12.txt"

5. Initialize the database
   airflow db init

6. Create admin user
   airflow users create \
   --username admin \
   --password admin \
   --firstname Admin \
   --lastname User \
   --role Admin \
   --email admin@example.com

7. Disable CSRF
   Open airflow/webserver_config.py
   Change WTF_CSRF_ENABLED = True to False

8. Start Airflow
   airflow webserver -D
   airflow scheduler -D

================================================================
                        USAGE
================================================================

START AIRFLOW :
   export AIRFLOW_HOME="/workspaces/ETL-with-Airflow/airflow"
   airflow webserver -D
   airflow scheduler -D

STOP AIRFLOW :
   pkill -f airflow

LIST DAGS :
   airflow dags list

TRIGGER A DAG :
   airflow dags trigger <dag_name>

VIEW DATABASE :
   sqlite3 lab/end-to-end/basic-etl-load-db.db
   SELECT * FROM top_level_domains LIMIT 10;

================================================================
                    ISSUES ENCOUNTERED
================================================================

1. Python 3.12 incompatible with Airflow 2.6.3
   Solution : Use Airflow 2.9.2

2. Bad Request error in Codespaces
   Solution : Update base_url in airflow.cfg

3. datahub.io URL not available
   Solution : Use data.iana.org as alternative source

================================================================
                    IMPORTANT NOTES
================================================================

- Airflow 2.9.2 is required for Python 3.12
- CSRF must be disabled for Codespaces
- base_url must match your Codespace URL
- SQLite is for development purposes only
- In production, use PostgreSQL or MySQL

================================================================
                          END OF README
================================================================
