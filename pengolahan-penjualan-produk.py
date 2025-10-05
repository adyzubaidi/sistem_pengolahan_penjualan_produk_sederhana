# --- DATA PENJUALAN PRODUK ---

data = [
    [120, 150, 130, 170, 200, 190], # PRODUK A
    [80, 100, 90, 110, 130, 120], # PRODUK B
    [200, 210, 190, 180, 220, 210] # PRODUK C
]
nama_produk = ['Produk A','Produk B','Produk C']
bulan = ['Bulan 1','Bulan 2','Bulan 3','Bulan 4','Bulan 5','Bulan 6']
#--- TOTAL HARGA PENJUALAN PRODUK SELAMA 6 BULAN ---
print('-'*10,'TOTAL HARGA PENJUALAN','-'*10)
for indeks, list in enumerate(data):
    total = sum(list)
    print(f'{nama_produk[indeks]} : {total}')

# --- HARGA PENJUALAN TERTINGGI DAN TERENDAH SETIAP PRODUK SELAMA 6 BULAN ---
print('-'*10,'HARGA PENJUALAN TERTINGGI DAN TERENDAH','-'*10)
for indeks, penjualan in enumerate(data):
    tertinggi = max(penjualan)
    bulanmax = penjualan.index(tertinggi) + 1
    terendah = min(penjualan)
    bulanmin = penjualan.index(terendah) + 1
    print(f'{nama_produk[indeks]} : ')
    print(f'Penjualan Tertinggi berjumlah {tertinggi} buah pada Bulan {bulanmax}')    
    print(f'Penjualan Terendah berjumlah {terendah} buah pada Bulan {bulanmin}')
    print('-'*20)    

#--- RATA RATA / MEAN PENJUALAN SETIAP PRODUK SELAMA 6 BULAN---
print('-'*10,'MEAN HARGA PENJUALAN','-'*10)
ambang_batas = 0.05
for i, rata in enumerate(data):
    total = sum(rata)
    rata2 = total//(len(rata))
    print(f'{nama_produk[i]} : {rata2}')
print('-'*20)
print('Ambang batas = 20% dari rata rata jumlah harga penjualan produk')
print('-'*20)

for i, lonjakan in enumerate(data):
    total = sum(lonjakan)
    rata2 = total//(len(lonjakan))
    ambang = int(rata2*ambang_batas) 
    total_lonjakan = rata2+ambang
    bulan_lonjakan = []
    print(f'{nama_produk[i]}')
    print(f'Batas lonjakan {nama_produk[i]} adalah : {total_lonjakan}')
    for n, list2 in enumerate(lonjakan):
        if list2 >= total_lonjakan:
            bulan_lonjakan.append(bulan[n])
            print(f'Bulan ke {n+1} dengan unit {list2} mengalami LONJAKAN')
        else:
            print(f'Bulan ke {n+1} dengan unit {list2} TIDAK mengalami LONJAKAN')
    if bulan_lonjakan:
        print(f'Mengalami lonjakan pada : {", ".join(bulan_lonjakan)}')
    else:
        print('Tidak mengalami lonjakan')
        


        
    