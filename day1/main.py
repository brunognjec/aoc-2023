f = open("case_1.txt","r")

sum = 0
list = []
con = 0

for i in f:
    d = i.translate({ord(i): None for i in 'qxabcdefghijklmnoprstuvwyz'})
    print("this is d:",d)
    print("num 1:",d[0])
    print("num 2:",d[len(d)-2])
    con = d[0] + d[len(d)-2]
    print("connected value:", con,"\n")
    list.append(con)

for number in list:
    ll = int(number)
    sum = ll +sum

print("sum:",sum)




    
