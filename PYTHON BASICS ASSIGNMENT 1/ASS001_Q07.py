# QUESTION 7

def count_dog(input_string):
    words = input_string.lower().split()
    return words.count('dog')

# Example usage
input_string = "I have a dog, and my friend also has a dog."
dog_count = count_dog(input_string)
print(dog_count)

