if __name__ == '__main__':
    import math

    print(math.floor(4.25))
    print(math.ceil(4.25))
    print(round(4.25))
    print(round(4.5))
    print(round(5.5))

    print(math.pi)
    print(math.e)
    print(math.inf)
    print(math.nan)
    print(math.log(math.e))

    print(math.sin(100))
    print(math.degrees(math.pi / 2))
    print(math.radians(100))

    import random

    print(random.randint(0, 100))
    print(random.randrange(0, 100, 5))

    random.seed(12)
    print(random.randint(0, 100))  # we're always going to same the same number because we've already specified a seed (result=60)

    new_list = list(range(0,20))
    print(random.choice(new_list))  # always the same choice

    print(random.choices(population=new_list, k=10))  # sampling with replacement = numbers could be repeated / picked twice
    print(random.sample(population=new_list, k=10))  # sampling without replacement = numbers won't be repeated / picked twice
    print(random.shuffle(new_list))

    print(random.uniform(a=0, b=100))
    print(random.gauss(mu=0, sigma=1))