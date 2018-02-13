
# coding: utf-8

# In[1]:


#calculo de moda y media 
import statistics as stats
print ("VALORES ALMACENADOS ESTATICAMENTE")
valor = [ 3 , 11, 6, 3, 2, 5 , 24, 9, 12, 20 ]
print (valor)
print (" ")
totaldata= len(valor)
print ("Total valores almacenados : ", totaldata)
print (" ")


#calculo de moda
numdata = 0
for i  in valor:
    numNew = valor.count(i)
    if numNew > numdata:
        numdata = numNew 

modas = []
for i in valor:
    numNew = valor.count(i)
    if numNew == numdata and i not in modas:
        modas.append(i)
        print ("Su respectiva moda", modas)
        
        
#calculo de mediana
valor.sort()

if len(valor) % 2 == 0:
    num = len(valor)
    mediana = (valor[num//2-1]+ valor[num//2] )//2
else:
         mediana =valor[len(valor)//2]
print ("Mediana es:", mediana)  

#calculo de varianza
print ("Varianza", (stats.pvariance(valor)))


#calculo de Covarianza
print ("Couvarianza", (stats.stdev(valor)))

