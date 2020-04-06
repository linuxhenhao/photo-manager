Photo manager
---

yet another photo manager, with simple but useful features.

* organize photos by date, with content based dedumplication
* find photos have visual similarities
* face based organization using state of art face recognition and identification
  deep learning models
* sqlite as metadata storage
* fsnotify based directory watching on linux (optional)

For now, none of the features above was provided, but content based dedumplication
will comming soon :).


## build

In debian/ubuntu:
```buildoutcfg
apt-get install libboost-python1.71-dev libexiv2-dev  # for py3exiv2
pip install -r requirements.txt
```


