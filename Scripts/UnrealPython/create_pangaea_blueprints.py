import os
import sys
import importlib


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

import setup_pangaea_assets
setup_pangaea_assets = importlib.reload(setup_pangaea_assets)


if __name__ == "__main__":
    setup_pangaea_assets.log("Creating Blueprint assets only")
    setup_pangaea_assets.create_blueprints()
    setup_pangaea_assets.unreal.EditorAssetLibrary.save_directory(
        "/Game/Pangaea/Blueprints",
        only_if_is_dirty=False,
        recursive=True,
    )
    setup_pangaea_assets.unreal.EditorAssetLibrary.save_directory(
        "/Game/Pangaea/UI",
        only_if_is_dirty=False,
        recursive=True,
    )
    setup_pangaea_assets.log("Blueprint setup complete")
