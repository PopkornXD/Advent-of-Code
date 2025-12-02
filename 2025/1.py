
#* 1

# password = 0
# pos = 50
# while True:
#     rotation = input("")
#     if (rotation == ""):
#         break

#     rotation = rotation.replace("L","-")
#     rotation = rotation.replace("R","+")

#     next_rot_string = str(pos) + (rotation)
    
#     pos = int(eval(next_rot_string))
    
#     while (pos < 0 or pos > 99):
#         if (pos < 0):
#             pos += 100
#         elif (pos > 99):
#             pos -= 100
        
#     if (pos == 0):
#         password += 1
        
# print(f"passord = {password}, pos = {pos}")



#* 2

password = 0
pos = 50
while True:
    rotation = input("")
    if (rotation == ""):
        break

    rotation = rotation.replace("L","-")
    rotation = rotation.replace("R","+")

    
    for i in range(int(rotation[1:])):
        evalString = str(pos) + rotation[0] + "1"
        pos = int(eval(evalString))
        
        if (pos == 100):
            pos = 0
        if (pos == -1):
            pos = 99
        
        if (pos == 0):
            password += 1
            
print(f"passord = {password}, pos = {pos}")