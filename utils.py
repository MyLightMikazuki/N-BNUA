import json, time, os

class Task:
    def __init__(self):
        self.url = str()
        self.path = list()
        self.comment = str()
        self.type = None

    def to_dict(self):
        out = dict()
        out['url'] = self.url
        out['path'] = self.path
        out['type'] = self.type
        out['comment'] = None # Don't output the comment to file.
        return out

    def from_dict(self, data):
        self.url = data['url']
        self.path = data['path']
        self.type = data['type']
        self.comment = data['comment']

    def __eq__(self, other):
        return self.url == other.url and \
                   self.type == other.type and \
                   os.path.join(*self.path) == os.path.join(*other.path)

    def __str__(self):
        out = str()
        out += 'url: {}\n'.format(self.url)
        out += 'path: {}\n'.format(self.path)
        out += 'comment: {}\n'.format(self.comment)
        return out

def load_tasks(filename):
    tasks = list()
    with open(filename, 'r') as jsonfile:
        datas = json.load(jsonfile)

    for d in datas:
        task = Task()
        task.from_dict(d)
        tasks.append(task)
    return tasks

def save_tasks(filename, tasks):
    datas = list()
    for t in tasks:
        datas.append(t.to_dict())

    with open(filename, 'w') as f:
        json.dump(datas, f)

class Timer:
    def __init__(self):
        self._clock_time = None
        self.clock()

    def clock(self):
        self._clock_time = time.time()

    def elapsed(self):
        return time.time() - self._clock_time

    @staticmethod
    def currtime():
        lt = time.localtime(time.time())
        return "[{y}-{m}-{d} {h:02d}:{mi:02d}:{s:02d}]".format(
                   y=lt.tm_year, m=lt.tm_mon,  d=lt.tm_mday, h=lt.tm_hour, mi=lt.tm_min, s=lt.tm_sec)

def make_dir(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)

def make_recursive_dir(root, path_list):
    path = list()
    for d in path_list:
        path.append(d)
        make_dir(os.path.join(root, *path))

