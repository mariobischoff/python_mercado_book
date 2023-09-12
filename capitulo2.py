import math as mt
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas_datareader.data as pdr

yf.pdr_override()

raio = float(input('Raio: '))
area = mt.pi*raio**2
print(f"Area: {area:.2f}")

x = float(input("x: "))
y = float(input("y: "))
x = 2
y = 3
z = mt.sqrt(x**2+y**2)-mt.log(x)+mt.exp(y)
print("z= ", z)

p1 = float(input("resultado do primeiro dia = "))
p2 = float(input("resultado do segundo dia = "))
retorno = p2 - p1
if retorno >= 0:
    print("lucro")
else:
    print("prejuizo")
    
n = 5
count = 1
s = 0
while count <= n:
    s = s + count
    count = count + 1
    print(s)

x = 0    
count = 1
while x < 100:
    x = count*5
    count+=1
    print(x)

count = 0
n = 50
s = 0
while count <= n:
    if count % 2 == 0:
        s += count
        print(s)
    count += 1
    
nomes=['mário', 'josé', 'mário', 'maria', 'carlos', 'ana', 'mário']
n=len(nomes)
count=1
while count<=n-1:
    if nomes[count] != 'mário':
        print(nomes[count])
    count+=1

n = 5
for i in range(0, n):
    print('bovespa')
    
lista_nomes=['um','dois','tres','quatro','cinco']
nova=[]
for i in range(len(lista_nomes)-1, -1, -1 ):
    nova.append(lista_nomes[i-len(lista_nomes)])

# Calculando o valor do Mini Indice
df = pdr.get_data_yahoo('^BVSP')
df = df.loc['2023-01-01':'2023-01-31']
df.loc[:,'diff'] = df['Adj Close'].diff()
df.dropna(inplace=True)
mini_indice = 0.2
n_contratos = 1
valor = df.loc[:,'diff'][1]*mini_indice*n_contratos
print('Valor R$:', valor)


x = int(input('Digite um numero: '))
if x > 0:
    print('positivo')
else:
    print('negativo')
    
l1 = int(input('lado 1 do triangulo: '))
l2 = int(input('lado 2 do triangulo: '))
l3 = int(input('lado 3 do triangulo: '))
if l1 == l2 and l2 == l3:
    print('equilatero')
elif l1 == l2 or l2 == l3 or l3 == l1:
    print('isosceles')
else:
    print('escaleno')
    
c = 12500
v = 18000
# < 10%
# 10% <> 20%
# > 20%
lucro_percent = ((v - c) / c) * 100 
lucro_percent
if lucro_percent < 10:
    print('lucro menor que 10%')
elif lucro_percent >= 10 and lucro_percent <= 20:
    print('lucro entre 10% e 20%')
else:
    print('lucro maior que 20%')

act_price = 17.3
baixa_historica = 10.5
alta_historica = 24.20
suport = baixa_historica + (alta_historica - baixa_historica) * 0.3
resist = baixa_historica + (alta_historica - baixa_historica) * 0.6
print('suporte: ', suport)
print('resistencia: ', resist)
if act_price >= suport and act_price <= resist:
    print('preco dentro da area de suporte-resistencia')

a=2
b=5
c=1
delta = b**2 - 4*a*c
if delta < 0:
    print('nao ha raizes')
elif delta  == 0:
    x1 = -b / (2*a)
    print('x1=', x1)
else:
    x1 = (-b + mt.sqrt(delta)) / (2 * a)
    x2 = (-b - mt.sqrt(delta)) / (2 * a)
    print('x1=', x1)
    print('x2=', x2)

valor_compra = 1001
if valor_compra <= 20:
    valor_compra += - valor_compra * 0.05
elif valor_compra > 20 and valor_compra <= 50:
    valor_compra += - valor_compra * 0.1
elif valor_compra > 50 and valor_compra <= 100:
    valor_compra += - valor_compra * 0.15
