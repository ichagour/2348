import math
Service = {'Oil change': 35, 'Tire rotation': 19, 'car wash': 7,'Car wax': 12}
total = 0
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")
oilChange = 35
tireRotation = 19
carWash = 7
carWax = 12
Service_1 = input('Select first service:\n')
Service_2 = input('Select second service:\n')
print('')
print("Davy's auto shop invoice\n")
if Service_1 == '-':
    print('Service 1: No service')
else:
    print('Service 1: %s, $%d' % (Service_1, Service.get(Service_1)))
if Service_2 == '-':
    print('Service 2: No service')
else:
    print('Service 2: %s, $%d' % (Service_2, Service.get(Service_2)))
total = Service.get(Service_1) + Service.get(Service_2)
print()
print('Total: $%d' % str(total))