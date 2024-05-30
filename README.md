# GYM MANAGEMENT SYSTEM
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Sumit%20Kumar-red)
---
## SCREENSHOTS
### Admin Dashboard
![dashboard snap](https://github.com/sumitkumar1503/gymmanagementsystem/blob/master/static/screenshots/admin_dashboard.png?raw=true)
### Member Dashboard
![dashboard snap](https://github.com/sumitkumar1503/gymmanagementsystem/blob/master/static/screenshots/member_dashboard.png?raw=true)

### Member List
![dashboard snap](https://github.com/sumitkumar1503/gymmanagementsystem/blob/master/static/screenshots/member_list.png?raw=true)
### Homepage
![dashboard snap](https://github.com/sumitkumar1503/gymmanagementsystem/blob/master/static/screenshots/homepage.png?raw=true)
---
## FUNCTIONS
## Member
- member will signup and login into system after account approval from admin.
- member can see beautiful dashboard showing their fee, trainers name, shift etc. 
- member can view all the trainer available in gym
- member can view all the packages (plan) available in gym
- member have permission view all the equiments that are available in gym
- member can see only their attendance, date wise.
- member do not have permission to see other member
- member do not have permission to add/delete/modify equipment/trainer/package
- member do not have permission to take attendance or view other member attendance.
- member can see their profile

---
## Trainer
- trainer will apply for job in gym and login into system after account approval from admin.
- trainer can see beautiful dashboard showing attendance of all member and other stats.
- trainer can view all the member registered in gym
- trainer can view their assigned member for training.
- trainer can view all the packages (plan) available in gym
- trainer have permission view all the equiments that are available in gym
- trainer can take and view attendance of any member registered in gym.
- trainer do not have permission to see other trainer
- trainer do not have permission to add/delete/modify equipment/member/package
- trainer can see their profile

---
### Admin
- First admin will login ( for username/password run following command in cmd )
```
py manage.py createsuperuser
```
- Give username, email, password and your admin account will be created.
- After login , admin can see total number of member, equipment, package, gym trainer on dashboard

- Admin can view/add/update/delete trainers.
- Admin can approve/reject trainers account (requested by trainers) based on their experience by giving salary and shift details.
- Admin can view/add/update/delete members.
- Admin can approve/reject members account (signup by trainers).
- Admin can take and view attendance of any registered member
- Admin can add/view/delete/update equipment , package.

---
### NOTE
- First Package and Trainer must be added by admin, then only member account can be created.
- if trainer/package is deleted by admin then all the associated member will be deleted automatically.


## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
python -m pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```

## Drawbacks/LoopHoles
- Attendance chart will show wrong data, if we mark attendance twice for same member for same day

## Disclaimer
This project is developed for demo purpose and it's not supposed to be used in real application.

## Feedback
Any suggestion and feedback is welcome. You can message me on facebook
- [Contact on Facebook](https://fb.com/sumit.luv)
- [Subscribe my Channel LazyCoder On Youtube](https://youtube.com/lazycoders)
