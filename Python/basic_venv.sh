# create using python
$python -m venv \path\to\myenv

# create using virtualenv
virtualenv --python=3.10 <venv> 

# activate on bash/zsh
$ source <venv>/bin/activate

# activate on terminal
activate <venv>

# activate in windows cmd
C:\> <venv>\Scripts\activate
.\<venv>\scripts\activate

# activate in windows PowerShell
PS C:\> <venv>\Scripts\Activate
.\<venv>\scripts\activate

# deactivate
deactivate

# On Windows you might have some issues running the activate script
PowerShell > Set-ExecutionPolicy Unrestricted 
PowerShell > Set-ExecutionPolicy Restricted # remember to run this when you done
