from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import sys

default_args = {
    'owner': 'mandrik',
    'depends_on_past': False,
    'start_date': datetime(2020, 7, 2),
    'retries': 0
}

dag = DAG('MANDRIK_miniproject_20.3', 
    default_args=default_args,
    schedule_interval='* 12 * * 1')

    
t1 = BashOperator(
    task_id='Collecting_data',
    bash_command='/home/jupyter-m.mandrik-1/MMandrik/collect_df.py',
    dag=dag)

t2 = BashOperator(
    task_id='Sending_VK',
    bash_command='/home/jupyter-m.mandrik-1/MMandrik/send_df_vk.py',
    dag=dag)

t1 >> t2
