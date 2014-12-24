django-votes   （votes app）
django版本：1.7.1  python 版本：2.7.8，git版本：Git-1.9.4-preview20140929
============

背景：
接触openstack开发已有3月，接触git已有大半年，一直没用它来管理程序，从这个APP开始，决定用git管理加速代码开发。

============  华丽丽的分割线


This is my first django votes app!

作为学习django之用。
----------

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'polls',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^polls/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.

---------------------
Thanks for your coming!
-----------

参考django http://django.readthedocs.org/en/1.7.x/
----------------------

ccbsfei@126.com

