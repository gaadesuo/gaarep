import numpy as np

# インデックス0を基準にソート
piyopiyo = [[8, 10], [7, 6], [7, 4]]
np_piyopiyo = np.array(piyopiyo)
sort_index = np.argsort(np_piyopiyo[:, 0])
# ソートしたインデックスが返される
print(sort_index)
sort_piyo = np_piyopiyo[sort_index]
print(sort_piyo)