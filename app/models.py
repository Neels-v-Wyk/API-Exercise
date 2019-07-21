from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

DB_URI = 'sqlite:///titanic.db'

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(DB_URI))
session = scoped_session(Session)
Base = declarative_base()

class Titanic(Base):             # Set up a table for SQLAlchemy

    __tablename__ = "passengers"

    uuid                        = Column(Boolean, primary_key=True)
    survived                    = Column(String(5))
    passengerClass              = Column(Integer)
    name                        = Column(String(30))
    sex                         = Column(String(6))
    age                         = Column(Integer)
    siblingsOrSpousesAboard     = Column(Integer)
    parentsOrChildrenAboard     = Column(Integer)
    fare                        = Column(Float)

    def __init__(survived, passengerClass, name, sex, age, siblingsOrSpousesAboard, parentsOrChildrenAboard, fare):

        self.survived                   = survived
        self.passengerClass             = passengerClass
        self.name                       = name
        self.sex                        = sex
        self.age                        = age
        self.siblingsOrSpousesAboard    = siblingsOrSpousesAboard
        self.parentsOrChildrenAboard    = parentsOrChildrenAboard
        self.fare                       = fare

    @classmethod
    def from_json(cls, data):
        return cls(**data)
    
    # Map the key/value pairs
    def to_json(self):
        make_serialized = ['survived', 'passengerClass', 'name', 'sex', 'age', 'siblingsOrSpousesAboard', 'parentsOrChildrenAboard', 'fare']
        d = {}
        for attr in unserialized:
            d[attr] = getattr(self, attr_name)
        return d

# Generate a DB
if __name__ == "__main__":

    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
