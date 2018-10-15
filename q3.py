"""
###################################################################################################
#   SETUP:                                                                                        #
#                                                                                                 #
#   1.capacity of cache: size of the list of objects                                              #
#   2.interval: how often (in seconds) will the program check for outdated objects to delete      #
#   3.timeout: after how many seconds will the object be erased from the cache                    #
##################################################################################################
"""
CAPACITY=4
INTERVAL=1
TIMEOUT=10

import datetime
from expiringdict import ExpiringDict
import threading
import time
#to create a cache item we only need a key and value, key will be converted to string
class cacheItem:
    def __init__(self, key, item):
        self.key=key 
        self.item=item 
        self.used=datetime.datetime.now().timestamp()
        self.born=datetime.datetime.now().timestamp()

    def toString(self):
        return("key: "+str(self.key)+ " | "+"value: "+str(self.item)+ " | "+"last used: "+str(int(datetime.datetime.now().timestamp()-self.used))+" seconds ago")
#a cache is just a list of cacheItem objects, and is one of the attributed of LRUcache object
class LRUCache:
    def __init__(self):
        self.capacity = CAPACITY
        #list of ovjects that will be organised by the date used last
        self.cache = []
        self.timeout=TIMEOUT
        self.keys=[]
        self.interval=INTERVAL
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution
    #checks whether some items are expired
    def check(self):
        todelete=[]
        now=datetime.datetime.now().timestamp()
        for i in range(len(self.cache)):
                        
            if int(now-self.cache[i].born)>=self.timeout:
                todelete.append(self.cache[i])

        for k in todelete:
            #print(k)
            self.cache.remove(k)
        self.cache=sorted(self.cache, key=lambda cacheItem: cacheItem.used)
    #runs in the background, always checking whether some items need to be deleted
    def run(self):
        """ Method that runs forever """
        print('checking for expired cache items...')

        while True:
            # Do something
            self.check()
            time.sleep(self.interval)




    #retrieve a value by its key
    def get(self, key):
        try:
            for item in self.cache:
                if item.key == str(key):
                    item.used=datetime.datetime.now().timestamp()
                    #resort the list according to datetime
                    self.cache=sorted(self.cache, key=lambda cacheItem: cacheItem.used)
                    return item
        except KeyError:
            return -1
    #add something to the cache list
    def set(self, one_item):
        if one_item.key not in self.keys:
            if len(self.cache)<self.capacity:

                self.cache.append(one_item)
                self.keys.append(one_item.key)
                self.cache=sorted(self.cache, key=lambda cacheItem: cacheItem.used)
                
            else:
                print('cache capacity reached')
        else:
            print('element already in cache.')

  