from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from ..core.database import Base


class SerialMixIn:
    id = Column(
        Integer, primary_key=True
    )


class users(SerialMixIn, Base):
    __tablename__ = 'users'
    name = Column(String)


class boards(SerialMixIn,Base):
    __tablename__ = 'boards'
    name = Column(String)
    secret = Column(Boolean, default=False)
    color_id = Column(Integer)
    user_id = Column(int, ForeignKey(users.id))

    user = relationship('boards')

class tasks(SerialMixIn, Base):
    __tablename__ = 'tasks'
    name = Column(String)
    completed = Column(Boolean, default=False)

