def swap_case(s):
    new=[]
    for i in s:
        if 'A'<=i and i<='Z':
            i=i.lower()
            new.append(i)
            
        elif 'a'<=i and i<='z':
            i=i.upper()
            new.append(i)
            
        else:
            new.append(i)

    return ''.join(new)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
