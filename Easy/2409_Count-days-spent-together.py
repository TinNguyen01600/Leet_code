# Alice and Bob are traveling to Rome for separate business meetings.
# You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. 
# Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), 
# while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). 
# Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.
# Return the total number of days that Alice and Bob are in Rome together.
# You can assume that all dates occur in the same calendar year, 
# which is not a leap year. Note that the number of days per month can be represented as: 
# [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

# Input: arriveAlice = "08-15", leaveAlice = "08-18", 
# arriveBob = "08-16", leaveBob = "08-19"
# Output: 3

# Input: arriveAlice = "10-01", leaveAlice = "10-31", 
# arriveBob = "11-01", leaveBob = "12-31"
# Output: 0

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
class visitor:
    def __init__(self, month_arrive, day_arrive, month_leave, day_leave) -> None:
        self.month_arrive = month_arrive
        self.day_arrive = day_arrive
        self.month_leave = month_leave
        self.day_leave = day_leave
    def ordinal_arrive(self):  # calculate the ordinal number in year of arrive date
        date = 0
        for i in range(self.month_arrive - 1): date += month[i]
        date += self.day_arrive
        return date
    def ordinal_leave(self):  # calculate the ordinal number in year of leave date
        date = 0
        for i in range(self.month_leave - 1): date += month[i]
        date += self.day_leave
        return date
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        Alice = visitor(int(arriveAlice[0] + arriveAlice[1]), int(arriveAlice[3] + arriveAlice[4]),
                        int(leaveAlice[0] + leaveAlice[1]), int(leaveAlice[3] + leaveAlice[4]))

        Bob = visitor(int(arriveBob[0] + arriveBob[1]), int(arriveBob[3] + arriveBob[4]),
                    int(leaveBob[0] + leaveBob[1]), int(leaveBob[3] + leaveBob[4]))

        al = Alice.ordinal_leave()
        ar = Alice.ordinal_arrive()
        bl = Bob.ordinal_leave()
        br = Bob.ordinal_arrive()
        l = [al - br + 1, bl - ar + 1, al - ar + 1, bl - br + 1]
        min = l[0]
        for i in l:
            if i < 0:   return 0
            elif i < min:   min = i
        return min