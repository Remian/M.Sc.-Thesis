import pandas as pd
import numpy as np
from numpy import load
from sklearn.decomposition import PCA
from numpy import save
from sklearn.preprocessing import minmax_scale


feature_local = load("7_feature_matrix_music.npy")
feature_shape = list(feature_local.shape)
feature_local_reshaped = feature_local.reshape(feature_shape[0], feature_shape[1]*feature_shape[2])

pca_music = PCA(n_components=100)
pca_matrix = pca_music.fit_transform(feature_local_reshaped)

print(pca_matrix[0,0])
print(pca_matrix[0])

print(pca_matrix.shape)




save("pca_feature_music_100_7.npy", pca_matrix)