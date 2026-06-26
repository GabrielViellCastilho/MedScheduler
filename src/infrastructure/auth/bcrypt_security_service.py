from passlib.context import CryptContext
from src.domain.services.security_service import SecurityService


class BcryptSecurityService(SecurityService):

    def __init__(self):
        self.pwd_context = CryptContext(
            schemes=["bcrypt"],
            deprecated="auto"
        )

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password[:72])

    def verify_password(self, password: str, hashed: str) -> bool:
        return self.pwd_context.verify(password[:72], hashed)