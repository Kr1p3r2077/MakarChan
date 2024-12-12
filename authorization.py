from authx import AuthXConfig, AuthX
from jose import jwt
from jose.exceptions import JWTError

config = AuthXConfig()
config.JWT_SECRET_KEY="___LETS TRAAXXX___"
config.JWT_ACCESS_COOKIE_NAME="makarchan_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]
config.JWT_COOKIE_CSRF_PROTECT = False

security = AuthX(config)


def get_user_id_from_token(token: str):
    decoded_token = jwt.decode(token, options={"verify_signature": False}, key=config.JWT_SECRET_KEY)
    id_from_token = decoded_token.get('sub')
    return id_from_token