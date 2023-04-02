# A Python quiz game that works with a database.

# Set up the project.

`docker run  -d 
        --name postgres_db2023 
        -e POSTGRES_USER=sirius_2023 
        -e POSTGRES_PASSWORD=change_me 
        -e PGDATA=/postgres_data_inside_container 
        -v ~/sirius_db_2023/postgres_data:/postgres_data_inside_container 
        -p 38746:5432 
        postgres:15.1`

docker start postgres_db2023

psql -h 127.0.0.1 -p 38746 -U sirius_2023 -d postgres -f init_db.ddl

# .env:
database name, host, port, passsword and user to connect 

`PG_HOST=127.0.0.1
PG_PORT=38746
PG_USER=sirius_2023
PG_PASSWORD=change_me
PG_DBNAME=postgres`

# run:
    python3 main.py 