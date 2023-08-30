# create
$python -m venv \path\to\myenv

virtualenv --python=3.10 <venv> 

# activate
terminal
activate <venv>

bash/zsh
$ source <venv>/bin/activate

cmd.exe
C:\> <venv>\Scripts\activate

PowerShell
PS C:\> <venv>\Scripts\Activate

# deactivate
deactivate

# On Windows you might have some issues running the activate script
PowerShell > Set-ExecutionPolicy Unrestricted 
PowerShell > Set-ExecutionPolicy Restricted # remember to run this when you done
