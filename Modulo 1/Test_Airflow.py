from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    return 'Hola, ¡este es un mensaje impreso desde Airflow!'

# Definir los argumentos de la DAG
default_args = {
    'owner': 'usuario',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 14),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definir la DAG
dag = DAG(
    'mi_primer_flujo_de_trabajo',
    default_args=default_args,
    description='Un simple flujo de trabajo con Airflow',
    schedule_interval=timedelta(days=1),
)

# Definir las tareas
hello_operator = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

# Definir la secuencia de tareas
hello_operator

if __name__ == "__main__":
    dag.cli()
