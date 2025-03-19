#example output
words = ["apple", "banana", "cherry", "date"]
#Expected Output:
['APPLE', 'BANANA', 'CHERRY', 'DATE']

words = ["apple", "banana", "cherry", "date"]
uppercase_words = list(map(lambda word: word.upper(), words))
print(uppercase_words)

#Problem 2: Filter Prime Numbers
  #You are given a list of numbers. Use filter() and a lambda function to extract only the prime numbers.


numbers = [10, 7, 15, 23, 17, 8, 29, 30]
#Expected output
[7, 23, 17, 29]

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

numbers = [10, 7, 15, 23, 17, 8, 29, 30]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)

#Problem 3: Find Palindromes

words = ["madam", "hello", "racecar", "python", "level"]

#Expected Output:
['madam', 'racecar', 'level']

words = ["madam", "hello", "racecar", "python", "level"]
palindromes = list(filter(lambda word: word == word[::-1], words))
print(palindromes)
