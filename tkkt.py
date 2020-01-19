import os
from time import sleep
import socket,struct,time,os,sys

def jalan(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2 / 3)

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
jalan(a+'UNTUK MEMUNCULKAN TOMBOL KIRI KANAN TERMUX')
jalan('Bayyu/Rexy')
jalan('Tunggu Woyy!!')
jalan('Sedang Menginstal...')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(b+'[!]Success !')
sleep(1)
jalan('[!]Menambahkan File Tambahan..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
anjir = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
anjir.write(key)
anjir.close()
sleep(1)
jalan('[!]Success')
sleep(1)
jalan('[!]Tunggu Sebentar')
sleep(1)
jalan('[!]Menyimpan File..')
sleep(1)
jalan('[!]Succsess')
sleep(2)
os.system('termux-reload-settings')
jalan(c+'UNTUK MELIHAT HASILNYA LEBIH BAGUS SILAHKAN RESTART TERMUX')
jalan(c+'ATAU BUKA SESION BERIKUTNYA ^_^')