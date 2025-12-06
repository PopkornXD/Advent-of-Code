
#* 1


# pickup = 0

# rutenett = []
# while True:
#     inp = input("")
    
#     if (inp == ""):
#         break
    
#     row = []
#     for j in inp:
#         row.append(j)
        
#     rutenett.append(row)
    
# takeable = 0
# for rad_index in range(len(rutenett)):
#     for roll_index in range(len(rutenett[rad_index])):
#         if (rutenett[rad_index][roll_index] == "@"):
#             adjecent_rolls = 0
#             for i in range(-1,2):
#                 for j in range(-1,2):
#                     if (i != 0 or j != 0):
#                         if (0 <= rad_index + j < len(rutenett) and 0 <= roll_index + i < len(rutenett[rad_index])):
#                             if (rutenett[rad_index + j][roll_index + i] == "@"):
#                                 adjecent_rolls += 1
                                
#             if (adjecent_rolls < 4):
#                 takeable += 1

# print(takeable)



#* 2

pickup = 0

rutenett = []
while True:
    inp = input("")
    
    if (inp == ""):
        break
    
    row = []
    for j in inp:
        row.append(j)
        
    rutenett.append(row)
    
old_takeable = -1
new_takeable = 0
while True:
    if (new_takeable == old_takeable):
        break
    old_takeable = new_takeable
    for rad_index in range(len(rutenett)):
        for roll_index in range(len(rutenett[rad_index])):
            if (rutenett[rad_index][roll_index] == "@"):
                adjecent_rolls = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if (i != 0 or j != 0):
                            if (0 <= rad_index + j < len(rutenett) and 0 <= roll_index + i < len(rutenett[rad_index])):
                                if (rutenett[rad_index + j][roll_index + i] == "@"):
                                    adjecent_rolls += 1
                                    
                                    
                if (adjecent_rolls < 4):
                    new_takeable += 1
                    rutenett[rad_index][roll_index] = "."
    

print(new_takeable)
