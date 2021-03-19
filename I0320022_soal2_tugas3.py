#dictionary
dict = {'Nama': 'Danendra Dimas Aryasatya',
        'Hobi': ['Fotografi', 'Videografi', 'Bermain game'],
        'Sosial media': ['Instagram : @danendra_dani', 'Facebook : Danendra Dani', 'Whatsapp : 089649251933'],
        'Lagu kesukaan': ['I Love You But Im Letting Go, Only One, Kenangan Manis'],
        'Makanan favorit': ['Ramen', 'Sushi', 'Yakiniku']
        }
print(dict)
print("")

#ubah hobi dan sosial media
dict['Hobi'][2] = ('Rebahan')
dict['Sosial media'][2] = ('Linkedin : Danendra Dani')

#hapus 2 makanan favorit
del dict['Makanan favorit'][0:2]

#tambah 1 hobi
dict['Hobi'].append('Mendengarkan lagu')

#tampilan dictionary setelah diubah
print(dict)