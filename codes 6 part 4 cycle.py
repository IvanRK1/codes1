string = "Hello welcome to the world of Python"
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)
print("Number of vowels=", count)