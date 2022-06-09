#条件判断，支持嵌套
{% if condition %}
     ... display
{% endif %}

{% if condition1 %}
   ... display 1
{% elif condition2 %}
   ... display 2
{% else %}
   ... display 3
{% endif %}

#for循环
#给定一个运动员列表 athlete_list 变量，我们可以使用下面的代码来显示这个列表
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
</ul>
#反向循环
{% for athlete in athlete_list reversed %}
...
{% endfor %}
#嵌套for循环
{% for athlete in athlete_list %}
    <h1>{{ athlete.name }}</h1>
    <ul>
    {% for sport in athlete.sports_played %}
        <li>{{ sport }}</li>
    {% endfor %}
    </ul>
{% endfor %}

#{% ifequal %} 标签比较两个值，当他们相等时，显示在 {% ifequal %} 和 {% endifequal %} 之中所有的值
{% ifequal user currentuser %}
    <h1>Welcome!</h1>
{% endifequal %}

{% ifequal section 'sitenews' %}
    <h1>Site News</h1>
{% else %}
    <h1>No News Here</h1>
{% endifequal %}

#Django 注释使用 {# #}

#模板过滤器可以在变量被显示前修改它，过滤器使用管道字符
{{ name|lower }}
{{ my_list|first|upper }}

#include 标签
{% include "nav.html" %}

#模板可以用继承的方式来实现复用。
#所有的 {% block %} 标签告诉模板引擎，子模板可以重载这些部分

