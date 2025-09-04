# 🌱 TaskOn — Pomodoro Timer App  

TaskOn is a lightweight, user-friendly productivity app built with **Python** and **Tkinter**, following the **Pomodoro Technique** to help you manage your time effectively. 
Unlike simple timers, TaskOn is built with **Object-Oriented Programming (OOP)** principles and follows **SOLID design practices** to ensure:  

- 🛠️ **Maintainability** — easy to update & extend  
- 🔄 **Reusability** — modular classes for timer, UI, audio, and task logic  
- 🧩 **Scalability** — add new features (themes, persistence, reports) without breaking existing code     
It helps you stay productive with focused work sessions, refreshing breaks, audio notifications, and visual progress tracking.  

TaskOn makes **focus rewarding** with **visual checkmarks, audio cues, and simple controls** — turning productivity into a habit.  

---

## 🎓 Purpose  

- 🧑‍💻 Stay **focused** with structured work & break sessions.  
- 🕒 Prevent burnout with **short and long breaks**.  
- 🌱 Track your progress visually with **checkmarks & icons**.  
- 🧠 Promote **habit building** with repetition + reinforcement.  
- 🛠️ Demonstrate a real-world **OOP + SOLID Python project**.  

---

## 🧠 Key Features

- ⏱️ **Automated Pomodoro sessions** (Work → Short Break → Work → Long Break).  
- 🎨 **Minimal Tkinter-based UI** with start/reset controls.  
- 🔔 **Audio alerts** for session transitions.  
- ✅ **Checkmarks** to celebrate completed work sessions.  
- ⚙️ **Customizable durations** (work, short/long breaks, repetitions).  
- 📝 **Session logging** — activities logged in console & `app.log`.

---

## 📸 TaskOn App Output (UI Preview)

<img width="254" height="384" alt="image" src="https://github.com/user-attachments/assets/437485d7-3cad-4e5c-ac3e-d55796154686" />


---

## ✨ Features  

- ⏱️ **Pomodoro Timer** — Work, Short Break, and Long Break sessions.  
- 🎨 **Minimal & Clean UI** powered by Tkinter.  
- 🔔 **Audio Notifications** with sound cues for session transitions.  
- 🌿 **Visual Feedback** — progress checkmarks and dynamic logos.  
- ⚙️ **Customizable Configurations** (session durations, repetitions, countdowns).  
- 📝 **Built-in Logging** — records actions in `app.log` and console.  
- 📦 **Lightweight** — runs with Python standard libraries and `pygame`.  

---

## 📌 How It Works  

1. Press **▶️ Start** → a short tick countdown begins.  
2. Timer alternates between:  
   - **Work sessions** 🧑‍💻  
   - **Short breaks** ☕  
   - **Long breaks** 🌿 after several work sessions.  
3. 🎶 **Audio alerts** notify when time’s up.  
4. ✅ **Checkmarks** track completed work sessions.  
5. Press **⏸️ Reset** anytime to clear progress.  

---

## 🎯 App Flow Overview

- ▶️ **Play** → Starts timer.  
- ⏳ **Tick countdown** → Quick prep before session begins.  
- ⏱️ **Work timer** → Focus until alarm.  
- 🌿 **Break timers** → Short or long depending on progress.  
- ✅ **Completion tracking** → Adds checkmarks to UI.  
- ⏸️ **Reset** → Clears timers, progress, and starts fresh.  

---

## 🔧 Core Functionalities

### ✅ `TaskManager`
- Tracks **session repetitions** and decides whether the next is work, short break, or long break.  

### ✅ `Timer`
- Handles **countdown logic** (tick + main timer).  
- Triggers **callbacks** to update UI and play sounds.  

### ✅ `TaskOnUI`
- Tkinter-based **user interface** with buttons, logos, and timers.  
- Displays countdowns, alarm messages, and checkmarks.  

### ✅ `AudioService`
- Plays **notification sounds** for transitions.  

### ✅ `ResourceLoader`
- Dynamically loads **images and icons** from `assets/`.

---

## 🖥️ System Requirements

- Python **3.8+**  
- Dependencies:  
  - `tkinter` (built-in with Python)  
  - `pygame` (for audio)  

Install dependencies with:  
```bash
pip install -r requirements.txt
```
---

## 🗂️ Project Structure  
```bash
TaskOnApp/ 
├── main.py              # Entry point (launches the app)
├── taskon/ 
│   ├── app.py           # Main TaskOnApp (coordinates everything)
│   ├── timer.py         # Timer class (countdowns & ticks)
│   ├── task_manager.py  # Controls session switching & repetition
│   ├── ui.py            # Tkinter-based UI
│   ├── audio_service.py # IAudioService interface + pygame implementation
│   ├── config.py        # Configurable durations & settings
│   ├── resources.py     # Loads images/icons
│   └── logger.py        # Centralized logging
└── assets/ 
    ├── audio/           # Sound files (beep.wav, congratulations.wav)
    └── images/          # Icons (play, pause, logos, checkboxes)
```
---

## 📦 Future Enhancements

- 🎨 Modern UI Themes — Add dark mode & customizable color schemes.

- 🔔 Custom Alerts — Allow users to upload/select their own sounds.

- 📊 Productivity Analytics — Track sessions completed & generate reports.

- 🌐 Cross-Platform Sync — Save sessions & configs to the cloud.

- 📝 Task Notes — Attach quick notes/todos to each work session.

---

## 🤝 Contributing

- 🍴 Fork the repo
- 🌱 Create a feature branch
- 🛠️ Commit changes
- 📤 Push branch & open Pull Request

- We welcome UI tweaks, new features, bug fixes, and documentation improvements!

---

## 💡 Inspiration

>TaskOn is inspired by Francesco Cirillo’s Pomodoro Technique, designed to help people work with time instead of against it.
This project also demonstrates how OOP + SOLID principles can be applied to build a real-world, extensible productivity app.
