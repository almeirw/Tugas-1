X = input('Nilai ujian teori: ')
Y = input('Nilai ujian praktek: ')
if int(X) == 70 and int(Y) == 70 or int(X) > 70 and int(Y) > 70:
    print("Selamat, anda lulus!")
elif int(X) > 70 and int(Y) < 70 or int(X) == 70:
    print('Anda harus mengulang ujian praktek.')
elif int(X) < 70 and int(Y) > 70 or int(Y) == 70 :
    print('Anda harus mengulang ujian teori.')
else:
    print('Anda harus mengulang ujian teori dan praktek.')