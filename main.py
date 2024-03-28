import math as m
from scipy.stats import norm 

S = 2300 # Underlying Price
K = 2200 # Strike Price
T = 0.5 #  Time to Maturity in Years
r = 0.1 # Risk-free Rate
sd= 0.2  # Standard Deviation / volatility

d1 = (m.log(S/K)+(r + 0.5 * sd**2)*T)/(sd* m.sqrt(T))
d2 = d1 - (sd* m.sqrt(T))

call = S * norm.cdf(d1) - K * m.exp(-r * T) * norm.cdf(d2)
put = K * m.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

print("The value of d1 : ", round(d1,4))
print("The value of d2 : ", round(d2,4))
print("The Price of Call option : Rs.", round(call,2))
print("The Price of Put option : Rs.", round(put,2))