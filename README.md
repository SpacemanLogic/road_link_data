# Docker-compose Road Links Data Processing and Visualization

This project is designed to process road links data from a text file, load it into a PostgreSQL database, and create data visualizations using Jupyter Notebook. It also provides Dockerization for a consistent and portable environment using docker-compose.This Docker Compose project provides a simple setup for running a Jupyter Notebook server with specific Python packages in a container. It allows users to get started with Jupyter quickly and without the need to install Python packages or configure the environment manually.

## Prerequisites
- [Docker](https://www.docker.com/) installed on your system.

## Table of Contents

- [Requirements](#requirements)
- [File Processing](#file-processing)
- [Database Loading](#database-loading)
- [Dockerization](#dockerization)
- [Data Visualization](#data-visualization)
- [Repository Structure](#repository-structure)

## Requirements

- **Docker**: To create a containerized environment for this project.
- **Docker-Compose**: For managing multi-container Docker applications.
- **Python 3**: To execute the file processing and data visualization scripts.
- **PostgreSQL**: To set up a database for storing road links data.
- **Jupyter Notebook**: To create data visualizations.

## File Processing

1. **Python Script**: Run the Python script `processing-loading.py` to read the provided text file containing road links data and parse it to extract road_id, Direction, and polyline data.

   ```bash
   python processing-loading.py

## Usage
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/SpacemanLogic/road_link_data.git
   cd docker-jupyter-compose
2. Create a requirements.txt file in the project directory with the Python packages you want to install. For example:
   ```bash
   numpy
   pandas
   matplotlib
3. Build the Docker image and start the Jupyter Notebook server:

   ```bash
   docker-compose up --build
   Access the Jupyter Notebook interface in your web browser at http://localhost:8888/lab.

You can now create, open, and work on Jupyter Notebooks within the /home/jovyan/work directory. Any notebooks you create or files you upload will be saved in this directory on your local machine.

4. To start the Jupyter server, use:
   ```bash
   docker-compose up -d
   
5. To stop the Jupyter server and remove the container, use:
   ```bash
   docker-compose down
