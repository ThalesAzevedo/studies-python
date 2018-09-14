print("Message Generator")
names = str(input("Enter the names separated by commas.")).title().replace(" ", "").split(",")
assing = str(input("Enter de assingments separated by commas.")).replace(" ", "").split(",")
grades = str(input("Enter the grades separated by commas."))replace(" ", "").split(",")

potential_grades = []

for i in range(len(names_list)):
    potential_grades.append((int(assing_list[i])*2)+int(grades_list[i]))
print(potential_grades)

for i in range(len(names_list)):
    print("""Hi {},\n\nThis is a reminder that you have {} assignments left to \n
    submit before you can graduate. You're current grade is {} and can increase \n
    to {} if you submit all assignments before the due date.\n\n""".format(names_list[i],assing_list[i],grades_list[i],potential_grades[i]))
