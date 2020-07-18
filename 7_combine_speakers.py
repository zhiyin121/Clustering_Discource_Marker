
p = open('space_dan_normalize_classification.txt', 'r', encoding = 'utf-8')

dic = {}

for line in p.readlines():
    lst = line.strip('\n').split('\t')
    if lst[1] in dic:
        dic[lst[1]].append(lst[0])
    else:
        dic[lst[1]] = lst[0].split()

#print(dic)
a = list(dic.keys())
b = list(dic.values())
dic_sum = {}
for i in range(len(a)):
    vector = []
    f = open('space_dan_normalize.txt', 'r', encoding = 'utf-8')
    for line in f.readlines():  
        lst = line.strip('\n').split('\t')
        id_turn = lst[0]
        if id_turn in b[i]:
            vector.append(lst[1:])
            #print(vector)
    dic_sum[a[i]] = vector  
#print(dic_sum)

dic_re = {}
for key in dic_sum:
    if key not in dic_re:
        
        sum_vector = []
        for j in range(len(dic_sum[key][0])):
            num = 0
            for i in range(len(dic_sum[key])):
                #print(dic_sum[key][i][j])
                num += float(dic_sum[key][i][j])
                #print(num)
            sum_vector.append(round(num/len(dic_sum[key]), 4))
        dic_re[key] = sum_vector
#print(dic_re)


w = open('space_dan_normalize_speaker.txt', 'w+', encoding = 'utf-8')
text = ''
for key in dic_re:
    vec = ''
    for i in range(len(dic_re[key])):
        vec += '\t' + str(dic_re[key][i]) 
    text += key + vec + '\n'
w.write(text)
            
