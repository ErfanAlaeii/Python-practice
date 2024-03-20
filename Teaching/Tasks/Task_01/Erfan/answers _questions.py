# Question 1

# Ask the user their name and store it in a variable
name = input("What is your name? ")

# Greet the user by name
print(f"My name is {name}.")

# Question 2
# Get a number from the user
try:
    number = int(input("Enter a number: "))

    # Check if the number is even or odd
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

except ValueError:
    print("Please enter only numbers")

# Question 3

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
except ValueError:
    print(" Please enter only numbers")
    exit()

# Check if the three numbers can form a triangle
if (num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1):
    print("Yes, these numbers can form a triangle.")
else:
    print("No, these numbers cannot form a triangle.")


# Question 4

def factorial_calculation():
    while True:
        try:
            # Get a number from the user
            number = int(input("Enter a number: "))
        except ValueError:
            print("Please enter only numbers")
            exit()
        # Check if the number is greater than 10
        if number > 10:
            print("Please enter a number less than 10")
            continue
        else:
            # Calculate the factorial of the number
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
        print(f"The factorial of {number} is: {factorial}")
        return factorial


factorial_calculation()

# Question 5

# Get five numbers from the user
numbers = []
for i in range(5):
    try:
        number = float(input(f"Enter number {i + 1}: "))
    except ValueError:
        print("Please enter only numbers")
        exit()
    numbers.append(number)

# Sort the numbers in descending order
numbers.sort(reverse=True)

# Print the sorted numbers
print("The numbers in descending order are:", numbers)

# Question 6

# Create empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Get 10 numbers from the user
for i in range(10):
    try:
        number = int(input(f"Enter number {i + 1}: "))
    except ValueError:
        print("Please enter only numbers")
        exit()
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Print the even and odd numbers
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# Question 7

# Get 10 numbers from the user
numbers = []
for i in range(10):
    try:
        number = int(input(f"Enter number {i + 1}: "))
    except ValueError:
        print("Please enter only numbers")
        exit()
    numbers.append(number)

# Find the largest and smallest numbers
largest = max(numbers)
smallest = min(numbers)

# Calculate the difference
difference = largest - smallest

# Print the difference
print(f"The difference between the largest and smallest numbers is: {difference}")


# Question 8

def is_prime(num):
    """Checks if a number is prime.

    Args:
        num: The number to check.

    Returns:
        True if the number is prime, False otherwise.
    """

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter only numbers")
    exit()

# Print the prime numbers less than the given number
if number <= 1:
    print("Please enter a number greater than 1.")

print("Prime numbers less than", number, ":")
for i in range(2, number):
    if is_prime(i):
        print(i)

# Question 9

# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Reverse the sentence
reversed_sentence = sentence[::-1]

# Print the reversed sentence
print("The reversed sentence is:", reversed_sentence)


# Question 10

def separate_letters_numbers(text):
    """Separates letters and numbers from a string and stores them in separate strings.

    Args:
        text: The string to separate.

    Returns:
        A tuple containing two strings: one with letters and one with numbers.
    """

    letters = ""
    numbers = ""
    for char in text:
        if char.isalpha():
            letters += char
        elif char.isdigit():
            numbers += char
    return letters, numbers


# Get a string from the user
text = input("Enter a string: ")

# Separate letters and numbers
letters, numbers = separate_letters_numbers(text)

# Print the separated letters and numbers
print("Letters:", letters)
print("Numbers:", numbers)


# Question 11
def fibonacci_up_to(n):
    """Generates a list of Fibonacci numbers up to a given number.

    Args:
        n: The maximum number in the Fibonacci sequence.

    Returns:
        A list of Fibonacci numbers less than or equal to n.
    """

    if n < 1:
        return []
    elif n == 1:
        return [1]
    else:
        fib_sequence = [1, 1]
        while fib_sequence[-1] <= n:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence[:-1]


