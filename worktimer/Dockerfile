FROM python:3.7-slim

ADD worktimer.py requirements.txt /src/

RUN pip install -r /src/requirements.txt

ENV ORC_PORT=33000

CMD [ "python", "/src/worktimer.py" ]