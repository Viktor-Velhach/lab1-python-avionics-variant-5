#Задача 1
force=float(input(''))
force_min=float(input(''))#
tank_level=float(input(''))
tank_level_min=float(input(''))#
l_to_zps=float(input(''))
l_max=float(input(''))#
if force<force_min and tank_level<tank_level_min and l_to_zps>l_max:
    print("Аварійна посадка в полі")
elif force<force_min and tank_level<tank_level_min and l_to_zps<l_max:
    print("Посадка на ЗПС")
elif force>force_min and tank_level>tank_level_min and l_to_zps<l_max:
    print("Продовження місії")

#Задача 2
'''event_type=
priority=
payload='''
event=(event_type=input(''), priority=int(input('')), payload=input(''))
match ...:
    case 

#Задача 3


#Задача 4