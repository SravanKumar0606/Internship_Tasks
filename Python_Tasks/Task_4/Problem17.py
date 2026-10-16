# Problem 17
# The provided code stub reads in a dictionary containing key/value pairs of name: [marks] for a list of students. 
# The goal is to calculate and print the average of the marks array for a specific student name provided as input, 
# formatted to show exactly 2 decimal places after the floating-point value.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
   
    scores = student_marks[query_name]

    average_score = sum(scores) / len(scores)
    print(f"{average_score:.2f}")
