import math

def co_eff(a,b,n,r,ex):

    if r<0:
        return ex

    else:

        constant = math.comb(n,r)*a**(r)*b**(n-r)
        ex += f'+{constant}(x^{r})(y^{n-r})'

        return co_eff (a,b,n,r-1,ex)

a, b, n = input().split(",")
a = int(a)
b = int(b)
n = int(n)
ex=f'{a**n}(x^{n})(y^0)'
print()
print(f'({a}x+{b}y)^{n} = {co_eff (a,b,n,n-1,ex)}')
