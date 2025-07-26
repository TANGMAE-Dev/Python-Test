start = int(input("แม่คูณ: "))
end = int(input("เลข: "))

for number in range(start,end+1):
    print("สูตรคูณแม่" ,number)
    print("-----------------")
    for i in range(1,13):
        print(number,"x",i,"=",number*i)
