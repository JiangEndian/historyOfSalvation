from django.http import HttpResponseRedirect 
from django.shortcuts import render
from django.utils.safestring import mark_safe #for tranfer html code
from tableDefine import * #导入自定义的东西
import re
def replaceOthers(Text):
    replaceInfo1 = re.compile('\[.*?\]')
    replaceInfo2 = re.compile('<.*?>')
    replaceInfo3 = re.compile('[ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ]')
    Text = replaceInfo1.sub('', Text)
    Text = replaceInfo2.sub('', Text)
    Text = replaceInfo3.sub('', Text)

    return Text.replace('\n', '\n\n').replace('\n\n\n', '\n\n').replace('\n\n\n', '\n\n').replace('  ', ' ')

##现在的任务是：
global my_dict_worshipAndBible
updateTimeInfo()

#用前打开生成数据库
def create_database_link():
    global common
    global every_week
    global every_month
    global every_year
    global conn, cursor
    conn, cursor = opendb('WorshipAndBible/PlanDatabase.sqlite')
    class Common(MyORM): #通用的计划放这里
        conn = conn
        cursor = cursor
        tableInfo = tableCommon
    class EveryWeek(MyORM): #通用的计划放这里
        conn = conn
        cursor = cursor
        tableInfo = tableEveryWeek
    class EveryMonth(MyORM): #通用的计划放这里
        conn = conn
        cursor = cursor
        tableInfo = tableEveryMonth
    class EveryYear(MyORM): #通用的计划放这里
        conn = conn
        cursor = cursor
        tableInfo = tableEveryYear
    
    common = Common()
    every_week = EveryWeek()
    every_month = EveryMonth()
    every_year = EveryYear()
def close_database_link():
    global conn, cursor
    closedb(conn,cursor)
    
