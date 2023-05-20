import random

def random_number_generator(min_value=1, max_value=100):
    return random.randint(min_value, max_value)

random_number = random_number_generator()
print("随机数是:", random_number)
