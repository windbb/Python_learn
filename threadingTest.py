import threading
import time

# 子執行緒的工作函數
def job():
  for i in range(5):
    if i==0:
        print("Child thread:", i)
        time.sleep(1)
    if i==1:
        print("Child thread 11111:", i)
        time.sleep(10)
    if i==2:
        print("Child thread22222:", i)
        time.sleep(15)
    if i==3:
        print("Child threa333333:", i)
        time.sleep(20)

# 建立一個子執行緒
t = threading.Thread(target = job)

# 執行該子執行緒
t.start()

# 主執行緒繼續執行自己的工作'

for i in range(3):
  print("Main thread:", i)
  time.sleep(1)

# 等待 t 這個子執行緒結束
t.join()


print("Done.")



