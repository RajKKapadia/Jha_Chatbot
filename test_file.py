from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):

    __tablename__='user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    @property
    def serialize(self):

        return{
            'id':self.id,
            'name':self.name,
            'email':self.email
        }

engine = create_engine("mysql+mysqlconnector://root:abc123@localhost/SQLAlchemy")
Base.metadata.create_all(bind=engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = DBSession()


user = User(name='krupesh', email='krupesh@raj.com')
session.add(user)
session.commit()