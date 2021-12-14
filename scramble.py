#scramble.py
from PIL import Image
import sys
import os
import random
from typing import Any
from logzero import logger
from chaoslib.types import Configuration, Secrets,Activity
from chaoslib.exceptions import ActivityFailed, InvalidActivity
import importlib
import inspect
import sys
import traceback

__all__=["steadystate","main","scramblePixels","unscramblePixels","seed","operation","getPixels"]

def openImage(configuration: Configuration=None,secrets: Secrets=None)->None:
    return Image.open(sys.argv[2])
    pass

def operation(configuration: Configuration=None,secrets: Secrets=None)->None:
    return sys.argv[1]
    pass

def seed(img,secrets: Secrets=None, configuration: Configuration=None)->None:
    random.seed(hash(img.size))
    pass

def getPixels(img,configuration: Configuration=None,secrets: Secrets=None)->None:
    w, h = img.size
    print("W",w)
    print("H",h)
    pxs = []
    for x in range(w):
        for y in range(h):
            pxs.append(img.getpixel((x, y)))
    return pxs
    pass

def scrambledIndex(pxs,configuration: Configuration=None, secrets: Secrets=None)->None:
    idx = list(range(len(pxs)))
    random.shuffle(idx)
    return idx
    pass

def scramblePixels(img,configuration: Configuration=None,secrets: Secrets=None)->None:
    seed(img)
    pxs = getPixels(img)
    idx = scrambledIndex(pxs)
    out = []
    for i in idx:
        out.append(pxs[i])
    return out
    pass


def steadystate(h: int,configuration: Configuration = None, secrets: Secrets=None)->Any:
    return h
    pass


def unScramblePixels(img,configuration: Configuration = None,secrets: Secrets=None)->Any:
    seed(img)
    pxs = getPixels(img)
    #print("Pixels",pxs)
    idx = scrambledIndex(pxs)
    #print("Idx",idx)
    out = list(range(len(pxs)))
    cur = 0
    for i in idx:
        out[i] = pxs[cur]
        cur += 1
    return out
    pass

def storePixels(name, size, pxs):
    outImg = Image.new("RGB", size)
    w, h = size
    print("Size",size)
    pxIter = iter(pxs)
    for x in range(w):
        for y in range(h):
            outImg.putpixel((x, y), next(pxIter))
    outImg.save(name)
    

def main(configuration: Configuration=None,secrets: Secrets=None)->None:
    img = openImage()
    if operation() == "scramble":
        pxs = scramblePixels(img)
        print("Pixels...",pxs)
        storePixels("scrambled.png", img.size, pxs)
    elif operation() == "unscramble":
        pxs = unScramblePixels(img)
        storePixels("unscrambled.png", img.size, pxs)
    else:
        sys.exit("Unsupported operation: " + operation())
    pass

if __name__ == "__main__":
    main()
