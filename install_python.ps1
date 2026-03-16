Write-Host "Installing Python..."

winget install -e --id Python.Python.3.12

Write-Host "Updating pip..."
python -m pip install --upgrade pip

Write-Host "Installing libraries..."

$packages = @(
    "cryptography"
)

foreach ($pkg in $packages) {
    python -m pip install $pkg
}

Write-Host "Setup complete!"

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\install_python.ps1