elif valor_compra > 100 and valor_compra <= 1000:
    valor_compra += - valor_compra * 0.20
else:
    valor_compra += - valor_compra * 0.3
print(valor_compra)

n = int(input('n: '))
vendas_par = []
vendas_impar = []
for i in range(n):
    valor = int(input('valor: '))
    if valor % 2 == 0:
        vendas_par.append(valor)
    else:
        vendas_impar.append(valor)
print('SP: ', sum(vendas_par))
print('SI: ', sum(vendas_impar))

n = 4
s = 0
for i in range(1, n+1):
    s += (71 - i) / (7 * i)
print(s)

n = 4
count_par = 0
count_impar = 0
soma = 0
for i in range(n):
    valor = int(input('n: '))
    soma += valor
    if valor % 2 == 0:
        count_par += 1
    else:
        count_impar += 1
print('pares: ', count_par)
print('impares: ', count_impar)
print('soma: ', soma)

n = 2
x = 8
s = 0
for i in range(1, n):
    s += x**(i+2) / (i+2) * mt.factorial(i)
print(s)

def find_pi():
    pi = 0
    count = 1
    sum = True
    while abs(pi - mt.pi) > 0.001:
        if sum:
            pi += (4 / count)
        else:
            pi -= ( 4 / count)
        count = count + 2
        sum = not sum
    return pi

count = 1
n = 4
s = 0
num = 1
while count <= n:
    s += num / count
    num += 2
    count += 1
s

lista = ['bbdc4', 'itub4', 'petr4', 'petr4', 'bbas3', 'petr4', 'sanb4', 'petr4', 'bpac3', 'petr4']
c = len(lista)
i = 0
while i < c:
    i += 1
    if lista[i - 1] == 'petr4': continue
    print('Ação de Banco: ', lista[i - 1])
    
    
lista = ['bbdc4', 'itub4', 'petr4', 'petr4', 'bbas3', 'petr4', 'sanb4', 'petr4', 'bpac3', 'petr4']
i = 0
while i < len(lista):
    if lista[i] == 'petr4':
        break
    i += 1
print('Petrobras aparece pela primeira vez no indice: ', i)

lista = ['bbdc4', 'itub4', 'petr4', 'petr4', 'bbas3', 'petr4', 'sanb4', 'petr4', 'bpac3', 'petr4']
c = 0
i = 0
while i < len(lista):
    if lista[i] == 'petr4' and c == 1:
        break
    elif lista[i] == 'petr4':
        c+=1
    i += 1
print('Petrobras aparece a segunda vez no indice: ', i)

palavras = [['comprar','vender'],['manter', 'alertar','indicar'], ['tendencia','crash','lucro']]
for i in palavras:
    print(i)

palavras = [['comprar','vender'],['manter', 'alertar','indicar'], ['tendencia','crash','lucro']]
for i in palavras:
    for j in i:
        print(j)
        
import statistics as st
lista = [[1,2,-1],[3,-1,4,],[0,0,1,2,-1],[-1,-1,2,2,-1,2,-1],[3,2,0],[1,1,-1,0,2]]
nova_lista = []
for i in lista:
    for j in i:
        nova_lista.append(j)
print(nova_lista)
print(sum(nova_lista))
print(max(nova_lista))
print(min(nova_lista))
print(st.mean(nova_lista))
print(st.mode(nova_lista))
print(st.pstdev(nova_lista))

lista = [['ontem','hoje','amanha'],['sp','rj','mg','ce'],['sao paulo','rio','santos','cuiaba']]
nova_lista = []
for i in lista:
    for j in i:
        nova_lista.append(j)
nova_lista.extend(['ferias','negocios'])
nova_lista.sort()
nova_lista

let = ['a','b','c','a','d','f','a','b','b','d','c']
new_let = []
for i in let:
    if not i in new_let:
        new_let.append(i)
new_let