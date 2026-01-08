for big_chicken in range(21):
    for hen in range(34):
        small_chicken = 100 - big_chicken - hen
        if small_chicken >= 0 and (5 * big_chicken + 3 * hen + small_chicken / 3) == 100:
            print(f"big chicken have: {big_chicken}, hen have: {hen}, small chicken have: {small_chicken}")