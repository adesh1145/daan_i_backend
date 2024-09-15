#                        --------------For Local Run-------
1. Install Python and venv
2. `python -m venv env`      create virtual Environment
3. `env\Scripts\activate`    Activate Env In Your System
4. `pip install -r requirements.txt`    install All Library
5. Go To  `daan_i_backend/daan_i_backend/settings.py`   and change database Setting For Local DataBase (Local Database Setting Already Writen and Commented)
6. `python manage.py makemigrations
   python manage.py migrate`        for Create Database Model /Table 

7. `python manage.py seed_states
   python manage.py seed_cities`    Seed Data In DataBase (Set All citiy and State)
8. (optional)   `python manage.py createsuperuser`  (Creating Super User For Admin)4
9. `python manage.py runserver`


