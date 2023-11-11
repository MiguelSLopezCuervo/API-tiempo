# -*- coding: utf-8 -*-

import swowpy
import AvisoTormenta
api_key = "fd9783118e7563a98a7f7b3f2acd4d7b"

print("Introduce 3 ciudades")
nombreciudad=[]
ciudad=[]
for i in range(0, 3):
    print("Ciudad", i+1, ":")
    nombreciudad.append(input())
    ciudad.append(swowpy.Swowpy(api_key, nombreciudad[i]))

for i in range(0, 3):
    print("Ciudad:", nombreciudad[i])
    print("Tiempo:", ciudad[i].current_weather())
    print("Temperatura:", int(ciudad[i].temperature()-273.15))
    presion=ciudad[i].pressure()
    print("Presión: ", presion, "Pa", sep="")
    AvisoTormenta.aviso(presion)
    print("-----------------------------------------------------")

