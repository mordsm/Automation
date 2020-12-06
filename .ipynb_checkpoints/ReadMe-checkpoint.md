#Automation


#

##Voice Chat
- [web speech documentation](https://wicg.github.io/speech-api/)
- [wrking demo](https://www.labnol.org/software/add-speech-recognition-to-website/19989/)
    - create Sites model 
        - name
        - file_name
    - when calling name
        - aproperiate file will be opened
        - using accessible name the file will traverse the 
            file till the suitable accessible name is found
            [before starting the traverse the accessible name will be searched]
            
     
###Create Django Project - actions

cd /home/moshe/workspace/projects/
django-admin startproject Automation
cd Automation/
python manage.py startapp selenium_convertor
source venv/bin/activate
python3 -m venv env
source env/bin/activate
pip3 install django
pip3 install psycopg2
python manage.py makemigrations selenium_convertor
python manage.py migrate
python manage.py shell
sudo su - postgres
psql
CREATE DATABASE automation;