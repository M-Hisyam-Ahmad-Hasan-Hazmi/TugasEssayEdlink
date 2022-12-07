import array as myarr
lulus = ['A','B','C','B+','C+']

list_nilai =[9]
jumlah_mahasiswa = int(input("Berapa Banyak Jumlah mahasiswa : "))
data = int(input("data ke - "))
Nim_mahasiswa = int(input("Masukan Nim Mahasiswa :"))
Masukan_nilai_UTS = int(input("Masukan nilai UTS :"))
Masukan_nilai_UAS = int(input("Masukan nilai UAS :"))
print("=============================================================")
print("NIM            UTS     UAS     Total  Grade     Keterangan")
print("=============================================================")

jumlah = (Masukan_nilai_UTS + Masukan_nilai_UAS ) / 2
if jumlah >= 90:
    lulus_tidak = 'A'

elif jumlah >=80:
    lulus_tidak = 'B+'

elif jumlah >=70:
    lulus_tidak = 'B'
        
elif jumlah >=60:
    lulus_tidak = 'C+'

elif jumlah >=50:
    lulus_tidak = 'C'

elif jumlah >=40:
    lulus_tidak = 'D'
        
elif jumlah >=30:
    lulus_tidak = 'E'
    
else:
    lulus_tidak = 'F'
    

if lulus_tidak in lulus:
    print(Nim_mahasiswa,end='\t')
    print(Masukan_nilai_UTS,end='\t')
    print(Masukan_nilai_UAS,end='\t')
    print(jumlah,end='\t')
    print(lulus_tidak,end='\t')
    print('LULUS',end='\t')
    

else :
    print(Nim_mahasiswa,end='\t')
    print(Masukan_nilai_UTS,end='\t')
    print(Masukan_nilai_UAS,end='\t')
    print(jumlah,end='\t')
    print(lulus_tidak,end='\t')
    print('TIDAK LULUS',end='\t')
    