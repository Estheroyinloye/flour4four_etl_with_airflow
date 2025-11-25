AIRFLOW_VERSION = 3.13
PYTHON VERSION = " $(python-c 'import sys; print (f"{sys.version_info.major}. {sys.version_info.minor}")')"
CONSTRAINT_URL = "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow[celery]==${AIRFLOW_VERSION}" --constraint {CONSTRAINT_URL}"

export AIRFLOW_HOME = $(pwd)/airflow
mkdir -p $AIRFLOW_HOME