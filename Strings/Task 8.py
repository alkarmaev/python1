s = "Abracadabra"                           #Вывести все символы строки через один в обратном порядке, начиная с последнего.
for i in range(11):
    if i % 2 == 0:
        print(s[i::-1])