import numpy as np
from numpy import load
from numpy import save

def get_feature():

    return load("hybrid_aug_pca_feature_music_100.npy")

def get_label():

    return load("hybrid_aug_label_music.npy")

def split_test_train():

    feature = get_feature()
    label = get_label()

    print(feature.shape)
    print(label.shape)

    f_train = feature[0:1260]
    f_test = feature[1260:1305]

    l_train = label[0:1260]
    l_test = label[1260:1350]

    save("split_data/f_train_hybrid_pca_100.npy", f_train)
    save("split_data/f_test_hybrid_pca_100.npy", f_test)

    save("split_data/l_train_hybrid_pca_100.npy", l_train)
    save("split_data/l_test_hybrid_pca_100.npy", l_test)



split_test_train()
