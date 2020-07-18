f = open('space_dan_normalize.txt', 'r', encoding = 'utf-8')
g = open('combine_extract.txt', 'r', encoding = 'utf-8')
d = open('speaker.txt', 'r', encoding = 'utf-8')
w = open('space_dan_normalize_classification.txt', 'w+', encoding = 'utf-8')


id_turns = []
for line in f.readlines():
    lst = line.split('\t')
    id_turn = lst[0]
    id_turns.append(id_turn)
#print(id_turns)

id_name_turns = {}
for line in g.readlines():
    lst = line.split('\t')
    id_turn = lst[0]
    name_turn = lst[6] 
    id_name_turns[id_turn] = name_turn
#print(id_name_turns)

name_gender = {}
for line in d.readlines():
    lst = line.split('\t')
    name = lst[0]
    gender = lst[2]
    name_gender[name] = gender
print(name_gender)

co = ''
for i in range(len(id_turns)):
    if str(id_turns[i]) in id_name_turns.keys():
        if name_gender[id_name_turns[str(id_turns[i])]] == '男':
            gender_one_hot = 0
        else:
            gender_one_hot = 1
        co += id_turns[i] + '\t' + \
              id_name_turns[str(id_turns[i])] + '\t' + \
              name_gender[id_name_turns[str(id_turns[i])]] + '\t' +\
              str(gender_one_hot) + '\n'
w.write(co)

