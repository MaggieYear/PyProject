#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import datetime
import schedule
import time


class SpiderSchedule:
    """爬虫定时器"""

    def job(self):
        print("Spider working...")

    def spiderStart(self):
        print("I'm working for job1")
        time.sleep(2)
        print("spiderStart:", datetime.datetime.now())

    def run(self):
        schedule.every(5).seconds.do(self.job)
        schedule.every(10).seconds.do(self.spiderStart)
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    spiderSchedule = SpiderSchedule()
    spiderSchedule.job()
    spiderSchedule.run()