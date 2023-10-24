FROM jupyter/base-notebook
# Set the working directory
WORKDIR /home/jovyan/work/
# Install PostgreSQL and psycopg2
RUN python -m pip install jupyter notebook -U
#RUN apt-get update && apt-get install -y postgresql postgresql-contrib && apt install -y build-essential libpq-dev
COPY ./notebooks /home/jovyan/work
COPY ./notebooks/requirements.txt /home/jovyan/work/requirements.txt
RUN pip install -r /home/jovyan/work/requirements.txt
EXPOSE 8888
CMD ["sh", "-c", "start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''"]
