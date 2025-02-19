# 🚀 Shoe Billing System  

## 📌 Overview  
The **Shoe Billing System** is a **Python-based application** integrated with **MySQL**, designed to manage customer details, billing, and record retrieval for a shoe store.  

## 🔑 Key Features  
- ✅ **Customer Management** – Store and manage customer details 📋  
- ✅ **Search Functionality** – Retrieve customer info by **shoe code** or **name** 🔍  
- ✅ **Billing System** – Generates bills with **GST & discounts** 💰  
- ✅ **User Authentication** – Secure system access for authorized users 🔐  
- ✅ **Database Integration** – Efficient **data storage & retrieval** with **MySQL** 💾  

## 🛠️ Tech Stack  
- 🔹 **Python** 🐍  
- 🔹 **MySQL** 🛢️  
- 🔹 **MySQL Connector** 🔗  

## 🎯 Project Purpose  
This project demonstrates **database handling, CRUD operations, error handling, and billing logic**, aligning with **CBSE Class 12 Computer Science practicals**.  

## 🚀 How to Run the Project  
1️⃣ Install required dependencies:  
```sh  
pip install mysql-connector-python  
```  
2️⃣ Set up the MySQL database and create the required table:  
```sql  
CREATE DATABASE shoe_billing;  
USE shoe_billing;  
CREATE TABLE IF NOT EXISTS shoe_details (  
   shoe_code CHAR(5) PRIMARY KEY,  
   brand_name CHAR(20),  
   customer_name VARCHAR(25),  
   customer_number CHAR(10),  
   customer_address VARCHAR(50),  
   amount INT  
);  
```  
3️⃣ Run the Python script:  
```sh  
python shoe_billing.py  
```  

## 📜 License  
This project is for educational purposes only.  

### 🔗 Connect with Me  
💬 Feel free to reach out for collaborations and suggestions!  

#Python #MySQL #BillingSystem #SoftwareDevelopment #CBSE #FinalYearProject

