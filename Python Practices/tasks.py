dicList = []
dic1 = {'name' : 'Basit', 'marks': [1,2,3], 'quizMarks': [10, 20], 'semesterMarks': 30}
dicList.append(dic1)
dic2 = {'name' : 'Talha', 'marks': [1,2,3], 'quizMarks': [1,2,3], 'semesterMarks': 3}
dicList.append(dic2)
dic3 = {'name' : 'Kamran', 'marks': [1,2,3], 'quizMarks': [1,2,3], 'semesterMarks': 85}
dicList.append(dic3)
dic4 = {'name' : 'Hamza', 'marks': [1,2,3], 'quizMarks': [1,2,3], 'semesterMarks': 300}
dicList.append(dic4)


def print_students(studenDic):
    for key in studenDic.keys():         
        print(key, ':' ,studenDic[key])

print_students(dic1)


def average(marks):
    sum = 0
    for item in marks:  
        sum = sum+item
    average = sum/len(marks)
    # print(average)   
    return average

average(dic1['marks'])

def get_average_of_students(studentDic):
    homeMarks = average(studentDic['marks'])
    quizMarks = average(studentDic['quizMarks'])
    averageTuple = (homeMarks, quizMarks)
    return averageTuple

print(get_average_of_students(dic1))

def weighted_average(tup, project):
    homeWeight = tup[0] * 0.15
    quizWeight = tup[1] * 0.40
    projectWeight = project * 0.35
    aver = (homeWeight+quizWeight+projectWeight)/3
    return aver

marks = weighted_average(get_average_of_students(dic1), dic1['semesterMarks'])
print(marks)

def get_letter_grade(marks):
    if marks >= 80 and marks <= 100:
        print( 'A')
    if marks >= 70 and marks <= 79:
        print('B')
    if marks >= 60 and marks <= 69:
        print('C')
    if marks >= 50 and marks <= 59:
        print('D')
    if marks < 50:
        print('F')

get_letter_grade(marks)

classMarks = []

for i in range(4):
    student = get_average_of_students(dicList[i])
    aver = weighted_average(student, dicList[i]['semesterMarks'])
    classMarks.append(aver)
    

def get_class_average(classMarks):
    sum = 0
    for item in classMarks:
        sum = item + sum
    average = sum/len(classMarks)
    return average

print(get_class_average(classMarks))

print("Enter the number of rows of matrix1: ")
rows1=int(input())
print("Enter the number of columns of matrix1")
col1=int(input())
print("Enter the  number of rows for matrix2:")
rows2=int(input())
print("Enter the number of columns of matrix2")
col2=int(input())

if col1==rows2:
    matrix1=[]
    result=[]
    for rows in range(rows1):
        row1=[]
        for columns in range(col1):
            row1.append(int(input("Enter the element of matrix1")))
        matrix1.append(row1)
    matrix2=[]
    for rows in range(rows2):
        row2=[]
        for columns in range(col2):
            row2.append(int(input("Enter the element of matrix2")))
        matrix2.append(row2)
    for i in range(len(matrix1)):
        myList = []
        for j in range(len(matrix2[0])):
            m = 0;
            for k in range(len(matrix2)):
                print("here")
                m += matrix1[i][k] * matrix2[k][j]
            myList.append(m)
        result.append(myList)
    for r in range(len(result)):
	    print(result[r])
else:
    print("Error!")


