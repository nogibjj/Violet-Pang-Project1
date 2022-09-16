# Violet-Pang-Project1
This is the repo for Violet's project 1: Cloud Continuous Delivery of Microservice (MLOps or Data Engineering Focused)


## Getting Started

Plese install all the libraries in the requirement.txt and set up a python environment to run this project on your machine.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Microsoft Azure - Databricks](https://azure.microsoft.com/en-us/products/databricks/)
- [Github Codespace](https://github.com/features/codespaces)


## Running the tests

# Test out CLI
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq

# Test Query
./hello_query_sql_db.py cli-query --query "SELECT * FROM default.mcdonalds LIMIT 3"

# Test Fast API
python fastapi-app.py


## Deployment

Add additional notes to deploy this on a live system

## Built With

  - [Pragmatic AI Lab](https://www.youtube.com/watch?v=DQFXx-ezbN0) 
  Python Statements with Google Colab, IPython and GitHub CodeSpaces


## Versioning

We use [Semantic Versioning](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/PurpleBooth/a-good-readme-template/tags).

## Authors
Violet Pang


## Acknowledgments
The concept of this project is modified from Prof. Noah Gift's lecture.
