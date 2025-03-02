from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    founding_year = Column(Integer, nullable=False)
    
   
    devs = relationship('Dev', back_populates='company', cascade='all, delete-orphan')
    
    
    freebies = relationship('Freebie', back_populates='company', cascade='all, delete-orphan')

    def __init__(self, name, founding_year):
        self.name = name
        self.founding_year = founding_year

    def give_freebie(self, dev, freebie_name, quantity):
       
        freebie = Freebie(name=freebie_name, quantity=quantity, company=self, dev=dev)
        self.freebies.append(freebie)  
        dev.freebies.append(freebie)   
        return freebie


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    
    company_id = Column(Integer, ForeignKey('companies.id'))

   
    company = relationship('Company', back_populates='devs')

   
    freebies = relationship('Freebie', back_populates='dev')

    


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    
    company_id = Column(Integer, ForeignKey('companies.id'))
    dev_id = Column(Integer, ForeignKey('devs.id'))

   
    company = relationship('Company', back_populates='freebies')
    dev = relationship('Dev', back_populates='freebies')

    def __init__(self, name, quantity, company, dev):
        self.name = name
        self.quantity = quantity
        self.company = company
        self.dev = dev



engine = create_engine('sqlite:///freebies.db', echo=True)


Base.metadata.create_all(engine)