def worshipAndBible(request):
    global common_info
    global every_year_info
    global every_month_info
    global every_week_info
    global my_dict_worshipAndBible
    global common
    global every_week
    global every_month
    global every_year
    
    #1、未复习且未有dump则查询好，并放到dict中dump
    #   此阶段生成四个info文件，准备用来查询及操作
    if os.path.exists('WorshipAndBible/4web_restudy/已复习') and not os.path.exists('WorshipAndBible/4web_restudy/common_info'):
        my_dict_worshipAndBible['showinfo'] = '本日已复习'
        my_dict_worshipAndBible['con'] = 't1'
        my_dict_worshipAndBible['env'] = 't2'
        my_dict_worshipAndBible['ext'] = 't3'
        #return HttpResponseRedirect('/alt1234') #复习完的直接回主页

        #复习完的再生成新的common
        day = datetime.now() + timedelta(days=0)
        ymd = day.strftime('%Y%m%d')
        
        create_database_link()
        
        every_year_info = {}
        every_month_info = {}
        every_week_info = {}
        dump2file('WorshipAndBible/4web_restudy/every_year_info', every_year_info)
        dump2file('WorshipAndBible/4web_restudy/every_month_info', every_month_info)
        dump2file('WorshipAndBible/4web_restudy/every_week_info', every_week_info)
        
        common_info = common.find('Ymd', ymd)
        dump2file('WorshipAndBible/4web_restudy/common_info', common_info)
        close_database_link()
        all_restudy = len(every_year_info)+len(every_month_info)+len(every_week_info)+len(common_info)
        my_dict_worshipAndBible['showinfo'] = '只是common的%s条复习，时间:%s' % (all_restudy, str(day))

        #return render(request, 'worshipAndBible.html', my_dict_worshipAndBible)
    elif os.path.exists('WorshipAndBible/4web_restudy/common_info'):
        every_year_info = loadffile('WorshipAndBible/4web_restudy/every_year_info')
        every_month_info = loadffile('WorshipAndBible/4web_restudy/every_month_info')
        every_week_info = loadffile('WorshipAndBible/4web_restudy/every_week_info')
        common_info = loadffile('WorshipAndBible/4web_restudy/common_info')

        all_restudy_list = [len(every_year_info), len(every_month_info), len(every_week_info), len(common_info)]
        all_restudy = all_restudy_list[0] +all_restudy_list[1] + all_restudy_list[2] + all_restudy_list[3]

        all_time = all_restudy*300
        all_time_m = int(all_time // 60)
        all_time_s = int(all_time % 60)
        if all_restudy_list[2] + all_restudy_list[1] + all_restudy_list[0]== 0:
            my_dict_worshipAndBible['showinfo'] = '待复习%s条(%s.%s)，将load继续' % (all_restudy, all_time_m, all_time_s)
        elif all_restudy_list[1] + all_restudy_list[0]== 0:
            my_dict_worshipAndBible['showinfo'] = '待复习%s(w:%s)条(%s.%s)，将load继续' % (all_restudy, all_restudy_list[2], all_time_m, all_time_s)
        elif all_restudy_list[0] == 0:
            my_dict_worshipAndBible['showinfo'] = '待复习%s(m:%s,w:%s)条(%s.%s)，将load继续' % (all_restudy, all_restudy_list[1], all_restudy_list[2], all_time_m, all_time_s)
        else:
            my_dict_worshipAndBible['showinfo'] = '待复习%s(y:%s,m:%s,w:%s)条(%s.%s)，将load继续' % (all_restudy, all_restudy_list[0], all_restudy_list[1], all_restudy_list[2], all_time_m, all_time_s)
    else:
        #day = datetime.now() + timedelta(days=0) + timedelta(hours=8) 
        #原来的复习没问题，这个得到的时间，就比我的时钟慢8个点了，奇怪，一样的过程。。。不懂，加上
        day = datetime.now() + timedelta(days=0)
        #后来查了下django时区问题，在setting里面改了时区为上海，然后，就没事了。。。（现在在韩国改为首尔了）
        week_day = day.strftime('%w')
        month_day = day.strftime('%d')
        ymd = day.strftime('%Y%m%d')
        
        #提前年的，所以，年的单独调出。把这两句复制到py3里，就可以准确演算了
        y_day = datetime.now() + timedelta(days=0)
        monthday = y_day.strftime('%m%d')
        #print('monthday='+monthday)

        create_database_link()

        every_year_info = every_year.find('MonthDay', monthday)
        dump2file('WorshipAndBible/4web_restudy/every_year_info', every_year_info)
        every_month_info = every_month.find('Day', month_day)
        dump2file('WorshipAndBible/4web_restudy/every_month_info', every_month_info)
        every_week_info = every_week.find('Day', week_day)
        dump2file('WorshipAndBible/4web_restudy/every_week_info', every_week_info)
        common_info = common.find('Ymd', ymd)
        dump2file('WorshipAndBible/4web_restudy/common_info', common_info)
        close_database_link()
        all_restudy = len(every_year_info)+len(every_month_info)+len(every_week_info)+len(common_info)
        my_dict_worshipAndBible['showinfo'] = '将开始dump新的%s条复习，时间:%s' % (all_restudy, str(day))
        
#2、每次调用，读取一次dict，并相应accept_cmd修改数据库和dict
    if every_year_info:
        temp_info = list(every_year_info)
        for e_info in temp_info:
            my_dict_worshipAndBible['con'] = e_info[2]
            my_dict_worshipAndBible['env'] = e_info[3]
            my_dict_worshipAndBible['ext'] = e_info[4]
            my_dict_worshipAndBible['every_info'] = 'year'
            #20200302更新：添加获取下一条的预读
            next_info_index = temp_info.index(e_info)+1
            if len(temp_info) > 1:
                next_info = temp_info[next_info_index]
                my_dict_worshipAndBible['next_con'] = next_info[3]
            #20200302更新：添加获取下一条的预读
            break
    elif every_month_info:
        temp_info = list(every_month_info)
        for e_info in temp_info:
            my_dict_worshipAndBible['con'] = e_info[2]
            my_dict_worshipAndBible['env'] = e_info[3]
            my_dict_worshipAndBible['ext'] = e_info[4]
            my_dict_worshipAndBible['every_info'] = 'month'
            #20200302更新：添加获取下一条的预读
            next_info_index = temp_info.index(e_info)+1
            if len(temp_info) > 1:
                next_info = temp_info[next_info_index]
                my_dict_worshipAndBible['next_con'] = next_info[3]
            #20200302更新：添加获取下一条的预读
            break
    elif every_week_info:
        temp_info = list(every_week_info)
        for e_info in temp_info:
            my_dict_worshipAndBible['con'] = e_info[2]
            my_dict_worshipAndBible['env'] = e_info[3]
            my_dict_worshipAndBible['ext'] = e_info[4]
            my_dict_worshipAndBible['every_info'] = 'week'
            #20200302更新：添加获取下一条的预读
            next_info_index = temp_info.index(e_info)+1
            if len(temp_info) > 1:
                next_info = temp_info[next_info_index]
                my_dict_worshipAndBible['next_con'] = next_info[3]
            #20200302更新：添加获取下一条的预读
            break
    elif common_info:
        temp_info = list(common_info)
        #temp_info1 = list(common_info)
        #temp_info = temp_info1[::-1] #review from last one
        for e_info in temp_info:
            my_dict_worshipAndBible['con'] = e_info[2]
            my_dict_worshipAndBible['env'] = e_info[3]
            my_dict_worshipAndBible['ext'] = e_info[4]
            my_dict_worshipAndBible['every_info'] = 'common'
            #20200302更新：添加获取下一条的预读
            next_info_index = temp_info.index(e_info)+1
            if len(temp_info) > 1:
                next_info = temp_info[next_info_index]
                my_dict_worshipAndBible['next_con'] = next_info[3]
            #20200302更新：添加获取下一条的预读
            break
#3、直到，查完事，结束并删除dump文件，生成已复习
    else:
        os.remove('WorshipAndBible/4web_restudy/every_year_info')
        os.remove('WorshipAndBible/4web_restudy/every_month_info')
        os.remove('WorshipAndBible/4web_restudy/every_week_info')
        os.remove('WorshipAndBible/4web_restudy/common_info')
        write2file('WorshipAndBible/4web_restudy/已复习', '复习完成')
        return HttpResponseRedirect('/alt1234')
    #测试直接把env置为video标签可行不
    my_dict_worshipAndBible['VideoEnv'] = '' #初始化，防止没有了还带着上次的内容
    if my_dict_worshipAndBible['env'] == 'NotAudioButVideo':
        #my_dict_worshipAndBible['VideoEnv'] = mark_safe('''<br/><video controls preload loop autoplay width="320" height="240" src="/static/grace_voice/TOEFL/%s" type="video/mp4"></video><br/>''' % my_dict_worshipAndBible['ext'])
        my_dict_worshipAndBible['VideoEnv'] = my_dict_worshipAndBible['ext']
    #context的'hello'对应模板html的变量{{ hello }}
    my_dict_worshipAndBible['con'] = replaceOthers(my_dict_worshipAndBible['con'])
    my_dict_worshipAndBible['env'] = replaceOthers(my_dict_worshipAndBible['env'])
    return render(request, 'worshipAndBible.html', my_dict_worshipAndBible)
    

def acceptCmdWorshipAndBible(request):
    global my_dict_worshipAndBible
    global common
    global every_week
    global every_month
    global every_year
    global common_info
    global every_year_info
    global every_month_info
    global every_week_info
    request.encoding='utf-8'
    every = request.GET['every']
    cmd = request.GET['cmd']
    print('every:%s, cmd:%s' % (every, cmd))
    #处理前打开数据库连接
    create_database_link()
    ############处理年的##############
    if every == 'year':
        if cmd == '8':
            every_year.delete('Other2',my_dict_worshipAndBible['ext'])
            every_month.add(Day=getnowtime('d'), Con=my_dict_worshipAndBible['con'], Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
            common.add(Ymd=getdaystime(1), Con=my_dict_worshipAndBible['con'], Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
            common.add(Ymd=getdaystime(3), Con=my_dict_worshipAndBible['con'], Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
            common.add(Ymd=getdaystime(5), Con=my_dict_worshipAndBible['con'], Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
        elif cmd == '2':
            every_year.delete('Other2',my_dict_worshipAndBible['ext'])
        every_year_info.pop(0)
        dump2file('WorshipAndBible/4web_restudy/every_year_info', every_year_info)
    ############处理月的##############
    elif every == 'month':
        if cmd == '8':
            every_month.delete('Other2', my_dict_worshipAndBible['ext'])
            every_week.add(Day=getnowtime('week'),Con=my_dict_worshipAndBible['con'], Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
            common.add(Ymd=getdaystime(1), Con=my_dict_worshipAndBible['con'], Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
            common.add(Ymd=getdaystime(3), Con=my_dict_worshipAndBible['con'], Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
            common.add(Ymd=getdaystime(5), Con=my_dict_worshipAndBible['con'], Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
        elif cmd == '2':
            every_month.delete('Other2', my_dict_worshipAndBible['ext'])
            every_year.add(MonthDay=getnowtime('md'),Con=my_dict_worshipAndBible['con'],  Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
        every_month_info.pop(0)
        dump2file('WorshipAndBible/4web_restudy/every_month_info', every_month_info)
    ############处理周的##############
    elif every == 'week':
        if cmd == '8':
            common.add(Ymd=getdaystime(1), Con=my_dict_worshipAndBible['con'], Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
            common.add(Ymd=getdaystime(3), Con=my_dict_worshipAndBible['con'], Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
            common.add(Ymd=getdaystime(5), Con=my_dict_worshipAndBible['con'], Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
        elif cmd == '2':
            every_week.delete('Other2', my_dict_worshipAndBible['ext'])
            every_month.add(Day=getnowtime('d'), Con=my_dict_worshipAndBible['con'], Other1=my_dict_worshipAndBible['env'], Other2=my_dict_worshipAndBible['ext'])
        every_week_info.pop(0)
        dump2file('WorshipAndBible/4web_restudy/every_week_info', every_week_info)
    ############处理Common的##############
    elif every == 'common':
        common_info.pop(0)
        #common_info.pop() #because review from last one, so remove last one
        dump2file('WorshipAndBible/4web_restudy/common_info', common_info)
    #处理完后，关闭数据库
    close_database_link()

    return HttpResponseRedirect('/worshipAndBible')

