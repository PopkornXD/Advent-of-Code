
#* 1

# batteries = []
# while True:
#     bank = input("")
#     if (bank == ""):
#         break
    
#     battery_list = []
#     for i in bank:
#         battery_list.append(int(i))
    
#     highest_num = 0 
#     for i in battery_list:
#         if (i > highest_num and battery_list.index(i) < len(battery_list)-1):
#             highest_num = i
#     after_highest_num = battery_list[battery_list.index(highest_num)+1:]
    
#     second_highest_num = 0 
#     for i in after_highest_num:
#         if (i > second_highest_num):
#             second_highest_num = i
    
#     battery = str(highest_num) + str(second_highest_num)
    
#     batteries.append(int(battery))

# print(sum(batteries))
    



#* 2


batteries = []
while True:
    bank = input("")
    if (bank == ""):
        break
    
    battery_list = []
    for i in bank:
        battery_list.append(int(i))
    
    digit_of_last_num = -1
    battery = ""
    for i in range(12):
        highest_num = -1
        for j in battery_list[:len(battery_list)-(11-i)]:
            if (j > highest_num):
                highest_num = j
        battery_list = battery_list[battery_list.index(highest_num)+1:]
        battery += str(highest_num)
    
    batteries.append(int(battery))
        
print(sum(batteries))