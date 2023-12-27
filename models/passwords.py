"""
------------------------------------------
@File       : passwords.py
@CreatedOn  : 2023/12/27
------------------------------------------
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, text

from models.base import Base


class Passwords(Base):
    __tablename__ = "passwords"

    password = Column(String(128), primary_key=True)
