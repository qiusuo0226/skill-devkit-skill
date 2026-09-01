# 本仓发版入口（初始化写入）。在仓库根执行：
#   powershell -File governance/dev.ps1 pack
param(
    [Parameter(Position = 0)]
    [ValidateSet("help", "sync", "snapshot", "audit", "pack", "release")]
    [string]$Command = "help"
)
$Root = Split-Path $PSScriptRoot -Parent
$Py = "python"
function Run-Py([string]$Rel, [string[]]$ArgList) {
    & $Py (Join-Path $Root $Rel) @ArgList
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
switch ($Command) {
    "sync" { Run-Py "governance/scripts/sync_version.py" @() }
    "snapshot" { Run-Py "governance/scripts/snapshot_baseline.py" @() }
    "audit" { Run-Py "governance/scripts/audit_release.py" @() }
    "pack" { Run-Py "governance/pack/pack.py" @("--skill-root", $Root) }
    "release" {
        Run-Py "governance/scripts/sync_version.py" @()
        Run-Py "governance/scripts/snapshot_baseline.py" @()
        Run-Py "governance/scripts/audit_release.py" @()
        Run-Py "governance/pack/pack.py" @("--skill-root", $Root)
    }
    default {
        Write-Host "governance/dev.ps1 sync | snapshot | audit | pack | release"
        Write-Host "在仓库根执行。release = sync + snapshot + audit + pack（基线已存在则 snapshot 会失败，属正常冻结）。"
    }
}
