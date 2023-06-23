# Events info http_server

# Set up the project.

# Do this command to clone my repo
git clone https://github.com/uvanqz/rpm-hws_7-2_2023
cd rpm-hws_7-2_2023
git checkout uvarova

# You need to move folder with name hw2.
cd hw2

# You need to create a docker container

`docker run  -d 
        --name postgres_db2023 
        -e POSTGRES_USER=sirius_2023 
        -e POSTGRES_PASSWORD=change_me 
        -e PGDATA=/postgres_data_inside_container 
        -v ~/sirius_db_2023/postgres_data:/postgres_data_inside_container 
        -p 38746:5432 
        postgres:15.1`

docker start postgres_db2023

# Create tables

psql -h 127.0.0.1 -p 38746 -U sirius_2023 -d postgres -f cmnds_init.ddl

# this server needs:

## postgres database
###### with tables: 
###### token (username text primary key, token uuid)
######  events (id int generated always as identity primary key, event TEXT, date_s date, description TEXT, location TEXT);

## .env:
database name, host, port, passsword and user to connect 

`PG_HOST=127.0.0.1
PG_PORT=38746
PG_USER=sirius_2023
PG_PASSWORD=change_me
PG_DBNAME=postgres`

# run:
    python3.X main.py

# And click the link: http://127.0.0.1:8001

# After this command you fill see the main page. You can choose which page to go to.

# You can open Postman and try to do POST/PUT/DELETE requests. 

# 1. POST request
paste the url http://127.0.0.1:8001/events
Go to Postman

Example of data that we send to post:
{
    "event": "event_1",
    "description": "description_1",
    "location": "Lyceum",
    "date_s": "2023-08-09"
}

After this command you will see a url with event id. You can press ctrl and click to the link. You will see your event.

# 2. PUT request
paste the url http://127.0.0.1:8001/events?id= after "=" you must to paste event id, witch you want to update.

Go to Postman
Example of data that we send to update:

{
    "event": "event_1",
    "description": "description_1",
    "location": "Arena",
    "date_s": "2023-08-09"
}

After this command you will see an updated event.

# 3. DELETE request
paste the url http://127.0.0.1:8001/events?id= after "=" you must to paste event id, witch you want to delete.
