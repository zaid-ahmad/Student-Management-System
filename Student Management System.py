from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def StudentFunc():
    NameOfStudent = var.get()
    File = open("info.txt", "r+")
    index = 0
    for line in File:
        if NameOfStudent == "":
            messagebox.showerror("No Student Entered", "Please enter student's name")
            break

        elif NameOfStudent == line.split(":")[0]:
            index = 1
            justforshow["text"] = ""
            name = line.split(':')[0]
            lastname = line.split(':')[1]
            roll = line.split(':')[2]
            ClassName = (line.split(':')[3]).strip('\n')
            number = (line.split(':')[4]).strip('\n')
            grNum = (line.split(':')[5]).strip('\n')
            studentNameLblEmpty["text"] = (name.title() + " " + lastname.title())
            studentClassLblEmpty["text"] = ClassName
            studentRollLblEmpty["text"] = roll
            studentNumberLblEmpty["text"] = number
            studentGrNumLblEmpty["text"] = grNum

            lbl576["text"] = "There you go -"
            studentNameLbl["text"] = "Name:"
            studentClassLbl["text"] = "Class:"
            studentRollLbl["text"] = "Roll number:"
            studentNumberLbl["text"] = "Number:"
            studentGrNumLbl["text"] = "Gr.number: "

    if index == 0:
        messagebox.showwarning("Student Management System", "No such student found")

    File.close()


def addStudent():

    def SubmitBtnFunc():
        stuname = NameOfNewStudent.get()
        stulastname = LastNameOfNewStudent.get()
        sroll = RollNumberOfNewStudent.get()
        sclass = ClassNameOfNewStudent.get()
        ssection = SectionOfNewStudent.get()
        sphone = PhoneNumberOfNewStudent.get()
        snumber = GrNumberOfNewStudent.get()

        if stuname == "" and sroll == "" and sphone == "" and snumber == "":
            messagebox.showerror("Student Management System", "Sorry, No input detected")

        else:
            File = open("info.txt", "a+")
            File.write("\n" + stuname + ":")
            File.write(stulastname + ":")
            File.write(sroll + ":")
            File.write(sclass + "-" + ssection + ":")
            File.write(sphone + ":")
            File.write(snumber)
            File.close()
            messagebox.showinfo("Student Management System", "Student added successfully")
            root2.destroy()

    root2 = Toplevel()
    root2.title("New Student")
    root2.geometry("350x350")

    NameOfNewStudent = StringVar()
    LastNameOfNewStudent = StringVar()
    RollNumberOfNewStudent = StringVar()
    ClassNameOfNewStudent = StringVar()
    SectionOfNewStudent = StringVar()
    PhoneNumberOfNewStudent = StringVar()
    GrNumberOfNewStudent = StringVar()

    lbl1 = Label(root2, text="Enter Student's Name: ")
    lbl1.grid(column=0, row=2, pady=10, padx=7)

    NewStudentName = ttk.Entry(root2, textvariable=NameOfNewStudent)
    NewStudentName.grid(column=1, row=2, pady=13)

    lbl2 = Label(root2, text="Enter Student's Last Name: ")
    lbl2.grid(column=0, row=3, pady=10, padx=7)

    LastNewStudentName = ttk.Entry(root2, textvariable=LastNameOfNewStudent)
    LastNewStudentName.grid(column=1, row=3, pady=13)

    lbl3 = Label(root2, text="Enter Student's roll number: ")
    lbl3.grid(column=0, row=4, padx=7)

    rollNumber = ttk.Entry(root2, textvariable=RollNumberOfNewStudent)
    rollNumber.grid(column=1, row=4)

    lbl4 = Label(root2, text="Enter Student's class: ")
    lbl4.grid(column=0, row=5, padx=7)

    className = ttk.Combobox(root2, values=["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"], textvariable=ClassNameOfNewStudent)
    className.current(8)
    className.grid(column=1, row=5, pady=10)

    lbl5 = Label(root2, text="Section: ")
    lbl5.grid(column=0, row=6, padx=7, pady=3)

    Section = ttk.Combobox(root2, values=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], textvariable=SectionOfNewStudent)
    Section.grid(column=1, row=6, pady=10)
    Section.current(0)

    lbl6 = Label(root2, text="Phone Number: ")
    lbl6.grid(column=0, row=7, padx=7, pady=3)

    StudentNumber = ttk.Entry(root2, textvariable=PhoneNumberOfNewStudent)
    StudentNumber.grid(column=1, row=7, pady=10)

    lbl7 = Label(root2, text="Gr. Number: ")
    lbl7.grid(column=0, row=8, padx=7, pady=10)

    StudentGrNumber = ttk.Entry(root2, textvariable=GrNumberOfNewStudent)
    StudentGrNumber.grid(column=1, row=8, pady=10)

    SubmitBtn = ttk.Button(root2, text="Submit", command=SubmitBtnFunc)
    SubmitBtn.grid(column=1, row=9, pady=5)

    root2.mainloop()


