import numpy as np

G = np.array([[1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
              [0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
              [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
              [0, 0, 0, 0, 0, 1, 0, 1, 0, 1]])

H = np.array([[1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
              [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
              [1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
              [0, 1, 1, 0, 0, 1, 0, 1, 0, 0]])

H_t = H.transpose()
res = np.matmul(G, H_t) % 2
print(res)
m = np.array([1, 1, 0, 1, 0, 0])
print(np.matmul(m, G) % 2)
