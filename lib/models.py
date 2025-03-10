from sqlalchemy import create_engine,Boolean,Integer,Column,String,ForeignKey,select
from sqlalchemy.orm import relationship,sessionmaker,declarative_base

Base=declarative_base()
engine=create_engine('sqlite:///theater.db')
class Theater (Base):
    __tablename__='theaters'
    id=Column(Integer,primary_key=True)
    name=Column(String)
class Audition(Base):
    __tablename__= 'auditions'
    id=Column(Integer,primary_key=True)
    actor=Column (String)
    location=Column(String)
    phone=Column(Integer)
    hired =Column(Boolean, default=False)
    role_id=Column(Integer,ForeignKey('roles.id'))
    #relationship(one-to-many)
    role=relationship("Role",back_populates= "auditions")
    def __repr__(self) -> str:
        return f"{self.actor} -{self.location}"

class Role (Base):
    __tablename__='roles'
    id=Column(Integer,primary_key=True)
    character_name=Column (String(20))
    auditions=relationship("Audition",back_populates="role")
#checking auditions for the role and filters the hired 
def lead(self):
    hired_auditions =[a for a in self.auditions if a.hired]
    if hired_auditions:
        return hired_auditions[0]
    return 'no actor has been hired for this role!'
#checks atleast two hired auditions
def understudy (self):
    hired_auditions=[a for a in self.auditions if a.hired]
    if len (hired_auditions)>=2:
        return hired_auditions[1]
    return 'no actor has ben hired for this role'

def actors(self):
    return [audition.actor for audition in self.auditions]
def location(self):
    return[audition.location for audition in self.auditions]
                 
Base.metadata.create_all(engine)
print("Tables created!")
session=sessionmaker(bind=engine)
session=session()
#adding roles
new_role=Role (character_name="Meech")
session.add(new_role)
session.commit()
audition1=Audition(actor="Daphine Michere",location="Nairobi",phone=23456,hired=True,role=new_role)
audition2=Audition(actor="Joy Mutanu",location="Rwaka",phone=1234567,hired=False,role=new_role)
audition3=Audition(actor="Mirriam Yego",location="Kilimani",phone=987654,hired=True,role=new_role)
session.add_all([audition1,audition2,audition3])
session.commit()
x=select(Audition)
for audition in session.scalars(x):
  print(audition)
