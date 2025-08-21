# Autowerkstatt Management System

Autowerkstatt is a comprehensive car service management system designed to streamline the processes of car tracking, measurement recording, user management, and reporting. The project provides an intuitive interface for both administrators and users, offering seamless functionality for managing vehicles, tracking maintenance records, and monitoring historical measurements.

---

## 🚀 Features

### **Authentication & Authorization**
- Secure user registration and login system
- Password reset and change functionalities
- Role-based access control for administrators and regular users

### **Car Management**
- Add, edit, and delete car details
- View a complete list of registered vehicles
- Search and filter vehicles easily

### **Measurement Management**
- Add, update, and delete measurement records
- View detailed measurement information
- Historical tracking for every car

### **User Profile Management**
- Update personal information
- Change passwords securely
- Manage associated vehicles and measurements

### **Dashboard & Reporting**
- Overview of total cars, measurements, and activities
- Interactive statistics and visualizations
- Quick access to frequently used actions

---

## 🛠️ Technologies Used

- **Frontend**: Blazor WebAssembly (C#)
- **Backend**: ASP.NET Core Web API
- **Database**: Microsoft SQL Server
- **Authentication**: JWT (JSON Web Token)
- **Styling**: Bootstrap & Custom CSS
- **Version Control**: Git & GitHub

---

## 📸 Screenshots

### **1. Home Dashboard**
![Home](screenshots/home.png)

### **2. User Authentication**
- **Login Page**
![Login](screenshots/login.png)
- **Register Page**
![Register](screenshots/register.png)

### **3. Car Management**
- Add Car
![Add Car](screenshots/add_car.png)
- Edit Car
![Edit Car](screenshots/edit_car.png)
- Delete Car
![Delete Car](screenshots/delete_car.png)
- Car List
![Car List](screenshots/car_list.png)

### **4. Measurement Management**
- Add Measurement
![Add Measurement](screenshots/add_measurement.png)
- Edit Measurement
![Edit Measurement](screenshots/edit_measurement.png)
- Delete Measurement
![Delete Measurement](screenshots/delete_measurement.png)
- Measurement List
![Measurement List](screenshots/measurement_list.png)
- Measurement Detail (1)
![Measurement Detail 1](screenshots/measuremnet_detail_1.png)
- Measurement Detail (2)
![Measurement Detail 2](screenshots/measurement_detail_2.png)
- Measurement Detail (3)
![Measurement Detail 3](screenshots/measuremnet_detail_3.png)

### **5. Profile & Security**
- Change Password
![Change Password](screenshots/change_password.png)

---

## ⚙️ Installation & Setup

### **Prerequisites**
- .NET 8 SDK or later
- Microsoft SQL Server
- Visual Studio / VS Code
- Git

### **Steps**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/autowerkstatt.git
   cd autowerkstatt
   ```
2. **Configure the database**:
   - Update the **connection string** in `appsettings.json`.
3. **Apply migrations**:
   ```bash
   dotnet ef database update
   ```
4. **Run the application**:
   ```bash
   dotnet run
   ```
5. Open the app in your browser:
   ```
   https://localhost:5001
   ```

---

## 📌 Future Enhancements

- Implement multi-language support
- Add advanced reporting and analytics
- Integrate notification systems for car maintenance reminders
- Enhance mobile responsiveness

---

## 🧑‍💻 Author
**Tuğba Aktürkk**  
Computer Engineering Student | Junior Software Developer
