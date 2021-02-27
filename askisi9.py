import math
count = 0
ascii_numbers = []
ascii_chars = []
# Άνοιγμα ενός .txt αρχείου
file1 = open('test.txt', 'r')
line = file1.readline()
while line:
    for x in line:
        remain = ord(x) % 2
        if remain != 0 and x.isalpha():
            ascii_numbers.insert(count, ord(x))
            ascii_chars.insert(count, x)
        count += 1
    line = file1.readline()


file1.close()
print(ascii_numbers)
ascii_chars.sort()
number_of_chars = len(ascii_chars)
if number_of_chars != 0:
    one_time_perc = math.ceil(100 / number_of_chars)
print(number_of_chars)
print(one_time_perc)
print(ascii_chars)
ascii_chars_set = set(ascii_chars)
for x in ascii_chars_set:
    print(x, " : ", "*" * int(ascii_chars.count(x) * one_time_perc))