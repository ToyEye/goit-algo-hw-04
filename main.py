from pathlib import Path


# Task 1

def total_salary(path):
  
    with open(path,'r',encoding='utf-8') as file:
        salary_list = file.readlines()
        total_salary = 0
        average_salary = 0

        for person in salary_list:
            salary = int(person.split(',')[1])
           
            total_salary = total_salary + salary

              
        average_salary = total_salary // len(salary_list)  


        return (total_salary,average_salary)   



p = Path('salary.txt')

if p.exists():
    total, average = total_salary(p)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

else:
    print('Path don\'t exist')    
