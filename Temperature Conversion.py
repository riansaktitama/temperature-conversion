print("PROGRAM KONVERTER SUHU")

def main():
    #=====celsius=====
    celsius = float(input("Masukkan suhu dalam celsius: "))
    print("Suhu adalah ", celsius , "celsius")

    reamur = celsius * 4/5
    print("Suhu adalah ", reamur , "reamur")

    farenheit = celsius * 9/5 + 32
    print("Suhu adalah ", farenheit , "farenheit")

    kelvin = celsius + 273
    print("Suhu adalah ", kelvin , "kelvin")


    #=====reamur======
    reamur = float(input("Masukkan suhu dalam reamur: "))
    print("Suhu adalah ", reamur , "reamur")
    
    celsius = reamur * 5/4
    print("Suhu adalah ", celsius , "celsius")

    farenheit = (reamur * 9/4) + 32
    print("Suhu adalah ", farenheit , "farenheit")

    kelvin = (reamur * 5/4) + 273
    print("Suhu adalah ", kelvin , "kelvin")


    #======farenheit======
    farenheit = float(input("Masukkan suhu dalam farenheit: "))
    print("Suhu adalah ", farenheit , "farenheit")

    celsius = (farenheit - 32) * 5/9
    print("Suhu adalah ", celsius , "celsius")

    reamur = (farenheit - 32) * 4/9
    print("Suhu adalah ", reamur , "reamur")

    kelvin = ((farenheit - 32) * 5/9) + 273
    print("Suhu adalah ", kelvin , "kelvin")


    #=====kelvin=====
    kelvin = float(input("Masukkan suhu dalam kelvin: "))
    print("Suhu adalah ", kelvin , "kelvin")

    farenheit = ((kelvin - 273) * 9/5) + 32
    print("Suhu adalah ", farenheit , "farenheit")

    celsius = kelvin - 273
    print("Suhu adalah ", celsius , "celsius")

    reamur = (kelvin - 273) * 4/5
    print("Suhu adalah ", reamur , "reamur")


    #=====looping=====
    print("Terima kasih sudah menggunakan program ini :)")
    print("Apakah mau mencoba lagi?")
    print("1 = Iya")
    print("2 = Tidak")
    repeat = float(input())
    if repeat==1:
        main()
    else:
        print("Byeee")
        exit()
        
main()
