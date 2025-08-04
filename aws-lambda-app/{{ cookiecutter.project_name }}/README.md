# {{ cookiecutter.project_name.title() }}

{{ cookiecutter.description }}

## Author
{{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})

## Architecture

This AWS Lambda application is built using {{ cookiecutter.infrastructure_tool }} and includes:

{% if cookiecutter.use_api_gateway == 'y' -%}
- API Gateway integration
{% endif -%}
{% if cookiecutter.use_s3_trigger == 'y' -%}
- S3 event triggers
{% endif -%}
{% if cookiecutter.use_eventbridge == 'y' -%}
- EventBridge scheduled events
{% endif -%}
{% if cookiecutter.use_dynamodb == 'y' -%}
- DynamoDB integration
{% endif -%}

## Quick Start

```bash
# Install dependencies
make install

# Run tests
make test

# Deploy to development
make deploy-dev

# Deploy to production  
make deploy-prod