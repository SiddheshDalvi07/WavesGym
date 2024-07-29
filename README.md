# Waves Gym

## Introduction

Welcome to Waves Gym! This platform provides a comprehensive solution to manage members, trainers, and administrative tasks within a gym setting. The system offers distinct features for members, trainers, and admins, ensuring smooth and efficient gym operations.

## Features

### Member Features:
- **Account Management:** Members can sign up and log in after receiving account approval from the admin.
- **Dashboard:** A user-friendly dashboard displaying fee details, trainer name, and shift information.
- **Trainer and Package Information:** Members can view all available trainers and gym packages (plans).
- **Attendance Tracking:** Members can view their own attendance records, sorted by date.

### Trainer Features:
- **Account Management:** Trainers can apply for a job and log in after receiving account approval from the admin.
- **Dashboard:** A dashboard displaying the attendance of all members and other relevant statistics.
- **Member Information:** Trainers can view all registered members and their assigned members for training.
- **Attendance Management:** Trainers can take and view the attendance of any registered member.

### Admin Features:
- **Trainer Management:** Admins can view, add, update, and delete trainers. They can also approve or reject trainer applications by providing salary and shift details.
- **Member Management:** Admins can view, add, update, and delete members. They can approve or reject member sign-ups.
- **Attendance Management:** Admins can take and view the attendance of any registered member.
- **Package and Equipment Management:** Admins can add, view, delete, and update equipment and packages.

## Installation

To get started with the Waves Gym Management System, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/waves-gym.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd waves-gym
   ```

3. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

4. **Install the necessary dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Member Registration:**
   - Members can sign up on the platform.
   - After admin approval, they can log in and access their dashboard.

2. **Trainer Application:**
   - Trainers can apply for a job through the platform.
   - Upon admin approval, they can log in and access their dashboard.

3. **Admin Operations:**
   - Admins have full control over member and trainer management.
   - They can manage attendance, packages, and equipment.

## Contributing

We welcome contributions to enhance the Waves Gym. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the development team.
- Thanks to all contributors and users for their feedback and support.

---
