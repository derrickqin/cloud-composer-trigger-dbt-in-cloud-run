from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
}

dag = DAG(
    "trigger_cloud_run_dag",
    description="trigger_cloud_run_dag",
    schedule_interval="0 3 * * *",
    start_date=datetime(2023, 4, 19),
    catchup=False,
    tags=["custom"],
)

trigger_cloud_run = BashOperator(
    task_id="trigger_cloud_run",
    bash_command='curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" https://run-dbt-blah.a.run.app',
    do_xcom_push=True,
    dag=dag
)

trigger_cloud_run