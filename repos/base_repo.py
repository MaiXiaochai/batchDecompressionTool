"""
------------------------------------------
@File       : base_repo.py
@CreatedOn  : 2023/12/29
------------------------------------------
"""
from abc import ABC
from sqlalchemy.exc import SQLAlchemyError

from utils import log


class BaseRepo(ABC):
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def add(self, model_data_obj):
        try:
            self.session.add(model_data_obj)
            self.commit()

        except SQLAlchemyError as err:
            log.error(str(err))
            self.session.rollback()

    def fetchall(self, column: str):
        """获取该model的column的所有值"""
        result = self.session.query(getattr(self.model, column)).all()
        if result:
            result = [x[0] for x in result]

        return result

    def commit(self):
        self.session.commit()
