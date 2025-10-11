# FastAPI Examples

This repository contains a collection of simple FastAPI examples that demonstrate various features of the framework.

## Table of Contents

- [Hands on](#hands-on)
- [With Pydantic](#with-pydantic)
- [Query](#query)
- [Post and Request](#post-and-request)
- [Annotated Type](#annotated-type)

## Examples

Each directory in this repository contains a self-contained FastAPI example.

### Hands on

This example demonstrates a basic FastAPI application with several endpoints to manage a list of bands. It includes endpoints to get all bands, get a band by ID, search for bands by name, and get bands by genre.

- **Source Code:** [`Hands on/FastAPI_1.py`](Hands%20on/FastAPI_1.py)

### With Pydantic

This example demonstrates how to use Pydantic models to define the data schema for your API. This allows for automatic data validation, serialization, and documentation.

- **Source Code:**
    - [`With Pydantic/FastAPI_2.py`](With%20Pydantic/FastAPI_2.py)
    - [`With Pydantic/schema_2.py`](With%20Pydantic/schema_2.py)

### Query

This example demonstrates how to use query parameters to filter the results of an endpoint. The `get_bands` endpoint accepts optional `genre` and `has_albums` parameters to filter the list of bands.

- **Source Code:**
    - [`Query/FastAPI_3.py`](Query/FastAPI_3.py)
    - [`Query/schema_3.py`](Query/schema_3.py)

### Post and Request

This example demonstrates how to handle `POST` requests to create new resources on the server. It uses a separate Pydantic model (`BandCreate`) for creating a band, which doesn't include the `id` field.

- **Source Code:**
    - [`Post and Request/FastAPI_4.py`](Post%20and%20Request/FastAPI_4.py)
    - [`Post and Request/schema_4.py`](Post%20and%20Request/schema_4.py)
    - [`Post and Request/app.http`](Post%20and%20Request/app.http)

### Annotated Type

This example demonstrates how to use `typing.Annotated` to add metadata to your API's parameters, which can be used for validation, documentation, and more. In this example, `Annotated` is used with `Query` to add a `max_length` validation to a query parameter and with `Path` to add a title to the path parameter in the documentation.

- **Source Code:**
    - [`Annotated Type/FastAPI_4.py`](Annotated%20Type/FastAPI_4.py)
    - [`Annotated Type/Annotated.py`](Annotated%20Type/Annotated.py)


## How to run the examples

1. **Install the dependencies:**

   ```bash
   pip install fastapi "uvicorn[standard]" pydantic
   ```

2. **Navigate to the example directory:**

   For example, to run the "Hands on" example:
   ```bash
   cd "Hands on/"
   ```

3. **Run the FastAPI application:**

   Use `uvicorn` to run the application. The file name and app instance might be different for each example. For the "Hands on" example, the file is `FastAPI_1.py` and the app instance is `app`.

   ```bash
   uvicorn FastAPI_1:app --reload
   ```

   Here's a list of the files for each example:
   - **Hands on:** `FastAPI_1.py`
   - **With Pydantic:** `FastAPI_2.py`
   - **Query:** `FastAPI_3.py`
   - **Post and Request:** `FastAPI_4.py`
   - **Annotated Type:** `FastAPI_4.py`
