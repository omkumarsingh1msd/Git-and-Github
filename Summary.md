# **ELECTRICITY BILL CALCULATOR – PROJECT SUMMARY**

**Name:** Om Kumar Singh\
**ERP:** RU-26-00919\
**Project:** Electricity Bill Calculator\
**Session:** 2026–27

## **1. Project Summary**

The Electricity Bill Calculator is a Python-based console application that calculates an electricity bill based on the number of units consumed by a consumer. It uses a slab-wise tariff system, adds a fixed charge of Rs. 50, calculates 5% tax on the energy charge and fixed charge, and displays the final electricity bill in a formatted manner.

## **2. Problems Faced During Development**

During the development of this project, I faced several challenges while implementing the electricity billing logic. The main problem was calculating the energy charge using the correct slab-wise tariff system.

The program had to apply Rs. 3 per unit for the first 100 units, Rs. 5 per unit for the next 100 units, and Rs. 8 per unit for units above 200. I had to carefully implement the conditional statements to ensure that each unit was charged according to its respective slab.

Another challenge was testing the boundary values, especially at 100 and 200 units. I tested different unit values to verify that the program calculated the energy charge correctly.

I also faced the challenge of handling invalid inputs. When a negative value was entered, the program needed to display an appropriate error message instead of calculating an incorrect bill. I implemented input validation to reject negative electricity units.

Finally, I had to ensure that the fixed charge and 5% tax were calculated correctly and that the final bill was displayed in a clear and readable format.

## **3. Testing and Results**

The program was tested with different electricity consumption values to verify the correctness of the calculations.

For 80 units, the energy charge was Rs. 240.00, the fixed charge was Rs. 50.00, the tax was Rs. 14.50, and the total bill was Rs. 304.50.

For 100 units, the energy charge was Rs. 300.00, the fixed charge was Rs. 50.00, the tax was Rs. 17.50, and the total bill was Rs. 367.50.

When a negative value of -20 units was entered, the program displayed an invalid-units message and rejected the input.

For 250 units, the energy charge was Rs. 1,200.00, the fixed charge was Rs. 50.00, the tax was Rs. 62.50, and the total bill was Rs. 1,312.50.

These test cases helped verify that the program worked correctly for different tariff slabs and invalid inputs.

## **4. Screenshot Evidence**

### **Screenshot 1: Program Code for Slab-wise Energy Charge Calculation**

This screenshot shows the Python function used to calculate the energy charge according to the different electricity tariff slabs.

<img width="1903" height="1015" alt="Screenshot 2026-11-23 114745" src="https://github.com/user-attachments/assets/e6e27e8c-2a4f-4926-9caf-a7ec9da6ddf4" />


### **Screenshot 2: Testing with 80 Units and 100 Units**

This screenshot shows the output of the program for 80 units and 100 units, including the energy charge, fixed charge, tax, and total bill.

<img width="1886" height="1156" alt="Screenshot 2026-11-23 114827" src="https://github.com/user-attachments/assets/b96425ae-6f54-4db5-89bc-4eb0d15eca67" />



### **Screenshot 3: Negative Unit Input Validation**

This screenshot shows how the program handles negative electricity units and displays an appropriate error message.

<img width="1900" height="805" alt="Screenshot 2026-11-23 114853" src="https://github.com/user-attachments/assets/70e2f3b5-0fa0-44dd-8f9e-7c65dfcd63b8" />


### **Screenshot 4: Testing with 250 Units**

This screenshot shows the calculation for 250 units, including the energy charge of Rs. 1,200.00 and the final bill of Rs. 1,312.50.

<img width="1917" height="976" alt="Screenshot 2026-11-23 114918" src="https://github.com/user-attachments/assets/d85e8db0-9d8f-489d-b0e0-39adcac3e39e" />


## **5. Conclusion**

This project helped me understand the practical application of Python programming concepts such as conditional statements, functions, arithmetic operations, input validation, and exception handling.

Through this project, I learned how to implement a slab-wise billing system and calculate the total electricity bill using different tariff rates. Testing the program with different unit values helped me identify and correct calculation errors and improve the accuracy of the billing logic.

The Electricity Bill Calculator successfully calculates and displays the electricity bill for valid inputs and handles negative unit values appropriately.![Uploading Screenshot 2026-11-23 114918.png…]()
