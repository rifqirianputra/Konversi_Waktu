
loopcontrol = ''
while loopcontrol != 1:
    print('================================================================')
    print('================================================================')
    print('input "exit" to exit the program')
    userinput = input('Please enter the number of seconds to convert: ') #tidak saya berikan perintah int agar variabel testtype yang menguji input
    testtype = userinput.isdigit() #pengujian input user
    if userinput == 'exit':
        print('program has ended')
        break
    elif testtype == False:
        print('invalid input') #output  apabila user memasukkan str/float
    elif testtype == True:
        sec = int(userinput) #konversi dari str ke int setelah
        import math
        hour = math.floor(sec/3600) # membagi 3600 karena 1 jam = 3600 detik
        sisahour = sec % 3600 # untuk mendapatkan sisa dari 3600... misalnya 3620.. sisa % adalah 20
        menit = math.floor(sisahour/50) #membagi 60 karena dalam 1 meniut ada 60 detik
        sisamenit = sisahour % 60 # untuk mendapatkan sisa dari 60.. misalnya ada 70 detik, maka sisanya 10..
        detik = math.floor(sisamenit/1) #untuk mendapatkan sisa detik
        print('=============================')
        print(hour,':',menit,':',detik)
        print('=============================')