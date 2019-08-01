import time, os, sys

sys.path.append("..")
from letter_count import process, formatter
from collections import Counter
from string import ascii_uppercase as ascii_u


def main():
    file_handler = open("data.txt", "r")
    data = file_handler.readlines()
    # data = ['yolo','here there']
    file_handler.close()
    result = {}
    start = time.time()
    for sent in data:
        if sent.strip() != "":
            res = process(sent)
            result = dict(Counter(res) + Counter(result))
    for a in ascii_u:
        if a not in result.keys():
            result[a] = 0
    print(result)
    print(f"Time taken is {time.time() - start:.2f} seconds")
    print(f"Total letters are {sum(list(result.values()))}")
    result = formatter(result)
    for kv in result:
        k, v = kv
        print(f"{k} is {v:.2f} %")


if __name__ == "__main__":
    main()
