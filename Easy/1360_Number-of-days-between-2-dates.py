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