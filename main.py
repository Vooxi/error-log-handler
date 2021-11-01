import os
import sys
import re
import tqdm

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
    result_file = open('result.txt', 'w')

    if os.path.isfile(path):
        checkFileAndWrite(path, word, result_file)

    if os.path.isdir(path):
        for file in os.listdir(path):
            if file.endswith(".log"):
                checkFileAndWrite(path + '\\' + file, word, result_file)

    result_file.close()


if __name__ == '__main__':
    main()
