from librarysorce import mysptotal, mysppron, myspgend
import os

p=input("Enter an Audio file name without .wav\n")

# c="/home/kali/Downloads/my-voice-analysis"
c = input("Enter an Audio file path\n")

total = mysptotal(p,c)
pron = mysppron(p,c)
gender = myspgend(p,c)

file_name = f"{p}.txt"
with open(file_name, "w") as output:
    output.write(total)
    output.write(pron)
    output.write(gender)

os.remove(f"{c}/{p}.TextGrid")