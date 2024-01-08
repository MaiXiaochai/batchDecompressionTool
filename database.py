"""
------------------------------------------
@File       : database.py
@CreatedOn  : 2023/12/29
------------------------------------------
"""
import logging
from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from config import settings as cfg
from models.base import Base
from utils import log


uri = f"mysql+pymysql://{cfg.db.user}:{quote(cfg.db.passwd)}@{cfg.db.host}:{cfg.db.port}/att?charset={cfg.db.charset}"
engine = create_engine(
    uri,
    pool_recycle=cfg.db.pool_recycle,
    pool_pre_ping=cfg.db.pool_pre_ping
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 考虑到线程安全，可以使用scoped_session
db_session = scoped_session(SessionLocal)

# 创建表
try:
    Base.metadata.create_all(engine)
except Exception as err:
    log.error(err)
