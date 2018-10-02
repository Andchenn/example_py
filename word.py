import re
import collections

path = 'test.txt'
with open(path, 'r', encoding='utf-8')as f:
    word_list = []
    word_reg = re.compile(r'\w+')
    for line in f:
        line_words = line.split()
        word_list.extend(line_words)
    # 避免重复查询（方法一）
    # word_set = set(word_list)
    # words_dict = {word: word_list.count(word) for word in word_set}

    # 使用Counter统计（方法二）
    words_dict = dict(collections.Counter(word_list))
    for k, v in words_dict.items():
        print(k, v)
