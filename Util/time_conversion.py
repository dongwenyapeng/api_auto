import datetime
import time

class TimeConversion:
    def date_now(self):
        # 获取当前时间时间戳精确到分
        now_date = int(time.time())
        timeArray = time.localtime(now_date)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M", timeArray)
        print("当前时间", otherStyleTime)

        return otherStyleTime

# date_now_test_01 =TimeConversion().date_now()


    def date_now_one(self):
        # 获取当前时间后几天的时间戳
        # days=1  为当前时间后一天时间
        now_time = datetime.datetime.now()
        date_time = (now_time + datetime.timedelta(days=+1)).strftime("%Y-%m-%d %H:%M")
        print("T+1时间：", date_time)
        return date_time

# date_now_test_02 = TimeConversion().date_now_one()