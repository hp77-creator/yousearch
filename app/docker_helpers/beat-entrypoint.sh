until cd /app
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A task beat --loglevel=info -E
