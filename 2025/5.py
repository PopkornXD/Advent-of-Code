
#* 1

# blank = False
# fresh_ranges = []
# fresh_amount = 0
# while True:
#     inp = input("")
    
#     if (inp == "" and blank == True):
#         break
    
#     if (blank == True):
#         for rang in fresh_ranges:

#             if (rang[0] <= int(inp) <= rang[1]):
#                 fresh_amount += 1
#                 break

#     if (inp == "" and blank == False):
#         blank = True
            
#     if (blank == False):
#         rang = inp.split("-")
#         fresh_ranges.append([int(rang[0]),int(rang[1])])
    
# print(fresh_amount)


#* 2

fresh_ranges = []
fresh = 0
while True:
    inp = input("")
    
    if (inp == ""):
        break


    rang = inp.split("-")
    fresh_ranges.append([int(rang[0]),int(rang[1])])
    
    
    
change = True
while True:
    if (change == False):
        break
    change = False
    for index_1, rang in enumerate(fresh_ranges):
        for index_2, rang2 in enumerate(fresh_ranges):
            if (index_1 != index_2):
                if (rang2[0] <= rang[0] <= rang2[1] <= rang[1]):
                    fresh_ranges.append([rang2[0],rang[1]])
                    fresh_ranges.remove(rang2)
                    fresh_ranges.remove(rang)
                    change = True
                    break
                
                if (rang[0] <= rang2[0] <= rang2[1] <= rang[1]):
                    fresh_ranges.remove(rang2)
                    change = True
                    break

for rang in fresh_ranges:
    fresh += rang[1]-rang[0]+1
print(fresh)