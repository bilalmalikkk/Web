def dumpStudentData(filename,studentData):
    try:
        f=open(filename,"a")
        records=[]
        for student in studentData:
            print(student)
            rollno=student["rollno"]
            name = student["name"]
            semmester = str(student["semmester"])
            cgpa = str(student["cgpa"])
            record=rollno+","+name+","+semmester+","+cgpa
            print(record)
            records.append(record)
        f.writelines(records)
    except Exception as e:
        print(str(e))
    finally:
        f.close()


def loadStudentData(filename):
    fr=open(filename)
    lines=fr.readlines()
    studentsData=[]
    for line in lines:
        record=line.split(",")
        if len(record)>=4:
            rollno=record[0]
            name = record[1]
            semmester = record[2]
            cgpa = record[3]
            dict_stu={"rollno":rollno,"name":name}
            dict_stu.update(semmester=semmester)
            dict_stu.update(cgpa=cgpa)
            studentsData.append(dict_stu)

    return studentsData
data=loadStudentData("data.txt")
dumpStudentData("newrecord.txt",data)
