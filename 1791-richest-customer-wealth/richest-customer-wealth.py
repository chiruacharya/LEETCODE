class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        # COMPLETELY OWN SOLVED
        max_wealth = 0
        for i in accounts:
            max_wealth = max(max_wealth,sum(i))
        return max_wealth