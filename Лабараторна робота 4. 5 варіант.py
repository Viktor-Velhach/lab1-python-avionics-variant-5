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
event=[]
dang_event=[]
ord_event=[]
l=int(input('Enter number of events'))
for i in l:
    event_type=input('')
    priority=int(input(''))
    payload=input('')
    event[i]=(event_type, priority, payload)
    match priority:
        case 1:   #add dangerous events in saparete list
            dang_event=event[i].append()     
        case 2|3: #add ordinary events in saparete list
            ord_event=event[i].append()

#Задача 3


#Задача 4