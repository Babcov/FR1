# Создайте файл models.py для определения моделей данных с помощью ORM (например, SQLAlchemy)
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String(12))
    operator_code = Column(Integer)
    tag = Column(String(50))
    timezone = Column(String(50))

class Mailing(Base):
    __tablename__ = 'mailings'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Добавьте остальные атрибуты для модели рассылки

class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Добавьте остальные атрибуты для модели сообщения
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String(12), nullable=False)
    operator_code = Column(String(10))
    tag = Column(String(50))
    timezone = Column(String(50))


class Mailing(Base):
    __tablename__ = 'mailings'

    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    message = Column(String(255), nullable=False)
    # Добавьте остальные атрибуты рассылки

    filter_client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    clients = relationship('Client', backref='mailings')


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    creation_time = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False)
    # Добавьте остальные атрибуты сообщения

    mailing_id = Column(Integer, ForeignKey('mailings.id'), nullable=False)
    mailing = relationship('Mailing', backref='messages')
