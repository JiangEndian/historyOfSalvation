from django.http import HttpResponseRedirect 
from django.http import HttpResponse
from django.shortcuts import render
import os, random

global glory
glory = 0
global dead_number
dead_number = 0
global big_pool 
big_pool = 600000
global all_man_list 
all_man_list = []
global year 
year = 0
global all_man_string_list
all_man_string_list = []
global all_man_number
all_man_number = 0

global name_number
name_number = {}
name_number['laborer'] = 1
name_number['elite'] = 1
name_number['christian'] = 1

def create_one_man(name_type, deposit, age=0):
    global all_man_list
    global name_number

    one_man_dict = {}
    if name_type == 0:
        one_man_dict['name'] = 'laborer' + str(name_number['laborer'])
        name_number['laborer'] += 1

        one_man_dict['eat'] = random.randint(4,8)
        one_man_dict['work_time'] = random.randint(8, 14) 
        one_man_dict['deposit'] = deposit
        one_man_dict['age'] = age
        one_man_dict['alive'] = True
        one_man_dict['children_number'] = 0
        all_man_list.append(one_man_dict)
    if name_type == 1:
        one_man_dict['name'] = 'elite' + str(name_number['elite'])
        name_number['elite'] += 1

        one_man_dict['eat'] = random.randint(40,80)
        one_man_dict['work_time'] = 0
        one_man_dict['deposit'] = deposit
        one_man_dict['age'] = age
        one_man_dict['alive'] = True 
        one_man_dict['children_number'] = 0
        all_man_list.append(one_man_dict)
    if name_type == 2:
        one_man_dict['name'] = 'christian' + str(name_number['christian'])
        name_number['christian'] += 1

        one_man_dict['eat'] = 3
        one_man_dict['work_time'] = 0
        one_man_dict['deposit'] = deposit  #every time 0, when can eat 1 or 2, reset this to 0
        one_man_dict['age'] = age
        one_man_dict['alive'] = True
        one_man_dict['children_number'] = 0
        all_man_list.append(one_man_dict)


def reset_world_emulator(request):
    global big_pool 
    big_pool = 600000
    global all_man_list 
    all_man_list = []
    global year 
    year = 0
    global all_man_string_list
    all_man_string_list = []
    global name_number
    name_number = {}
    name_number['laborer'] = 1
    name_number['elite'] = 1
    name_number['christian'] = 1
    create_one_man(0, 600, 1)
    return HttpResponseRedirect('/world_emulator')

def reset_family_calculator(request):
    global glory
    glory = 0
    global dead_number
    dead_number = 0
    global big_pool 
    big_pool = 600000
    global all_man_list 
    all_man_list = []
    global year 
    year = 0
    global all_man_string_list
    all_man_string_list = []
    global name_number
    name_number = {}
    name_number['laborer'] = 1
    name_number['elite'] = 1
    name_number['christian'] = 1
    for i in range(70):
        create_one_man(0, 600, 1)
    return HttpResponseRedirect('/family_calculator')

create_one_man(0, 600, 1)
all_man_number += 1

