"""
------------------------------------------
@File       : base_repo.py
@CreatedOn  : 2023/12/27
------------------------------------------
"""
from sqlalchemy import Column, DateTime, text, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseTable(Base):
    # CURRENT_TIMESTAMP,in MySQL out: 2022-10-29 11:28:02
    created_on = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), comment="密码创建时间")
    updated_on = Column(DateTime, default=func.now(), onupdate=func.now())
