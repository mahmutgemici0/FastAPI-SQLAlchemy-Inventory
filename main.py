from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound

app = FastAPI()

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to add or update an item
@app.post("/items/{item_name}/{quantity}")
def add_item(item_name: str, quantity: int, db: SessionLocal = Depends(get_db)):
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0.")

    try:
        item = db.query(Item).filter(Item.name == item_name).one()
        item.quantity += quantity
    except NoResultFound:
        item = Item(name=item_name, quantity=quantity)
        db.add(item)

    db.commit()
    return {"item_id": item.id, "item_name": item.name, "quantity": item.quantity}

# Route to list a specific item by ID
@app.get("/items/{item_id}")
def list_item(item_id: int, db: SessionLocal = Depends(get_db)):
    try:
        item = db.query(Item).filter(Item.id == item_id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Item not found.")
    return {"item_id": item.id, "item_name": item.name, "quantity": item.quantity}

# Route to list all items
@app.get("/items")
def list_items(db: SessionLocal = Depends(get_db)):
    items = db.query(Item).all()
    return {"items": [{"item_id": item.id, "item_name": item.name, "quantity": item.quantity} for item in items]}

# Route to delete a specific item by ID
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: SessionLocal = Depends(get_db)):
    try:
        item = db.query(Item).filter(Item.id == item_id).one()
        db.delete(item)
        db.commit()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Item not found.")
    return {"result": "Item deleted."}
