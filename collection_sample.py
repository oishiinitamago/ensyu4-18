# scores = {'network':60, 'database':80,'security':50}
# scores['programming'] = 100
# scores['security'] = 77

# del scores['database']

# print(scores)
# print(scores['database'])


# scores = (77,100,40,94)
# print(scores)
# print(scores[0])
# print(len(scores))

# d = dict()
# l = list()
# t = tuple()
# s = set()

# d['network'] = 60
# d['security'] = 50
# l.append(100)
# l.append(54)
# print(d)
# print(l)
# print(t)
# print(s)

# scores[0] = 100
# # score_list = []

# scores ={70,80,55,80}
# scores.add(80)
# print(scores)
# print(len(scores))


# 重複している値は切り捨てられる
# Listは[]で囲む
# tupleは()で囲む
# ディクショナリ{}で囲む

# scores = {'network:60','database':80,'security:50'}
# print(list(scores))
# print(list(scores.values()))
# result = (
#     {'id': 1, 'name': 'takahashi', 'age': 30},
#     {'id': 2, 'name': 'hosokawa', 'age': 40},
#     {'id': 3, 'name': 'takada', 'age': 50},
# )

# print(result[1]['age'])
# 40と出力される

# 二次元リスト
# array = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(array[1][1])
# a_set = {1, 2, 3, 4, 5}
# b_set = {3, 4, 5, 6, 7}
# print(a_set | b_set) 和集合
# print(a_set & b_set) 積集合

# a_list = [1,2,3,4,5]
# b_list = [3,4,5,6,7]
# print(a_list + b_list)
# data = {'name':'yamada', 'age':21, 'score':100, 'class':'2-1'}

# print(f"{data['class']}の{data['name']}({data['age']})さんは{data['score']}点です。")
# scores = {'technology':85, 'strategy':71, 'management':93}

# scores2 = tuple(scores)

# print(scores2[1])
# scores = [10, 20, 30]
# scores2 = [40, 50, 60]

# total_scores = scores + scores2

# print(total_scores[4])
# print(sum(total_scores))
key_list = input().split()
value_list = input().split()
scores = dict(zip(key_list, value_list))  # 対象の変数scores
scores = {'takahashi':70,'hosokawa':81,'takada':76}
print(scores.value())