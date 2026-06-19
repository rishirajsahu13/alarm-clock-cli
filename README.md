Here’s a clean, complete `README.md` you can drop into your project.

---

# ⏰ Alarm Clock CLI (Python)

A simple command-line alarm clock built in Python.
Supports alarms, recurring daily alarms, snooze functionality, and persistent storage using JSON.

---

## 📦 Requirements

* Python 3.8+
* pip

Install dependencies:

```bash
pip install pytest
```

(Optional but recommended)

```bash
pip freeze > requirements.txt
```

---

## 📁 Project Structure

```text
alarm-clock-cli/
│
├── main.py
├── scheduler.py
├── storage.py
├── models.py
├── cli.py
├── alarms.json
│
└── tests/
    ├── test_scheduler.py
    ├── test_storage.py
```

---

## 🚀 Features

* Add alarms
* List alarms
* Delete alarms
* Recurring daily alarms
* Snooze (5 minutes)
* Persistent storage (JSON file)
* CLI-based scheduler loop

---

## ▶️ How to Run the App

### 1. Add an alarm

```bash
python main.py add --when "2026-06-20T07:00:00" --label "Wake Up"
```

### 2. Add a daily alarm

```bash
python main.py add --when "2026-06-20T07:00:00" --label "Daily Wake Up" --daily
```

### 3. List alarms

```bash
python main.py list
```

### 4. Delete an alarm

```bash
python main.py delete <alarm_id>
```

### 5. Run the scheduler

```bash
python main.py run
```

When an alarm triggers:

* You’ll see an alert in terminal
* Options:

  * `s` → Snooze 5 minutes
  * `d` → Dismiss

---

## 🧪 Running Tests

Tests are written using `pytest`.

### Run tests

From project root:

```bash
PYTHONPATH=. pytest -v
```

OR

```bash
python -m pytest -v
```

### Test coverage

* Snooze logic
* Alarm storage (save/load)
* Data integrity checks

---

## ⚙️ Environment Setup (Recommended)

Create virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install pytest
```

---

## 📌 Notes / Design Decisions

* Uses JSON file instead of database for simplicity
* Scheduler uses polling loop (1-second interval)
* Input handling is blocking (CLI simplicity over concurrency)
* Time format stored as ISO 8601 strings

---

## 🚧 Future Improvements

### 1. Efficient Scheduler

Replace polling loop with:

* `heapq` priority queue
* or sleep until next alarm

---

### 2. Non-blocking Architecture

Separate:

* scheduler thread
* input handler thread

---

### 3. Natural Language Time Parsing

Support:

```bash
--when "in 30 minutes"
--when "tomorrow 7am"
```

---

### 4. Persistent Database

Replace JSON with:

* SQLite
* or lightweight ORM

---

### 5. Packaging as CLI Tool

Enable:

```bash
alarm add ...
alarm list
alarm run
```

via `pip install -e .`

---

### 6. Better UX

* sound alerts
* desktop notifications
* timezone support

---

## 🧠 Design Philosophy

This project prioritizes:

* simplicity over scalability
* readability over optimization
* CLI usability over architecture complexity

---

If you want, I can next help you turn this into a **real installable CLI tool (`alarm` command globally)** — that’s usually the final “production-level” step for a project like this.
