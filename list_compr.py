# 1.
consist_seven = [i for i in range(7, 998) if '7' in str(i)]
print(consist_seven)

# 2.
sentence = 'Would it save you a lot of time if I just gave up and went mad now?'
vowels = 'AaEeIiOoUu'
sentence_without_vowels = ''.join([i for i in sentence if i not in vowels])
print(sentence_without_vowels)

# 3.
sentence_2 = "The ships hung in the sky in much the same way that bricks don't"
dict_words = {word: len(word) for word in sentence_2.split(' ')}
print(dict_words)


# 4*. Для чисел от 1 до 1000 наибольшая цифра, на которую они делятся (1-9).
answ = [max(dev for dev in range(9, 0, -1) if i % dev == 0) for i in range(1, 1001)]
print(answ)

# 5*. Список всех чисел от 1 до 1000, не имеющих делителей среди чисел от 2 до 9.
answ_2 = [i for i in range(1, 1001) if 0 == len([dev for dev in range(2, 10) if i % dev == 0])]
print(answ_2)
