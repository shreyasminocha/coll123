from secret import flag
with open("out", "w")as f:f.write("".join(map(lambda x:chr(ord(x)+32768),flag)))