# Get a number from the user
try:
    number = float(input("Enter a number: "))
except ValueError:
    print("Please enter only numbers")
    exit()

if number < 1:
    print("Please enter a number greater than 1")
else:
    # Print the Fibonacci numbers less than the given number
    print("Fibonacci numbers less than", int(number), ":")
    fibonacci_sequence = fibonacci_up_to(number)
    print(fibonacci_sequence)

# Question 12

# Get a sentence from the user
sentence = input("Enter a sentence: ")

if sentence.isalpha():

    number_of_words = len(sentence)

    # Print the number of words
    print("The sentence has", number_of_words, "words.")

else:
    print("Please enter letters")


# Question 13

def create_user_info_dict():
    """Creates a dictionary to store user information.

    Returns:
        A dictionary containing user information (name, surname, age, location, favorite movie, favorite color).
    """

    user_info = {}
    user_info["name"] = input("What is your name? ")
    user_info["surname"] = input("What is your surname? ")
    try:
        user_info["age"] = int(input("How old are you? "))
    except ValueError:
        print("Enter Number")
    user_info["location"] = input("Where are you from? ")
    user_info["favorite_movie"] = input("What is your favorite movie? ")
    user_info["favorite_color"] = input("What is your favorite color? ")
    return user_info


# Create a dictionary to store user information
user_info = create_user_info_dict()

# Print the user information
print("User information:")
for key, value in user_info.items():
    print(f"{key.capitalize()}: {value}")


# Question 14

def is_prime(num):
    """Checks if a number is prime.

    Args:
        num: The number to check.

    Returns:
        True if the number is prime, False otherwise.
    """

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


number = input("Enter a four-digit number:")

if number.isdigit():
    if len(number) == 4:
        prime_numbers = []
        for i in range(2, int(number)):
            if is_prime(i):
                prime_numbers.append(i)
        print(sorted(prime_numbers, reverse=True))
    else:
        print("The number you entered must be four digits")
else:
    print("Please enter a number")


# Question 15

def compare_dates():
    """Compares two dates entered by the user and prints the earlier date.

    Returns:
        None
    """

    def get_date_as_numbers():
        """Gets a date from the user in YYYY/MM/DD format and converts it to a list of integers.

        Returns:
            A list containing the year, month, and day as integers.
        """

        date_text = input("Enter a date in YYYY/MM/DD format: ")
        year, month, day = map(int, date_text.split("/"))
        return [year, month, day]

    try:
        # Get the first date
        print("Enter the first date:")
        date1 = get_date_as_numbers()

        # Get the second date
        print("Enter the second date:")
        date2 = get_date_as_numbers()
    except Exception:
        print("Please enter the numbers according to the requested format")
        exit()
    # Compare the dates
    if date1 < date2:
        print("The earlier date is:", "/".join(map(str, date1)))
    else:
        print("The earlier date is:", "/".join(map(str, date2)))


# Call the function to compare dates
compare_dates()


# Question 16

def print_colored_characters():
    """Prints a string's characters in different colors based on their type (number, uppercase letter, lowercase letter).

    Args:
        None

    Returns:
        None
    """

    text = input("Enter a string: ")
    color_codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }

    for char in text:
        if char.isdigit():
            color = color_codes["green"]
        elif char.isupper():
            color = color_codes["red"]
        elif char.islower():
            color = color_codes["blue"]
        else:
            print("Enter letters or numbers")
            continue

        print(color + char + color_codes["reset"], end='')


# Call the function to print colored characters
print_colored_characters()


