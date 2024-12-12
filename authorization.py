from authx import AuthXConfig, AuthX

config = AuthXConfig()
config.JWT_SECRET_KEY="___LETS TRAAXXX___"
config.JWT_ACCESS_COOKIE_NAME="makarchan_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]
config.JWT_COOKIE_CSRF_PROTECT = False

security = AuthX(config)