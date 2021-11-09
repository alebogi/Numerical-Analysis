#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math 
from decimal import *


# Uvodimo klasu kojom predstavljamo razlomak (razlomak je oblika p/q):

# In[2]:


class Fraction: #p/q
    def __init__(self, p, q):
        self.p = p
        self.q = q
        
    def set_p(self, p): #brojilac
        self.p = p
    def set_q(self, q): #imenilac
        self.q = q 
        
    def set_e1(self, alpha): #vrednost apsolutne greske, za racunanje prve vrste
        self.e1 = np.absolute(alpha-self.p/self.q)
    
    def set_e2(self, alpha): #vrednost apsolutne greske, za racunanje druge vrste
        self.e2 = np.absolute(self.q*alpha-self.p)
        
    def printFr(self):
        res = str(self.p) + "/" + str(self.q)
        return res
    
    def verizniRazlomak(self):  #algoritam za racunanje veriznog razlomka
        k = 10
        self.verizni = []
        x0 = Decimal(self.p/self.q)
        a0 = Decimal(math.floor(Decimal(x0)))
        d0 = Decimal(x0 - a0)
        x=[]
        x.append(x0)
        a=[]
        a.append(a0)
        self.verizni.append(a0)
        d=[]
        d.append(d0)
        
        
        for i in range(1,k):
            if d[i-1] <= 0.00000001:
                break
            xx = Decimal(1 / d[i-1])
            x.append(xx)
            
            aa = Decimal(math.floor(xx))
            a.append(aa)
            self.verizni.append(aa)
            
            dd = Decimal(xx - aa)
            d.append(dd)
        
        last_index = len(a)-1
        if a[last_index] == 1:
            a[last_index - 1] = a[last_index - 1] + 1
            self.verizni[last_index - 1] = self.verizni[last_index - 1] + 1
            del a[last_index]
            del self.verizni[last_index]
            
        return
    
    def printVerizni(self):
        res = "["
        for i in range(len(self.verizni)):
            res = res + str(self.verizni[i])
            if(i==0 and len(self.verizni)>1):
                res = res + ";"
            else:
                if i!=len(self.verizni)-1:
                    res = res + "," 
        res = res + "]"
        return res


# Uvodimo nizove gde cemo smestati:
# all_fractions - sve razlomke p/q
# best_first - najbolje racionalne aproksimacije prve vrste
# best_second - najbolje racionalne aproksimacije druge vrste

# In[3]:


all_fractions = []
best_first = []
best_second = []


# Uvodimo promenljivu u kojoj cemo cuvati minimalnu gresku i koji razlomak daje tu gresku

# In[4]:


e1_min = float("inf")
e2_min = float("inf")


# Unosimo vrednosti alfa, n i m.
# alfa=2.2955871
# n = 1
# m = 15

# In[5]:


badInput = True
while badInput:
    alpha = float(input("Uneti realan broj: "))
    n = int(input("Uneti vrednost n: "))
    m = int(input("Uneti vrednost m, tako da je n<m: "))
    if(n>=m):
        print("Nije ispunjen uslov n<m! Ponovite unos.")
    else:
        badInput = False


# Algoritam za ispis razlomaka p/q:
# Formiramo niz razlomaka (all_fractions) oblika p/q, tako da je:
#     q = (n, n+1, n+2,..,m) 
#     p = alpha * q, zaokruzeno na najblizi prirodan broj

# In[6]:


for q in range(n, m+1):
    p = int(np.round(alpha*q))
    fr = Fraction(p, q)
    fr.set_e1(alpha)
    fr.set_e2(alpha)
    fr.verizniRazlomak()
    all_fractions.append(fr)


# Ispis razlomaka i greske:

# In[7]:


for i in range(len(all_fractions)):
    print(all_fractions[i].printFr() + " " + all_fractions[i].printVerizni()  + 
          "  e1 = "+ str(all_fractions[i].e1) +"  e2 = "+ str(all_fractions[i].e2))
    


# Sortiranje i ispis liste po uslovu minimalnosti apsolutne greske |alpha-p/q|:

# In[8]:


