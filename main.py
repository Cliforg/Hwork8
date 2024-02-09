from datetime import date, timedelta

def get_birthdays_per_week(users):

    def get_day_name(day_code): 
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days_of_week[day_code]

    result = {}
    if len(users) == 0:
        return result
    today = date.today()
    today_weekday = today.weekday()
    for user in users:
        name = user['name']
        birthday = user['birthday']
        if (date.today().month == 12) and (user['birthday'].month == 1):
            days_until_birthday = (birthday.replace(year=date.today().year+1) - date.today()).days
            us_bd_current_year = user["birthday"].replace(year=date.today().year+1)
        else:
            days_until_birthday = (birthday.replace(year=date.today().year) - date.today()).days
            us_bd_current_year = user["birthday"].replace(year=date.today().year)
       
        match today_weekday:                                               
            case 0:                                                                 
                if days_until_birthday in (-2, -1 , 0):
                    if "Monday" not in result:
                        result["Monday"] = [user["name"]]
                    else:
                        result["Monday"].append(user["name"])
                elif days_until_birthday in (1, 2, 3, 4):
                    birthday_weekday_name = get_day_name(us_bd_current_year.weekday())
                    if birthday_weekday_name not in result:
                        result[birthday_weekday_name] = [user["name"]]
                    else:                    
                        result[birthday_weekday_name].append(user["name"])

            case 6:                                                                
                if days_until_birthday in (-1, 0, 1):
                    if "Monday" not in result:
                        result["Monday"] = [user["name"]]
                    else:
                        result["Monday"].append(user["name"])
                elif days_until_birthday in (2, 3, 4, 5):
                    birthday_weekday_name = get_day_name(us_bd_current_year.weekday())
                    if birthday_weekday_name not in result:
                        result[birthday_weekday_name] = [user["name"]]
                    else:                    
                        result[birthday_weekday_name].append(user["name"])

            case _:                                                                 
                birthday_weekday_name = get_day_name(us_bd_current_year.weekday())   
                if birthday_weekday_name in ("Saturday", "Sunday"):
                    birthday_weekday_name = "Monday"  
                if days_until_birthday in (0, 1, 2, 3, 4, 5, 6):
                    if birthday_weekday_name not in result:
                        result[birthday_weekday_name] = [user["name"]]
                    else:                    
                        result[birthday_weekday_name].append(user["name"])
    return result

users = [
    {"name": "Bill", "birthday": date(2002, 1, 8)},
    {"name": "Jan", "birthday": date(2004, 1, 9)},
    {"name": "aaa", "birthday": date(2004, 1, 10)},
    {"name": "bbb", "birthday": date(2000, 1, 6)},
    {"name": "ccc", "birthday": date(1998, 1, 7)},
]

print(get_birthdays_per_week(users))

