# How to run dbt with Cloud Composer and Cloud Run

This is a sample project that demonstrates how to use Google Cloud Composer to trigger a Cloud Run service using Airflow BashOperator. The project shows how to use Cloud Run to run your dbt CLI in a containerized, platform-agnostic environment without relying on the Python packages already installed in Cloud Composer.

## Purpose of the Project

The purpose of this project is to avoid Python dependency issues inside of Cloud Composer and move the compute of dbt out of Cloud Composer/Airflow. By using Cloud Run, you can run dbt securely in a separate environment.

## How it Works

Cloud Composer uses the Airflow BashOperator to trigger the Cloud Run service that executes the dbt CLI.

> Cloud Composer -> BashOperator to trigger a Cloud Run service -> Cloud Run container runs dbt CLI

Once deployed, the Cloud Run service listens for HTTP requests and provides an HTTP endpoint. From within the Airflow worker, `gcloud` is used to invoke Cloud Run service secured by Google Cloud IAM. The Cloud Run service then runs the specified dbt CLI command.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine.
2. Set up a Google Cloud project if you haven't already done so.
3. Enable the necessary APIs (Cloud Build, Cloud Run) in your Google Cloud project.
4. Create a Cloud Run service that listens for HTTP requests by running `deploy.sh`.
5. Update the Cloud Run URL in `trigger_cloud_run_dag.py`. 
6. Upload the `trigger_cloud_run_dag.py` DAG to the `/dags` directory of your Cloud Composer environment.
7. Run the DAG in your Cloud Composer environment to trigger the Cloud Run service.

## Screenshots

TODO

## License

This project is licensed under the MIT License - see the LICENSE file for details.
