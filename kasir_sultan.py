#Harga Barang
harga_roko=20000
harga_minyak=25000
harga_gula=11000

#diskon
diskon=10000

#saldo
saldo_ucup=100000

#total belanja
total_belanja = harga_roko + harga_minyak + harga_gula - diskon

#kembalian
kembalian=saldo_ucup - total_belanja

print("total belanja ucup adalah:", total_belanja)
print("diskon:", diskon)
print("jumlah kembalian ucup adalah:", kembalian)