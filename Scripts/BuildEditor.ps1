param(
	[string]$UnrealRoot = "F:\gameEngineering\UE_5.7",
	[switch]$SingleThread
)

$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$ProjectFile = Join-Path $ProjectRoot "Pangaea.uproject"
$BuildBat = Join-Path $UnrealRoot "Engine\Build\BatchFiles\Build.bat"

if (-not (Test-Path -LiteralPath $ProjectFile)) {
	throw "Project file not found: $ProjectFile"
}

if (-not (Test-Path -LiteralPath $BuildBat)) {
	throw "Build.bat not found. Check UnrealRoot: $UnrealRoot"
}

$Args = @(
	"PangaeaEditor",
	"Win64",
	"Development",
	"-Project=$ProjectFile",
	"-WaitMutex",
	"-FromMsBuild"
)

if ($SingleThread) {
	$Args += "-NoXGE"
	$Args += "-MaxParallelActions=1"
}

& $BuildBat @Args
