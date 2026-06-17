import statistics
import matplotlib.pyplot as plt

students = []

def add_student():
    name = input("Enter Name : ")
    marks = int(input("Enter Marks : "))
    students.append((name, marks))
    print("New Student Added")

def update_student():
    name = input("Enter Student Name : ")
    for i in range(len(students)):
        if students[i][0] == name:
            marks = int(input("Enter New Marks : "))
            students[i] = (name, marks)
            print("Marks Updated")
            return
    print("Student Doesn't Exist")

def delete_student():
    name = input("Enter Student Name : ")
    for i in range(len(students)):
        if students[i][0] == name:
            students.pop(i)
            print("Student Removed")
            return
    print("Student Doesn't Exist")

def display_students():
    print("\nAll Students : \n")
    for name, marks in students:
        print(name, "->", marks)

def statistics_report():
    marks = []
    for name, mark in students:
        marks.append(mark)
    print("Mean=", statistics.mean(marks))
    print("Median=", statistics.median(marks))
    print("Mode=", statistics.mode(marks))
    print("Range=", max(marks) - min(marks))
    print("Variance=", statistics.variance(marks))
    print("Standard Deviation=", statistics.stdev(marks))
    sorted_marks = sorted(marks)
    q1 = sorted_marks[len(sorted_marks)//4]
    q3 = sorted_marks[(3*len(sorted_marks))//4]
    print("Q1=", q1)
    print("Q3=", q3)
    print("IQR=", q3 - q1)

def probability_report():
    marks = []
    for name, mark in students:
        marks.append(mark)
    total_students = len(marks)
    count = 0
    for m in marks:
        if m >= 80:
            count += 1
    probability = count / total_students
    print("\nProbability of student with marks >= 80 : ",probability)
    count_90 = 0
    for m in marks:
        if m >= 90:
            count_90 += 1
    conditional_probability = count_90 / count
    print("Conditional Probability P(>=90 | >=80) : ",conditional_probability)

def generate_charts():
    names = []
    marks = []
    for name, mark in students:
        names.append(name)
        marks.append(mark)

    plt.hist(marks)
    plt.title("Histogram")
    plt.savefig("screenshots/histogram.png")
    plt.close()

    plt.bar(names, marks)
    plt.title("Bar Chart")
    plt.savefig("screenshots/barchart.png")
    plt.close()

    plt.boxplot(marks)
    plt.title("Box Plot")
    plt.savefig("screenshots/boxplot.png")
    plt.close()

    plt.scatter(names, marks)
    plt.title("Scatter Plot")
    plt.savefig("screenshots/scatterplot.png")
    plt.close()

    plt.plot(names, marks)
    plt.title("Line Chart")
    plt.savefig("screenshots/linechart.png")
    plt.close()



while True:
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Statistics")
    print("6. Probability")
    print("7. Charts")
    print("8. Exit")
    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        add_student()
    elif choice == 2:
        update_student()
    elif choice == 3:
        delete_student()
    elif choice == 4:
        display_students()
    elif choice == 5:
        statistics_report()
    elif choice == 6:
        probability_report()
    elif choice == 7:
        generate_charts()
    elif choice == 8:
        break
    else:
        print("Enter Valid Choice")