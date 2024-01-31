from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///gorm_analysis_crud.db')
Base = declarative_base()
class ToDo(Base):
    __tablename__ = 'todo_table'
    id = Column(Integer, primary_key=True)
    task = Column(String(50))
