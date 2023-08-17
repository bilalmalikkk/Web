dicList = []
dic1 = {'name' : 'Bilal', 'marks': [1,2,3], 'quizMarks': [10, 40], 'semesterMarks': 30}
dicList.append(dic1)
dic2 = {'name' : 'Talha', 'marks': [1,2,3], 'quizMarks': [1,2,6], 'semesterMarks': 3}
dicList.append(dic2)
dic3 = {'name' : 'Abdullah', 'marks': [1,2,3], 'quizMarks': [1,2,9], 'semesterMarks': 85}
dicList.append(dic3)
dic4 = {'name' : 'Hamza', 'marks': [1,2,3], 'quizMarks': [1,2,3], 'semesterMarks': 300}
dicList.append(dic4)


def print_students(studenDic):
    for key in studenDic.keys():         
        print(key, ':' ,studenDic[key])

print_students(dic1)