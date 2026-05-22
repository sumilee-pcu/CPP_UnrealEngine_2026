param(
	[string]$UnrealRoot = "F:\gameEngineering\UE_5.7"
)

$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$ProjectFile = Join-Path $ProjectRoot "Pangaea.uproject"
$Ubt = Join-Path $UnrealRoot "Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.dll"
$DotNet = Join-Path $UnrealRoot "Engine\Binaries\ThirdParty\DotNet\8.0.412\win-x64\dotnet.exe"

if (-not (Test-Path -LiteralPath $ProjectFile)) {
	throw "Project file not found: $ProjectFile"
}

if (-not (Test-Path -LiteralPath $Ubt)) {
	throw "UnrealBuildTool not found. Check UnrealRoot: $UnrealRoot"
}

if (-not (Test-Path -LiteralPath $DotNet)) {
	$DotNet = "dotnet"
}

& $DotNet $Ubt -ProjectFiles -Project="$ProjectFile" -Game -Engine
