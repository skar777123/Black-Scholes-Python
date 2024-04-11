import math as m
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm 
fig, ax = plt.subplots()

S = 2000    # Stock Price
K = 2100    # Strike Price
T = 1       # Time to Maturity in Years
r = 0.1     # Risk-free Rate
sd= 0.2     # Standard Deviation / volatility
Mp= (S/10)  # Market Premium Price

d1 = (m.log(S/K)+(r + 0.5 * sd**2)*T)/(sd* m.sqrt(T))
d2 = d1 - (sd* m.sqrt(T))

call = S * norm.cdf(d1) - K * m.exp(-r * T) * norm.cdf(d2)
put = K * m.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

if (call > Mp or put):
      a = "H0: We should place Call Option"
      pf= call - Mp 
else:
      a = "Ha: We should place Put Option"
      pf= put - Mp

ax.plot([1,100], [1,call], label= 'Call')
ax.plot([1,100], [1,put], label='Put')
ax.plot([1,100], [1,Mp], label='Market Premium')
ax.text(0,100, 'Market Premium: %s\n\n The value of d1 : %s\n The value of d2 : %s \n\n The Price of Call option : Rs. %s \n The Price of Put option : Rs. %s \n\n %s \n Profit of Rs. %s' % (Mp,round(d1,4),round(d2,4),round(call,2), round(put,2),a, round(pf,2)))
ax.set_title('Black-Scholes-Merton Model')
ax.legend()
plt.show()

