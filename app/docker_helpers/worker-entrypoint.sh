until cd /app
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A task worker --loglevel=info --concurrency 1 -E
