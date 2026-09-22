# KisanSetu Backend

Backend API for KisanSetu - Farmer Market Linkage and Price Discovery.

## Technology

- Python
- FastAPI
- SQLite
- Pydantic

## API Endpoints

### 1. Health Check

GET /

Checks whether the backend is running.

### 2. Register

POST /api/register

Creates a new user account.

Request:
```json
{
  "name": "Ramesh",
  "email": "ramesh@example.com",
  "password": "123456",
  "role": "farmer"
}
{
  "email": "ramesh@example.com",
  "password": "123456"
}
{
  "type": "market",
  "name": "Bhubaneswar Market",
  "location": "Bhubaneswar",
  "crop": "Tomato",
  "quantity": 500,
  "price": 25,
  "capacity": 1000,
  "description": "Local vegetable market",
  "created_by": 1
}
### 5. View Lots

GET /api/lots

Returns all available lots.

### Filter Lots

GET /api/lots?type=market

Supported types:

- market
- buyer
- storage

## Current Scope

This version uses a demo SQLite database.

External APIs such as AGMARKNET and data.gov.in are not connected yet.
