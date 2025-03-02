from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    founding_year = Column(Integer, nullable=False)
    
    # Relationship: A company can have many developers
    devs = relationship('Dev', back_populates='company', cascade='all, delete-orphan')
    
    # Relationship: A company can give many freebies
    freebies = relationship('Freebie', back_populates='company', cascade='all, delete-orphan')

    def __init__(self, name, founding_year):
        self.name = name
        self.founding_year = founding_year

    def give_freebie(self, dev, freebie_name, quantity):
        # Create a new freebie and associate it with the company and dev
        freebie = Freebie(name=freebie_name, quantity=quantity, company=self, dev=dev)
        self.freebies.append(freebie)  # Add to company's freebies
        dev.freebies.append(freebie)   # Add to dev's freebies
        return freebie


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Foreign key to the company that the developer works for
    company_id = Column(Integer, ForeignKey('companies.id'))

    # Relationship: A dev belongs to a company
    company = relationship('Company', back_populates='devs')

    # Relationship: A dev can receive many freebies
    freebies = relationship('Freebie', back_populates='dev')

    # No need to manually define __init__ since SQLAlchemy handles it automatically


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    # Foreign keys to associate the freebie with a company and dev
    company_id = Column(Integer, ForeignKey('companies.id'))
    dev_id = Column(Integer, ForeignKey('devs.id'))

    # Relationships: A freebie belongs to a company and a developer
    company = relationship('Company', back_populates='freebies')
    dev = relationship('Dev', back_populates='freebies')

    def __init__(self, name, quantity, company, dev):
        self.name = name
        self.quantity = quantity
        self.company = company
        self.dev = dev


# Create an SQLite database in memory for testing (or you can specify a file path)
engine = create_engine('sqlite:///freebies.db', echo=True)

# Create the tables in the database
Base.metadata.create_all(engine)
