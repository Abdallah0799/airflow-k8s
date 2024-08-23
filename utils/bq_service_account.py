import json
import base64
import os

SERVICE_ACCOUNT_BQ_ADMIN = json.loads(
    base64.b64decode(os.environ["SERVICE_ACCOUNT_BQ_ADMIN"])
)


def save_key_as_json():
    # Construct the full file path
    file_path = "/opt/airflow/dbt/bq_key.json"
    data_dict = SERVICE_ACCOUNT_BQ_ADMIN
    # Save the dictionary as a JSON file
    with open(file_path, "w") as json_file:
        json.dump(data_dict, json_file, indent=4)


save_key_as_json()
