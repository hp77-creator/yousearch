# YouSearch

__Goal__ : To create an API to fetch latest videos descending order of the time in which they were published on youtube


## Requirements

- [] Server should call youtube API continuously in background after certain interval for a predefined search query

- [] Store the response in DB with following fields - Video Title, Description, Publishing datetime, thumbnails URL, Channel name(Optional)

- [] GET API to fetch data from DB in descending order
- [] Search API to search the stored videos using their __title__ and their __description__
- [] Dockerize the project
- [] Should be scalable and optimised

## [!Warning] Bonus points

- [] Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available keys ( :thinking: maybe searching a list of keys in env, if at anytime there is a particular response received from YT server, update the API_KEY env variable)
- [] Make a dashboard to see the stored videos with filter
- [] Search with partial keywords


## Implementation Choices

predefined_query = `NBA`, `Basketball`, `Vim`





### Tech Stack

- Backend:
    - flask for APIs
    - sqlite for DB
        - Not good for concurrent operations like read & write together
        - Going with __PostgreSQL__ instead [MVCC](https://www.postgresql.org/docs/7.1/mvcc.html)
    - celery for task queue to fetch record and enter in the DB

Methods:
- 3 Docker Containers:
    One for Backend server
    One for background worker
    One for DB

- 1 Docker container:
    DB, Backend service and Background worker all are in same container


### References


[Youtube API Data](https://developers.google.com/youtube/v3/docs/search/list?apix=true&apix_params=%7B%22part%22:%5B%22snippet%22%5D,%22q%22:%22NBA%22%7D)






