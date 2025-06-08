n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

if query_name in student_marks:
    marks=student_marks[query_name]
    avg_mark=sum(marks)/len(marks)
    print(f'{avg_mark:.2f}')
