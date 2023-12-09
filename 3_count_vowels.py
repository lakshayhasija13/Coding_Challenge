def count_vowels(input_str):
    vowels = "aeiouAEIOU"
    return sum(1 for char in input_str if char in vowels)

count_vowels("Hello, World!")  # Should return 3
count_vowels("Programming is fun")  # Should return 5

----------------------------------------------------------------------------------------------------------------------

def count_vowels(input_str):
    vowel_count = 0
    vowels = 'aeiouAEIOU'
    for char in input_str:
        if char in vowels:
            vowel_count += 1
    return vowel_count

count_vowels("Hello, World!")  # Should return 3
count_vowels("Programming is fun")  # Should return 5
