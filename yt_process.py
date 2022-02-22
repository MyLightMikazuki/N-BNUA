from pytube import YouTube
from utils import *

import glob, os

class YtProcess:
    def __init__(self, *args, **kwargs):
        self.saved_dir = kwargs.get('saved_directory', 'saved')
        self.tasks_dir = kwargs.get('tasks_directory', 'tasks')
        self._run()

    def _run(self):
        self._gather_tasks()
        self._download()

    def _gather_tasks(self):
        self.tasks = list()
        print(self.tasks_dir)
        for f in glob.glob(os.path.join(self.tasks_dir, '*.json')):
            loaded_tasks = load_tasks(f)
            for t in loaded_tasks:
                # Remove the repeat tasks.
                if t not in self.tasks:
                    self.tasks.append(t)
                    print(t)

    def _download(self):
        timer = Timer()

        # Build the root directory.
        make_dir(self.saved_dir)

        cnt = 0
        for t in self.tasks:
            # Try to get the video stream.
            try:
                yt = YouTube(t.url)
            except VideoUnavailable:
               print('Video {u} is unavaialable, skipping.'.format(u=t.url))

            # Select video or audio stream
            stream = None
            stype = None
            if t.audio_only:
                stream = yt.streams.get_audio_only()
                stype = 'audio'
            else:
                stream = yt.streams.get_highest_resolution()
                stype = 'video'

            make_recursive_dir(self.saved_dir, t.path)

            # Now download it.
            print('Downloading {t}: {u}'.format(t=stype, u=t.url))
            stream.download(output_path=os.path.join(self.saved_dir, *t.path))
            cnt += 1

        print('Speed {:.4f}(task/sec)'.format(cnt/timer.elapsed()))
