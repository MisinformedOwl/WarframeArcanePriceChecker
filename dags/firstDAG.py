# dags/firstDAG.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pathlib import Path
import sys
package_dir = str(Path(__file__).parent / "firstDagContent")
sys.path.append(package_dir)
from firstDagContent.firstmethod import run as running

def print_hi():
    print("HI FROM AIRFLOW!")

def addCount():
    running()

with DAG(
    dag_id='first-DAG',
    start_date=datetime(2025, 1, 1),
    schedule="*/5 * * * *",
    catchup=False,
    tags=['example'],
) as dag:
    say_hi = PythonOperator(
        task_id='say_hi',
        python_callable=print_hi,
    )

    add_count = PythonOperator(
        task_id="Add-count",
        python_callable=addCount
    )