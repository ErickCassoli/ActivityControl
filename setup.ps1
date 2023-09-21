# Defina o nome da virtual environment (venv)
$venvName = ".env"

# Verifique se a venv já existe
if (-not (Test-Path -Path $venvName -PathType Container)) {
    # Crie a venv
    python -m venv $venvName
    Write-Host "Virtual environment '$venvName' criada."
}

# Ative a venv
& $venvName\Scripts\Activate
Write-Host "Virtual environment '$venvName' ativada."

# Instale os requisitos do requirements.txt (certifique-se de que o arquivo requirements.txt esteja no mesmo diretório)
if (Test-Path -Path "requirements.txt") {
    pip install -r requirements.txt
    Write-Host "Requisitos instalados a partir de requirements.txt."
} else {
    Write-Host "O arquivo 'requirements.txt' não foi encontrado."
}
