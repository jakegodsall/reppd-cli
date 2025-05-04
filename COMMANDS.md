# 🛠 Reppd CLI – Command Reference

This document provides a complete overview of the available `reppd` CLI commands, with usage examples and expected behaviors. Use the CLI to log actions, review your habit history, manage configuration, and sync with the Reppd API.

---


## 🚀 `reppd init`

Initializes the CLI for the current user.

- Authenticates using your API token.
- Fetches all available competencies and actions.
- Caches data locally in:
  - `~/.reppd/config.yaml`
  - `~/.reppd/actions.json`

### ✅ Usage
```bash
reppd init
```

---

## 📥 `reppd log`

Log a completed action (habit) to Reppd. You can specify the action directly or specify both the competency and the action name to avoid ambiguity.

### ✅ Basic Usage
```bash
reppd log
```
Prompts interactively for competency, action, and value.

### ➕ Log by Action Name
```bash
reppd log --action "Read in Polish" --value 20
```

### 🧠 Log with Full Context (Competency + Action)
```bash
reppd log --competency "Language Learning" --action "Read in Polish" --value 20
```

---

## 🕓 `reppd history`

View recently logged actions.

### ✅ Basic Usage
```bash
reppd history
```

### 🔍 Filter by Action Name
```bash
reppd history --action "Reading"
```

### 📅 Specify Date Range
```bash
reppd history --days 30
```

---

## ⚙️ `reppd config`

Manage CLI configuration, including API tokens and sync settings.

### 🔍 View Current Config
```bash
reppd config show
```

### 🛡 Set API Token
```bash
reppd config set token <API_TOKEN>
```

### ❌ Clear Config
```bash
reppd config clear
```

---


## 🆘 `reppd help`

Shows available commands and usage examples.

### ✅ Usage
```bash
reppd help
```

---
