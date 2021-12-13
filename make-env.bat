python -m virtualenv venv

start /MAX cmd /k "title CMD && cls && cd venv/Scripts && activate && cd .. & cd .. && echo #################### && echo Installing Dependencies && echo #################### && pip install -r requirements.txt"

