import os
import sys
import re
import tqdm

FILE_RESULT_PATH = 'result.txt'

def checkFileAndWrite(rfile_path, line_mask, wfile):
    with tqdm.tqdm(total=os.path.getsize(rfile_path)) as progress_bar:
        with open(rfile_path, 'r') as rfile:
            for line in rfile:
                progress_bar.update(len(line) + 1)
                if re.search(line_mask, line):
                    wfile.write(line)


def main():
    path = sys.argv[1]
    word = sys.argv[2]

    with open(FILE_RESULT_PATH, 'w') as result_file:
        if os.path.isfile(path):
            checkFileAndWrite(path, word, result_file)

        if os.path.isdir(path):
            for file in os.listdir(path):
                if file.endswith(".log"):
                    checkFileAndWrite(path + '\\' + file, word, result_file)


if __name__ == '__main__':
    main()
