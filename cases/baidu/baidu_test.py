# -*- coding: utf-8 -*-
# Author : Li Wei
# Date   : 2019/10/9 19:34

from locust import HttpLocust, TaskSet, task

# 用户行为
class UserBehavior(TaskSet):
    @task(1)
    def baidu_home(self):
        self.client.get("/")


# 性能测试设置
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "http://www.baidu.com"
    min_wait = 1000
    max_wait = 6000