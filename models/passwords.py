"""
------------------------------------------
@File       : passwords.py
@CreatedOn  : 2023/12/27
------------------------------------------
"""
from sqlalchemy import Column, Integer, String, UniqueConstraint

from models.base import BaseTable


class Passwords(BaseTable):
    __tablename__ = "passwords"

    id = Column(Integer, autoincrement=True)
    password = Column(String(128))

    __table_args__ = (
        UniqueConstraint('password', name='uic_password'),
    )
