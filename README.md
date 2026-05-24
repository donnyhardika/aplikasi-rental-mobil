# PROGRAM CRUD RENT CAR APPLICATION
Python CRUD Application for Rental Mobil
A comprehensive Python application for managing Rental Mobil data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the car rental business domain, specifically addressing the need to manage rental car data efficiently.
Rental Mobil is utilized in the Python app to represent the core entity in the rental process.

**Benefits:**

Improved accuracy and consistency of rental car data

Streamlined management of available cars and pricing

Enhanced decision-making through readily available car inventory information

Simplified integration with other business systems (optional)

**Target Users:**
This application is designed for rental managers, staff, or customer service agents to facilitate their car rental-related business tasks.

## Features

* **Create:**
  *Add new car entries with essential details (ID, merk, tahun, harga).
  *Implement validation rules to ensure data integrity (e.g., year range, positive price).

* **Read:**
  *Display all available cars in a structured table format.
  *Search cars by merk using keyword-based search.

* **Update:**
  *Modify existing car entries through a predefined interface.
  *Validate that modifications are permissible (e.g., year range, price > 0).

* **Delete:**
  *Remove car entries permanently from the list.
  *Confirmation required before deletion to avoid accidental data loss.

* **Reporting:**
  *Generate a summary of available cars.
  *Search results displayed in a readable format.
  *Deployable as a CLI application for easy use.

## Installation

1. **Prerequisites:**
  *Python installed (version 3.8 or higher recommended).

2. **Installation:**
 ```bash
git clone https://github.com/donnyhardika/aplikasi-rental-mobil
cd aplikasi-rental-mobil

pip install -r requirements.txt  # If using a requirements.txt file
    ```

3. **Database Setup (if applicable):**
    Follow specific instructions for configuring your database connection, aligning with the business's chosen database management system.
## Usage

1. **Run the application:**
```bash
   python rental_mobil.py
    ```
python rental_mobil.py
2. **CRUD Operations:**

* **Create:** Tambah data mobil baru (merk, tahun, harga).

* **Searching:** Cari daftar mobil berdasarkan merk.

* **Read:** Lihat daftar mobil atau cari mobil berdasarkan merk.

* **Update:** Ubah data mobil berdasarkan ID.

* **Delete:** Hapus data mobil berdasarkan ID.

* **Exit:** Keluar dari program dengan aman.

Data Model
This project utilizes a list of dictionaries to represent car entities. The following fields are used:

id – Unique identifier for each car

merk – Car brand/model

tahun – Year of manufacture

harga – Rental price per day

## Contributing
We welcome contributions to this project!
Please feel free to open a pull request, contact via donny.hardika@gmail.com, or submit an issue if you encounter any problems.
