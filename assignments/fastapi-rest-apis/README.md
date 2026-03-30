# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework to practice creating endpoints, handling request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI application and implement core CRUD-style endpoints for a simple resource such as books, songs, or tasks.

#### Requirements
Completed program should:

- Create a FastAPI app with a root endpoint that returns a welcome message.
- Implement at least three endpoints using different HTTP methods such as GET, POST, and DELETE or PUT.
- Return JSON responses with clear fields and status messages.

### 🛠️ Add Validation and Error Handling

#### Description
Use Pydantic models to validate incoming request data and add basic error handling for missing items or invalid input.

#### Requirements
Completed program should:

- Define at least one Pydantic model for request body validation.
- Return a clear error response when a requested item does not exist.
- Include simple in-memory data storage and update it through API requests.
