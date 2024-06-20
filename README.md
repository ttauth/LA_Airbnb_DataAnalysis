# Airbnb Data Analysis

## Project Overview

### Key Stakeholders
The primary stakeholders for this project are my aunt and uncle, who are looking to invest in the Airbnb market in Los Angeles (LA). Initially, they wanted to understand how the Airbnb market is performing in LA. This led to two overarching questions:

1. How much are the top Airbnb earners making?
2. Who are the potential customers for an Airbnb cleaning business?

### Objectives
1. **Determine the earnings of top Airbnb operators in LA**: Calculate the total projected revenue of the top 20 Airbnb operators based on their nightly price and booking data.
2. **Identify potential customers for an Airbnb cleaning business**: Identify Airbnb operators who might require cleaning services based on the frequency and volume of their bookings.

### Methodology
1. **Data Import**:
   - Imported data from CSV files into a MySQL database using a Python script.
   - The dataset includes listings, calendar, and reviews data.

2. **Data Analysis and Visualization**:
   - Connected Tableau to the MySQL database to create visualizations that answer the key questions.
   - Created queries to extract relevant data for analysis.

### Steps to Solve the Problems
1. **Top Airbnb Earners**:
   - **Query**: Created a query to extract the `id`, `listing_url`, `name of listing`, `number of booked days in the next 30 days`, `nightly price`, and calculated the total projected revenue.
   - **Findings**: The initial analysis showed that many top listings were either booked out for the entire year due to their popularity or not available for booking for the next year. This indicated high demand and limited availability.

2. **Potential Customers for a Cleaning Business**:
   - Based on the findings from the first query, the stakeholders considered that it might be more lucrative to start a cleaning business targeting these high-demand Airbnb operators.
   - **Query**: Extracted data to identify Airbnb operators with frequent bookings, high booking rates, and consistent demand for cleaning services.

### Insights and Recommendations
The analysis revealed that the top 20 Airbnb listings in LA are fully booked throughout the year, generating substantial annual revenue, primarily around $364,635. Many of these listings belong to the Palihotel brand, indicating a strong market presence and high demand for luxury accommodations. Furthermore, the popularity of pet-friendly options suggests a niche market opportunity. Given the consistent high occupancy rates, it is recommended to invest in properties in high-demand areas like Hollywood and Culver City, and to consider starting a cleaning business to service these high-turnover properties.

### Results
1. **Top Airbnb Earners**:
   - Identified the top 20 Airbnb operators in LA by projected monthly revenue.
   - Many of these top operators have high occupancy rates and substantial revenue potential.

2. **Potential Cleaning Business Customers**:
   - Identified potential customers for the cleaning business by analyzing booking frequency and patterns.
   - Provided a list of operators who might benefit from regular cleaning services due to high turnover rates.

## Files
- `import_csv_to_mysql.py`: Script to import CSV data into MySQL.