def delStudent():

    def gofunction():
        std = studentsToDelete.get()

        with open("info.txt", "r") as f:
            lines = f.readlines()

        with open("info.txt", "w") as f:
            for line in lines:
                if line.split(":")[0] != std:
                    f.write(line)

        messagebox.showinfo("Student Mangement System", "Student deleted successfully")

    root3 = Toplevel()
    root3.geometry("295x300")

    studentsToDelete = StringVar()

    Label(root3, text="Enter Student's Name").grid(column=0, row=0, pady=5, padx=10)
    ttk.Entry(root3, textvariable=studentsToDelete).grid(column=1, row=0, padx=10, pady=10)

    ttk.Button(root3, text="Delete", command=gofunction).grid(column=1, row=1)


root = Tk()
root.title("Student Management System")
root.geometry("290x420")
root.resizable(False, False)

var = StringVar()

l1 = Label(root, text="Enter Student's Name:").grid(column=0, row=0, pady=5, padx=5)

inputStudent = ttk.Entry(root, textvariable=var).grid(column=1, row=0, pady=10, padx=5)

getBtn = ttk.Button(root, text="Get Student Info", width=20, command=StudentFunc)
getBtn.grid(column=1, row=1)

addBtn = ttk.Button(root, text="Add Student", command=addStudent)
addBtn.grid(column=1, row=30, pady=95, ipadx=20)

delBtn = ttk.Button(root, text="Delete Student", command=delStudent)
delBtn.grid(column=0, row=30, ipadx=20, padx=10)

justforshow = Label(root, text="Student Info Would Display Here...", font=28)
justforshow.grid(columnspan=2, column=0, row=5)

lbl576 = Label(root, text="", font=10)
lbl576.grid(column=0, row=3)

studentNameLbl = ttk.Label(root, text="")
studentNameLbl.grid(column=0, row=7, pady=10)

studentClassLbl = ttk.Label(root, text="")
studentClassLbl.grid(column=0, row=8)

studentRollLbl = ttk.Label(root, text="")
studentRollLbl.grid(column=0, row=9, pady=10)

studentNumberLbl = Label(root, text="")
studentNumberLbl.grid(column=0, row=10)

studentGrNumLbl = Label(root, text="")
studentGrNumLbl.grid(column=0, row=11, pady=10)

studentNameLblEmpty = Label(root, text="")
studentNameLblEmpty.grid(column=1, row=7)

studentClassLblEmpty = Label(root, text="")
studentClassLblEmpty.grid(column=1, row=8)

studentRollLblEmpty = Label(root, text="")
studentRollLblEmpty.grid(column=1, row=9)

studentNumberLblEmpty = Label(root, text="")
studentNumberLblEmpty.grid(column=1, row=10)

studentGrNumLblEmpty = Label(root, text="")
studentGrNumLblEmpty.grid(column=1, row=11)

root.mainloop()
