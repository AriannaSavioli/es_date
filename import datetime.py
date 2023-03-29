import datetime
#stampare la data corrente
oggi = datetime.datetime.now()
print(oggi)
#creare una data con il proprio compleanno
compleanno = datetime.datetime(2023, 5, 16)
#stampare la data del compleanno
print(compleanno)
#stampare la data del compleanno da numerica a stringa
print(compleanno.strftime("%Y"))
print(compleanno.strftime("%B"))
print(compleanno.strftime("%D"))
#calcola la differenza tra le due date

