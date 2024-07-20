# Energonexus API Documentation

## Introduction

Welcome to the Energonexus API documentation! This API provides access to energy usage and production data, as well as advanced analytics and machine learning models.

## Endpoints

### Energy Usage

* `GET /energy/usage`: Retrieve energy usage data for a specific device or location.
* `POST /energy/usage`: Create a new energy usage data point.
* `PUT /energy/usage/{id}`: Update an existing energy usage data point.
* `DELETE /energy/usage/{id}`: Delete an energy usage data point.

### Energy Production

* `GET /energy/production`: Retrieve energy production data for a specific device or location.
* `POST /energy/production`: Create a new energy production data point.
* `PUT /energy/production/{id}`: Update an existing energy production data point.
* `DELETE /energy/production/{id}`: Delete an energy production data point.

### Analytics

* `GET /analytics/energy_usage`: Retrieve energy usage analytics for a specific device or location.
* `GET /analytics/energy_production`: Retrieve energy production analytics for a specific device or location.

### Machine Learning Models

* `GET /models/energy_usage_prediction`: Retrieve energy usage prediction model.
* `GET /models/energy_production_prediction`: Retrieve energy production prediction model.

## Authentication

The Energonexus API uses JSON Web Tokens (JWT) for authentication. To obtain a JWT, send a `POST` request to `/auth/login` with your username and password.

## Rate Limiting

The Energonexus API has a rate limit of 100 requests per minute. Exceeding this limit will result in a 429 error.

## Error Handling

The Energonexus API uses standard HTTP error codes to indicate errors. See the [Error Codes](#error-codes) section for more information.

## Error Codes

* 400: Bad Request
* 401: Unauthorized
* 403: Forbidden
* 404: Not Found
* 429: Too Many Requests
* 500: Internal Server Error

## Contact

For more information or to report an issue, please contact [support@energonexus.com](mailto:support@energonexus.com).
