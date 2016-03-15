def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        print("Digite uma Cidade valida")

def rental_car_cost(day):
    if day >= 7:
        return (day * 40) - 50
    elif day >= 3:
        return (day * 40) - 20
    else:
        return day * 40
def spending_money(card):
    return card

def trip_cost(city, day, card):
    return rental_car_cost(day) + hotel_cost(day) + plane_ride_cost(city) + spending_money(card)
