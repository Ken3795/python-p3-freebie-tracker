#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

# Connect to the database
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Enter the interactive debugger
import ipdb; ipdb.set_trace()

# Create some sample data to test
company = Company(name="TechCorp", founding_year=2005)
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

# Add company and devs to the session
session.add(company)
session.add(dev1)
session.add(dev2)
session.commit()

# Give a freebie to Alice
company.give_freebie(dev1, "T-Shirt", 10)

# Check if the freebie was added correctly
freebie = session.query(Freebie).first()
print(freebie.print_details())  # Should print: Alice owns a T-Shirt from TechCorp

# Test if Alice has received a T-Shirt
print(dev1.received_one("T-Shirt"))  # Should return True

# Give Alice's T-Shirt to Bob
dev1.give_away(dev2, freebie)

# Verify if the freebie was given away
print(freebie.dev.name)  # Should print: Bob
