import os
import shutil
import re


occ_market_dir = './Occluded_Market/'
origin_market_dir = './market1501/'
origin_mars_dir = './MARS/'


def generate_new_split_market(source_dir, target_dir, list_name):
    # read the re-splited name lists
    with open(os.path.join(occ_market_dir, list_name),'r') as f:
        imgs=f.readlines()

    source_split = os.path.join(origin_market_dir, source_dir)
    target_split = os.path.join(occ_market_dir, target_dir)
    if not os.path.exists(target_split):
        os.makedirs(target_split)

    for img in imgs:
        if(img.endswith('\n')):
            img = img[:-1]
        target_path = os.path.join(target_split, img)
        source_path = os.path.join(source_split, img)
        if os.path.isfile(source_path):
            shutil.copy(source_path, target_path)
        else:
            print("[{}]\tImage: {} does not exist.".format(img, source_path))
    print("Generate {} split from Market-1501 finished.".format(target_dir))


def generate_new_split_mars(source_train, source_test, target_dir, list_name):
    # read the re-splited name lists
    with open(os.path.join(occ_market_dir, list_name),'r') as f:
        imgs=f.readlines()

    source_train_dir = os.path.join(origin_mars_dir, source_train)
    source_train_ids = os.listdir(source_train_dir)
    source_test_dir = os.path.join(origin_mars_dir, source_test)
    source_test_ids = os.listdir(source_test_dir)
    target_split = os.path.join(occ_market_dir, target_dir)
    if not os.path.exists(target_split):
        os.makedirs(target_split)

    for img in imgs:
        if(img.endswith('\n')):
            img = img[:-1]
        if len(img.split('*')) >= 2:
            split = [s for s in re.split("[_cs]",img.split('*')[1]) if s!='']
            img = img.split('*')[0]
        else:
            split = [s for s in re.split("[_cs]",img) if s!='']
        img_src = split[0]+'C'+split[1]+'T'+split[2]+'F'+split[3]
        if split[0] in source_train_ids:
            source_path = os.path.join(source_train_dir, split[0], img_src)
        elif split[0] in source_test_ids:
            source_path = os.path.join(source_test_dir, split[0], img_src)
        else:
            print("[{}]\tID: {} does not exist.".format(img, split[0]))
            continue
        target_path = os.path.join(target_split, img)
        if os.path.isfile(source_path):
            shutil.copy(source_path, target_path)
        else:
            print("[{}]\tImage: {} does not exist.".format(img, source_path))
    print("Generate {} split from MARS finished.".format(target_dir))

def main():
    # generate the new dataset
    generate_new_split_market(source_dir="bounding_box_train", target_dir="occluded_train", list_name="train_market.list")
    generate_new_split_market(source_dir="bounding_box_test", target_dir="bounding_box_test", list_name="test.list")
    generate_new_split_market(source_dir="query", target_dir="occluded_query", list_name="query_market.list")
    generate_new_split_mars(source_train="bbox_train", source_test="bbox_test", target_dir="occluded_train", list_name="train_mars.list")
    generate_new_split_mars(source_train="bbox_train", source_test="bbox_test", target_dir="occluded_query", list_name="query_mars.list")


    print("\nSuccessfully generate the new Occluded-Market dataset.")
    print("The dataset folder is {}".format(occ_market_dir))


if __name__ == '__main__':
    main()

