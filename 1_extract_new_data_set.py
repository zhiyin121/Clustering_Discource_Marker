'''
#1
#deleted turns which words counts under 100
#add id for each turns

f = open('macau.txt', 'r', encoding = 'utf-8')
w = open('macau_extract.txt', 'w+', encoding = 'utf-8')
new = ''
n = 0
for line in f.readlines():
    lst = line.replace('\n', '').split('\t')
    if len(lst[7]) > 100:
        n += 1
        new = str(n) + '\t' + line
        w.write(new)


f = open('hongkong.txt', 'r', encoding = 'utf-8')
w = open('hongkong_extract.txt', 'w+', encoding = 'utf-8')
new = ''
n = 0
for line in f.readlines():
    lst = line.replace('\n', '').split('\t')
    if len(lst[7]) > 100:
        n += 1
        new = str(n) + '\t' + line
        w.write(new)
        

f_macau = open('macau.txt', 'r', encoding = 'utf-8')
f_hongkong = open('hongkong.txt', 'r', encoding = 'utf-8')
w = open('combine_extract.txt', 'w+', encoding = 'utf-8')
new = ''
n = 0
for line in f_macau.readlines():
    lst = line.replace('\n', '').split('\t')
    if len(lst[7]) > 100:
        n += 1
        new = str(n) + '\t' + line
        w.write(new)

for line in f_hongkong.readlines():
    lst = line.replace('\n', '').split('\t')
    if len(lst[7]) > 100:
        n += 1
        new = str(n) + '\t' + line
        w.write(new)
w.close()
'''

#2
#generate a 3-gram dictionary which '噉' in the middle
import jieba
import jieba.posseg
jieba.load_userdict("./cantonese-corpus-master/data/dict.txt")

key_term = []
punc = ['(\'，\', \'x\')','(\'。\', \'x\')','(\'？\', \'x\')','(\'！\', \'x\')']

f = open('combine_extract.txt', 'r', encoding = 'utf-8')
w = open('pattern_of_dan.txt', 'w+', encoding = 'utf-8')
for line in f.readlines():
    lst = line.replace('\n', '').split('\t')
    text = '噉'
    if text in lst[8]: #select turns that 'dan' appears
        words = jieba.posseg.cut(lst[8]) #tokenize turn's content
        word_list = []
        for word, pos in words:
            a = (word, pos)
            word_list.append(a) #A list consist of tuple(word, pos) 
        #print(word_list)
        for i in range(len(word_list)):
            if text in word_list[i][0]:
                term = [word_list[i-1],word_list[i],word_list[i+1]] #3-gram with 'dan' in the middle
                if str(term[0]) in punc:
                    term[0] = ('punc', 'x')
                    if str(term[2]) in punc and term[1][1] == 'r':
                        pass
                    else:
                        if str(term[2]) in punc and term[1][1] != 'r':
                            term[0] = ('text', 'x')
                            term[2] = ('punc', 'x')
                            if term not in key_term:
                                key_term.append(term)
                        else:
                            if term not in key_term:
                                key_term.append(term)                            
                else:
                    if str(term[2]) in punc and term[1][1] == 'r':
                        pass
                    else:
                        if str(term[2]) in punc and term[1][1] != 'r':
                            term[0] = ('text', 'x')
                            term[2] = ('punc', 'x')
                        #print(term)
                            if term not in key_term:
                                key_term.append(term)
                        else:
                            if term not in key_term:
                                key_term.append(term)                       

print('The dictionary of 3-gram is set up.')
for i in range(len(key_term)):
    pattern = str(key_term[i]) +'\n'
    w.write(pattern)
f.close()
w.close()


#3
# fliter out some meaningful '噉' of 3-gram dictionary
f = open('pattern_of_dan.txt', 'r', encoding = 'utf-8')
r = open('pattern_of_dan_fliter.txt', 'w+', encoding = 'utf-8')
new_dic = ''
for line in f.readlines():
    line = line[2:-3]
    line = line.split('), (')
    #print(line)
    if '噉樣' not in line[1]:
        if '係噉' not in line[1]:
            if '嘅' not in line[2]:
                if 'r' not in line[2]:
                    if len(line[1]) < 10:
                        #print(len(line[1]))
                        #print(line[1])
                        line = ','.join(line).strip('\'')
                        line = line.replace('\', \'', '\t')
                        line = line.replace('\',\'', '\t')
                        #print(line)
                        new_dic += line + '\n'
                        
print(new_dic)
r.write(new_dic)
f.close()
r.close()



