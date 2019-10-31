def find_common_words(first, second):
    first = first.split(',')
    second = second.split(',')
    common_words = dict((word, 1) for word in first)
    for word in second:
        try:
            common_words[word] += 1
        except: pass
    answer = sorted(word for word in common_words if common_words[word] > 1 )
    return ','.join(answer)


print(find_common_words("hello,world", "hello,earth") == "hello")
print(find_common_words("one,two,three", "four,five,six") == "")
print(find_common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two")
print(find_common_words("one,two,three", "four,five,one,two,six,three"))
