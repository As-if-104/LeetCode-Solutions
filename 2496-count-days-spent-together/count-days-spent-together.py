class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def days_of_year(date: str) -> int:
            month = int(date[:2])
            day = int(date[3:])

            return sum(days_in_month[:month-1]) + day
        
        arriveA = days_of_year(arriveAlice)
        arriveB = days_of_year(arriveBob)
        leaveA = days_of_year(leaveAlice)
        leaveB = days_of_year(leaveBob)

        start = max(arriveA, arriveB)
        end = min(leaveA, leaveB)

        return max(0, end-start+1)
        