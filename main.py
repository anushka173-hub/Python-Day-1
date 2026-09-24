# ASSIGNMENR A

employees = [
    {"id":1,"name":"John","salary":100000},
    {"id":2,"name":"Jane","salary":120000},
    {"id":3,"name":"Mike","salary":90000}
    ]

#1 all employees

def print_all_employees():
    for emp in employees:
        print(emp)

print( "All emplyees :")    
print_all_employees()        


#2 Highest Paid

def find_highest_paid():
    highest = employees[0]
    for emp in employees:
        if emp ["salary"]> highest ["salary"]:
            highest = emp
        return highest

print ("Highest Paid Employee : ")
print(find_highest_paid())
    

#3 Avarage Salary

def calculate_avarage():
    total_salary = 0
    total_count = 0 
    for emp in employees:
        total_salary = total_salary + emp["salary"]
        total_count = total_count + 1
    avarage = total_salary / total_count
    return avarage

print(" Avarage Salary : ")
print( calculate_avarage())

#4 earning > 100000

def get_rich_employee():
    rich__list = []
    for emp in employees:
        if emp in employees:
            if emp ["salary"]> 100000:
                rich__list.append(emp)
    return rich__list

print (" salary greater than 100000 :")
print(get_rich_employee())


#5 count

def count_emplyees():
    count = 0
    for emp in employees:
        count = count + 1 
    return count  

print(" Count Employees : ")
print(count_emplyees())



#ASSIGNMENT B


# 7 

def reverse_String (text):
    return text[::-1]

print(" Reverse String")
print(reverse_String("Hello"))

# 8 

def is_palindrome(text):
    return text == text[::-1]

print("Palindrome check")
print(is_palindrome("madam"))

# 9

def validate_salary(salary):
    if isinstance(salary,(int,float)) and salary >= 0:
        return True
    return False

print("Salary Validation :")
print(validate_salary(200000))

# 10

def safe_get_salary(salary_input):
    try:
        salary = float(salary_input)
        if salary >= 0:
            return f"TRUE salary: {salary}"
        else:
            return "Invalid: Salary cannot be negative"
    except ValueError:
        return "Please input the right value (numbers only)"


print("Handle Invalid Input Safety")
print(safe_get_salary("120000"))
print(safe_get_salary("abc"))


#Day 1 Hard Scenario-----------------


employees = [
    {"id": 1, "name": "John", "salary": 100000},
    {"id": 2, "name": "Jane", "salary": None},  # Hard scenario: salary is None
    {"id": 3, "name": "Mike", "salary": 90000}
]

def calculate_average_salary(emp_list):
    
    if not emp_list:
        return 0
    
    total = 0
    count = 0
    
    for emp in emp_list:
        # Check if salary is not None before adding
        if emp["salary"] is not None:
            total += emp["salary"]
            count += 1
            
    # Avoid division by zero if all salaries are None
    if count == 0:
        return 0
        
    return total / count

print("Average Salary:", calculate_average_salary(employees))





                





  




    


