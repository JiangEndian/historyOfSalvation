from django.conf.urls import url
from django.views.generic.base import RedirectView #重定向到给定的URL
#from django.contrib import admin

from . import alt3, alt3_common, alt2, alt2_common, alt4, alt4_common, alt1, alt1_common, index, all_rm, sleep_pc, download, for_text, grace_calculator, world_emulator, worshipAndBible, mother_common, churchSystem, videosDeal, dealGreekHebrew, hebrewCalendar

#pattern模范，典范，模型，模式
urlpatterns = [
    url(r'^favicon.ico',RedirectView.as_view(url=r'/static/favicon.ico')),
    url(r'^hebrewCalendar$', hebrewCalendar.hebrewCalendar),
    url(r'^hebrew', dealGreekHebrew.dealGreekHebrew),
    url(r'^greek', dealGreekHebrew.dealGreekHebrew),
    #以hebrew开头的，重定向到静态的hebrew文件夹下，这个应该不能用，但我现在没网，没法搜索
    #换了另一种思路：把hebrew和greek加入到静态文件夹列表中
    #（不行，这是链接的），去看源代码去。。。
    #尝试直接在源代码里加上点if。。。
    #不行，，算了，直接把这个链接转到一个方法里，方法里再转到另一处。。。
    url(r'^$', download.download),
    url(r'^alt$', download.download),
    url(r'^runThoseCmds$', download.runThoseCmds),
    url(r'^ftpGetFrom$', download.ftpGetFrom),
    url(r'^backBT_ALL$', download.backBT_ALL),
    url(r'^deleteFile$', download.deleteFile),
    url(r'^video_view$', download.video_view),
    url(r'^video_name$', download.video_name),
    url(r'^upload_file$', download.upload_file),
    url(r'^bibletimeDownload$', download.bibletimeDownload),
    url(r'^age2days$', download.age2days),

    #处理视频用
    url(r'^videos$', videosDeal.download),
    url(r'^deleteVideo$', videosDeal.deleteVideo),
    url(r'^upload_video$', videosDeal.upload_video),
    url(r'^reverseVideos$', videosDeal.reverseVideos),
    url(r'^deleteVideos$', videosDeal.deleteVideos),
    #url('admin/', admin.site.urls),
    #url(r'^$', view.hello) #任意url用此函数
    #url(r'^hello$', view.hello), #此url用此函数
    #url函数可接收4个参数，regex正则表达式,view执行与正则表达式匹配的 URL 请求,kwargs: 视图使用的字典类型的参数,name: 用来反向获取 URL
    url(r'^grace_calculator$', grace_calculator.grace_calculator),
    url(r'^grace_calculator_viewer$', grace_calculator.grace_calculator_viewer),
    url(r'^accept_grace$', grace_calculator.accept_grace),
    url(r'^world_emulator$', world_emulator.world_emulator),
    url(r'^reset_world_emulator$', world_emulator.reset_world_emulator),
    url(r'^family_calculator$', world_emulator.family_calculator),
    url(r'^family_calculator$', world_emulator.reset_family_calculator),
    #ChurchSystem
    url(r'^churchSystem$', churchSystem.grace_calculator),
    url(r'^churchSystem_viewer$', churchSystem.grace_calculator_viewer),
    url(r'^churchSystemAccept_grace$', churchSystem.accept_grace),

    url(r'^alt1$', alt1.alt1),
    url(r'^alt1-common$', alt1_common.alt1_common),
    url(r'^accept-cmd-alt1$', alt1.accept_cmd_alt1),
    url(r'^accept-cmd-alt1-common$', alt1_common.accept_cmd_alt1),

    url(r'^alt2$', alt2.alt2),
    url(r'^alt2-common$', alt2_common.alt2_common),
    url(r'^accept-cmd-alt2$', alt2.accept_cmd_alt2),
    url(r'^accept-cmd-alt2-common$', alt2_common.accept_cmd_alt2),

    url(r'^alt3$', alt3.alt3),
    url(r'^alt3-common$', alt3_common.alt3_common),
    #url(r'^mother_common$', mother_common.mother_common),
    #url(r'^accept_mother_common$', mother_common.accept_cmd_mother),
    url(r'^accept-cmd-alt3$', alt3.accept_cmd_alt3),
    url(r'^configurationsWeb$', alt3.configurationsWeb),
    url(r'^updateConfigurationsWeb$', alt3.updateConfigurationsWeb),
    url(r'^accept-cmd-alt3-common$', alt3_common.accept_cmd_alt3),
    url(r'^alt3_all_mp3$', alt3.alt3_all_mp3),

    url(r'^worshipAndBible$', worshipAndBible.worshipAndBible),
    url(r'^acceptCmdWorshipAndBible$', worshipAndBible.acceptCmdWorshipAndBible),

    url(r'^alt4$', alt4.alt4),
    url(r'^alt4-common$', alt4_common.alt4_common),
    url(r'^accept-cmd-alt4$', alt4.accept_cmd_alt4),
    url(r'^accept-cmd-alt4-common$', alt4_common.accept_cmd_alt4),

    url(r'^alt1234$', index.index),
    url(r'^submitToGithub$', index.submitToGithub),

    url(r'^alt1234rm1602080439868326077$', all_rm.all_rm),
    
    url(r'^life_code$', all_rm.life_code),
    url(r'^addTask$', all_rm.addTask),
    url(r'^delTask$', all_rm.delTask),

    #url(r'^sleep$', sleep_pc.sleep),

    url(r'^accept-text$', for_text.accept_text),
]
