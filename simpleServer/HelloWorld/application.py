from django.http import HttpResponseRedirect 
from django.shortcuts import render
from table4grace import * #导入自定义的东西


#用前打开生成数据库
def create_database_link():
    global grace_database
    global conn, cursor
    conn, cursor = opendb('application.sqlite')
    class Grace_database(MyORM): 
        conn = conn
        cursor = cursor
        tableInfo = tableCommon
    grace_database = Grace_database()

def close_database_link():
    global conn, cursor
    closedb(conn,cursor)


def grace_calculator_data():
    global grace_database
    my_dict = {}

    create_database_link()
    grace_info = grace_database.find()

    if not grace_info:
        my_dict['name_time'] = '人：时间'
        my_dict['name_money'] = '人：金钱'
    #如果有数据，则提取整个数据库后，money/time从小到大的排序，组成两条文字
    #例：name1,money,usage,time,usage,other123 \n name2...
    else:
        #遍历数据库，把数据处理成两列可供展示
        all_info_list = []
        for one_info in grace_info:
            all_info_list.append(str(one_info))
        all_info_list_reversed = all_info_list[::-1]
        all_info_reversed = '\n'.join(all_info_list_reversed)
        my_dict['all_info_reversed'] = all_info_reversed
        #遍历数据库，把数据处理成两列可供展示

        name_list = []
        name_money = {}
        name_time = {}
        #遍历数据库，按名字合并为名字：金钱，名字：时间字典
        for one_info in grace_info:
            name = one_info[1]
            money = int(one_info[2])
            time = int(one_info[4])
            if name in name_list:
                name_money[name] += money
                name_time[name] += time
            else:
                name_list.append(name)
                name_money[name] = money
                name_time[name] = time
        #对合并后的两个字典都按大小排序（如果是给帮助者看，得小大排免得其天天看到骄傲）
        name_time_sorted = sorted(name_time.items(), key=lambda x:x[1])
        name_money_sorted = sorted(name_money.items(), key=lambda x:x[1])
        
        #然后排版上面生成的元组形成的列表，生成个字符串的列表
        #加上自有永有的唯一之主的恩典
        name_time_string_list = ['יהוה אלהינו\n赐予一生时间\n且有永生应许\n',]
        name_money_string_list = ['יהוה אחד\n赐予万物所有\n唯他自有永有\n',]
        for one_item in name_time_sorted:
            if int(one_item[1]) > 0:
                #name_time_string_list.append(one_item[0]+':'+str(one_item[1])+'min')
                name_time_string_list.append(one_item[0])
        for one_item in name_money_sorted:
            if int(one_item[1]) > 0:
                #name_money_string_list.append(one_item[0]+':'+str(one_item[1])+'rmb')
                name_money_string_list.append(one_item[0])
        
        #最后把生成的字符串列表联合成一个字符串
        my_dict['name_time'] = '\n'.join(name_time_string_list)
        my_dict['name_money'] = '\n'.join(name_money_string_list)
        my_dict['other3'] = str(getnowtime()) + '周' + str(getnowtime('week'))
        
    return my_dict

def grace_calculator_data_all():
    global grace_database
    my_dict = {}

    create_database_link()
    grace_info = grace_database.find()

    if not grace_info:
        my_dict['name_time'] = '人：时间'
        my_dict['name_money'] = '人：金钱'
    #如果有数据，则提取整个数据库后，money/time从小到大的排序，组成两条文字
    #例：name1,money,usage,time,usage,other123 \n name2...
    else:
        #遍历数据库，把数据处理成两列可供展示
        all_info_list = []
        for one_info in grace_info:
            all_info_list.append(str(one_info))
        all_info_list_reversed = all_info_list[::-1]
        all_info_reversed = '\n'.join(all_info_list_reversed)
        my_dict['all_info_reversed'] = all_info_reversed
        #遍历数据库，把数据处理成两列可供展示

        name_list = []
        name_money = {}
        name_time = {}
        #遍历数据库，按名字合并为名字：金钱，名字：时间字典
        for one_info in grace_info:
            name = one_info[1]
            money = int(one_info[2])
            time = int(one_info[4])
            if name in name_list:
                name_money[name] += money
                name_time[name] += time
            else:
                name_list.append(name)
                name_money[name] = money
                name_time[name] = time
        #对合并后的两个字典都按大小排序（如果是给帮助者看，得小大排免得其天天看到骄傲）
        name_time_sorted = sorted(name_time.items(), key=lambda x:x[1])
        name_money_sorted = sorted(name_money.items(), key=lambda x:x[1])
        
        #然后排版上面生成的元组形成的列表，生成个字符串的列表
        #加上自有永有的唯一之主的恩典
        name_time_string_list = ['יהוה אלהינו\n赐予一生时间\n且有永生应许\n',]
        name_money_string_list = ['יהוה אחד\n赐予万物所有\n唯他自有永有\n',]
        for one_item in name_time_sorted:
            if int(one_item[1]) > 0:
                name_time_string_list.append(one_item[0]+':'+str(one_item[1])+'min')
                #name_time_string_list.append(one_item[0])
        for one_item in name_money_sorted:
            if int(one_item[1]) > 0:
                name_money_string_list.append(one_item[0]+':'+str(one_item[1])+'rmb')
                #name_money_string_list.append(one_item[0])
        
        #最后把生成的字符串列表联合成一个字符串
        my_dict['name_time'] = '\n'.join(name_time_string_list)
        my_dict['name_money'] = '\n'.join(name_money_string_list)
        my_dict['other3'] = str(getnowtime()) + '周' + str(getnowtime('week'))
        
    return my_dict

def grace_calculator(request):
    my_dict = grace_calculator_data()
    #context的'hello'对应模板html的变量{{ hello }}
    return render(request, 'grace_calculator.html', my_dict)

def grace_calculator_viewer(request):
    my_dict = grace_calculator_data_all()
    return render(request, 'grace_calculator_viewer.html', my_dict)


def accept_grace(request):
    my_dict = {}
    global grace_database
    request.encoding='utf-8'
    
    #得到所有的表单信息
    my_dict['Chinese_name'] = request.GET['Chinese_name']
    my_dict['money'] = request.GET['money']
    my_dict['money_usage'] = request.GET['money_usage']
    my_dict['time'] = request.GET['time']
    my_dict['time_usage'] = request.GET['time_usage']
    my_dict['other1'] = request.GET['other1']
    my_dict['other2'] = request.GET['other2']
    my_dict['other3'] = request.GET['other3']

    create_database_link() #打开了database4grace.sqlite
    grace_database.add(Name=my_dict['Chinese_name'], Money=my_dict['money'], Money_usage=my_dict['money_usage'], Time=my_dict['time'], Time_usage=my_dict['time_usage'], Other1=my_dict['other1'], Other2=my_dict['other2'], Other3=my_dict['other3'])
    

    return HttpResponseRedirect('/grace_calculator')

