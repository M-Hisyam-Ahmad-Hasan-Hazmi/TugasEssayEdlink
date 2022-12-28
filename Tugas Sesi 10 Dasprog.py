def luas_dan_keliling():
    # Program Menghitung Luas dan Keliling
    print
    print("------------------------------------------------")
    print("Program Menghitung Luas dan Keliling")
    print("------------------------------------------------")
    print
    # Pilihan
    while True:
        try:
            print("Luas dan Keliling:")
            print(" 1. Luas Segitiga \n 2. Luas Persegi Panjang \n 3. Keliling Persegi Panjang \n 4. Keliling Lingkaran \n 5. Back \nPilih Salah Satu: ")
            pilih = int(input("Masukan Pilihan Anda: "))
            print()
        except ValueError:
            print("Inputan harus berupa number!")
            print()
        else:
            if pilih == 1:
                print("Hitung Luas Segitiga")
                print("-------------------------------")
                
                alas = float(input('Masukan alasnya: '))
                tinggi = float(input('Masukan tingginya: '))

                luas = 1/2 * (alas * tinggi)
                print('\nLuasnya =', str(luas))
                print()

            elif pilih == 2:
                print('Hitung Luas Persegi Panjang')
                print("------------------------------")

                panjang = float(input('Masukan panjangnya: '))
                lebar = float(input('Masukan lebarnya: '))

                luas = panjang * lebar
                print('\nLuasnya =', str(luas))
                print()

            elif pilih == 3:
                print('Hitung Keliling Persegi Panjang')
                print("------------------------------")

                panjang = float(input('Masukan panjangnya: '))
                lebar = float(input('Masukan lebarnya: '))

                keliling = 2 * (panjang + lebar)
                print('Kelilingnya =', str(keliling))
                print()

            elif pilih == 4:
                print("Hitung Keliling Lingkaran")
                print("--------------------------------")

                phi = 3.14
                r = float(input("Masukkan panjang jari-jari lingkaran: "))

                keliling = 2 * phi * r
                print('Kelilingnya =', str(keliling))
                print()
            
            elif pilih == 5:
                break

            else:
                print("Error: Inputkan Angka Yang Benar!")
                print()


