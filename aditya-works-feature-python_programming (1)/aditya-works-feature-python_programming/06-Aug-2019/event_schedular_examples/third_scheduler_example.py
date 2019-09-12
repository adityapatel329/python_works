from crontab import CronTab
empty_cron = CronTab()
my_user_cron = CronTab(user = True)
user_cron = CronTab(user = 'aditya')
