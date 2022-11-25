#!/usr/bin/env bash

cd /app

if [[ -f "requirements_local.txt" ]];
then
    pip install --no-cache-dir --root-user-action=ignore -r requirements_local.txt
fi

# image can run in multiple modes
if [[ "${1}" == "celery_worker" ]]; then
    exec celery -A celeryapp worker -l info  -Q $WORKER_QUEUE_NAME
elif [[ "${1}" == "celery_beat" ]]; then
    exec celery -A celeryconfig beat -l info
elif [[ "${1}" == "celery_flower" ]]; then
    exec celery flower --port=5555
fi

exec "$@"