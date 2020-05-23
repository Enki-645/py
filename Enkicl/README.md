Enkicl Django rest framework<br>
====
DjangoRestFramework<br>
本项目是个人为学习用而做的一个磁力搜索网站<br>
使用python基于django rest framework框架搭建的restful API网站<br>



数据来源
--
通过爬虫在各种磁力网站爬取资源<br>

项目启动
--
进入Enkicl<br>
命令行:python manage.py runserver <br>

URL
--
Get磁力列表：127.0.0.1:8000/api/magnet/?title=\<title>&ordering=\<ordering>&page=\<page>/ <br>
Get磁力详情：127.0.0.1:8000/api/magnet/\<id>/ <br>
接口文档地址：127.0.0.1:8000/docs/
