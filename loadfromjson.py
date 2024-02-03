from pythonnet import load
import sys
import os
load("coreclr")
import clr
sys.path.append(os.path.join(os.getcwd(), "netstandard2.0"))
clr.AddReference("UAssetAPI")
from UAssetAPI import UAsset

with open("DT_BaseCampLevelData.json", "r", encoding="utf-8") as f:
    myAsset = UAsset.DeserializeJson(f.read())

myAsset.Write("DT_BaseCampLevelData.uasset")
