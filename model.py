from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.orm import sessionmaker,Session,declarative_base
from datetime import datetime
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key=True)
    product_name = Column(String(length=200),nullable=False)
    brand_name = Column(String(length=100),nullable=False)
    price = Column(Integer,nullable=False)
    # review = Column(String(length=100),nullable=False)
    created_at = Column(DateTime,default=datetime.now())

engine = create_engine("mysql+pymysql://root:root@localhost/Alembic_DB_Migration")

session_maker = sessionmaker(bind=engine)
session   = session_maker()
products = [
    Product(product_name = "Redmi Note 14",brand_name="Redmi",price=65758,),
    Product(product_name = "Iphone 18 Pro",brand_name = "Apple",price=7689,),
    Product(product_name = "Fitbit",brand_name = "Google",price=89745,)
]
def save_product():
    for product in products:
        session.add(product)

        session.commit()

print("-------")
# save_product()

def delete_product(id):
    product = session.query(Product).filter(Product.id==id).first()
    session.delete(product)
    session.commit()

# delete_product(16)