sorted_all_fr = sorted(all_fractions, key=lambda fr : fr.e1)
print("Sortirana lista razlomaka po minimalnosti apsolutne greske e=|alpha-p/q| :")
for i in range(len(sorted_all_fr)):
    print(sorted_all_fr[i].printFr()+ " " + sorted_all_fr[i].printVerizni()  +"  e1 = "+ str(sorted_all_fr[i].e1))


# Sortiranje i ispis liste po uslovu minimalnosti apsolutne greske |alpha*q-p|:

# In[9]:


sorted_all_fr2 = sorted(all_fractions, key=lambda fr : fr.e2)
print("Sortirana lista razlomaka po minimalnosti apsolutne greske e=|alpha*q-p| :")
for i in range(len(sorted_all_fr)):
    print(sorted_all_fr2[i].printFr()+ " " + sorted_all_fr2[i].printVerizni()  +"  e2 = "+ str(sorted_all_fr2[i].e2))


# Trazimo verizne razlomke za datu konstantu alpha:

# In[10]:


k = m-n
alpha_verizni=[]

x0 = Decimal(alpha)
a0 = Decimal(math.floor(Decimal(x0)))
d0 = Decimal(x0 - a0)
x=[]
x.append(x0)
a=[]
a.append(a0)
alpha_verizni.append(a0)
d=[]
d.append(d0)


for i in range(1,k):
    if d[i-1] <= 0.000000000000000000000000000000000000000001:
        break
    xx = Decimal( 1 / d[i-1])
    x.append(xx)
    aa = Decimal(math.floor(Decimal(xx)))
    a.append(aa)
    alpha_verizni.append(aa)

    dd = Decimal(xx - aa )
    d.append(dd)
    
last_index = len(a)-1
if a[last_index] == 1:
    a[last_index - 1] = a[last_index - 1] + 1
    alpha_verizni[last_index - 1] = alpha_verizni[last_index - 1] + 1
    del a[last_index]
    del alpha_verizni[last_index]
    
res = "["
for i in range(len(alpha_verizni)):
    res = res + str(alpha_verizni[i])
    if(i==0 and len(alpha_verizni)>1):
        res = res + ";"
    else:
        if i!=len(alpha_verizni)-1:
            res = res + "," 
res = res + "]"
print(res)


# Trazimo aproksimacije prve i druge vrste:
# 

# In[11]:


for i in range(0, len(all_fractions)):
    fr = all_fractions[i]
    if fr.e2 < e2_min:
        e2_min = fr.e2
        best_second.append(fr)
        if fr.e1 < e1_min:
            e1_min = fr.e1
        continue
    if fr.e1 < e1_min:
        e1_min = fr.e1
        best_first.append(fr)


# Ispis prve vrste:

# In[12]:


print("APROKSIMACIJE PRVE VRSTE:")
for fr in best_first:
    print(fr.printFr() + " " + fr.printVerizni()  + "  e1 = "+ str(fr.e1) +"  e2 = "+ str(fr.e2))

print("Sortirano:")
sorted_best_first = sorted(best_first, key=lambda fr : fr.e1)
for fr in sorted_best_first:
    print(fr.printFr() + " " + fr.printVerizni()  + "  e1 = "+ str(fr.e1) +"  e2 = "+ str(fr.e2))


# Ispis druge vrste:

# In[13]:


print("APROKSIMACIJE DRUGE VRSTE:")
for fr in best_second:
    print(fr.printFr() + " " + fr.printVerizni()  + "  e1 = "+ str(fr.e1) +"  e2 = "+ str(fr.e2))

print("Sortirano:")
sorted_best_second = sorted(best_second, key=lambda fr : fr.e1)
for fr in sorted_best_second:
    print(fr.printFr() + " " + fr.printVerizni()  + "  e1 = "+ str(fr.e1) +"  e2 = "+ str(fr.e2))


# Konacan ispis:

# In[14]:


for fr in sorted_all_fr:
    if fr in best_first:
        print(fr.printFr() + " " + fr.printVerizni()  + "  e1 = "+ str(fr.e1) + "   I")
    elif fr in best_second:
         print(fr.printFr() + " " + fr.printVerizni()  + "  e1 = "+ str(fr.e1) + "  II")
    else:
         print(fr.printFr() + " " + fr.printVerizni()  + "  e1 = "+ str(fr.e1) + "  N")


