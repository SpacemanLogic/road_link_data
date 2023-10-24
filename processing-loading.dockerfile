# Dockerfile APP
FROM python:3.8

# Set the working directory
WORKDIR /app

# Install PostgreSQL and psycopg2
RUN apt-get update && apt-get install -y postgresql postgresql-contrib && apt install -y build-essential libpq-dev


COPY processing-loading.py /app
COPY sample_file.txt /app
COPY data-push.py /app
#COPY sql_table_create.sql /app
COPY requirements.txt /app/

# Install any dependencies
RUN pip install -r requirements.txt

# Entrypoint
CMD [ "python", "processing-loading.py" ]