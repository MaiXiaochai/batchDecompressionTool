"""
------------------------------------------
@File       : passwords.py
@CreatedOn  : 2023/12/27
------------------------------------------
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, text, UniqueConstraint

from models.base import Base


class Passwords(Base):
    __tablename__ = "passwords"

    id = Column(Integer, autoincrement=True)
    password = Column(String(128))
    # CURRENT_TIMESTAMP,in MySQL out: 2022-10-29 11:28:02
    created_on = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), comment="密码创建时间")

    __table_args__ = (
        UniqueConstraint('password', name='uic_password'),
    )
