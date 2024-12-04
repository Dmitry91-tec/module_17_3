from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String
engine = create_engine("sqlite:///taskmaneger.db", echo = True)

SessionLocal =sessionmaker(bind=engine)

class Base(DeclarativeBase):                 #базовый класс, сопоставляет классы моделей и таблицы БД
    pass
