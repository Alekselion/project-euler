task = "How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"

norm_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
years = [norm_year] * 100
for i in range(3, len(years), 4):
    years[i] = leap_year

current_day = 365 % 7
result = 0
for year in years:
    for month in year:
        if current_day % 7 == 6:
            result += 1
        current_day += month % 7

print(f"Task: {task}\nAnswer: {result}")