# Simple Blogging Platform API

This repository contains the code for a RESTful API for a simple blogging platform. The API allows users to perform CRUD operations on blog posts, comment on posts, and like/dislike them. The data is stored in a MongoDB database. The API is implemented using Python FastAPI framework while adhering to object-oriented programming principles.

## Requirements
- Python 3.x
- FastAPI
- Pydantic
- pymongo

Install the required Python libraries by running:
```bash
pip install -r requirements.txt
```

## Usage
To run the API, execute the following command:
```bash
uvicorn main:app --reload
```

Once the server is running, you can interact with the API using HTTP requests.

### Endpoints

#### 1. Get All Blogs
- **URL:** `/blogs`
- **Method:** GET
- **Description:** Retrieves all blog posts.

#### 2. Create Blog
- **URL:** `/blogs/`
- **Method:** POST
- **Description:** Creates a new blog post.

#### 3. Update Blog
- **URL:** `/{id}`
- **Method:** PUT
- **Description:** Updates an existing blog post.

#### 4. Like Blog
- **URL:** `/{id}/like`
- **Method:** PUT
- **Description:** Increments the like count of a blog post.

#### 5. Dislike Blog
- **URL:** `/{id}/dislike`
- **Method:** PUT
- **Description:** Increments the dislike count of a blog post.

#### 6. Comment on Blog
- **URL:** `/{id}/comment`
- **Method:** PUT
- **Description:** Adds a comment to a blog post.

#### 7. Delete Blog
- **URL:** `/{id}`
- **Method:** DELETE
- **Description:** Deletes a blog post.

## Folder Structure
- **models/**: Contains Pydantic models for data validation.
- **routes/**: Contains route handlers for API endpoints.
- **config/**: Contains database configuration.
- **schema/**: Contains functions for serializing data.
- **main.py**: Main Python script containing the FastAPI application.
- **requirements.txt**: File containing the required Python libraries.

## Authors
- [Mohammad Danish Sheikh](https://github.com/Danish811) (GitHub: Danish811)

