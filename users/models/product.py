from base import Base
from sqlalchemy.orm import Mapped

class Products(Base):
    __tablename__ = "products"
    
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]


