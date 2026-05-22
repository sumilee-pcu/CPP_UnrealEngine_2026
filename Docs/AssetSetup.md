# Asset Setup

The C++ module must be built before this setup can run. If the editor opens successfully, the module is built.

## Option A: Run Inside The Open Editor

1. Open `Output Log`.
2. Run:

```text
py "F:/gameEngineering/Pangaea573/Scripts/UnrealPython/setup_pangaea_assets.py"
```

## Option B: Run With The Editor Closed

Close Unreal Editor, then run:

```powershell
cd F:\gameEngineering\Pangaea573
.\Scripts\RunAssetSetup.ps1
```

The script creates `/Game/Pangaea` folders, imports the FBX/TGA assets from `ImportAssets/PangaeaAssets`, and creates starter Blueprint assets based on the project C++ classes.
