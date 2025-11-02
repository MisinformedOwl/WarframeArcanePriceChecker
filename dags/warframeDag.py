from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pathlib import Path
import sys
package_dir = str(Path(__file__).parent / "warframeArcanePricing")
sys.path.append(package_dir)
from warframeArcanePricing.CollectArcanes import priceArcanes

def updateArcanePrices():
    priceArcanes()

with DAG(
    dag_id="Warframe-Arcane-Pricing",
    description="Acquires the new prices based on current trades on warframe marketplace.",
    schedule="@hourly",
    catchup=False,
    tags=["Warframe"],
) as dag:
    updatePrices = PythonOperator(
        task_id="Pricing-update",
        python_callable=updateArcanePrices
    )