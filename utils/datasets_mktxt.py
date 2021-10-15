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
        res = []
        for l in ll:
            l2 = l.split(' ')
            cls = l2[8]
            cls_num = wordname_15.index(cls)

            x1 = max([int(float(l2[0])), int(float(l2[2])), int(float(l2[4])), int(float(l2[6]))])
            x2 = min([int(float(l2[0])), int(float(l2[2])), int(float(l2[4])), int(float(l2[6]))])
            y1 = max([int(float(l2[1])), int(float(l2[3])), int(float(l2[5])), int(float(l2[7]))])
            y2 = min([int(float(l2[1])), int(float(l2[3])), int(float(l2[5])), int(float(l2[7]))])
            xx = (x1 + x2) // 2 + 1
            yy = (y1 + y2) // 2 + 1
            ww = x1 - x2
            hh = y1 - y2
            l3 = []
            l3.append(str(cls_num))
            l3.append(str(xx))
            l3.append(str(yy))
            l3.append(str(ww))
            l3.append(str(hh))
            line = ','.join(l3)
            res.append(line + '\n')
            # cv.line(img, (x1, y1), (x2, y1), point_color, thickness, lineType)
            # cv.line(img, (x2, y2), (x2, y1), point_color, thickness, lineType)
            # cv.line(img, (x2, y2), (x1, y2), point_color, thickness, lineType)
            # cv.line(img, (x1, y1), (x1, y2), point_color, thickness, lineType)
        f = open(save_path + label_name, 'w')
        f.writelines(res)
        f.close()
# mktxt('train1024')
coco2txt('train1024')