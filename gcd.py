def gcd(a,b):
    return gcd(b,a%b) if a%b!=0 else b

# 輾轉相除法求GCD原理
# 若 a = bq + r
# 則 gcd(a,b) == gcd(b,r)
