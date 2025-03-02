#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

# Connect to the database
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()


import ipdb; ipdb.set_trace()


company = Company(name="TechCorp", founding_year=2005)
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")


session.add(company)
session.add(dev1)
session.add(dev2)
session.commit()


company.give_freebie(dev1, "T-Shirt", 10)


freebie = session.query(Freebie).first()
print(freebie.print_details())  


print(dev1.received_one("T-Shirt"))  


dev1.give_away(dev2, freebie)


print(freebie.dev.name)  
