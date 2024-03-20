def kidsWithCandies(candies, extraCandies):
    max_candies=max(candies)
    return [x+extraCandies>=max_candies for x in candies ]
if __name__ == '__main__':
    print(kidsWithCandies([2, 3, 5, 1, 3], 3))
