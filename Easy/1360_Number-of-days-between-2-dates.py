# Write a program to count the number of days between two dates.
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1

# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def leap(year) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
class Date:
    def __init__(self, year, month, day) -> None:
        self.day = day
        self.month = month
        self.year = year
    def ordinal(self):
        date = 0
        if leap(self.year): month[1] = 29
        else:   month[1] = 28
        for i in range(self.month - 1): date += month[i]
        date += self.day
        return date
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = Date(int(date1[0] + date1[1] + date1[2] + date1[3]), int(date1[5] + date1[6]),
             int(date1[8] + date1[9]))
        d2 = Date(int(date2[0] + date2[1] + date2[2] + date2[3]), int(date2[5] + date2[6]),
                    int(date2[8] + date2[9]))
        if d1.year == d2.year:
            result = abs(d1.ordinal() - d2.ordinal())
        else:
            if d1.year < d2.year: 
                before = d1
                after = d2
            elif d2.year < d1.year:
                before = d2
                after = d1
            if leap(before.year):    
                result = 366 - before.ordinal() + after.ordinal()
            else:   
                result = 365 - before.ordinal() + after.ordinal()
            for i in range(before.year + 1, after.year):
                result += 365 + leap(i)
        return result
    
class Solution2:
    def ordinal(date) -> int:
        y, m, d = map(int, date.split("-"))
        ordinal = 0
        if leap(y): month[1] = 29
        else:       month[1] = 28
        for i in range(m-1):    ordinal += month[i]
        ordinal += d
        return ordinal
    def days_between_dates(self, date1: str, date2: str) -> int:
        if date1 > date2:
            date1, date2 = date2, date1
        y1, m1, d1 = map(int, date1.split("-"))
        y2, m2, d2 = map(int, date2.split("-"))
        d = (date1, date2)
        ord = map(self.ordinal, d)   
        ord = list(ord)
        if y1 == y2:    # same year
            result = ord[1] - ord[0]
        else:
            result = 365 - ord[0] + ord[1] + leap(y1)
            for i in range(y1 + 1, y2): result += 365 + leap(i)