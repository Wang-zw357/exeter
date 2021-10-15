import numpy as np
import numpy
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.core.numeric import tensordot
from scipy.linalg import norm, pinv
import csv

np.random.seed(30)

class RBF:
    """
    RBF
    """
    def __init__(self, input_dim, num_centers, out_dim):
        self.input_dim = input_dim
        self.num_centers = num_centers
        self.out_dim = out_dim
        self.beta = 8
        self.centers = [np.random.uniform(-1,1, input_dim) for i in range (num_centers)]
        self.W = np.random.random((self.num_centers,self.out_dim))

    def _basisfunc(self, c, d):
        return np.exp(-self.beta * norm(c - d) **2)
 
    def _calcAct(self, X):
        G = np.zeros((X.shape[0], self.num_centers), dtype=np.float)
        for ci, c in enumerate(self.centers):
            for xi, x in enumerate(X):
                G[xi, ci] = self._basisfunc(c,x)
        return G
        pass

    def train(self,X,Y):
        
        rnd_idx = np.random.permutation(X.shape[0])[:self.num_centers]
        self.centers = [X[i,:] for i in rnd_idx]

        G = self._calcAct(X)

        self.W = np.dot(pinv(G),Y)

        pass
    def predict(self,X):
        G = self._calcAct(X)
        Y = np.dot(G, self.W)
        return Y
        pass



ws = []
with open('D:/windata/test.csv', 'r') as f:
    reader = csv.reader(f)  
    for i in reader:
        i[0] = float(i[0])
        #i[0]=('%.2f' % i[0])
        #print(i[0])
        ws.append(i[0])

n = 1452
#x_train = np.linspace(0,1,n).reshape(n, 1)#time
x_train = np.array(ws[0:1451])
y_train = np.array(ws[1:1452])

rbf = RBF(1, 500, 1)
rbf.train(x_train,y_train)
z = rbf.predict(x_train)

plt.plot(x_train, y_train, 'k-', label=u'true_value')
plt.plot(x_train, z, 'r-', linewidth=2 ,label=u'predict')

plt.xlim(-0.1, 1.1)
plt.title(u'rbf', fontsize = 20, color = 'r')
plt.legend(loc='upper left')
plt.show()
