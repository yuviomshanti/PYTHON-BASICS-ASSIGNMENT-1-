# QUESTION 15

def sum_of_series(n):
    terms = [int('2' * i) for i in range(1, n + 1)]
    series_sum = sum(terms)
    return series_sum

# Calculate the sum of the series for n = 5
n = 5
result = sum_of_series(n)
print(result)

