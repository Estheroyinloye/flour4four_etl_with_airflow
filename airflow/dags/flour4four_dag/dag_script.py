# from datetime import datetime, timedelta
# from airflow import DAG
# from airflow.operators.bash import BashOperator

# VENV_PYTHON = "C:\Users\Admin\Desktop\10Alytics\flour4four_etl_with_airflow\.venv\Scripts\python.exe"
# PROJECT_DIR = "C:/Users/Admin/Desktop/10Alytics/flour4four_etl_with_airflow"

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

VENV_PYTHON = "/mnt/c/Users/Admin/Desktop/10Alytics/flour4four_etl_with_airflow/.venv/bin/python"
PROJECT_DIR = "/mnt/c/Users/Admin/Desktop/10Alytics/flour4four_etl_with_airflow"


default_args = {'owner': 'airflow',
                'depends_on_past' : False,
                'start_date' : datetime(2025, 11, 26),
                'email' : 'yettyexcel36@gmail.com',
                'email_on_faliure': True,
                'email_on_retry' : True,
                'retries' : 2,
                'retries_delay' : timedelta(minutes = 1)

}

with DAG(
    dag_id = "flour4four_etl_pipeline",
    default_args= default_args,
    start_date=datetime(2025,12,8),
    schedule="@daily",
    catchup=False,
    tags=["etl","flour4four"],
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command=f"{VENV_PYTHON} {PROJECT_DIR}/export.py",
    )

    transform = BashOperator(
        task_id="transform",
        bash_command=f"{VENV_PYTHON} {PROJECT_DIR}/transform.py",
    )

    load = BashOperator(
        task_id="load",
        bash_command=f"{VENV_PYTHON} {PROJECT_DIR}/load.py",
    )

    extract >> transform >> load
