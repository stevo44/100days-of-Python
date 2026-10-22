# Python Dictionaries: They are made up of keys and values

dic = {"key": "values"}

programming_dictionary = {
    "Bug": "An error in a programming language",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again",
}

# print(programming_dictionary["Bug"])
# print(programming_dictionary["Function"])
#
# #Adding new items to a dictionary
# programming_dictionary["forLoop"] = "Do it again and again"
#
# print(programming_dictionary)

student_score = {
    "Harry": 81,
    "Ran": 78,
    "Hermine": 99,
    "Draco": 74,
    "Neville": 62,
}

students_grades = {}

for key in student_score:
    students_grades[key] = student_score[key]
    if student_score[key] >= 91:
       students_grades[key] = "outstanding"
    elif student_score[key] >= 81:
        students_grades[key] = "Exceeds Expectation"
    elif student_score[key] >= 71:
        students_grades[key] = "Acceptable"
    else:
        students_grades[key] = "Fail"
# print(students_grades)

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "England": "London",
}

#Nesting a list in a Dictionary

travel_log = {
    "France": ['Paris', 'Lille', 'Nice'],
    "Germany": ['Berlin', 'Hamburg', 'Struttgart '],
}

#Nesting a Dictionary in a Dictionary

travel_details = {
    "France": {
        "Cities_travelled": ['Paris', 'Lille', 'Nice'],
        "Time_travelled": ['13-oct-2025', '16-nov-2025', '11-Jan-2026'],
        "Total_visits": 3,
    },
    "Germany": {
        "Cities_travelled": ['Berlin', 'Hamburg', 'Struttgart '],
    }
}

#Nesting a Dictionary inside a List

travel_details_nd = [
    {"country": "France",
     "Cities_travelled": ['Paris', 'Lille', 'Nice'],
     "Time_travelled": ['13-oct-2025', '16-nov-2025', '11-Jan-2026'],
     "Total_visits": 3,
    },
    {"country": "Germany",
     "Cities_travelled": ['Berlin', 'Hamburg', 'Struttgart '],
    }
]

travel_log_new = [
    {
        "country": "France",
        "visits" : 12,
        "cities" : ['Paris', 'Lille', 'Nice'],
    },
    {
        "country": "Germany",
        "visits" : 5,
        "cities" : ['Berlin', 'Hamburg', 'Struttgart '],
    }
]

def add_new_countries(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] =  visits
    new_country["cities"] = cities
    travel_log_new.append(new_country)

# add_new_countries("Russia", 5, ["Moscow", "St. Petersburg"])
# add_new_countries("Russia")
# print(travel_log_new)


print("welcome to auction")

name = input("Enter your name: ")
amount = int(input("Enter your bit: "))
biders = input("Are they other biders? enter 'yes' or 'no': ").lower()
biders_info = []
single_bider = {"name": name, "amount": amount}
biders_info.append(single_bider)
if biders == "no":
    print(f"You are the winner, {single_bider["name"]} with a bid of ${single_bider["amount"]}")
else:
    while biders == "yes":
        name = input("Enter your name: ")
        amount = int(input("Enter your bit: "))
        biders = input("Are they other biders? enter 'yes' or 'no': ").lower()
        next_bider = {"name": name, "amount": amount}
        biders_info.append(next_bider)

        if biders == "no":
            for n in biders_info:
                if n["amount"] == max(0, amount):
                    print(f"The winner is {n["name"]} with a bid of ${n["amount"]}, ")

# print(biders_info)
# print(travel_log_new)