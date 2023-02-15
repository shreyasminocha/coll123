from itertools import starmap
from secret import flag
l=list(enumerate(map(lambda n:128-n,map(ord,flag))))
with open("out", "w")as f:f.write(str(list(starmap(lambda a,b:a*b,filter(lambda n:n[0]&1,l)))+list(starmap(lambda a,b:a+b,filter(lambda n:2+~(n[0]&1),l)))))
