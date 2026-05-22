param(
	[string]$UnrealRoot = "F:\gameEngineering\UE_5.7"
)

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$ProjectFile = Join-Path $ProjectRoot "Pangaea.uproject"
$ScriptFile = Join-Path $ProjectRoot "Scripts\UnrealPython\setup_pangaea_assets.py"
$Editor = Join-Path $UnrealRoot "Engine\Binaries\Win64\UnrealEditor.exe"

if (-not (Test-Path -LiteralPath $ProjectFile)) {
	throw "Project file not found: $ProjectFile"
}

if (-not (Test-Path -LiteralPath $ScriptFile)) {
	throw "Python setup script not found: $ScriptFile"
}

if (-not (Test-Path -LiteralPath $Editor)) {
	throw "UnrealEditor.exe not found. Check UnrealRoot: $UnrealRoot"
}

$RunningEditor = Get-Process UnrealEditor -ErrorAction SilentlyContinue | Where-Object {
	$_.Path -like "$UnrealRoot*"
}

if ($RunningEditor) {
	Write-Host "Unreal Editor is currently running. Close the Pangaea editor window before running this script."
	exit 2
}

$env:PANGAEA_SETUP_QUIT = "1"
try {
	& $Editor $ProjectFile -ExecutePythonScript="$ScriptFile" -nop4 -nosplash
}
finally {
	Remove-Item Env:\PANGAEA_SETUP_QUIT -ErrorAction SilentlyContinue
}
