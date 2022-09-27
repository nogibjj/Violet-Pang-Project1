# Violet-Pang-Project1
This is the repo for Violet's project 1: Cloud Continuous Delivery of Microservice and Write a Big Data Script that uses the Pandas API for Spark or Dask

This project included below features: <br>
Configure the scafflod <br>
Establish Databricks codespace and use spark functionality to explore NoaaWeather dataset <br>
Create a Microservice in Fast API <br>
Build a "unit of work", test it with IPython <br>
Write a Big Data Script that uses the Pandas API for Spark or Dask <br>
Push source code to Github <br>
Configure Build System to Deploy changes <br>
Use IaC (Infrastructure as Code) to deploy code <br>
Use either Azure-Databricks to depoly the data files <br>


## Getting Started

Plese install all the libraries in the requirement.txt and set up a python environment to run this project on your machine.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Microsoft Azure - Databricks](https://azure.microsoft.com/en-us/products/databricks/)
- [Github Codespace](https://github.com/features/codespaces)


## Running the testsx

# Test out CLI
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq

# Test Query
./hello_query_sql_db.py cli-query --query "SELECT * FROM default.mcdonalds LIMIT 3"

# Test Fast API
python fastapi-app.py


## Deployment
To deploy this project, please open it with codespace and connect your codespace with databricks clusters.

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
