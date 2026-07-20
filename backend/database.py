from sqlalchemy import create_engine
# Used to connect Python with the database.

from sqlalchemy.orm import sessionmaker, declarative_base
# sessionmaker -> Creates database sessions.
# declarative_base -> Base class for all SQLAlchemy models (tables).

# Database URL (SQLite database file)
DATABASE_URL = "sqlite:///./books.db"

# Creates the connection to the database.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Creates a session factory.
# Every time we call SessionLocal(), we get a new database session.
SessionLocal = sessionmaker(
    autocommit=False,   # Changes are not saved automatically.
    autoflush=False,    # Data is not sent automatically.
    bind=engine         # Connect this session to our database.
)

# Base class that every table(model) inherits from.
Base = declarative_base()

# Function to provide a database session.
def get_db():
    db = SessionLocal()     # Open a new database session.
    try:
        yield db            # Give the session to the route.
    finally:
        db.close()          # Close the session after the request is complete.