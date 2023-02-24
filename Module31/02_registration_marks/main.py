import re


car_nums = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_car_pattern = r'\b\w{1}\d{3}\w{2}\d{2,3}'
taxi_pattern = r'\b\w{2}\d{5,6}'

res = re.findall(private_car_pattern, car_nums)
print("Список номеров частных автомобилей:", res)

res_2 = re.findall(taxi_pattern, car_nums)
print("Список номеров такси:", res_2)
