class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        # COMPLETELY OWN SOLVED
        a = sorted(seats)
        b = sorted(students)
        answer = 0
        for i in range(len(seats)):
            answer += abs(a[i]-b[i])
        return answer
