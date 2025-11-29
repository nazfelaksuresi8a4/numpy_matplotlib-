"""Gerekli Modüller"""
import matplotlib.pyplot as plt
import numpy as np 

"""Arraylar"""
x_array = []
y_array = []

"""üs değeri"""
nm = 2

"""fonksiyon"""
def f(x):       
    x_array.append(1.1*x - 1 ** nm)     
    y_array.append(1.1*x - 1 ** nm)

"""sayılar(degerler)"""
vals = [i for i in range(-10,15)]
sorted_ = sorted(vals)

"""degerlerin medyan sayısı"""
median = sorted_[len(sorted_) // 2] 

"""Döngü"""
for q in vals:
    f(q) #fonksiyon çağırsı

    plt.plot(x_array,y_array) #her çağrıda çizilen fonsksiyon grafiği
    plt.annotate(text='A',xy=(median,median),color='blue') #fonksiyona verilen degerlerin medyan sayısına A markerini koy

"""Kartezyen İslemleri"""
plt.axhline(y=0,color='black')  #dik kartezyen ekseni(y)
plt.axvline(x=0,color='black')  #yatay kartezyen ekseni(x)

"""Goster"""
plt.show()  #göster
