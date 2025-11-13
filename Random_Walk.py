import numpy as np
import numpy.random as rnd
from matplotlib import pyplot as plt
from scipy.stats import norm as nm

N=1000
M=300
p_r= 0.5
l=1

time= np.linspace(0,M, M)
scoring= []
avg= [0]*M
for j in range(N):
    x=[0]
    for i in range(M-1):
       c= rnd.uniform(0,1)
       if c<p_r:
          x.append(x[i]+l)
       else:
          x.append(x[i]-l)
       avg[i+1]+= x[i+1]
    scoring.append(x[M-1])
    plt.step(time, x, alpha= 0.4)

for i in range(M):
   avg[i]= avg[i]/N

m, b= np.polyfit(time, avg, 1)
reg= m*time + b

scoring_= np.array(scoring)
num= (scoring_.max()-scoring_.min())/len(scoring_)
rge= np.arange(scoring_.min(), scoring_.max(), )
pdf= nm.pdf(rge, loc= np.average(scoring_), scale= (np.var(scoring_))**0.5)

plt.plot(time, avg, color= 'black', label= 'Posició Mitja')
plt.plot(time, reg, color= 'aqua', linestyle= '--', label= 'Recta de Regressió')
plt.title('Trajectòries Individuals de %i' %N + ' partícules amb p= %s' %p_r)
plt.xlabel('Temps')
plt.ylabel('x(t)')
plt.legend()
plt.show()
plt.title('Histograma Normalitzat de les Posicions Finals')
plt.ylabel('Freqüència')
plt.xlabel('Posicions')
plt.plot(rge, pdf, color= 'black', label= 'FDP Ajustada')
plt.hist(scoring, bins=20, color= 'lightgreen', edgecolor='black', density= True)
plt.show()