"""
1491. Average Salary Excluding the Minimum and Maximum Salary

You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary.

Constraints:

3 <= salary.length <= 100
1000 <= salary[i] <= 10^6
All the integers of salary are unique.
"""

def average(salary: list[int]) -> float:
    salary.remove(min(salary))
    salary.remove(max(salary))
    return sum(salary) / len(salary)

if __name__ == "__main__":
    print(average(salary = [4000,3000,1000,2000])) # 2500
    print(average(salary = [1000,2000,3000])) # 2000
