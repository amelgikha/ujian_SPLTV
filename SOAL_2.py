import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d 
import matplotlib.tri as mtri

p = np.array([[1,-2,1],[3,1,-2],[7,-6,-1]])
h = np.array([6,4,10])
hasil = np.linalg.solve(p,h)

x = round(hasil[0],1)
y = round(hasil[1],1)
z = round(hasil[2],1)
print('nilai x =', x)
print('nilai y =', y)
print('nilai z =', z)

#persamaan 1 : x -2y + z = 6
x = 6 #jika y dan z 0
y = -3 #jika x dan z 0
z = 6 #jika x dan y 0

x1 = [x,0,0]
y1 = [0,y,0]
z1 = [0,0,z]

triang = mtri.Triangulation(x1, y1)
fig = plt.figure('Ini 3D Plot',figsize = (9,4))
ax = fig.add_subplot(1,3,1, projection='3d')
ax.plot_trisurf(triang, z1, color = 'red',alpha=0.5)
ax.scatter(x1,y1,z1, marker='.', s=15, color = 'blue')
ax.set_xlabel('Nilai X')
ax.set_ylabel('Nilai Y')
ax.set_zlabel('Nilai Z')
plt.title('x -2y + z = 6')


# ##persamaan 2 : 3x + y - 2z = 4
x = 0.75 #jika y dan z 0
y = 4 #jika x dan z 0
z = -2 #jika x dan y 0

x2 = [x,0,0]
y2 = [0,y,0]
z2 = [0,0,z]

triang = mtri.Triangulation(x2, y2)
ax = fig.add_subplot(1,3,2, projection='3d')
ax.plot_trisurf(triang, z2,color = 'yellow',alpha = 0.5)
ax.scatter(x2,y2,z2, marker='.', s=15, color = 'red')
ax.set_xlabel('Nilai X')
ax.set_ylabel('Nilai Y')
ax.set_zlabel('Nilai Z')
plt.title('3x + y - 2z = 4')

# ##persamaan 3: 7x - 6y - z = 10
x = 10/7 #jika y dan z 0
y = -10/6 #jika x dan z 0
z = -10 #jika x dan y 0

x3 = [x,0,0]
y3 = [0,y,0]
z3 = [0,0,z]

triang = mtri.Triangulation(x3, y3)
ax = fig.add_subplot(1,3,3, projection='3d')
ax.plot_trisurf(triang, z3,color='blue',alpha=0.5)
ax.scatter(x3,y3,z3, marker='.', s=5, color = 'green')
ax.set_xlabel('Nilai X')
ax.set_ylabel('Nilai Y')
ax.set_zlabel('Nilai Z')
plt.title('7x - 6y - z = 10')
plt.show()