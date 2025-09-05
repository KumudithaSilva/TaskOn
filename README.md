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
├── taskon/                           # Main application package
│   ├── __init__.py
│   ├── main.py                       # Entry point 
│   ├── app.py                        # App logic coordinator
│   ├── timer.py                      # Timer logic
│   ├── task_manager.py               # Pomodoro/task session controller
│   ├── ui.py                         # Tkinter UI
│   ├── audio_service.py              # Audio abstraction layer
│   ├── config.py                     # Configurable durations
│   ├── resources.py                  # Loads icons/audio
│   ├── logger.py                     # Centralized logging
│   └── assets/                       # Static files
│       ├── audio/                    # .wav, .mp3 files
│       └── images/                   # .png, .ico files
│
├── tests/                            # Unit tests
│   ├── __init__.py
│   ├── test_timer.py
│   └── test_task_manager.py
│
├── dist/                                  # Built files (output)
│   ├── TaskOnApp.exe                      # Windows executable (PyInstaller)
│   └── taskonapp-0.1.0-py3-none-any.whl   # Python package
│
├── build/                                 # PyInstaller build cache
│   └── ...
│
├── .github/                               # GitHub Actions workflows
│   └── workflows/
│       └── taskon-tests.yml               # CI/CD (test, Sonar, PyInstaller)
│
├── .gitignore                             # Ignore build files, __pycache__, etc.
├── README.md                              # Project overview, setup, usage
├── requirements.txt                       # Runtime dependencies (pygame, etc.)
├── MANIFEST.in                            # Includes assets in Python package
├── pyproject.toml                         # Modern build system config
├── TaskOnApp.spec                         # PyInstaller config file

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

## 🔀 Git Flow Workflow

The development process follows a **Git Flow** style workflow to keep development organized and efficient. Currently, it uses these branches:

- 🌿 **`master`** — Stable, production-ready code (released versions)  
- 🌱 **`task_oop`** — Main development branch for ongoing work  

### Future branch structure :

- ✨ **`feature/*`** — For developing new features, branched off `task_oop`  
- 🛠️ **`release/*`** — For preparing releases, branched off `task_oop`  
- 🩹 **`hotfix/*`** — For urgent bug fixes, branched off `master`  

### Typical workflow (future plan):

1. 📥 Pull the latest changes from `task_oop`  
2. 🌟 Work on your changes (directly on `task_oop` for now)  
3. 🔀 Open a Pull Request (PR) to merge into `task_oop`  
4. ✅ After review and testing, merge PR into `task_oop`  
5. 🚀 When ready for release, create a `release/*` branch from `task_oop` for final testing and polishing  
6. 🎉 Merge `release/*` into `master` and tag the new version  
7. ⚡ For urgent fixes, create a `hotfix/*` branch off `master`  
8. 🔄 Merge `hotfix/*` back into both `master` and `task_oop`  

This workflow helps maintain **stable releases** while supporting **safe feature development** and **quick fixes** as the project grows.

---

## 💡 Inspiration

>TaskOn is inspired by Francesco Cirillo’s Pomodoro Technique, designed to help people work with time instead of against it.
This project also demonstrates how OOP + SOLID principles can be applied to build a real-world, extensible productivity app.
