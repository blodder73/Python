#D:\Programming\Python\Giraffe\employees.txt

# you have different modes after open("path", "")
# open("path", "r") = read file
# open("path", "r+") = reading and writing
# open("path", "w") = write / modify file
# open("path", "a") = append file, only append to the file
employee_file = open("D:\\Programming\\Python\\Giraffe\\employees.txt", "r")

print(employee_file.readable())
#print(employee_file.readline())
#print(employee_file.readline())
#print(employee_file.readlines()[2])

for employee in employee_file.readlines():
    print(employee)


employee_file.close()