# smart-dashboard-api-python
An abstraction layer that exposes routes for internal UI use.
Utilizes 3rd party APIs using SDKs built in other projects.
To be used internally by a Smart Home Dashboard UI TBD.

## Structure
### Controllers
The controllers simplify the API and making it more RESTful.
### API examples
Are located in [tests](tests/) folder. Currently, manuel tests.

## Setup
1. `pip install -r requirements.txt`
2. Get API Keys for all the services and supply them as environment variables
   - `HYDRAWISE_API_KEY=...` 

## Usage
`python src/app.py`