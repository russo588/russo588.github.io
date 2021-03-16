import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons
from sklearn.svm import SVC



clf= SVC(gamma=1, C=1) #gamma is adjustable, it can overfit if too high #using gaussians

X, y = make_moons(noise=0.1, random_state=0) #generate some fake data

X = StandardScaler().fit_transform(X) #removing the mean and scaling to unit variance

clf.fit(X,y)


figure = plt.figure()

cm_redblue = ListedColormap(['#FF0000', '#0000FF'])

plt.title("RBF SVM")


plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cm_redblue, edgecolors='k')


# create grid to evaluate model
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()


xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
XX, YY = np.meshgrid(xx, yy)

xy = np.vstack([XX.ravel(), YY.ravel()]).T


Z = clf.decision_function(xy).reshape(XX.shape)


# plot decision boundary and margins
boundary=ax.contour(XX, YY, Z, colors='k', levels=0)
ax.clabel(boundary, inline=1, fontsize=10)
# plot support vectors
ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')


plt.show()