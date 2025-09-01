
#listas con slicing y métodos

listas = ['Pera','Manzana','Platano']
print(listas[:1])
print(listas[1:])
print(listas[:-1])
print(listas[-1:])

listas.append('Pitaya')
print(listas)

print(listas.index('Manzana'))

listas.insert(2,'Limón')
print(listas)

print(type(listas))

print('--------------------------------------------------------------')

#tuplas

numeros = (1,2,3,3,4,5,6)
print(tuple(numeros))

print(numeros.count(3))

print(numeros.index(3))

#dict

dict = {

    'Nombre':'Adrián',
    'Apellido':'GR'
}
print(dict)
print(type(dict))

dict['edad'] = 31
print(dict)

dict.update({'Sexo':'Másculino'})
print(dict)

for claves in dict.keys():
    print(claves)

for valores in dict.values():
    print(valores)