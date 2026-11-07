# make_token.py - creates a 1-hour test JWT using the secret from the environment
import os
import datetime
import jwt
secret = os.environ["JWT_SECRET"]
payload = {
   "sub": "testuser",
   "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1),
}
print(jwt.encode(payload, secret, algorithm="HS256"))
