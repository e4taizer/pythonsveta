######################задание №1
# from collections import Counter
# poetry="""Я вас любил: любовь еще, быть может,
# В душе моей угасла не совсем;
# Но пусть она вас больше не тревожит;
# Я не хочу печалить вас ничем.
# Я вас любил безмолвно, безнадежно,
# То робостью, то ревностью томим;
# Я вас любил так искренно, так нежно,
# Как дай вам Бог любимой быть другим."""
# word_counter = Counter(poetry.lower().split())
# word_counter1 = dict(word_counter)
#
# print(word_counter1)
#
# print(word_counter.most_common(3))
#######################################задание 2
# from collections import defaultdict
# a = [808, 824, 101, 242, 703, 145, 42, 874, 704, 986, 437, 56, 84, 471, 19, 327, 265, 1000, 385, 137, 367,
#  923, 461, 968, 632, 10, 710, 117, 803, 604, 783, 999, 909, 849, 850, 774, 905, 879, 80, 800, 439, 874,
#  580, 347, 229, 638, 571, 920, 12, 378, 265, 799, 464, 422, 147, 479, 935, 955, 458, 28, 183, 892, 608,
#  289, 594, 300, 757, 167, 919, 852, 900, 436, 704, 69, 82, 675, 778, 918, 476,976,732,557, 858, 593,
#  562, 236, 592, 252, 123, 813, 730, 84, 548, 759, 925, 263, 361, 883, 530, 698]
# count = defaultdict(int)
# for item in a:
#     count[item] +=1
# filtered_dict = {key: value for key, value in count.items() if key % 2}
# filtered_dict2 = {key: value for key,value in count.items() if not key % 2}
# total_matches_nechet = sum(filtered_dict.values())
# total_matches_chet = sum(filtered_dict2.values())
# spisok_chetnyx =list(filtered_dict2.keys())
# spisok_nechhetnyx= list(filtered_dict.keys())
# spisok_nechhetnyx_dict = {"kolichestvo_nechetnix":total_matches_nechet,"perechen_nechetnyx":spisok_nechhetnyx}
# spisok_chhetnyx_dict = {"Количетсво четных":total_matches_chet,"перечень четных":spisok_chetnyx}
#
# print(spisok_chhetnyx_dict)
# print(spisok_nechhetnyx_dict)
#### задание №2 чат жпт сделал проще)
# from collections import defaultdict
#
# # Исходный список
# a = [808, 824, 101, 242, 703, 145, 42, 874, 704, 986, 437, 56, 84, 471, 19, 327, 265, 1000, 385, 137, 367,
#      923, 461, 968, 632, 10, 710, 117, 803, 604, 783, 999, 909, 849, 850, 774, 905, 879, 80, 800, 439, 874,
#      580, 347, 229, 638, 571, 920, 12, 378, 265, 799, 464, 422, 147, 479, 935, 955, 458, 28, 183, 892, 608,
#      289, 594, 300, 757, 167, 919, 852, 900, 436, 704, 69, 82, 675, 778, 918, 476, 976, 732, 557, 858, 593,
#      562, 236, 592, 252, 123, 813, 730, 84, 548, 759, 925, 263, 361, 883, 530, 698]
#
# # Использование defaultdict
# result = defaultdict(lambda: {"count": 0, "numbers": []})
#
# for num in a:
#     category = "even" if num % 2 == 0 else "odd"
#     result[category]["count"] += 1
#     result[category]["numbers"].append(num)
#
# # Итоговый вывод
# print("Четные числа:", result["even"])
# print("Нечетные числа:", result["odd"])