def world_emulator(request):
    
    global big_pool
    global all_man_list
    global year
    global glory
    global dead_number
    global all_man_number
    all_man_string_list = []

    year += 1
    laborer_number = 0
    elite_number = 0
    christian_number = 0

    for one_man_dict in all_man_list:

        if not one_man_dict['alive']:
            dead_number += 1
            all_man_list.pop(all_man_list.index(one_man_dict))
            continue

        one_man_dict['age'] += 1
        one_man_dict['deposit'] -= one_man_dict['eat']
    
        if 'laborer' in one_man_dict['name']:
            laborer_number += 1
            if laborer_number <= 1000:
                harvest = one_man_dict['work_time'] * 60
                one_man_dict['deposit'] += int(harvest * 0.2)
                big_pool += int(harvest * 0.8)
            else: #这个laborer_number是增长的。嗯。先来的101人有份，后来的人越来越少
                harvest = 600000/laborer_number
                one_man_dict['deposit'] += int(harvest * 0.2)
                big_pool += int(harvest * 0.8)
            
            if one_man_dict['deposit'] <= 0 and big_pool <= 0:
                #dead_number += 1
                one_man_dict['alive'] = False
                laborer_number -= 1
                continue
            
            if one_man_dict['deposit'] > 2000 and one_man_dict['age'] > 30:
                if one_man_dict['deposit'] > 20000:
                    if one_man_dict['age'] > 70:
                        #dead_number += 1
                        one_man_dict['alive'] = False
                        laborer_number -= 1
                        create_one_man(1, one_man_dict['deposit'])
                        all_man_number += 1
                    elif one_man_dict['children_number'] < 3:
                        create_one_man(1, 20000)
                        all_man_number += 1
                        one_man_dict['deposit'] -= 18000
                        one_man_dict['children_number'] += 1
                else:
                    if one_man_dict['age'] > 70:
                        #dead_number += 1
                        one_man_dict['alive'] = False
                        laborer_number -= 1
                        create_one_man(0, one_man_dict['deposit'])
                        all_man_number += 1
                    elif one_man_dict['children_number'] < 3:
                        create_one_man(0, 100)
                        all_man_number += 1
                        one_man_dict['deposit'] -= 100
                        one_man_dict['children_number'] += 1
                
                if random.randint(0, 100000) == 0:
                    create_one_man(2, 100)
                    all_man_number += 1

            elif one_man_dict['age'] > 70: #died as a poor man
                #dead_number += 1
                one_man_dict['alive'] = False
                laborer_number -= 1
                big_pool += one_man_dict['deposit']
    
        elif 'elite' in one_man_dict['name']:
            elite_number += 1
            if one_man_dict['deposit'] <= 0:
                #dead_number += 1
                one_man_dict['alive'] = False
            elif big_pool <= 0:
                if (one_man_dict['deposit'] + big_pool) <= 0:
                    big_pool += one_man_dict['deposit']
                    one_man_dict['deposit'] = 0
                else:
                    one_man_dict['deposit'] += big_pool
                    big_pool = 0
            else:
                earn = int(one_man_dict['deposit'] * 0.02)
                one_man_dict['deposit'] += earn
                big_pool -= earn
        
        elif 'christian' in one_man_dict['name']:
            christian_number += 1
            if one_man_dict['deposit'] <= -9 and big_pool <= 0:
                #dead_number += 1
                one_man_dict['alive'] = False
                glory += 1
                continue
            elif big_pool > 0:
                big_pool -= one_man_dict['eat']
                one_man_dict['deposit'] = 0

        if 'elite' in one_man_dict['name'] or 'christian' in one_man_dict['name']:
            one_man_string = one_man_dict['name'] + '\t, ' + str(one_man_dict['eat']) + '\t, ' + str(one_man_dict['work_time']) + '\t, ' +  str(one_man_dict['deposit']) + '\t, ' + str(one_man_dict['age']) + '\t, ' + str(one_man_dict['alive'])
            all_man_string_list.append(one_man_string)
        
    info_dict = {}
    info_dict['year'] = year
    info_dict['all_man_number'] = all_man_number
    info_dict['big_pool'] = big_pool
    info_dict['inflation_rate'] = '无，因每1是劳动时间的产出，归给谁收藏呢，愿真神富有'
    info_dict['laborer_number'] = str(laborer_number) + ', ' + str(int(laborer_number/all_man_number*100)) + '%'
    info_dict['elite_number'] = str(elite_number) + ', ' + str(int(elite_number/all_man_number*100)) + '%'
    info_dict['christian_number'] = str(christian_number) + ', ' + str(int(christian_number/all_man_number*100)) + '%'
    info_dict['dead_number'] = str(dead_number) + ', ' + str(int(dead_number/all_man_number*100)) + '%'
    info_dict['glory'] = str(glory) + ', ' + str(int(glory/all_man_number*100)) + '%'
    info_dict['all_man_info'] = all_man_string_list

    return render(request, 'world_emulator.html', info_dict) 
    


def family_calculator(request):
    
    global big_pool
    global all_man_list
    global year
    all_man_string_list = []

    year += 1
    laborer_number = 0
    elite_number = 0
    christian_number = 0
    dead_number = 0

    for one_man_dict in all_man_list:
        one_man_dict['age'] += 1

        if not one_man_dict['alive']:
            dead_number += 1
            continue

        laborer_number += 1

        if one_man_dict['children_number'] <= 3:
            if one_man_dict['age'] > 30:
                create_one_man(0, 15000)
                laborer_number += 1
                one_man_dict['children_number'] += 1
        if one_man_dict['age'] > 70:
            dead_number += 1
            one_man_dict['alive'] = False

    

    info_dict = {}
    info_dict['year'] = year
    info_dict['all_man_number'] = len(all_man_list)
    info_dict['laborer_number'] = laborer_number
    info_dict['dead_number'] = dead_number
    #info_dict['all_man_info'] = all_man_string_list

    return render(request, 'world_emulator.html', info_dict) 
    


