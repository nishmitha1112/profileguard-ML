#  ProfileGuard ML – Fake Profile Detection System

ProfileGuard ML is a Machine Learning–based web application that detects whether a given social media profile is **REAL or FAKE** using a Random Forest model.

---

##  Live Demo

 Frontend:  
👉 https://profileguard-ml.vercel.app/
---

##  Project Overview

The system analyzes key profile metrics and detects whether a given profile is real or fake in real time.

- Input: Profile features  
- Output: **REAL USER / FAKE USER**  
- Type: Binary Classification  

---

## Tech Stack

- Python  
- Machine Learning (Random Forest)  
- Flask (Backend API)  
- HTML, CSS, JavaScript (Frontend)  

---

## Features

- Real-time fake profile detection  
- Single profile prediction system  
- Web-based interactive dashboard  
- REST API integration  
- Model accuracy around **99%**  

---

## Machine Learning Model

- Algorithm: Random Forest Classifier  
- Type: Binary Classification  

**Input Features:**
- followers_count  
- friends_count  
- ff_ratio  
- verified  
- default_profile  

**Output:**
- 1 → Real User  
- 0 → Fake User  

---

## Project Structure
456/
│
├── data/ # Dataset files
├── models/ # Trained ML model (.pkl)
├── notebooks/ # Model training
├── backend/ # Flask API
├── frontend/ # UI (HTML, CSS, JS)
├── vercel.json # Routing config

---
## Screenshots

<img width="1894" height="892" alt="Screenshot 2025-12-08 220732" src="https://github.com/user-attachments/assets/f78db002-3992-437b-ae7b-0194d3b1d986" />
<img width="1893" height="882" alt="Screenshot 2025-12-08 221305" src="https://github.com/user-attachments/assets/71f53cbc-285a-415e-a911-ec62686f576e" />
<img width="1889" height="889" alt="Screenshot 2025-12-08 221333" src="https://github.com/user-attachments/assets/6afd02f9-cac0-4276-a1a3-86fe85f13e99" />

