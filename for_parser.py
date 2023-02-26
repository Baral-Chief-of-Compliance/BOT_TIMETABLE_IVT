from bs4 import BeautifulSoup
import requests
from datetime import date, timedelta
import for_date as fd


def timetable_on_week():
    with open("time_table.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    all_tables = soup.find_all(class_ = "table table-bordered table-striped table-3")
    all_tables.pop(6)

    result = ""

    for item in all_tables:
        day_titel = item.find(class_="title")
        subjects_title = item.find_all("tr")
        subjects_title.pop(0)

        result = result + "----" + day_titel.text + "----\n"
        for subject in subjects_title:
            subjects_td = subject.find_all("td")
            i = 0
            for subject_td in subjects_td:
                i += 1
                if i == 1:
                    result = result + subject_td.text + ") "
                else:
                    result = result + subject_td.text + " "
            result = result + "\n"
        result = result + "----------------" + "\n\n"

    return result


def timetable_on_today():

    with open("time_table.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    all_tables = soup.find_all(class_ = "table table-bordered table-striped table-3")
    all_tables.pop(6)

    result = ""

    today = date.today()
    isoWeekDay = today.isoweekday()

    if isoWeekDay == 7:
        result = 'Сегодня выходной, папаша'
    else:

        i = 1

        for item in all_tables:
            if isoWeekDay == i:
                day_titel = item.find(class_="title")
                subjects_title = item.find_all("tr")

                subjects_title.pop(0)

                result = result + "----" + day_titel.text + "----\n"
                for subject in subjects_title:
                    subjects_td = subject.find_all("td")
                    i = 0
                    for subject_td in subjects_td:
                        i += 1
                        if i == 1:
                            result = result + subject_td.text + ") "
                        else:
                            result = result + subject_td.text + " "
                    result = result + "\n"
                result = result + "----------------" + "\n\n"
            i += 1

    return result


def timetable_next_week():
    with open("next_week_timetable.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    all_tables = soup.find_all(class_ = "table table-bordered table-striped table-3")
    all_tables.pop(6)

    result = ""

    for item in all_tables:
        day_titel = item.find(class_="title")
        subjects_title = item.find_all("tr")
        subjects_title.pop(0)

        result = result + "----" + day_titel.text + "----\n"
        for subject in subjects_title:
            subjects_td = subject.find_all("td")
            i = 0
            for subject_td in subjects_td:
                i+=1
                if i == 1:
                    result = result + subject_td.text + ") "
                else:
                    result = result + subject_td.text + " "
            result = result + "\n"
        result = result + "----------------" + "\n\n"

    return result


def get_schedule_time():
    return (
        "1 пара\n"
        "09:00 - 09:45\n"
        "09:50 - 10:35\n\n"
        "2 пара\n"
        "10:45 - 11:30\n"
        "11:35 - 12:20\n\n"
        "3 пара\n"
        "12:40 - 13:25\n"
        "13:30 - 14:15\n\n"
        "4 пара\n"
        "14:45 - 15:30\n"
        "15:35 - 16:20\n\n"
        "5 пара\n"
        "16:30 - 17:15\n"
        "17:20 - 18:05\n\n"
        "6 пара\n"
        "18:15 - 19:00\n"
        "19:05 - 19:50\n\n"
        "7 пара\n"
        "20:00 - 20:45\n"
        "20:50 - 21:35\n\n"
    )