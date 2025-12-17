param(
    [Parameter(Position=0)] [string]$SourcePath = ".",
    [string]$OutRoot = "",
    [switch]$Recursive,
    [string]$Author = "",
    [string]$PythonExe = ""
)

Set-StrictMode -Version Latest

try { $sourceResolved = (Resolve-Path -Path $SourcePath).Path } catch { Write-Error "SourcePath not found: $SourcePath"; exit 1 }

if (-not $OutRoot) { $OutRoot = Join-Path $sourceResolved "translations" }

if (-not $PythonExe) {
    $py = Get-Command python -ErrorAction SilentlyContinue
    if (-not $py) { $py = Get-Command python3 -ErrorAction SilentlyContinue }
    if ($py) { $PythonExe = $py.Path }
}

if (-not $PythonExe) {
    $fallback = "C:\pro\Python\Python314\python.exe"
    if (Test-Path $fallback) { $PythonExe = $fallback } else { Write-Error "python executable not found; pass -PythonExe"; exit 1 }
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$translateScript = Join-Path $scriptDir "src\translate.py"
if (-not (Test-Path $translateScript)) { Write-Error "translate.py not found: $translateScript"; exit 1 }

if ($Recursive) { $mdFiles = Get-ChildItem -Path $sourceResolved -Filter *.md -File -Recurse } else { $mdFiles = Get-ChildItem -Path $sourceResolved -Filter *.md -File }
if (-not $mdFiles) { Write-Host "No .md files found in $sourceResolved"; exit 0 }

$total = 0; $succeeded = 0; $failed = 0

foreach ($f in $mdFiles) {
    $total++
    $fileFull = $f.FullName
    $rel = $fileFull.Substring($sourceResolved.Length).TrimStart('\')
    $relDir = [System.IO.Path]::GetDirectoryName($rel)
    if ($relDir) { $targetOutDir = Join-Path $OutRoot $relDir } else { $targetOutDir = $OutRoot }
    New-Item -ItemType Directory -Force -Path $targetOutDir | Out-Null

    Write-Host "[$total] Translating: $fileFull -> $targetOutDir"

    $args = @('-i', $fileFull, '-o', $targetOutDir, '-a', $Author)
    $procOutput = & $PythonExe $translateScript @args 2>&1
    $exit = $LASTEXITCODE
    if ($exit -eq 0) {
        $succeeded++
        $poName = [System.IO.Path]::ChangeExtension($f.Name, ".po")
        Write-Host "  Success: " (Join-Path $targetOutDir $poName)
    } else {
        $failed++
        Write-Warning "  Failed (exit $exit): $fileFull"
        if ($procOutput) { Write-Host $procOutput }
    }
}

Write-Host "`nSummary: Total=$total, Succeeded=$succeeded, Failed=$failed"
if ($failed -gt 0) { exit 2 } else { exit 0 }
