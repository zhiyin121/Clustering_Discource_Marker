from numpy import *
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from numpy import genfromtxt
import numpy as np

def pca(dataMat, k):
    average = np.mean(dataMat, axis=0) #按列求均值
    m, n = np.shape(dataMat)
    meanRemoved = dataMat - np.tile(average, (m,1)) #减去均值
    normData = meanRemoved / np.std(dataMat) #标准差归一化
    covMat = np.cov(normData.T)  #求协方差矩阵
    print( covMat)
    eigValue, eigVec = np.linalg.eig(covMat) #求协方差矩阵的特征值和特征向量
    eigValInd = np.argsort(-eigValue) #返回特征值由大到小排序的下标
    selectVec = np.matrix(eigVec.T[:k]) #因为[:k]表示前k行，因此之前需要转置处理（选择前k个大的特征值）
    finalData = normData * selectVec.T #再转置回来
    return finalData


#dataSet:聚类数据集
#k:指定的k个类（大佬）
def kmeans(dataSet, k):
    #得到数据样本的维度n
    sampleNum, col = dataSet.shape
     #初始化为一个(k,n)的矩阵=簇
    cluster = mat(zeros((sampleNum, 2)))
    #生成全零阵
    centroids = zeros((k, col))
    #选择质心
    for i in range(k):
        #索引为随机生成的int类型的且在0-sampleNum间的数
        index = int(random.uniform(0, sampleNum))
        centroids[i, :] = dataSet[index, :]
    #设置flag，查看聚类结果是否发生变化
    clusterChanged = True
     #只要聚类结果一直发生变化，就一直执行聚类算法，直至所有数据点聚类结果不变化
    while clusterChanged:
        #聚类结果变化布尔类型置为false
        clusterChanged = False
         #遍历数据集每一个样本向量
        for i in range(sampleNum):
            #使用sqrt函数（二分法）
            minDist = sqrt(sum(power(centroids[0, :] - dataSet[i, :], 2)))
            minIndex = 0
            #计算点到质心的距离
            for j in range(1,k):
                distance = sqrt(sum(power(centroids[j, :] - dataSet[i, :], 2)))
                #当前最小距离一定时，索引为J
                if distance < minDist:
                    minDist  = distance
                    minIndex = j

            # 当前聚类结果中第i个样本的聚类结果发生变化：布尔类型置为true，继续聚类算法
            if cluster[i, 0] != minIndex:
                clusterChanged = True
                #更新聚类结果和平方误差
                cluster[i, :] = minIndex, minDist**2
        #遍历每一个质心
        for j in range(k):
            #筛选出属于当前质心类的所有样本
            pointsInCluster = dataSet[nonzero(cluster[:, 0].A == j)[0]]
            #计算列的均值（使用axis=0：求列的均值）
            centroids[j, :] = mean(pointsInCluster, axis = 0)

    return centroids, cluster

#创建简单数据集以及进行可视化

f = open('space_dan_normalize_speaker.txt', 'r', encoding = 'utf-8')
dataSet = []
for line in f.readlines():
    lst = line.strip('\n').split('\t')
    lst = lst[1:]
    lst_int = []
    for i in range(len(lst)):
        num = float(lst[i])
        if num == 0:
            num = random.randint(0,1)
        else:
            num += 1 

        '''
        if num <= 0.0025:
            num += 10
        elif 0.0025 < num <= 0.005:
            num += 20
        elif 0.005 < num <= 0.0075:
            num += 30
        elif 0.0075 < num <= 0.01:
            num += 40
        elif 0.01 < num <= 0.0125:
            num += 50
        elif 0.0125 < num <= 0.015:
            num += 60
        elif 0.015 < num <= 0.0175:
            num += 70
        elif num > 0.0175:
            num += 80
        '''
        lst_int.append(num)
    #print(lst_int)
    dataSet.append(lst_int)
#print(dataSet)

r = open('space_dan_normalize_speaker.csv', 'r', encoding = 'utf-8')
dataMat = genfromtxt(r, delimiter=',')
print(dataMat.shape)
print(np.isnan(dataMat).any())
dataMat = np.nan_to_num(dataMat)



s = open('space_dan_normalize_speaker_classification.txt', 'r', encoding = 'utf-8')
genders = []
for line in s.readlines():
    lst = line.strip('\n').split('\t')
    #gender = lst[2]+'/'+lst[3]+'/'+lst[4]+'/'+lst[5]
#    list = ['41','60','61','37','47','66','6','52','11','70','65','88','62','44','83']
    if lst[4] == 'F':
        gender = lst[4] + ' & ' + lst[14]
    else:
        gender = ' '
    genders.append(gender)


    
#print(dataMat)
k_value = [2,3]
for i in range(len(k_value)):
    finalData = pca(dataMat, k_value[i])
    print(finalData,shape)
    print(len(dataMat[:-1]))
    print(len(dataMat[1:]))
    #plt.scatter(dataMat.T[:-1],dataMat.T[1:], color='red',alpha=0.2, s=20)

    a = np.array(finalData.T[:-1])
    b = np.array(finalData.T[1:])
    plt.scatter(a,b, color='blue',alpha=0.1, s=30)
    plt.show()
    plt.close()

#dataSet = [[1.555,1,0,0,0,4],[0,6,0,4,0,0],[3,0,0,0,0,2],[8,0,0,1,1,0]]
#dataSet = [[1,1],[3,1],[1,4],[2,5],[11,12],[14,11],[13,12],[11,16],[17,12],[28,10],[26,15],[27,13],[28,11],[29,15]]

    dataSet = mat(finalData)
    k = 4
    centroids, cluster = kmeans(dataSet, k)
    sampleNum, col = dataSet.shape

    mark = ['ob', 'ok', 'oc', 'or', 'om', 'og']

    for i in range(sampleNum):
        markIndex = int(cluster[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex], alpha=0.6, markersize=6)

    name = genders
    for i in range(len(dataSet)):
        plt.text(dataSet[:, 0][i],dataSet[:, 1][i],name[i])

    mark = ['+b', '+k', '+c', '+r', '+m', '+g']
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=12)

    plt.show()

