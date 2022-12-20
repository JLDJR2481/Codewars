def rental_car_cost(d):
    d > 0

    if d < 3:
        return 40 * d
    elif d >= 3 and d < 7:
        return (40 * d) - 20
    else:
        return (d * 40) - 50


if __name__ == "__main__":
    assert rental_car_cost(1) == 40
    assert rental_car_cost(4) == 140
    assert rental_car_cost(7) == 230
    assert rental_car_cost(8) == 270
