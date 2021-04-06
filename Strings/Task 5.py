s = "Abracadabra"                   #Вывести все символы с четными индексами (считайте, что 0 - четный индекс).
for row in range(11):
    if row % 2 == 0:
        print(s[row])