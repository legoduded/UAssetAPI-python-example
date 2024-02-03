from pythonnet import load
import sys
import os
load("coreclr")
import clr
sys.path.append(os.path.join(os.getcwd(), "netstandard2.0"))
clr.AddReference("UAssetAPI")
from UAssetAPI import UAsset
from UAssetAPI.UnrealTypes import EngineVersion

myAsset = UAsset("DT_BaseCampLevelData.uasset", EngineVersion.VER_UE5_1, useSeparateBulkDataFiles=True)
with open("DT_BaseCampLevelData.json", "w", encoding="utf-8") as f:
    f.write(myAsset.SerializeJson())
