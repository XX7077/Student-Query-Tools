
def SQT():
    my_file = open('Students.txt', mode='r', encoding='utf-8')
    contents = my_file.read()
    lines = contents.split('\n')
    student_record = []
    for i in range(len(lines)):
        student_record.append(lines[i].split('\t'))

    print("This is Student Query Tool (SQT).\nIt will help you read student records")
    print("You have following option:")
    print("\tfor displaying all student records,enter 'All' ")
    print("\tfor displaying students whose last name begins with a certain string (case insensitive),enter 'B'")
    print("\tfor displaying all records for students whose graduating year is a certain year,enter'C' ")
    print("\tfor displaying a summary report of number and percent of students in each program,for")
    print("\tstudents graduating on/after a certain year,enter'D': ")
    C1 = input("Enter your first command: ")
    program(student_record, C1)
    reply = input('Do you want to continue? Y/N: ')
    while reply != 'Y' and reply != 'N':
        print("Invalid command")
        reply = input('Do you want to continue? Y/N: ')
        while reply == 'Y':
            print("You have following option:")
            print("\tfor displaying all student records,enter 'All': ")
            print("\tfor displaying students whose last name begins with a certain string (case insensitive),enter'B': ")
            print("\tfor displaying all records for students whose graduating year is a certain year,enter'C': ")
            print("\tfor displaying a summary report of number and percent of students in each program,for")
            print("\tstudents graduating on/after a certain year,enter'D': ")
            print("\tfor stop,enter 'Stop'")
            C1 = input("Enter your first command: ")
            if C1 == "Stop":
                break

            program(student_record, C1)
            reply = input('Do you want to continue? Y/N: ')
        if reply == 'N':
            break
    while reply == 'Y':
        print("You have following option:")
        print("\tfor displaying all student records,enter 'All': ")
        print("\tfor displaying students whose last name begins with a certain string (case insensitive),enter 'B': ")
        print("\tfor displaying all records for students whose graduating year is a certain year,enter'C': ")
        print("\tfor displaying a summary report of number and percent of students in each program,for")
        print("\tstudents graduating on/after a certain year,enter'D': ")
        print("\tfor stop,enter 'Stop'")
        C1 = input("Enter your first command: ")
        if C1 == "stop":
            break

        program(student_record, C1)
        reply = input('Do you want to continue? Y/N: ')
        if reply == 'N':
            break
        while reply != 'Y' and reply != 'N':
            print("Invalid command")
            reply = input('Do you want to continue? Y/N: ')

        if reply == 'N':
            break


def program(s, C1):
    if C1 == "All":
        for stud in s:
            for attr in stud:
                print(attr,end='\t')
            print('\n')
    elif C1 == 'B':
        C2 = input("Enter the starting string of the last name: ")
        C2_1 = C2.lower()
        length = len(C2_1)
        answer = 0
        for stud in s:
            if C2_1[:length] == stud[1][:length].lower() and stud[0] != "ID":
                print(s[0])
                break
        for stud in s:
            if C2_1[:length] == stud[1][:length].lower() and stud[0] != "ID":
                print(stud)
                answer = 1
        if answer == 0:
            print("Invalid string-No data found")
    elif C1 == 'C':
        C2 = input('Enter the graduating year: ')
        answer = 0
        for stud in s:
            if C2 == stud[3]:
                print(stud)
                answer = 1
        if answer == 0:
            print("Invalid year")
    elif C1 == 'D':
        C2 = input("On/After certain year?(on/after) ")
        C2_1 = C2.lower()

        if C2_1 != 'on' and C2_1 != 'after':
            print('Invalid command')
            g = 1
        else:
            C3 = int(input("Which year? "))
            answer = 0
            summary_n = {}
            total = 0
            g = 0
            if C2_1 == 'on':
                for stud in s:
                    if stud[0] != "ID" and C3 == int(stud[3]):
                        total += 1
                        if stud[5] in summary_n:
                            summary_n[stud[5]] += 1
                        else:
                            summary_n[stud[5]] = 1
            elif C2_1 == 'after':
                for stud in s:
                    if stud[0] != "ID" and C3 < int(stud[3]):
                        total += 1
                        if stud[5] in summary_n:
                            summary_n[stud[5]] += 1
                        else:
                            summary_n[stud[5]] = 1
            if total == 0 and g == 0:
                print("Invalid year-No data found")
            else:
                summary = [["Degree program", "Number", "Percentage"]]
                for n in summary_n.keys():
                    summary.append([n, summary_n[n], summary_n[n]/total])

                for record in summary:
                    for attr in record:
                        print(attr, end='\t')
                    print('\n')
    else:
        print('Invalid command')



SQT()






