

file_1 = 'task1.txt'
s = open(file_1, mode='r', encoding='utf-8')
f_1=s.read(1)
print (s.read())

file_2 = 'task2.txt'
p = open(file_2, mode='r', encoding='utf-8')
f_2  = p.read(1)
print (p.read())

#----------------situation1---------------


with open("./task1.txt") as file:
    recner_1 = file.readlines()

with open("./task2.txt") as file:
    recner_2 = file.readlines()

def optionen(list_1, list_2):
    new_list = []
    for i in recner_1:
        if i not in recner_2:
            new_list.append(i)
    return new_list

def option_1 ( ather_list):
    if ather_list:
        for i in ather_list:
            print (i, end = " ")
        print("")
    else:
        print (" All string match")
print (" optionen for now for the first file:")
option_1(optionen(recner_1, recner_2))

print ("----------------------------------------")
print(" optionen for now for the second file:")
option_1(optionen(recner_2,recner_1))
print("------------------------------------------")

print("-----------count------------------------")
s = open("./task1.txt", "r")
lines = 0
words = 0
ch = 0
for line in s:
    wordslist = line.split()
    lines = lines+1
    words = words + len(wordslist)
    ch = ch + len(line)
print ( "The File_1 how:")
print(lines)
print(words)
print(ch)
print("---------------------------")

s = open("./task2.txt", "r")
lines = 0
words = 0
ch = 0
for line in s:
    wordslist = line.split()
    lines = lines+1
    words = words + len(wordslist)
    ch = ch + len(line)
print("The Flile_2 how:")
print(lines)
print(words)
print(ch)

