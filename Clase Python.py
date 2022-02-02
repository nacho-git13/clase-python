from functools import reduce

def run():
    cuadraditos = []
    
    i = 1
    while i <= 100:
        nums = i**2
        cuadraditos.append(nums)
        i+=1


    """list comprehension"""
    cuadrados = [i**2 for i in range(1, 101) if i % 3 != 0]
    # print(cuadrados)

    multiples = [i for i in range (1, 1000) if i % 4 == 0 if i % 6 ==0 if i % 9 == 0]
    # print(multiples)

    """dictionary comprehension"""
    my_dict = {i: i**3  for i in range(1, 101) if i % 3 != 0}
     # print(my_dict)

    """Higher Order Functions"""
    lista = [1, 2, 3, 4, 5, 6]

    reduced = reduce(lambda a, b: a*b, lista)
    # print("reduce:", reduced)

    filtered = list(filter(lambda a: a % 3 != 0, lista))
    # print("filter:", filtered)

    mapped = list(map(lambda x: x**2, lista))
    # print("map:", mapped)



if __name__ == "__main__":
    run()