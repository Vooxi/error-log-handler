import os
import sys
import re
import tqdm

path = sys.argv[1]
word = sys.argv[2]
file_for_write = open('result.txt', 'w')


def checking(file, word, file_for_write):
    with tqdm.tqdm(total=os.path.getsize(file)) as progress_bar:
        with open(file, 'r') as file_for_read:
            for line in file_for_read:
                progress_bar.update(len(line) + 1)
                if re.search(word, line):
                    file_for_write.write(line)


if os.path.isfile(path):
    checking(path, word, file_for_write)

if os.path.isdir(path):
    for file in os.listdir(path):
        if file.endswith(".log"):
            checking(path + '\\' + file, word, file_for_write)

file_for_write.close()
