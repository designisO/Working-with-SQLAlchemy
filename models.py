from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///blacbloc.db', echo=True)
# engine = create_engine('postgresql:///mydatabase')  
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# creating db model
class Employees(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    first = Column(String)
    last = Column(String)
    age = Column(Integer)
    role_type = Column(String)

    # returns in console 
    def __repr__(self):
        return f'{self.id} | {self.first}, {self.last}, {self.age}, {self.role_type}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)





