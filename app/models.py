from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension
from db_ready import make_db_ready

DB_URI = "sqlite:///titanic.db"

Session = sessionmaker(autocommit=False, autoflush=False, bind=create_engine(DB_URI))
session = scoped_session(Session)
Base = declarative_base()


class Titanic(Base):  # defines a model for SQLAlchemy

    __tablename__ = "passengers"
    __table_args__ = {"sqlite_autoincrement": True}

    uuid = Column(String(36), primary_key=True)
    survived = Column(Boolean)
    passengerClass = Column(Integer)
    name = Column(String(30))
    sex = Column(String(6))
    age = Column(Integer)
    siblingsOrSpousesAboard = Column(Integer)
    parentsOrChildrenAboard = Column(Integer)
    fare = Column(Float)

    @classmethod
    def from_json(cls, data):
        return cls(**data)

    # Map the key/value pairs
    def to_json(self):
        make_serialized = [
            "uuid",
            "survived",
            "passengerClass",
            "name",
            "sex",
            "age",
            "siblingsOrSpousesAboard",
            "parentsOrChildrenAboard",
            "fare",
        ]
        d = {}
        for attr in unserialized:
            d[attr] = getattr(self, attr_name)
        return d


# Generate a DB
if __name__ == "__main__":

    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    make_db_ready("titanic.csv", engine, Titanic.__tablename__, "replace")
