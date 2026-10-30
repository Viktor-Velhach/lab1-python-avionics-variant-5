#Задача 1
power=float(input('Enter a power of engine(in %): '))
power_min=float(input('Enter minimal power of engine(in %): '))#Necessary reference data for comparison
tank_level=float(input('Enter a tank level (in %): '))
tank_level_min=float(input('Enter a minimal tank level (in %): '))#Necessary reference data for comparison
l_to_zps=float(input('Enter a distance to runway: '))
l_max=float(input('Enter maximal distance to runway: '))#Necessary reference data for comparison
if power<power_min and tank_level<tank_level_min and l_to_zps>l_max:
    print("Аварійна посадка в полі")
elif power<power_min and tank_level<tank_level_min and l_to_zps<l_max:
    print("Посадка на ЗПС")
elif power>power_min and tank_level>tank_level_min and l_to_zps<l_max:
    print("Продовження місії")

#Задача 2
event=[]
dang_event=[]
ord_event=[]
l=int(input('Enter number of events: '))
for i in l:
    event_type=input('Enter event_type: ')
    priority=int(input('Enter priority: '))
    payload=input('Enter payload: ')
    event[i]=(event_type, priority, payload)
    match priority:
        case 1:   #add dangerous events in saparete list
            dang_event=event[i].append()     
        case 2|3: #add ordinary events in saparete list
            ord_event=event[i].append()
print("Dangerous events: ", dang_event)

#Задача 3


#Задача 4