#nama teman
list = ['Ilham', 'Hafiz', 'Fadhila', 'Ahmed', 'Vian', 'Hani', 'Diva', 'Fahruddin', 'Sasa', 'Issa']
print(list)
print("")

#tampilan isi indeks 4, 6, 7
print(list[4])
print(list[6])
print(list[7])
print("")

#ganti nama 3, 5, 9
list[3] = 'Cita'
list[5] = 'Bagus'
list[9] = 'Attar'
print(list)
print("")

#menambah teman
list.append('Alifiana')
list.append('Candrika')
print(list)
print("")

#perulangan
for x in list:
    print(x)
print("")

#panjang list
print(len(list))