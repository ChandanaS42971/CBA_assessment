sentence = input("Enter a sentence: ").replace(" ", "").lower()

if sentence == sentence[::-1]:
    print("The sentence is a palindrome.")
else:
    print("The sentence is not a palindrome.")
