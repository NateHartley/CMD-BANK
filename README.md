![Usability](https://img.shields.io/badge/Free_to_use-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen) 

<img src="images/logo.png" alt="CMD-BANK" width="120px"/>

# CMD-BANK

CMD-BANK is a CLI app that lets you save and retreive your favourite commands directly from the terminal.<br>
No more jumping back and forth between your shell and scattered notes to find commands!

### Initialise venv on local machine
1. Clone repo `git clone https://github.com/NateHartley/CMD-BANK.git`
2. Enter /CMD-BANK dir `cd PATH/CMD-BANK`
3. Initialise venv `python3 -m venv venv`
4. Activate venv:
    1. (bash/zsh) `source venv/bin/activate`
    2. (cmd.exe) `venv\Scripts\activate.bat`
    3. (PS) `venv\Scripts\Activate.ps1`
5. `pip install -r requirements.txt`

### Run
`./main`

### Fixes 
If modules not recognised (venv not activated properly):<br>
`source PATH/CMD-BANK/venv/bin/activate`