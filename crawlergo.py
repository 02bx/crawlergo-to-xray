#!/usr/bin/python3
# coding: utf-8

import simplejson
import subprocess
import requests
import warnings
import time
import threading
import queue
warnings.filterwarnings(action='ignore')


exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("start sub_thread：" + self.name)
        process_data(self.threadID,self.name, self.q)
        print ("exit sub_thread：" + self.name)
        
def process_data(id,threadName, q):
    while not exitFlag:
        if q.empty() == False:
            req = q.get()
            print ("%s processing domain %s" % (threadName, req))
            
            target = req
            # TODO：自行修改配置参数
            headers = {
                "User-Agent": "",
                "Cookie": ""
            }   
            # TODO：自行修改配置参数
            cmd = ["./crawlergo", "-c", "/usr/bin/google-chrome","-t", "10","-f","smart","--fuzz-path", "--output-mode", "json","--ignore-url-keywords", "quit,exit,logout",  "--custom-headers", simplejson.dumps(headers),"--robots-path","--log-level","debug","--push-to-proxy","http://xray_username:xray_password@xray_ip:xray_port",target]
            rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = rsp.communicate()
            try:
                result = simplejson.loads(output.decode().split("--[Mission Complete]--")[1])
            except:
                return
        time.sleep(1)

# TODO：自行修改配置参数
workQueue = queue.Queue(10000)
threads = []
threadID = 1

# TODO：自行修改配置参数
file = open("targets.txt")
for text in file.readlines():
    domain = text.strip('\n')
    workQueue.put(domain)

# TODO：自行修改配置参数
for num in range(1,10):
    tName = "thread-" + str(num)
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()
print ("exit main thread")

