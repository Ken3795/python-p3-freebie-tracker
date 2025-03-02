from models import Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()


engine.execute("PRAGMA foreign_keys = ON")




company1 = session.query(Company).filter_by(name="TechCorp").first()
if not company1:
    company1 = Company(name="TechCorp", founding_year=2000)
    session.add(company1)

company2 = session.query(Company).filter_by(name="DevSolutions").first()
if not company2:
    company2 = Company(name="DevSolutions", founding_year=2010)
    session.add(company2)

session.commit()  


dev1 = session.query(Dev).filter_by(name="Alice").first()
if not dev1:
    dev1 = Dev(name="Alice", company=company1)
    session.add(dev1)

dev2 = session.query(Dev).filter_by(name="Bob").first()
if not dev2:
    dev2 = Dev(name="Bob", company=company1)
    session.add(dev2)

dev3 = session.query(Dev).filter_by(name="Charlie").first()
if not dev3:
    dev3 = Dev(name="Charlie", company_id=company2.id)
    session.add(dev3)

session.commit()  


freebie1 = session.query(Freebie).filter_by(name="Free Laptop", dev=dev1).first()
if not freebie1:
    freebie1 = Freebie(name="Free Laptop", quantity=5, company=company1, dev=dev1)
    session.add(freebie1)

freebie2 = session.query(Freebie).filter_by(name="Free Phone", dev=dev2).first()
if not freebie2:
    freebie2 = Freebie(name="Free Phone", quantity=10, company=company1, dev=dev2)
    session.add(freebie2)

freebie3 = session.query(Freebie).filter_by(name="Free Tablet", dev=dev3).first()
if not freebie3:
    freebie3 = Freebie(name="Free Tablet", quantity=15, company=company2, dev=dev3)
    session.add(freebie3)

session.commit()  


print("Companies:")
for company in session.query(Company).all():
    print(f"{company.name} ({company.founding_year})")

print("\nDevelopers:")
for dev in session.query(Dev).all():
    print(f"{dev.name} from {dev.company.name}")

print("\nFreebies:")
for freebie in session.query(Freebie).all():
    print(f"{freebie.name} - {freebie.quantity} - {freebie.dev.name} - {freebie.company.name}")

# Close session
session.close()
