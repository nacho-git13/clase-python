def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {
        "firstname": "Nacho",
        "lastname": "Molano"
    }

    super_list = [
        {"firstname": "Nacho", "lastname": "Molano"}, 
        {"firstname": "Isabela", "lastname": "Montoya"}, 
        {"firstname": "Samuel", "lastname": "Penagos"},
        {"firstname": "Ignacio", "lastname": "Mora"},
        {"firstname": "Pablo", "lastname": "Bastilla"},
        {"firstname": "Lucas", "lastname": "Bello"}
    ]

    super_dict = {
        "natural nums": [1, 2, 3, 4, 5],
        "integer nums": [-1, -2, 0, 1, 2],
        "floating nums": [1.1, 3.5, 6.55]
    }

    for key, value in super_dict.items():
        print(key, "-", value)



if __name__ == "__main__":
    run()