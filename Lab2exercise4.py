def calc_average_temperature(temperature_values_list):
    total = sum(temperature_values_list)
    average = total / len(temperature_values_list)
    return average

def calc_min_max_temperature(temperature_values_list):
    min_temp = min(temperature_values_list)
    max_temp = max(temperature_values_list)
    return [min_temp, max_temp]
