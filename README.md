⚡ Electricity Bill Calculator

A simple Python-based Electricity Bill Calculator that calculates the total electricity bill based on the number of units consumed. The program uses a slab-wise pricing system, adds a fixed charge, and calculates 5% tax to generate the final electricity bill.

📌 Features
Accepts consumer name and electricity units.
Calculates energy charges using slab-wise rates.
Adds a fixed charge of Rs. 50.
Calculates 5% tax on the energy charge and fixed charge.
Displays a formatted electricity bill.
Handles invalid inputs and negative unit values.
Uses Python functions for better code organization.
💰 Electricity Tariff Structure
Units Consumed	Rate Per Unit
0–100 units	Rs. 3
101–200 units	Rs. 5
Above 200 units	Rs. 8

Additional Charges:

Fixed Charge: Rs. 50
Tax: 5% of (Energy Charge + Fixed Charge)
🛠️ Technologies Used
Python 3
Conditional Statements (if-elif-else)
Functions
Exception Handling (try-except)
User Input and Output
🚀 How to Run the Project
1. Clone the Repository
bash
git clone https://github.com/your-username/electricity-bill-calculator.git

2. Navigate to the Project Folder
bash
cd electricity-bill-calculator

3. Run the Python Program
bash
python electricity_bill.py

💻 Sample Output
text
Enter consumer name: Rahul
Enter units consumed: 250

========== ELECTRICITY BILL ==========
Consumer Name : Rahul
Units Consumed: 250.0
Energy Charge : Rs. 1200.00
Fixed Charge  : Rs. 50.00
Tax (5%)      : Rs. 62.50
--------------------------------------
Total Bill    : Rs. 1312.50
======================================

📂 Project Structure
text
electricity-bill-calculator/
│
├── electricity_bill.py
└── README.md

🧮 Billing Formula

Energy Charge:

First 100 units: Units × 3
Next 100 units: 100 × 3 + (Units − 100) × 5
Above 200 units: 100 × 3 + 100 × 5 + (Units − 200) × 8

Tax:

text
Tax = 5% × (Energy Charge + Fixed Charge)


Total Bill:

text
Total Bill = Energy Charge + Fixed Charge + Tax

⚠️ Input Validation
Negative electricity units are not accepted.
Invalid numerical inputs are handled using exception handling.
The program displays an appropriate error message for invalid input.
🔮 Future Improvements
Add a graphical user interface (GUI).
Store consumer billing records.
Generate downloadable PDF bills.
Add monthly electricity consumption history.
Support multiple consumers.
👨‍💻 Author
