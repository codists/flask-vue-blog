# @Date: 2021/5/24
# @Author: Hugh
# @Email: 609799548@qq.com

import json
import functools
import threading

utf8_open = functools.partial(open, encoding='utf8')


class Cache:
    __instance = None
    lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        with cls.lock:
            cls.__instance = super().__new__(cls)
            return cls.__instance

    def __init__(self):
        self.filename = 'cache.json'
        self.file_lock = threading.Lock()

        with utf8_open(self.filename, 'w') as f:
            json.dump({}, f)

    def set(self, key, value):
        with self.file_lock:
            with utf8_open(self.filename, 'r+') as f:
                data = json.load(f)
                data.update({key: value})
                f.seek(0)
                f.truncate(0)
                json.dump(data, f)

    def get(self, key):
        with self.file_lock:
            with utf8_open(self.filename) as f:
                return json.load(f).get(key)


cache = Cache()