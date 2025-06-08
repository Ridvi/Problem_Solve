if __name__ == '__main__':
    s = input()

list = [False, False, False, False, False]

for c in s:
    if c.isalnum():
        list[0] = True
    if c.isalpha(): 
        list[1] = True
    if c.isdigit(): 
        list[2] = True
    if c.islower(): 
        list[3] = True
    if c.isupper(): 
        list[4] = True

for e in list:
    print(e)
