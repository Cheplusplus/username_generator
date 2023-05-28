from xml.dom import UserDataHandler
import datetime

def user_details():
    check = False
    while not check:
        name = input("Insert your first name\n")
        if name == "":
            print("Invalid first name")
            continue
        for x in name:
            if x.isdigit():
                print("Invalid first name")
                break
        else:
            check = True
    check = False
    while not check:
        surname = input("Insert your last name\n")
        if surname == "":
            print("Invalid last name")
            continue
        for x in surname:
            if x.isdigit():
                print("Invalid last name")
                break
        else:
            check = True
    
    check = False
    while not check:
        year = int(input("Insert your cohort\n"))
        today = datetime.date.today()
        c_year = today.year
        if year < c_year:
            print("Invalid cohort")
        else:
            check = True
    check = False
    while not check:
        campus = user_campus(input("Insert the campus you will be attending in\n").lower())
        if not campus:
            print("Invalid campus")
        else:
            check = True
    username =create_user_name(name, surname, year, campus)
    print(username)

def create_user_name(first_name, last_name, cohort, final_campus):
    if len(first_name) < 3:
        while len(first_name) < 3:
            first_name+="o"
    if len(last_name) < 3:
        while len(last_name) < 3:
            last_name+="o"
    part1 = first_name[-3::].lower()
    part2 = last_name[:3].lower()
    return part1 + part2 + str(cohort) + final_campus

def user_campus(campus):
    if campus == "johannesburg":
        return "JHB"
    elif campus == "durban":
        return "DBN"
    elif campus == "cape town":
        return "CPT"
    elif campus == "phokeng":
        return "PHO"
    else:
        return False

if __name__ == '__main__':
    user_details()