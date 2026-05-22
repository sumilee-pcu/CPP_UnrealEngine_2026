# Pangaea UE 5.7.4 Practice

This is a UE 5.7.4 practice project scaffold adapted from the Chapter 12 source code in `Unreal-Engine-5-Game-Development-with-C-Scripting`.

## Version Target

- Unreal Engine: 5.7.4
- Visual Studio: 2022
- Project path: use ASCII-only paths, for example `F:\gameEngineering\Pangaea573`

## Notes

- The module name remains `Pangaea` so existing `PANGAEA_API` code does not need to be renamed.
- `Target.cs` uses UE 5.7.4-compatible build settings: `BuildSettingsVersion.V6`, `Unreal5_7` include order, and C++20.
- `Build.cs` includes `UMG`, `Slate`, and `SlateCore` because the final chapter uses `UUserWidget` and `UProgressBar`.
- `UPawnSensingComponent` is deprecated in UE 5.7.4. It can be kept for the class exercise, but AI Perception is the modern replacement.

## Next Steps After UE Update

1. Right-click `Pangaea.uproject` and generate Visual Studio project files.
2. Open the generated solution.
3. Build `PangaeaEditor` in `Development Editor | Win64`.
4. Open the project in Unreal Editor and create/import maps, Blueprint classes, widgets, meshes, and animations.
