# ============================================
# Price Tracker - Ejecucion Automatizada
# Archivo: run_scheduler.ps1
# ============================================

$ErrorActionPreference = "Stop"
$ProjectPath = "C:\Users\info\price_tracker_case1"
$VenvPath = "$ProjectPath\.venv\Scripts\python.exe"
$MainScript = "$ProjectPath\main.py"
$LogPath = "$ProjectPath\logs\automation.log"
$DataPath = "$ProjectPath"
$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# Crear carpetas necesarias si no existen
if (!(Test-Path "$ProjectPath\logs")) { New-Item -ItemType Directory -Path "$ProjectPath\logs" -Force | Out-Null }
if (!(Test-Path "$ProjectPath\data\processed")) { New-Item -ItemType Directory -Path "$ProjectPath\data\processed" -Force | Out-Null }

function Write-Log {
    param([string]$Message, [string]$Level = "INFO")
    $LogEntry = "[$Timestamp] [$Level] $Message"
    Add-Content -Path $LogPath -Value $LogEntry -Encoding UTF8
    if ($Level -eq "ERROR") { Write-Host $LogEntry -ForegroundColor Red }
    else { Write-Host $LogEntry -ForegroundColor Gray }
}

Write-Log "=== INICIO EJECUCION ==="

# Verificar entorno virtual
if (!(Test-Path $VenvPath)) {
    Write-Log "ERROR: Entorno virtual no encontrado en $VenvPath" "ERROR"
    exit 1
}
Write-Log "Entorno virtual localizado"

# Ejecutar scraper principal
try {
    Write-Log "Iniciando main.py..."
    & $VenvPath $MainScript
    Write-Log "main.py ejecutado sin errores criticos"
}
catch {
    Write-Log "ERROR al ejecutar main.py: $_" "ERROR"
    exit 1
}

# Validacion: CSV generado hoy (ajustado a tu nombre real de archivo)
$TodayCSV = Get-ChildItem -Path $DataPath -Filter "precios_competidores.csv" |
Where-Object { $_.LastWriteTime.Date -eq (Get-Date).Date }

if ($TodayCSV) {
    $FileSize = [math]::Round($TodayCSV.Length / 1KB, 2)
    Write-Log "CSV generado: $($TodayCSV.Name) ($FileSize KB)"
}
else {
    Write-Log "ADVERTENCIA: No se detecto CSV nuevo hoy" "WARN"
}

# Validacion: Registros en DB (opcional, usa Python interno)
try {
    $DBPath = "$ProjectPath\tracker.db"
    if (Test-Path $DBPath) {
        $Query = "SELECT COUNT(*) FROM prices WHERE date(date_added) = date('now');"
        $Result = & $VenvPath -c "import sqlite3; conn=sqlite3.connect('$DBPath'); print(conn.execute('$Query').fetchone()[0]); conn.close()" 2>$null
        if ($Result) { Write-Log "Registros anadidos hoy: $Result" }
    }
}
catch {
    Write-Log "No se pudo consultar la DB (opcional, no critico)" "WARN"
}

# Limpieza logs antiguos (7 dias)
$LogFiles = Get-ChildItem -Path "$ProjectPath\logs" -Filter "*.log" |
Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-7) }
foreach ($File in $LogFiles) {
    Remove-Item $File.FullName -Force
    Write-Log "Log antiguo eliminado: $($File.Name)"
}

Write-Log "=== FIN EJECUCION ==="
Write-Host ""
exit 0