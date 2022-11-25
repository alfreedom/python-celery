import time
from os import environ as env
from celery import Celery
#from .celeryconfig import CeleryConfig


class CeleryConfig:
    """Class to configure celery"""
    ## Broker settings.
    broker_url = env.get("CELERY_BROKER_URL")

    ## Using the database to store task state and results.
    result_backend = env.get("CELERY_RESULT_BACKEND")
    #include = ["mathapp.tasks"]


app = Celery("My Celery App")
app.config_from_object(CeleryConfig)
app.autodiscover_tasks(['mathapp'])

@app.task(name="test_task")
def test_task():
    """ Simple test task"""

    print("This is a sample celery tasks, waiting 5 seconds...")
    time.sleep(5)
    print("Sample task finished")
    return True
