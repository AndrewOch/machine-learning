import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow_datasets as tfds

ds, ds_info = tfds.load('emnist/byclass', with_info=True, as_supervised=True)
train_ds, test_ds = ds['train'], ds['test']

save_path_test = 'minus/test'
save_path_train = 'minus/train'
os.makedirs(save_path_test, exist_ok=True)
os.makedirs(save_path_train, exist_ok=True)

minus_label_code = 44


def save_images(dataset, save_path, label_code):
    count = 0
    for img, label in tfds.as_numpy(dataset):
        if label == label_code:
            img_rgb = np.repeat(img[..., np.newaxis], 3, -1)
            plt.imsave(os.path.join(save_path, f'minus_{count}.png'), img_rgb, cmap='gray')
            count += 1


save_images(train_ds, save_path_train, minus_label_code)
save_images(test_ds, save_path_test, minus_label_code)
