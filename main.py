import random

def generate_random_list(num_elements):
    return [random.randint(5, 800) for _ in range(num_elements)]

if __name__ == "__main__":
    num_elements = 18
    random_list = generate_random_list(num_elements)
    print(random_list)
