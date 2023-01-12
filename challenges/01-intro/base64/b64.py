import base64
from secret import flag

print("flag = " + base64.b64encode(flag).decode("utf-8"))
