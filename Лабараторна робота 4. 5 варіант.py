
def problem_1():
 power=float(input('Enter a power of engine(in %): '))
 power_min=float(input('Enter minimal power of engine(in %): '))#Necessary reference data for comparison
 tank_level=float(input('Enter a tank level (in %): '))
 tank_level_min=float(input('Enter a minimal tank level (in %): '))#Necessary reference data for comparison
 l_to_zps=float(input('Enter a distance to runway: '))
 l_max=float(input('Enter maximal distance that dron can fly: '))#Necessary reference data for comparison
 if power<power_min or tank_level<tank_level_min and l_to_zps>l_max:
     print("Аварійна посадка в полі")
 elif power<power_min or tank_level<tank_level_min and l_to_zps<l_max:
     print("Посадка на ЗПС")
 elif power>=power_min and tank_level>=tank_level_min:
     print("Продовження місії")

def problem_2():
 list_events=[]
 dang_event=[]
 ord_event=[]
 l=int(input('Enter number of events: '))
 for i in range(l):
     event_type=input('Enter event_type: ')
     priority=int(input('Enter priority: '))
     payload=input('Enter payload: ')
     event=[event_type, priority, payload]
     list_events.append(event)
     match priority:
         case 1:   #add dangerous events in saparete list
             dang_event.append(list_events[i])     
         case 2|3: #add ordinary events in saparete list
             ord_event.append(list_events[i])
 print("Dangerous events: ", dang_event)
 print("Ordinary events: ", ord_event)

def problem_3():
 drop=float(input('Enter how much the oxygen level drops: '))
 levelO2=float(input('Enter oxygen level(in %): '))
 while levelO2>0:
     if levelO2<=5:
         print('Oxygen level is less then 5%')
         break
     elif levelO2<=20:
         print('WARNING!Oxygen level is too low (',levelO2,')')
     levelO2-=drop

def problem_4():
 keys=['Engine','Nav','LifeSupport']
 values=[float(input('Enter power Engine: ')),float(input('Enter power Nav: ')),float(input('Enter power LifeSupport: '))]
 d={k:v for (k,v) in zip(keys,values)} #concatenating two lists in dictionary
 m=0
 p=''
 for k,v in d.items():
     if v>m: #Search the largest values of power
         m=v
         p=k #name of system that eat the most power
 print('The system that eat the most power: ',p)