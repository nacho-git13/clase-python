from audioop import mul


def run():
    # cuadrados = []
    
    # i = 1
    # while i <= 100:
    #     nums = i**2
    #     cuadrados.append(nums)
    #     i+=1


    # list comprehension
    cuadrados = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(cuadrados)

    multiples = [i for i in range (1, 1000) if i % 4 == 0 if i % 6 ==0 if i % 9 == 0]
    print(multiples)

    #


if __name__ == "__main__":
    run()