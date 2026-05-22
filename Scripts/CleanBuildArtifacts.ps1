$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Targets = @("Binaries", "DerivedDataCache", "Intermediate", "Saved")

foreach ($Name in $Targets) {
	$Path = Join-Path $ProjectRoot $Name
	if (Test-Path -LiteralPath $Path) {
		$Resolved = (Resolve-Path -LiteralPath $Path).Path
		if (-not $Resolved.StartsWith($ProjectRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
			throw "Refusing to remove outside project root: $Resolved"
		}
		Remove-Item -LiteralPath $Resolved -Recurse -Force
	}
}

Write-Host "Cleaned build artifacts under $ProjectRoot"
