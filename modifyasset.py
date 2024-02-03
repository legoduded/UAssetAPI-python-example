from pythonnet import load
import json
import sys
import os
load("coreclr")
import clr
sys.path.append(os.path.join(os.getcwd(), "netstandard2.0"))
clr.AddReference("UAssetAPI")
from UAssetAPI import UAsset
from UAssetAPI.UnrealTypes import EngineVersion

myAsset = UAsset("DT_BaseCampLevelData.uasset", EngineVersion.VER_UE5_1, useSeparateBulkDataFiles=True)
json_asset = json.loads(myAsset.SerializeJson())

# Double all of the WorkerMaxNum
for data in json_asset["Exports"][0]["Table"]["Data"]:
    for value in data["Value"]:
        if value["Name"] == "WorkerMaxNum":
            value["Value"] = value["Value"] * 2

myModifiedAsset = UAsset.DeserializeJson(json.dumps(json_asset))
myModifiedAsset.Write("DT_BaseCampLevelData_Double.uasset")
