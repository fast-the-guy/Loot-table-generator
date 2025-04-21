#f = open("input.txt", "r")
#def read_line():
#    f = open("input.txt", "r")
#    line = (f.readline)
#    return line


#line = read_line()
#print (line)

def read_a_line():
    with open("input.txt", "r") as file:
        lines = file.readline([2,1])
        #for line in lines:
        #print(lines.strip())
    return lines.strip()




line = read_a_line()

print (line)
