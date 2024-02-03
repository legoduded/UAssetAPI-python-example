# UAssetAPI in Python

Here is an example showing how to call the [UAssetAPI](https://github.com/atenfyr/UAssetApi) functions in python using [PythonNet](https://github.com/pythonnet/pythonnet)


## Compiling UAssetAPI.dll
Following Steps 1 and 2 from their build installation page: https://atenfyr.github.io/UAssetAPI/guide/build.html
\
\
In Visual Studio, add the following to the UAssetAPI Project to build with the dependencies copied to the output directory
```xml
<CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>
```
![CopyLocalLockFileAssemblies](/assets/CopyLocalLockFileAssemblies.png)
\
Continue to step 3 of the build instruction to build the DLL


## Importing into Python

```python
import sys
from pythonnet import load
load("coreclr")
import clr
sys.path.append("/path/to/dll")
clr.AddReference("UAssetAPI")
from UAssetAPI import UAsset
from UAssetAPI.UnrealTypes import EngineVersion
```
Now we can call UAsset from UAssetAPI

## Load and Modify an Asset
```python
myAsset = UAsset("myAsset.uasset", EngineVersion.VER_UE5_1)
json_asset = json.loads(myAsset.SerializeJson())

# Make modifications to JSON

myModifiedAsset = UAsset.DeserializeJson(json.dumps(json_asset))
myModifiedAsset.Write("myModifiedAsset.uasset")
```