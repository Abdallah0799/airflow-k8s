FROM apache/airflow:2.10.0-python3.12

# Install pipenv
RUN pip install pipenv

RUN mkdir -p /opt/airflow/dbt

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY --chown=airflow . ./

ENV PYTHONPATH /app

# Install dependencies from Pipfile
RUN pipenv install

# Save BQ KEY to folder
RUN pipenv run python utils/bq_service_account.py