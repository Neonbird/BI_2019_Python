def find_common_words(first, second):
    first = first.split(',')
    second = second.split(',')
    common_words = sorted([word for word in first if first.count(word) > 0 and second.count(word) > 0])
    return ','.join(common_words)

print(find_common_words("hello,world", "hello,earth") == "hello")
print(find_common_words("one,two,three", "four,five,six") == "")
print(find_common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two")
print(find_common_words("one,two,three", "four,five,one,two,six,three"))

