from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Item  # Import the Item model

# Database setup (use the same database URL as your FastAPI app)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create a new database session
db = SessionLocal()

# Query all items
items = db.query(Item).all()
for item in items:
    print(f"Item ID: {item.id}, Name: {item.name}, Quantity: {item.quantity}")

# Query a specific item by ID
item_id = 1  # Replace with the ID of the item you want to query
item = db.query(Item).filter(Item.id == item_id).first()
if item:
    print(f"Item ID: {item.id}, Name: {item.name}, Quantity: {item.quantity}")
else:
    print("Item not found")

# Close the session
db.close()
