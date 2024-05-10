""" This module calculates the age """
import datetime

def get_age(yyyy:int, mm:int, dd:int) -> int:
""" This function return the age """
    dob = datetime.date(yyyy, mm, dd)
    today = datetime.date.today()
    age = round((today - dob).days / 365.25)
    return age
