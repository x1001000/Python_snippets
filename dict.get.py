# -*- coding: utf8 -*-
sentence = '見山是山，見水是水。見山不是山，見水不是水。見山仍是山，見水仍是水。'.decode('utf8')
def dictionary(sentence):
    result = dict()
    for word in sentence:
        result[word] = result.get(word, 0) + 1
    return result
print sentence.encode('utf8') + '\n　：總共 ' + str(len(sentence)) + ' 個字'
result = dictionary(sentence)
for word in result:
    print word.encode('utf8') + '：出現 ' + str(result[word]) + ' 次'
