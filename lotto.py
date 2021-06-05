import random


def drawn_numbers():  # function for drawing random 6 numbers without duplicates
    nums_array = random.sample(range(1, 50), 49)
    random_arr = []
    random_arr_temp = []
    while len(random_arr) < 6:
        random_arr_temp.append(random.choice(nums_array))
        for elem in random_arr_temp:
            if elem not in random_arr:
                random_arr.append(elem)

    return sorted(random_arr)


def user_numbers():  # drawing 6 different numbers from user
    print("Podaj sześć liczb w zakresie 1-49")
    user_array = []
    i = 1
    while i < 7:
        try:
            user_input = int(input(f"Podaj {i} liczbę: "))
            if user_input not in range(1, 50):
                raise TypeError("Błędny zakres liczb!")
        except ValueError:
            raise ValueError("Błędny typ danych")
        for elem in user_array:
            if user_input in user_array:
                raise TypeError("Dubel !")
        user_array.append(user_input)
        i += 1
    return sorted(user_array)


def print_numbers(numbers):  # function for printing results
    print(", ".join(str(number) for number in sorted(numbers)))


def lotto():  # main app func
    user_nums = user_numbers()
    print("Numbers you picked: ")
    print_numbers(user_nums)
    random_nums = drawn_numbers()
    print("Lotto numbers: ")
    print_numbers(random_nums)

    counter = 0
    for i in user_nums:
        if i in random_nums:
            counter += 1
    print(f"You guessed {counter} numbers !")


if __name__ == '__main__':
    lotto()
