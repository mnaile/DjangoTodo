
from django.conf import settings
from to_do.settings import SECRET_KEY
import jwt


def jwt_decode_handler(token):
    secret_key = SECRET_KEY

    return jwt.decode(
        token, 
        secret_key,
        audience=settings.SIMPLE_JWT.get("AUDIENCE"),
        issuer=settings.SIMPLE_JWT.get("ISSUER"),
        algorithms=[settings.SIMPLE_JWT.get("ALGORITHM")]
        )