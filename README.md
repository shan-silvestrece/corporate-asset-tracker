# Enterprise Corporate Asset Tracker

**Name:** Shan G. Silvestrece  
**Subject:** IT383 - Integrative Programming and Technologies 2  
**Section:** BSIT - 3B  
**Instructor:** Mr. Jessie R. Paragas  
**University:** Eastern Visayas State University - Main Campus  

---

## 📌 Project Overview
The **Enterprise Corporate Asset Tracker** is a Django-based web application designed to help corporate IT and Finance departments manage company hardware. It tracks asset assignments, monitors individual maintenance histories, dynamically calculates the total cost of ownership, and provides raw data exporting capabilities for financial auditing.

## ✨ Key Features
* **Executive Dashboard:** Displays a high-level overview of total asset costs grouped by department.
* **Asset Inventory:** A paginated list (5 items per page) of all corporate assets, showing original purchase costs and dynamically calculated repair investments.
* **Maintenance Logging:** A relational database feature (One-to-Many) that allows IT staff to log individual repairs, which automatically update the parent asset's total repair cost.
* **CSV Exporting:** Allows the accounting department to instantly download the current asset database into a `.csv` file for Excel imports.
* **Responsive UI/UX:** Styled completely with Bootstrap 5, featuring progress bars, status indicators, and intuitive navigation.

## 🛠️ Technology Stack
* **Backend:** Python 3, Django
* **Database:** SQLite3 (Pre-populated with 15 assets and 5 maintenance logs)
* **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons
* **Version Control:** Git & GitHub

---

## 🚀 How to Run the Project Locally

Because the Python Virtual Environment (`venv`) is properly excluded from this repository, follow these steps to run the app on your local machine:

**1. Clone the repository**
```bash
git clone [https://github.com/shan-silvestrece/corporate-asset-tracker.git](https://github.com/shan-silvestrece/corporate-asset-tracker.git)
cd corporate-asset-tracker