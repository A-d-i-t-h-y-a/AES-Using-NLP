@echo off

echo Initializing the Environment...
python -m venv ./.venv

echo Activating the Environment
call ./.venv/Scripts/activate

echo Installing Django==5.1.1
pip install django==5.1.1

echo Installing django-widget-tweaks==1.5.0
pip install django-widget-tweaks==1.5.0

echo Installing keras==3.5.0
pip install keras==3.5.0

echo Installing tensorflow==2.17.0
pip install tensorflow==2.17.0

echo Installing nltk==3.9.1
pip install nltk==3.9.1

echo Installing gensim==4.3.3
pip install gensim==4.3.3

echo Installing transformers==4.46.0
pip install transformers==4.46.0

echo Installing spacy==3.8.2
pip install spacy==3.8.2

echo Installing en_core_web_sm
python -m spacy download en_core_web_sm

echo Installing numpy==1.26.4
pip install numpy==1.26.4

echo All modules installed successfully!
pause
