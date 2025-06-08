def solve(s):
    names=s.split(' ')
    correct=[]

    for name in names:
        correct.append(name.capitalize())
    return ' '.join(correct)
