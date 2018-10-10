from decimal import *
getcontext().prec = 100
import matplotlib.pyplot as plt

data = []
phi = (1 + Decimal(5).sqrt())/2 
for n in range(0,100):
    phi_n = phi**n
    data.append(phi_n - phi_n.to_integral_value())


plt.plot(data)
plt.show()

plt.plot([abs(datum).log10() for datum in data])
plt.show()
