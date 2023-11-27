## FastAPI-SQLAlchemy-Inventory

### Description
This repository contains a basic inventory management system built with FastAPI and SQLAlchemy. It demonstrates CRUD (Create, Read, Update, Delete) operations using FastAPI as the web framework and SQLAlchemy for ORM (Object-Relational Mapping), with SQLite as the database.

### Features
- Add items to the inventory with name and quantity.
- Retrieve details of a specific item by ID.
- List all items in the inventory.
- Update the quantity of an existing item.
- Delete an item from the inventory.

### Installation
To get this project up and running on your local machine, follow these steps:

1. Clone the Repository
```bash
    git clone https://github.com/mahmutgemici0/FastAPI-SQLAlchemy-Inventory.git

    cd FastAPI-SQLAlchemy-Inventory
```

2. Set up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000.

### Usage
Once the application is running, you can perform API requests to:

- Add an item: POST /items/{item_name}/{quantity}
- Get an item by ID: GET /items/{item_id}
- List all items: GET /items
= Delete an item: DELETE /items/{item_id}

You can also interact with the API using the Swagger UI at http://127.0.0.1:8000/docs.

### Contributing
Contributions to this project are welcome. Please feel free to fork the repository and submit pull requests.

### License
MIT

