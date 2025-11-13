from secrets import token_urlsafe, token_hex
import os

class FlaskConfig:
	SECRET_KEY = token_hex(32)
	AUTH_USERS = {
    	"keno": token_urlsafe(16),
    	"tenk": token_urlsafe(16)
	}
	FLAG = os.environ.get('FLAG','bctf{fake_flag_for_testing}')
	# print(AUTH_USERS)
