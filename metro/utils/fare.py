def calculate_fare (num_station):
    if num_station <= 5:
        return 20
    elif num_station <=10:
        return 30
    elif num_station <= 15:
        return 40
    else :
        return 50