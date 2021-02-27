import random

count_list = []
Array_with_s_o = []
times_repeat = 5
m=6
n=int(m/2)
K=100
for i in range(K):
    Array_with_s_o=[]
    for i in range(times_repeat):
        line_array = random.sample(['S', 'O'], counts=[n , n], k=m)  
        Array_with_s_o.insert(i, line_array)
        #print(line_array)

    count = 0
    for y in range(len(Array_with_s_o)-1):  # cycle through every line
        for x in range(len(Array_with_s_o[0]) - 1):  # cycle through every column
            if Array_with_s_o[y][x] == 'S':
                # check if it will go out of boundaries horizontally
                if x < len(Array_with_s_o[0]) - 2:
                    if Array_with_s_o[y][x+1] == 'O' and Array_with_s_o[y][x+2] == 'S':
                        # this will execute if there is a horizontal SOS
                        #print(f"Found horizontal SOS at position HOR y: {y}; x: {x}")
                        count += 1
                # check if it will go out of boundaries horizontally and vertically
                if (x < len(Array_with_s_o[0]) - 2) and (y < len(Array_with_s_o) - 2):
                    if Array_with_s_o[y+1][x+1] == 'O' and Array_with_s_o[y+2][x+2] == 'S':
                        # this will execute if there is a diagonal SOS
                        #print(f"Found diagonal SOS at position  DIAG y: {y}; x: {x}")
                        count += 1

                # check if it will go out of boundaries vertically
                if y < len(Array_with_s_o) - 2:
                    if Array_with_s_o[y+1][x] == 'O' and Array_with_s_o[y+2][x] == 'S':
                        # this will execute if there is a vertical SOS
                        #print(f"Found vertical SOS at position VER   y: {y}; x: {x}")
                        count += 1


    count_list.insert(i,count)
print('',count_list)
print('Ο ΜΕΣΟΣ ΟΡΟΣ "SOS" EINAI:',sum(count_list)/K)