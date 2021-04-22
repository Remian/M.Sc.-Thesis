import os
from numpy import load
from numpy import save
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def load_feature():

    return load("pca_feature_music_100_7.npy")

def load_label():

    return load("7_label_vector_music.npy")


def train_test_split_func():

    feature_matrix_local = load_feature()
    label_vector_local = load_label()

    nn_feature_train, nn_feature_test, nn_label_train, nn_label_test = train_test_split(
        feature_matrix_local, label_vector_local, test_size=0.1
    )

    save("7_music_split_data/music_nn_feature_train_pca_100.npy", nn_feature_train)
    save("7_music_split_data/music_nn_feature_test_pca_100.npy", nn_feature_test)
    save("7_music_split_data/music_nn_label_train_pca_100.npy", nn_label_train)
    save("7_music_split_data/music_nn_label_test_pca_100.npy", nn_label_test)

    nn_label_test_list = nn_label_test.tolist()

    print(nn_label_test)
    print("0 : " + str(nn_label_test_list.count(0)))
    print("1 : " + str(nn_label_test_list.count(1)))
    print("2 : " + str(nn_label_test_list.count(2)))

train_test_split_func()


