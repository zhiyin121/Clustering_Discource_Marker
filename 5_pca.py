import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import random

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
        lst_int.append(num)
    #print(lst_int)
    dataSet.append(lst_int)
#print(np.array(dataSet))


s = open('space_dan_normalize_speaker_classification.txt', 'r', encoding = 'utf-8')
genders = []
for line in s.readlines():
    lst = line.strip('\n').split('\t')
    #gender = lst[2]+'/'+lst[3]+'/'+lst[4]+'/'+lst[5]
#    list = ['41','60','61','37','47','66','6','52','11','70','65','88','62','44','83']
#    if lst[1] in list:
#        print('\t'.join(lst))
    gender = lst[1]
    genders.append(gender)


print(__doc__)
#a = [2,3,4,5,6]
#print(np.array(a))

# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

# import some data to play with
#iris = datasets.load_iris()
X = np.array(dataSet)  # we only take the first two features.
y = np.array(genders)
#X = iris.data[:, :2]  # we only take the first two features.
#y = iris.target
#print(X[:, 0], X[:, 1])

'''
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
            edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
'''

# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
fig = plt.figure(1, figsize=(16, 12))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(X)

ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c='w',
           cmap=plt.cm.Set1, edgecolor='#1f77b4', s=40)

name = genders
for i in range(len(X_reduced)):
    ax.text(X_reduced[:, 0][i],X_reduced[:, 1][i],X_reduced[:, 2][i],name[i])
    
#print(X_reduced)

ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

plt.show()


