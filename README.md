# 🏯 **Anime Score Visualizer**

**A Python-based project that retrieves top anime data from the Jikan API, stores it in MongoDB, and visualizes the scores using Matplotlib.**

---

## 📋 **Table of Contents**
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

---

## 🌟 **Features**
- Fetches top anime data from the **Jikan API**.
- Stores the data securely in **MongoDB Atlas**.
- Visualizes anime scores using **Matplotlib**.
- Efficient data handling and updates.

---

## 🛠 **Technologies Used**
- **Python 3.x**
- **MongoDB Atlas** for cloud-based storage.
- **Matplotlib** for data visualization.
- **requests** for API calls.

---

## ⚙️ **Prerequisites**
Before you begin, ensure you have the following installed:
- **Python 3.x**
- **pip** (Python package installer)
- **MongoDB Atlas account** (free tier is sufficient)
- **Git** (optional for cloning the repository)

---

## 📦 **Installation**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/anime-score-visualizer.git
   cd anime-score-visualizer

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use venv\Scripts\activate

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
---

## 🔧  **Configuration**
1. **Edit the database connection details directly in the script::**
   ```python
   username = quote_plus(os.getenv("MONGO_USER", "test-user"))
   password = quote_plus(os.getenv("MONGO_PASS", "test-user"))
   uri = f"mongodb+srv://{username}:{password}@testCluster.h7h9r.mongodb.net/?   retryWrites=true&w=majority&appName=testCluster&tlsAllowInvalidCertificates=true"

---

## 🚀 **Usage**
- Run the main script to fetch data, store it in MongoDB, and visualize the scores:
    ```bash
    python api.py
---

## 🤝 **Contributing**
Before you begin, ensure you have the following installed:
1. Fork the repository.
2. Create a new branch: git checkout -b feature/AmazingFeature.
3. Commit your changes: git commit -m 'Add some AmazingFeature'.
4. Push to the branch: git push origin feature/AmazingFeature.
5. Open a Pull Request.

---

## ⭐️ **Star this repository if you found it useful!**
📞 Contact
- GitHub: https://github.com/Nikolai9906
- Email: nikolaibermudez99@gmail.com

---
