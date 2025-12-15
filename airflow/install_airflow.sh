# AIRFLOW_VERSION = 3.1.3
# PYTHON VERSION = " $(python-c 'import sys; print (f"{sys.version_info.major}. {sys.version_info.minor}")')"
# CONSTRAINT_URL = "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# pip install "apache-airflow[celery]==${AIRFLOW_VERSION}" --constraint {CONSTRAINT_URL}"

# export AIRFLOW_HOME = $(pwd)/airflow
# mkdir -p $AIRFLOW_HOME

!/bin/bash


AIRFLOW_VERSION=3.1.3

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow[celery]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

export AIRFLOW_HOME=$(pwd)/airflow
mkdir -p $AIRFLOW_HOME
echo "Airflow installed successfully!"
echo "AIRFLOW_HOME is set to: $AIRFLOW_HOME"


