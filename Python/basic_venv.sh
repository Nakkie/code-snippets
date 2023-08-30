# create
$python -m venv \path\to\myenv

virtualenv --python=3.10 <venv> 

# activate
terminal
activate <venv>

bash/zsh
$ source <venv>/bin/activate

cmd.exe
C:\> <venv>\Scripts\activate.bat

PowerShell
PS C:\> <venv>\Scripts\Activate.ps1

# deactivate
deactivate

# On Windows you might have some issues running the activate script
PowerShell > Set-ExecutionPolicy Unrestricted 
PowerShell > Set-ExecutionPolicy Restricted # remember to run this when you done
