import jieba
import jieba.posseg
jieba.load_userdict("./cantonese-corpus-master/data/dict.txt")
punc = ['(\'，\', \'x\')','(\'。\', \'x\')','(\'？\', \'x\')','(\'！\', \'x\')']
fliter = [260, 229, 133, 96, 203, 308, 73, 310, 130, 180, 88, 44, 123, 179, 64, 78, 80, 217, 126, 105, 224, 112, 101, 225, 160, 277, 99, 309, 77, 150, 293]


d = open('pattern_dan_dic_final.txt', 'r', encoding = 'utf-8')
dic = {}
n = 1
m = 1
for line in d.readlines():
    line = line.rstrip('\n').split('\t')
    tup = (line[0],line[1]),(line[2],line[3]),(line[4],line[5])
    #print(tup)
    if n in fliter:
        dic[tup] = m
        m += 1
    n += 1
print(len(dic))
d.close()


s = open('./train_val_test_set/train_set.txt', 'r', encoding = 'utf-8')
c = open('space_dan_counts.txt', 'w+', encoding = 'utf-8')
n = open('space_dan_normalize.txt', 'w+', encoding = 'utf-8')
row_count = ''
row_normalize = ''
for line in s.readlines():
    length = len(line)
    line_dic = {}
    lst = line.rstrip('\n').split('\t')
    words = jieba.posseg.cut(lst[8])
    word_list = []
    for word, pos in words:
        a = (word, pos)
        word_list.append(a)
    #print(word_list)
    for i in range(len(word_list)):
        if '噉' in word_list[i][0]:
            term = [word_list[i-1],word_list[i],word_list[i+1]]
            if str(term[0]) in punc:
                term[0] = ('punc', 'x')
            if str(term[2]) in punc and term[1][1] != 'r':
                term[0] = ('text', 'x')
                term[2] = ('punc', 'x')
            #print(tuple(term))
            if tuple(term) in dic:
                if dic[tuple(term)] not in line_dic:
                    line_dic[dic[tuple(term)]] = 1
                else:
                    line_dic[dic[tuple(term)]] += 1
    
    if line_dic:
        #print(line_dic)
        vector = 31 * [0]
        for k, y in line_dic.items():
            vector[k-1] = y
        vector = str(vector).strip('[]').replace(',', '\t')
        #print(vector)
        row_count += lst[0] + '\t' + vector + '\n'
        #print(lst[0])


    if line_dic:
        #print(line_dic)
        vector = 31 * [0]
        for k, y in line_dic.items():
            vector[k-1] = round(y/length * 1000, 4) #normalize with turns' length
        vector = str(vector).strip('[]').replace(',', '\t')
        #print(vector)
        row_normalize += lst[0] + '\t' + vector + '\n'
        #print(lst[0])


print(row_count)
print(row_normalize)
c.write(row_count)
n.write(row_normalize)
s.close()
c.close()
n.close()




                              
'''
dic ={55: 1, 260: 26, 229: 55, 133: 185, 96: 166, 203: 186, 52: 7, 308: 60, 14: 10, 114: 1, 73: 22, 310: 28, 76: 9, 119: 3, 130: 35, 250: 1, 85: 6, 180: 66, 88: 25, 44: 18, 40: 2, 219: 1, 123: 41, 179: 43, 64: 13, 78: 14, 31: 1, 80: 70, 45: 2, 305: 7, 75: 1, 181: 2, 217: 11, 7: 1, 126: 23, 178: 3, 39: 3, 166: 2, 231: 7, 105: 15, 108: 1, 224: 15, 112: 11, 279: 3, 187: 4, 280: 1, 186: 1, 265: 1, 247: 4, 236: 3, 233: 1, 65: 7, 216: 3, 212: 2, 101: 21, 257: 1, 141: 2, 25: 3, 204: 4, 225: 13, 124: 6, 160: 11, 131: 1, 118: 5, 209: 1, 107: 2, 251: 1, 62: 1, 291: 3, 70: 1, 173: 6, 48: 4, 92: 7, 168: 2, 266: 6, 29: 5, 61: 1, 148: 9, 198: 3, 163: 2, 145: 5, 277: 31, 192: 1, 99: 31, 54: 1, 300: 1, 159: 1, 283: 2, 27: 1, 309: 22, 243: 3, 165: 2, 297: 1, 183: 4, 77: 13, 276: 1, 213: 2, 84: 4, 79: 2, 41: 2, 303: 1, 171: 3, 150: 12, 20: 3, 8: 1, 264: 1, 57: 1, 21: 4, 98: 3, 193: 1, 153: 1, 125: 3, 208: 4, 227: 1, 51: 1, 33: 3, 43: 1, 169: 3, 185: 1, 223: 8, 10: 1, 36: 1, 170: 4, 239: 8, 82: 1, 66: 2, 1: 1, 271: 1, 195: 1, 67: 1, 26: 2, 184: 3, 267: 1, 158: 1, 281: 1, 240: 3, 2: 1, 202: 1, 288: 2, 182: 9, 102: 1, 293: 13, 278: 1, 13: 1, 147: 1, 46: 1, 176: 1, 154: 2, 290: 1, 270: 1, 274: 3, 71: 1, 30: 1, 49: 8, 23: 2, 304: 1, 140: 1, 161: 3, 301: 1, 122: 3, 127: 1, 47: 1, 34: 3, 248: 1, 9: 2, 254: 1, 174: 2, 252: 1, 262: 1, 91: 1, 116: 1, 220: 1, 194: 2, 90: 1, 235: 2, 132: 1, 188: 1, 115: 1, 230: 1, 60: 1, 201: 1, 200: 1, 87: 1, 139: 1, 15: 2, 35: 1, 215: 1, 189: 1, 295: 1, 32: 2, 242: 1, 136: 1, 152: 2, 237: 1, 16: 1, 258: 1, 167: 1, 261: 1, 50: 2, 256: 3, 106: 1, 111: 2, 245: 1, 299: 1, 214: 1, 22: 1, 5: 1, 155: 1, 74: 1, 109: 1, 142: 1, 129: 1, 285: 1, 199: 1, 117: 1, 206: 1, 56: 2, 97: 1, 28: 1, 12: 1, 4: 1, 83: 1, 135: 1, 172: 1, 94: 1, 81: 1, 121: 1, 100: 1, 269: 1, 253: 3, 259: 3, 104: 1, 275: 4, 298: 1, 196: 1, 69: 1, 249: 1, 11: 1, 255: 2, 289: 2, 134: 1, 284: 1, 175: 1, 221: 1, 120: 2, 228: 1, 146: 1, 238: 1, 17: 1, 6: 1, 18: 1, 226: 1, 205: 1, 302: 1, 287: 1, 191: 1, 72: 1, 19: 1, 218: 1, 38: 1, 24: 1, 68: 1, 307: 1, 89: 1, 137: 1, 282: 1, 138: 1}
'''
