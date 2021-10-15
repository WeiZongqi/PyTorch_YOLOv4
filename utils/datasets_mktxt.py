import os
import cv2 as cv

def mktxt(path_name):
    root_path = '/home/muyun99/data/wzq/dota2-split-1024/'
    with open(root_path + path_name + '/' + path_name + '.txt', 'w+') as save:
        list_images = os.listdir(root_path + path_name + '/images/')
        for name in list_images:
            save.write(root_path + path_name + '/images/' + name + '\n')



wordname_15 = ['plane', 'baseball-diamond', 'bridge', 'ground-track-field', 'small-vehicle', 'large-vehicle', 'ship', 'tennis-court',
               'basketball-court', 'storage-tank',  'soccer-ball-field', 'roundabout', 'harbor', 'swimming-pool', 'helicopter']


def coco2txt(path_name):
    root_path = '/home/muyun99/data/wzq/dota2-split-1024/'
    imgs_path = root_path + path_name + '/images/'
    label_path = root_path + path_name + '/labelTxt/'

    save_path = imgs_path.replace('/images/', '/labelTxt2/')
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    imgs = os.listdir(imgs_path)
    for img_path in imgs:
        img = cv.imread(imgs_path + img_path)
        w, h, _ = img.shape
        label_name = img.replace('.png', '.txt')
        ll = open(label_path + label_name).readlines()
        
mktxt('train1024')
# coco2txt('train1024')