batteries = []
while True:
    bank = input("")
    if (bank == ""):
        break
    
    battery_list = []
    for i in bank:
        battery_list.append(int(i))
    
    highest_num = 0 
    for i in battery_list:
        if (i > highest_num and battery_list.index(i) < len(battery_list)-1):
            highest_num = i
    after_highest_num = battery_list[battery_list.index(highest_num)+1:]
    
    second_highest_num = 0 
    for i in after_highest_num:
        if (i > second_highest_num):
            second_highest_num = i
    
    battery = str(highest_num) + str(second_highest_num)
    
    batteries.append(int(battery))

print(sum(batteries))
    