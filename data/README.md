
# HotelIQ Data

This folder documents the datasets used in the HotelIQ project.

## Main Dataset
Hotel Booking Demand dataset

## Data Preparation
- Original records: 119,390
- Cleaned analysis records: 118,564
- Removed 826 records with invalid booking information
- Created additional fields for booking analysis

## Derived Data
- HotelIQ_SQL_Ready.csv
- HotelIQ_Final_Model_Metrics.csv
- HotelIQ_Feature_Importance.csv

## Data Notes
The original dataset contains no verified unique booking ID.
Exact duplicate rows were therefore retained.

The estimated booking value is an analytical estimate,
not confirmed hotel revenue.


Dataset: Hotel Booking Demand

Original researchers:
Nuno António, Ana de Almeida, and Luís Nunes (2019).

Dataset source:
https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

License:
Creative Commons Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/

Modifications made for HotelIQ:
- Cleaned missing and invalid values
- Excluded 826 invalid booking records
- Created additional analytical features
- Prepared data for PostgreSQL and Power BI

This is a modified version of the original dataset.
The original authors do not endorse this project.
