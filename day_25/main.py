
def convert(input):
    if input == "=":
        return -2
    elif input == "-":
        return -1
    elif input == "0":
        return 0
    elif input == "1":
        return 1
    elif input == "2":
        return 2

def revert(input):
    if input == -2:
        return "="
    elif input == -1:
        return "-"
    elif input == 0:
        return "0"
    elif input == 1:
        return "1"
    elif input == 2:
        return "2"

def SNAFU(input,output):
    for n in range(1,30):
        tmp = input/pow(5, n)
        tmp_floor = round(abs(tmp))

        if(tmp_floor == 1 or tmp_floor ==2 or tmp_floor==0):
            if(tmp < 0):
                output[n] = revert(-tmp_floor)
                input -= pow(5, n)*-tmp_floor
            else:
                output[n] = revert(tmp_floor)
                input -= pow(5, n)*tmp_floor
            
            if(input > -3 and input < 3):
                output[0] = revert(input)
                return
            else:
                SNAFU(input,output)
                return
                
with open('input.txt', 'r') as f:
    lines = f.readlines()

sum_lines = 0
for line in lines:
    sum_line = 0
    for i in range(len(line)-1):
        sum_line += pow(5, i)*convert(line[len(line)-2-i])
    sum_lines += sum_line
    # print(sum_line)

print(sum_lines)

output = ["0"] * 20
SNAFU(sum_lines,output)
print("".join(list(reversed(output)))) #2-2=12=1-=-1=000=222
