from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Questions(Base):

    __tablename__='questions'
    id = Column(Integer, primary_key=True)
    topic = Column(String(200))
    title = Column(String(200))
    question = Column(String(200))
    op_a = Column(String(150))
    op_b = Column(String(150))
    op_c = Column(String(150))
    op_d = Column(String(150))
    answer = Column(String(150))

    @property
    def serialize(self):

        return{
            'id':self.id,
            'topic':self.topic,
            'title':self.title,
            'question':self.question,
            'op_a':self.op_a,
            'op_b':self.op_b,
            'op_c':self.op_c,
            'op_d':self.op_d,
            'answer':self.answer,
        }

engine = create_engine("mysql+mysqlconnector://root:abc123@localhost/question_chatbot")
Base.metadata.create_all(bind=engine)