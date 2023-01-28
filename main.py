import datetime
import time

DateCreation = datetime.datetime.today().strftime("%d-%m-%Y")
TimeCreation = time.strftime("%H.%M.%S")

print("Local Date: ", TimeCreation + " " + DateCreation, "\n")

print("before import salary", "\n")

import application.salary

print("Module salary was imported", "\n")

print("before import people", "\n")

import application.db.people

print("Module people was imported", "\n")

print("Начато выполнение if __name__ == '__main__'", "\n")
if __name__ == '__main__':
    application.salary.calculate_salary()
    application.db.people.get_employees()
print("Закончено выполнение if __name__ == '__main__'")



