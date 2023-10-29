from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base


class SerialMixIn:
    id = Column(
        Integer, primary_key=True
    )


class User(SerialMixIn, Base):
    __tablename__ = 'users'
    name = Column(String)

    boards = relationship('Board')


class Board(SerialMixIn, Base):
    __tablename__ = 'boards'
    name = Column(String)
    secret = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey(User.id))
    color_id = Column(Integer)
    users = relationship('User')
    tasks = relationship('Task')


class Task(SerialMixIn, Base):
    __tablename__ = 'tasks'
    name = Column(String)
    completed = Column(Boolean, default=False)
    completed_date = Column(DateTime(timezone=True))
    start_date = Column(DateTime(timezone=True), default=func.now())
    estimated_date = Column(DateTime(timezone=True))
    task_priority = Column(Integer, default=0)
    color_id = Column(Integer)
    board_id = Column(Integer, ForeignKey(Board.id))

    board = relationship('Board')
