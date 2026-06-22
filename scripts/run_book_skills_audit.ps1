param(
    [string]$Priority,
    [string]$Checks,
    [switch]$Json,
    [switch]$List,
    [string[]]$Files
)

$argsList = @()
if ($Priority) { $argsList += @("--priority", $Priority) }
if ($Checks) { $argsList += @("--checks", $Checks) }
if ($Json) { $argsList += "--json" }
if ($List) { $argsList += "--list" }
if ($Files) { $argsList += "--files"; $argsList += $Files }

& 'C:\Python314\python.exe' "$PSScriptRoot\run_book_skills_audit.py" @argsList
