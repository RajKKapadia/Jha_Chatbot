from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

from databaseSetup import Questions, Base

engine = create_engine("mysql+mysqlconnector://root:abc123@localhost/question_chatbot")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

questions = pd.read_csv("Questions.csv")

insert_que = Questions()

for i in range(len(questions)):

    que = questions.iloc[i]
    insert_que.topic = que.Topic
    insert_que.title = que.Titles
    insert_que.question = que.Question
    insert_que.op_a = que.OptionA
    insert_que.op_b = que.OptionB
    insert_que.op_c = que.OptionC
    insert_que.op_d = que.OptionD
    insert_que.answer = que.Answer

    try:
        session.add(insert_que)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

print("All data added successfully.")