FROM postgres

LABEL author="R Rajasekar"
LABEL description="Roadlink Data Processing and Loading"
LABEL version="1.0"

COPY *.sql /docker-entrypoint-initdb.d/

CMD ["docker-entrypoint.sh", "postgres"]
