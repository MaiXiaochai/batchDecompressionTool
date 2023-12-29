"""
------------------------------------------
@File       : passwords_repo.py
@CreatedOn  : 2023/12/29
------------------------------------------
"""
from models.passwords import Passwords
from repos.base_repo import BaseRepo


class PasswordsRepo(BaseRepo):
    def __init__(self, session):
        super().__init__(session, Passwords)
        self.column_password = 'password'

    def fetchall_passwords(self):
        return self.fetchall(self.column_password)

    def exist_password(self, password: str):
        """判断是否已经存在该 message_id"""
        # .scalar() 方法，如果查询不到任何结果，它将返回 None
        return self.session.query(self.model.password).filter(self.model.password == password).scalar() is not None
