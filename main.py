import math as m
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm 


S = 2000    # Stock Price
K = 2000    # Strike Price
T = 1       # Time to Maturity in Years
r = 0.1     # Risk-free Rate
sd= 0.2     # Standard Deviation / volatility
Mp= (S/10)  # Market Price Premium 

d1 = (m.log(S/K)+(r + 0.5 * sd**2)*T)/(sd* m.sqrt(T))
d2 = d1 - (sd* m.sqrt(T))

call = S * norm.cdf(d1) - K * m.exp(-r * T) * norm.cdf(d2)
put = K * m.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

print()
print("Market price:",Mp)
print()
print("The value of d1 : ", round(d1,4))
print("The value of d2 : ", round(d2,4))
print()
print("The Price of Call option : Rs.", round(call,2))
print()
print("The Price of Put option : Rs.", round(put,2))

if (call > Mp or put):
      print()
      print("H0: We should place Call Option")
else:
      print()
      print("Ha: We should place Put Option")

fig, ax = plt.subplots()
ax.plot([1,100], [1,call], label='Call')
ax.plot([1,100], [1,put], label='Put')
ax.plot([1,100], [1,Mp], label='Market Premium')
ax.set_xlabel('Stock Price')
ax.set_ylabel('Option Price')
ax.set_title('Black-Scholes-Merton Model')
ax.legend()
plt.show()

