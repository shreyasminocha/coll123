a=["zero","one","two","three","four","five","six","seven","eight","nine"]
d=['thir','for','fif',a[6],a[7],'eigh',a[9]]
b=[,,"twen",...d].map(_=>_+"ty")
x="teen"
c=["ten","eleven",'twelve',...d.map(_=>_+x)]
c[4]=a[4]+x
_=Math.floor
f=x=>x<10?a[x]:x<20?c[x-10]:x<100?b[_(x/10)]+(x%10?"-"+f(x%10):""):x<1e3?f(_(x/100))+" hundred"+(x%100?" and "+f(x%100):""):"one thousand"
arguments.map(a=>print(f(a)))