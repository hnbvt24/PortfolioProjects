# Welcome to my Portfolio!

### Here, you'll discover the various ways in which I have used SQL & Python for problem solving and wrangling data.

## [Project 1 - Coffee Taste Preferences Analysis](/Coffee_Taste_Preferences.ipnyb)
- The "Coffee Taste Preferences Analysis" Python code project explores coffee drinkers' preferences using data from the 'Great American Coffee Taste Test.'
- The code covers various aspects, including demographic information, brewing methods, and taste preferences.
- Visualizations offer insights into popular coffees, preferences by gender, age, and expertise level.
- The project combines web scraping and data analysis techniques to provide actionable insights for businesses in the coffee industry.

## [Project 2 - COVID 19 Deaths Analysis](/COVID_19_Deaths_Analysis.sql)
  - This Python project involves comprehensive data analysis on COVID-19 deaths in the USA.
  - The initial steps include data cleaning, where 'N/A' and 'Data not available' fields are replaced with NULL for accurate calculations.
  - The project then delves into various aspects, such as identifying states with the highest positive tests and hospital admissions, investigating changes in admissions, and assessing death rates over different periods.
  - Notably, the analysis uncovers insights into regional variations, with regions 4 and 5 facing significant challenges.
  - Analyze the following:
    * The number of people who tested positive for Covid 19 by State
    * Which region has the most Hospitalizations of patients with COVID 19 in the past week
    * Which states are in Region 5 to determine where we need to support hospital staff
    * Change in new hospital admissions over the prior week to see how much it's fluctuated in each region
    * Which states are in that area to see if it's densely populated
    * Which region has the most hospital admissions since early on in the Pandemic (Aug 2020)
    * What percentage of these cases resulted in death during the past week by state (exclude supressed data)
    * Death Rate over the last 3 months to get a bigger picture into recent events
    * Total Deaths are for each state to see if these 3 states have remained fairly consistent over the trajectory of this dataset
    * The percentage of people who died of Covid 19 out of the people who tested positive for Covid 19 by State

## [Project 3 - House Project](/House_Project.sql)
  - This project is to showcase the ways in which you can clean data for a Housing Dataset.
  - Based on the dataset found on the [CDC's website](https://covid.cdc.gov/covid-data-tracker/#maps_percent-covid-deaths).
  - Includes the following:
    * Populating missing data fields
    * Splitting Addresses into Street Address, City, State Columns
    * Updating text strings
    * Removing duplicates
    * Deleting unnecessary columns

## [Project 4 - BMI Calculator](/BMI_Calculator.py)
  - This project is to showcase requesting user input for conducting calculations.
  - Based on the dataset found on the [CDC's website](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/english_bmi_calculator/bmi_calculator.html).
  - Includes the following:
    * Request user input for height and weight
    * Output their BMI based on the calculations provided by the CDC website

## [Project 5 - Automatic File Sorter in File Explorer](/Automatic_File_Sorter_in_File_Explorer.py)
  - This project is to showcase how to sort and move files withing your local computer.
  - Includes the following:
    * Create folders for various file types
    * Move files into their respective folders by file type

## [Project 6 - Scraping Data from Wikipedia](/Scraping_Data_From_Wikipedia.py)
  - This project is to showcase how to scrape table data from a website, in our case - Wikipedia.
  - Referencing the following [Wikipedia page](https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue)
  - Includes the following:
    * Extracting data from a website
    * Recreating a table in python

## [Project 7 - Scraping Data from an Amazon Product Page](/AmazonWebScraping.py)
  - This project is to showcase how to scrape product data from Amazon.
  - Referencing the following [Purina Pro Plan High Protein Dog Food With Probiotics for Dogs, Shredded Blend Chicken & Rice Formula - 18 lb. Bag](https://www.amazon.com/Purina-Pro-Plan-Shredded-Chicken/dp/B001VIWHMY/ref=sr_1_1_sspa?c=ts&dib=eyJ2IjoiMSJ9.gTlB5Nw7kn5_xISkmyyvDNEcy5lBTgMwVve74BV4FSuk92cRMtaoje1zlHB2Pv4ttxluzKLSHb-IBu_4M6tEKQ.g6yhi4W91euRABnH1G6S55Fr4Vau_9AfY50wHwoNoSA&dib_tag=se&keywords=Dog%2BFood&qid=1704995498&rdc=1&s=pet-supplies&sr=1-1-spons&ts_id=2975359011&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)
  - Includes the following:
    * Extracting data from Amazon
    * Creating a csv file on our local machine
    * Create a Function to insert data into our csv
    * Setting a timer to run our function every day
