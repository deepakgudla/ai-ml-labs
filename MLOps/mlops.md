# MLOps: Machine Learning Operations

`MLOps` (Machine Learning Operations) supports CI/CD (Continuous Integration and Continuous Deployment) for machine learning projects, providing a standardized approach to deploying and managing ML models. Key components include:

- **Standardizing deployment and management** of ML models.
- **Building and deploying** ML models to production.
- **Automating environments** and processes for deploying ML projects to production.

- `MLOps` represents a fusion of machine learning and operations, encapsulating the processes and practices necessary for effective deployment of ML models in production environments.

### MLOps and Continuous Improvement

MLOps is rooted in the concept of continuous improvement, drawing inspiration from the Japanese philosophy of `Kaizen`.
- **`Kaizen`**: Focuses on improving all aspects of a business activity, from model accuracy to the broader ML ecosystem.
---

### What is MLOps?
- `MLOps` is not just about tracking loccal experiment or it is not about just placing a model behind an API endpoint.
- `MLOps` is about an automated environment and the process for continuously delivering projects to the production environment

## Stages of MLOps

The MLOps workflow consists of four major components:

1. [Data Collection and Preparation](#data-collection-and-preparation)
2. [Model Development and Training](#model-development-and-training)
3. [ML Service Deployment](#ml-service-deployment)
4. [Continuous Feedback and Monitoring](#continuous-feedback-and-monitoring)

---

## 1. Data Collection and Preparation

Data is the foundation for ML model development. This stage includes:

- **Data Ingestion, Preparation, and Exploration**: Define goals and identify data sources, prepare, label, and explore raw data.
- **Data Refinement** (`raw-data`):
  - Conversion of data to required formats (e.g., numerical data).
  - Normalization or scaling of features.
  - Encoding of categorical data.
  - Addressing spelling errors, missing values, and other data quality issues.

---

## 2. Model Development and Training

In this stage, data is transformed and utilized to train ML models. Key steps include:

- **Data Extraction**: Using prepared data to build ML models.
- **Model Training and Validation**: Training the model and validating its performance.
- **Model Evaluation**: Assessing the model’s effectiveness on evaluation data.

### ML Pipeline

An `ml-pipeline` is a crucial, modularized, and automated workflow that enables streamlined ML processes. Key features include:

- **Modularization** of code for reusable components.
- **Experiment Tracking**: Track code, dependencies, data, parameters, and outputs.
- **Version Control**: Versioning for all data and artifacts used in the pipeline.
- **CI Techniques**: Automating pipeline initiation, testing, review, and approval.

---

## 3. Machine Learning Service Deployment

Deploying ML models involves integrating them with applications and managing their production lifecycle. Major aspects include:

- **Application Integration**: Embedding ML models in existing applications.
- **Frontend Development** (if necessary).
- **Containerization**: Packaging the ML model/application into containers for portability.
- **API Services**:
  - Defining one or more serving endpoints.
  - Managing model endpoints for scalability.
- **Monitoring Services**:
  - Monitoring model performance, resource usage, and setting up alerting mechanisms.

---

## 4. Continuous Feedback and Monitoring

Ensuring models perform optimally in production requires ongoing monitoring and feedback. This stage includes:

- **Data and Infrastructure Tracking**: Monitor the data pipeline and compute resources.
- **Model and Application Metrics**: Track performance metrics for models and applications.
- **Alerting System**:
  - Alerts when a model is underperforming or requires retraining.
- **Staleness Monitoring**:
  - Receive alerts if the model has not been deployed recently, ensuring freshness.

---

## packaging ML models

* modularization approach for writing code
* virtual environments - setting up
* serialization and de serialization
* packaging in python
* developing, building and deploying ML packages
