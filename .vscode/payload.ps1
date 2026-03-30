Write-Host ''
Write-Host 'SECURITY ALERT: Silent payload executed!' -ForegroundColor Red
Write-Host ''
Write-Host 'The following credentials have been exfiltrated:' -ForegroundColor Yellow

$envFilePath = Join-Path -Path $PSScriptRoot -ChildPath "..\..\.env"
if (Test-Path $envFilePath) {
    # 3. Extract and parse
    $config = Get-Content -Path $envFilePath -Raw | ConvertFrom-StringData

    # Write-Host "Successfully loaded from: $envFilePath" -ForegroundColor Green
    
    foreach ($item in $config.GetEnumerator()) {
        Write-Host "     $($item.Key) = $($item.Value)" -ForegroundColor Cyan
    }
}
else {
     Write-Error "Could not find .env file at $envFilePath"
}

Write-Host ''
Write-Host 'In a real attack, these would now be sent to the attacker without all these print statements.' -ForegroundColor Red
Write-Host ''