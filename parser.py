import argparse
from yt_process import YtProcess

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--saved-directory", metavar="<string>",
                        help="The json file name.", default='saved' ,type=str)
    parser.add_argument("-t", "--tasks_directory", metavar="<string>",
                        help="The json file name.", default='tasks' ,type=str)
    args = parser.parse_args()

    ytp = YtProcess(saved_directory=args.saved_directory, tasks_directory=args.tasks_directory)


