# Occluded-Market-Dataset

## Dataset Description

The **Occluded-Market** is proposed for occluded ReID task, which is derived from MARS and Market-1501. We notice that these two datasets own two advantages to constructing Occluded-Market. 1) MARS contains abundant samples of occluded persons with a variety of obstacles, including bicycles, other persons, balustrades, and et al. 2) MARS and Market-1501 are collected from the same scene and share the same identities of persons.

## Dataset Converting

We only provide the image name lists of our Occluded-Market dataset in './Occluded_Market'.  The source datasets should be downloaded and put in following directory structure:

```
Occluded_Market_Dataset
├── Occluded_Market
|	└──train_market.list
|	└──train_mars.list
|	└──test.list
|	└──query_market.list
|	└──query_mars.list
├── market1501
|	└──bounding_box_train ..
|	└──bounding_box_test ..
|	└──query ..
├── MARS
|	└──bbox_train ..
|	└──bbox_test ..
├── convert_to_occ_market.py
```

You can convert Market-1501 and MARS to Occluded-Market by running the following script：

```shell
python convert_to_occ_market.py
```