# Question 17
def calculate_fruit_cost():
    """Calculates the total cost of fruits based on user input and a provided fruit price dictionary.

    Returns:
        None
    """

    fruits_dict = {
        "Sib": 15000,
        "Anbe": 23000,
        "Moz": 12000,
        "Portagal": 20000
    }

    # Get quantities of each fruit
    quantities = {}
    for fruit in fruits_dict.keys():
        try:
            quantity = float(input(f"How many kilograms of {fruit} did you buy? "))
        except Exception:
            print("Enter an integer")
            exit()
        if quantity > 0:
            quantities[fruit] = quantity
        else:
            print("We do not have negative weight, some weight is positive")
            return

            # Calculate the total cost for each fruit
    total_costs = {}
    for fruit, quantity in quantities.items():
        total_costs[fruit] = fruits_dict[fruit] * quantity

    # Calculate the total cost of all fruits
    total_cost = sum(total_costs.values())

    # Print the total cost for each fruit and the grand total
    print("Fruit costs:")
    for fruit, cost in total_costs.items():
        print(f"{fruit}: {cost}")
    print(f"Grand total: {total_cost}")


# Call the function to calculate fruit cost
calculate_fruit_cost()



# Question 18

def strong_password_checker():
    """Checks if a password meets strong password criteria.

    Returns:
        True if the password is strong, False otherwise.
    """

    while True:
        even_flag = False
        odd_flag = False
        lower_flag = False
        upper_flag = False
        char_flag = False
        char = "@ # $ ! %"
        chars_upper = True
        chars_numeric = True

        user = input("Enter Password:")
        if len(user) > 5:
            for i in user:
                if i.isdigit():
                    numbers = int(i)
                    if numbers % 2 == 0:
                        even_flag = True
                    else:
                        odd_flag = True

                if i.islower():
                    lower_flag = True

                if i.isupper():
                    upper_flag = True

                if i in char:
                    char_flag = True

            for i in range(len(user) - 1):
                try:
                    if user[i].isupper() and user[i + 1].isupper():
                        chars_upper = False
                except IndexError:
                    pass

            for i in range(len(user) - 2):
                try:
                    if user[i].isdigit() and user[i + 1].isdigit() and user[i + 2].isdigit():
                        chars_numeric = False
                except IndexError:
                    pass

        if not all([even_flag, odd_flag, lower_flag, upper_flag, char_flag, char, chars_upper, chars_numeric]):
            print(
                "Password must contain at least one uppercase letter, lowercase letter, number, and special character.")

            continue
        else:
            return True


if strong_password_checker():
    print("Your password correct")


# Question 19

def count_character_occurrences():
    """Prompts the user for a sentence and creates a dictionary to store the frequency of each character.

    Returns:
        None
    """

    sentence = input("Enter a sentence: ")
    char_counts = {}

    for char in sentence:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    if not char_counts:
        print("Please enter a valid value and do not leave it blank")
        return

        # Print the character occurrences (excluding spaces)
    print("Character occurrences (excluding spaces):")
    for char, count in char_counts.items():
        if char != " ":
            print(f"{char}: {count}")


# Call the function to count character occurrences
count_character_occurrences()


# Question 20
import datetime


# Function to calculate time difference until the next alert
def calculate_alert(hour, minute, second):
    # Get the current time
    current_time = datetime.datetime.now()
    # Create a datetime object for the desired alert time
    alert_time = datetime.datetime.replace(current_time, hour=hour, minute=minute, second=second)

    # Calculate the time difference between current time and alert time
    time_diff = alert_time - current_time

    # If the alert time is in the past (i.e., next day), add a day to the time difference
    if time_diff < datetime.timedelta(0):
        time_diff += datetime.timedelta(days=1)

    return time_diff


# Take input for hour, minute, and second from the user
hour = int(input("Enter hour:"))
minute = int(input("Enter minute:"))
second = int(input("Enter second:"))

# Check if the input values are valid (hour, minute, and second should be within valid ranges)
if 0 < hour < 24 and 0 < minute < 60 and 0 < second < 60:
    # Calculate the time difference until the next alert
    difference = calculate_alert(hour, minute, second)
    # Print the time difference
    print(difference)
else:
    # If the input values are not valid, print an error message
    print("Enter a valid value")

# finish answer
