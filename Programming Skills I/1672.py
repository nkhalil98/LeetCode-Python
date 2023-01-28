"""
1672. Richest Customer Wealth

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100
"""

def maximumWealth(accounts: list[list[int]]) -> int:
        wealths = [sum(account) for account in accounts]
        return max(wealths)

if __name__ == "__main__":
    # test cases
    assert maximumWealth([[1,2,3],[3,2,1]]) == 6
    assert maximumWealth([[1,5],[7,3],[3,5]]) == 10
    assert maximumWealth([[2,8,7],[7,1,3],[1,9,5]]) == 17