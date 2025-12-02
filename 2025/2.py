
#* 1

# IDs = input("")

# id_range_list = IDs.split(",")

# invalid_ids = []
# for id_range in id_range_list:
#     end_start = id_range.split("-")
    
#     for i in range(int(end_start[0]),int(end_start[1])+1):
#         i = str(i)
#         if (len(i) % 2 == 0):
#             first_half = i[:len(i)//2]
#             second_half = i[len(i)//2:]
#             if (first_half == second_half):
#                 invalid_ids.append(int(i))

# print(sum(invalid_ids))



#* 2


IDs = input("")

id_range_list = IDs.split(",")

invalid_ids = []
for id_range in id_range_list:
    end_start = id_range.split("-")
    
    for i in range(int(end_start[0]),int(end_start[1])+1):
        i = str(i)
        for j in range(2,len(i)+1):
            if (len(i) % j == 0):
                segment_len = len(i)//j
                split = []
                for k in range(0,j):
                    split.append(i[k*segment_len:k*segment_len+segment_len])
            
                diff_num = []
                for l in split:
                    if (l not in diff_num):
                        diff_num.append(l)
                
                if (len(diff_num) == 1 and int(i) not in invalid_ids):
                    invalid_ids.append(int(i))

print(sum(invalid_ids))