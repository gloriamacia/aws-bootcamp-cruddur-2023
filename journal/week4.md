# Week 4 — Postgres and RDS

We started creating an RDS posgresql instance in our AWS account: 

    aws rds create-db-instance \
    --db-instance-identifier cruddur-db-instance \
    --db-instance-class db.t3.micro \
    --engine postgres \
    --engine-version  14.6 \
    --master-username root \
    --master-user-password gooddbPassword123 \
    --allocated-storage 20 \
    --availability-zone eu-west-1a \
    --backup-retention-period 0 \
    --port 5432 \
    --no-multi-az \
    --db-name cruddur \
    --storage-type gp2 \
    --publicly-accessible \
    --storage-encrypted \
    --enable-performance-insights \
    --performance-insights-retention-period 7 \
    --no-deletion-protection

We did this first because it takes a while to provision. Then we stopped it (only for 7 days!) to avoid costs of the managed EC2 instance running it. This will be our production database. We created the connection string following [this syntax](https://stackoverflow.com/questions/3582552/what-is-the-format-for-the-postgresql-connection-string-url).

    export PROD_CONNECTION_URL="postgresql://root:gooddbPassword123@cruddur-db-instance.ci9btkxlyb6o.eu-west-1.rds.amazonaws.com:5432/cruddur"

    gp env PROD_CONNECTION_URL="postgresql://root:gooddbPassword123@cruddur-db-instance.ci9btkxlyb6o.eu-west-1.rds.amazonaws.com:5432/cruddur"
  
For the development, we will use the local postresql instance, defined in our docker-compose file. 

    db:
      image: postgres:13-alpine
      restart: always
      environment:
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=password
      ports:
        - '5432:5432'
      volumes: 
        - db:/var/lib/postgresql/data
 
Once its container is running, we can find it in the terminal and run the following commands: 

    \x on -- expanded display when looking at data
    \q -- Quit PSQL
    \l -- List all databases
    \c database_name -- Connect to a specific database
    \dt -- List all tables in the current database
    \d table_name -- Describe a specific table
    \du -- List all users and their roles
    \dn -- List all schemas in the current database
    CREATE DATABASE database_name; -- Create a new database
    DROP DATABASE database_name; -- Delete a database
    CREATE TABLE table_name (column1 datatype1, column2 datatype2, ...); -- Create a new table
    DROP TABLE table_name; -- Delete a table
    SELECT column1, column2, ... FROM table_name WHERE condition; -- Select data from a table
    INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...); -- Insert data into a table
    UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition; -- Update data in a table
    DELETE FROM table_name WHERE condition; -- Delete data from a table

We can also do this actions from the outside if we connect to it: 

    psql -Upostgres --host localhost

This command runs all the commands in schema.yml: 

    psql cruddur < db/schema.sql -h localhost -U postgres

The connection string of the develop database is: 

    gp env CONNECTION_URL="postgresql://postgres:password@127.0.0.1:5432/cruddur"
    export CONNECTION_URL="postgresql://postgres:password@127.0.0.1:5432/cruddur"

We also use some bash scrips, they are not executable by default so we need to make them: 

     ls -la
     chmod u+x db-create db-drop db-schema-load 
