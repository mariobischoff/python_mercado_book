import matplotlib.pyplot as plt
import random

aleat = []
for i in range(100):
    x = random.random()
    aleat.append(x)
    
plt.plot(aleat, color='green')
plt.xlabel('eixo horizontal')
plt.ylabel('eixo vertical')
plt.show()

# distribuicao uniforme
aleat = []
for i in range(1000):
    x = random.uniform(-1, 1)
    aleat.append(x)

plt.subplot(211)
plt.plot(aleat, color='red')
plt.xlabel('eixo horizontal')
plt.ylabel('eixo vertical')

plt.subplot(212)
plt.hist(aleat,bins=20,color='gray')
plt.xlabel('classes')
plt.ylabel('frequencia')
plt.show()

aleat = []
for i in range(1000):
    x = random.gauss(0,1)
    aleat.append(x)
