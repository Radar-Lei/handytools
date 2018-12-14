#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import os
import sys
import glob


def main():
    file_list = glob.glob(os.getcwd()+"/*.txt")
    for each_one in file_list:
        txt_file = open(each_one, encoding="utf-8")
        a = txt_file.read()
        a = a.replace('\n', '')
        out_file = open('1_'+os.path.basename(txt_file.name),
                        'w', encoding='utf-8')
        out_file.write(re.sub(r'(?<=[.])(?=[^\s])', r'\n', a))
        out_file.close()
        txt_file.close()


if __name__ == "__main__":
    main()
