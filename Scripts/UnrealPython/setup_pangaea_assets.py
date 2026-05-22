import os
import unreal


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IMPORT_ROOT = os.path.join(PROJECT_DIR, "ImportAssets", "PangaeaAssets")


def log(message):
    unreal.log("[PangaeaSetup] " + message)


def ensure_dir(asset_path):
    if not unreal.EditorAssetLibrary.does_directory_exist(asset_path):
        unreal.EditorAssetLibrary.make_directory(asset_path)


def import_file(source_file, destination_path, replace=False):
    if not os.path.exists(source_file):
        unreal.log_warning("[PangaeaSetup] Missing source file: " + source_file)
        return []

    ensure_dir(destination_path)
    asset_name = os.path.splitext(os.path.basename(source_file))[0]
    asset_path = destination_path + "/" + asset_name
    if not replace and unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        log("Asset already exists: " + asset_path)
        return [asset_path]

    task = unreal.AssetImportTask()
    task.filename = source_file
    task.destination_path = destination_path
    task.automated = True
    task.save = True
    task.replace_existing = replace

    ext = os.path.splitext(source_file)[1].lower()
    if ext == ".fbx":
        options = unreal.FbxImportUI()
        options.import_mesh = True
        options.import_textures = False
        options.import_materials = False
        options.import_as_skeletal = False
        options.automated_import_should_detect_type = True
        task.options = options

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    return list(task.imported_object_paths)


def make_blueprint(asset_name, destination_path, parent_class, is_widget=False):
    if parent_class is None:
        unreal.log_warning("[PangaeaSetup] Parent class not found for " + asset_name)
        return None

    ensure_dir(destination_path)
    asset_path = destination_path + "/" + asset_name
    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        log("Blueprint already exists: " + asset_path)
        return asset_path

    asset_class = unreal.Blueprint
    if is_widget:
        factory = unreal.WidgetBlueprintFactory()
        factory.set_editor_property("parent_class", parent_class)
        asset_class = unreal.WidgetBlueprint
    else:
        factory = unreal.BlueprintFactory()
        factory.set_editor_property("parent_class", parent_class)

    asset = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name,
        destination_path,
        asset_class,
        factory,
    )
    if asset:
        unreal.EditorAssetLibrary.save_loaded_asset(asset)
        log("Created Blueprint: " + asset_path)
    return asset_path


def import_assets():
    imports = [
        ("LobbyBG.png", "/Game/Pangaea/UI"),
        ("DefenseTower/DefenseTower.FBX", "/Game/Pangaea/Meshes/DefenseTower"),
        ("DefenseTower/DefenseTower_c.TGA", "/Game/Pangaea/Textures/DefenseTower"),
        ("Enemy/Enemy.FBX", "/Game/Pangaea/Meshes/Enemy"),
        ("Enemy/T_Enemy_COL.tga", "/Game/Pangaea/Textures/Enemy"),
        ("Enemy/T_Enemy_NOR.TGA", "/Game/Pangaea/Textures/Enemy"),
        ("Hero/Hero.FBX", "/Game/Pangaea/Meshes/Hero"),
        ("Hero/Hero_Anim_Attack.FBX", "/Game/Pangaea/Animations/Hero"),
        ("Hero/Hero_Anim_Die.FBX", "/Game/Pangaea/Animations/Hero"),
        ("Hero/Hero_Anim_Hit.FBX", "/Game/Pangaea/Animations/Hero"),
        ("Hero/Hero_Anim_Idle.FBX", "/Game/Pangaea/Animations/Hero"),
        ("Hero/Hero_Anim_Run.FBX", "/Game/Pangaea/Animations/Hero"),
        ("Hero/Hero_Anim_Walk.FBX", "/Game/Pangaea/Animations/Hero"),
        ("Hero/T_CharA_COL.TGA", "/Game/Pangaea/Textures/Hero"),
        ("Hero/T_CharA_NOR.TGA", "/Game/Pangaea/Textures/Hero"),
        ("Weapons/Axe/Axe.FBX", "/Game/Pangaea/Meshes/Weapons/Axe"),
        ("Weapons/Axe/Axe_c.TGA", "/Game/Pangaea/Textures/Weapons/Axe"),
        ("Weapons/Hammer/Hammer.FBX", "/Game/Pangaea/Meshes/Weapons/Hammer"),
        ("Weapons/Hammer/hammer_c.TGA", "/Game/Pangaea/Textures/Weapons/Hammer"),
        ("Weapons/Sword/Sword.FBX", "/Game/Pangaea/Meshes/Weapons/Sword"),
        ("Weapons/Sword/Sword_c.TGA", "/Game/Pangaea/Textures/Weapons/Sword"),
    ]

    for relative_file, destination in imports:
        source = os.path.join(IMPORT_ROOT, *relative_file.split("/"))
        result = import_file(source, destination)
        if result:
            log("Imported " + relative_file + " -> " + ", ".join(result))


def create_blueprints():
    def pangaea_class(class_name):
        loaded = unreal.load_class(None, "/Script/Pangaea." + class_name)
        if loaded is None:
            unreal.log_warning("[PangaeaSetup] Could not load /Script/Pangaea." + class_name)
        return loaded

    classes = {
        "BP_PlayerAvatar": pangaea_class("PlayerAvatar"),
        "BP_Enemy": pangaea_class("Enemy"),
        "BP_DefenseTower": pangaea_class("DefenseTower"),
        "BP_Projectile": pangaea_class("Projectile"),
        "BP_Weapon": pangaea_class("Weapon"),
        "BP_PangaeaGameMode": pangaea_class("PangaeaGameMode"),
        "BP_PangaeaPlayerController": pangaea_class("PangaeaPlayerController"),
        "BP_PangaeaGameInstance": pangaea_class("PangaeaGameInstance"),
        "BP_HealthBarWidget": pangaea_class("HealthBarWidget"),
    }

    for name, parent in classes.items():
        if name == "BP_HealthBarWidget":
            make_blueprint(name, "/Game/Pangaea/UI", parent, is_widget=True)
        elif name.startswith("BP_Pangaea"):
            make_blueprint(name, "/Game/Pangaea/Blueprints/System", parent)
        else:
            make_blueprint(name, "/Game/Pangaea/Blueprints/Actors", parent)


def main():
    log("Starting setup")
    for path in [
        "/Game/Pangaea",
        "/Game/Pangaea/Blueprints",
        "/Game/Pangaea/Blueprints/Actors",
        "/Game/Pangaea/Blueprints/System",
        "/Game/Pangaea/Meshes",
        "/Game/Pangaea/Textures",
        "/Game/Pangaea/Animations",
        "/Game/Pangaea/UI",
        "/Game/Pangaea/Maps",
    ]:
        ensure_dir(path)

    import_assets()
    create_blueprints()
    unreal.EditorAssetLibrary.save_directory("/Game/Pangaea", only_if_is_dirty=False, recursive=True)
    log("Setup complete")
    if os.environ.get("PANGAEA_SETUP_QUIT") == "1":
        unreal.SystemLibrary.quit_editor()


if __name__ == "__main__":
    main()
