user=input("Enter the letter: ")
vowels="aeiouAEIOU"
for char in user:
    if char in vowels:
        print("Vowel found:", char)
        break
    else:
        print("Vowel not found")