-- Preview the dataset and review columns we want to use
Select TOP 10 * from [PortfolioProject].[dbo].[us_covid19_deaths]


-- OBSERVATION: The dataset was created with fields that have 'N/A'  and 'Data not available' rather than NULL to indicate an empty field. 
--              Let's try replacing those so we can run some calculations on the data.

-- Select all fields and use the nullif() formula to convert each 'N/A' and 'Data not available' to NULL. 
-- We'll test this fist before updaating the table directly.


-- Since the State_Territory is our Primary Key, we'll use that within our Where clause for updating
SELECT
    [State_Territory],
    [HHS_Region]
FROM [PortfolioProject].[dbo].[us_covid19_deaths]
WHERE [HHS_Region] LIKE '%N/A%' OR [HHS_Region] LIKE 'Data not available'

-- Let's get the rows that have N/A by the Primary Key
SELECT
    [State_Territory],
    [HHS_Region]
FROM [PortfolioProject].[dbo].[us_covid19_deaths]
WHERE State_Territory IN (
                            'American Samoa', 
                            'Federated States of Micronesia', 
                            'Guam', 'New York (excludes NYC)', 
                            'New York City', 
                            'Northern Mariana Islands', 
                            'Palau', 
                            'Republic of Marshall Islands'
                        )

-- Update the column HHG_Region with NULL
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths]
SET HHS_Region = NULL
WHERE State_Territory IN (
                            'American Samoa', 
                            'Federated States of Micronesia', 
                            'Guam', 'New York (excludes NYC)', 
                            'New York City', 
                            'Northern Mariana Islands', 
                            'Palau', 
                            'Republic of Marshall Islands'
                        )

-- Let's verify the changes were made to the right cells in the HHS_Region column
SELECT
    *
FROM [PortfolioProject].[dbo].[us_covid19_deaths]
WHERE State_Territory IN (
                            'American Samoa', 
                            'Federated States of Micronesia', 
                            'Guam', 'New York (excludes NYC)', 
                            'New York City', 
                            'Northern Mariana Islands', 
                            'Palau', 
                            'Republic of Marshall Islands'
                        )


-- NOTE: This is going to take forever doing this one-by-one. So I'm going to do a select statement 
--       that helps me to gather all values in the table that match 'N/A' and Update each of those column cells with NULL.

-- Create UPDATE statements that select all cells that match 'N/A' for each column
SELECT 'UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET ' + name + ' = NULL WHERE ' + name + ' LIKE ''%N/A%'' OR ' + name + ' LIKE ''%Data not available%'';'
FROM PortfolioProject.sys.syscolumns
WHERE id = object_id('[PortfolioProject].[dbo].[us_covid19_deaths]')
  AND isnullable = 1;

-- Run the following Update statements. We won't need the State_Territory since it's our Primary Key and we can ignore HHS_Region since we already updated that column.
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET New_hospital_admissions_of_confirmed_COVID_19_past_week_total = NULL WHERE New_hospital_admissions_of_confirmed_COVID_19_past_week_total LIKE '%N/A%' OR New_hospital_admissions_of_confirmed_COVID_19_past_week_total LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET New_COVID_19_hospital_admissions_per_100000_population_past_week_total = NULL WHERE New_COVID_19_hospital_admissions_per_100000_population_past_week_total LIKE '%N/A%' OR New_COVID_19_hospital_admissions_per_100000_population_past_week_total LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Change_in_new_hospital_admissions_of_confirmed_COVID_19_from_the_prior_week = NULL WHERE Change_in_new_hospital_admissions_of_confirmed_COVID_19_from_the_prior_week LIKE '%N/A%' OR Change_in_new_hospital_admissions_of_confirmed_COVID_19_from_the_prior_week LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Total_hospital_admissions_of_confirmed_COVID_19_since_August_1_2020 = NULL WHERE Total_hospital_admissions_of_confirmed_COVID_19_since_August_1_2020 LIKE '%N/A%' OR Total_hospital_admissions_of_confirmed_COVID_19_since_August_1_2020 LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Staffed_inpatient_beds_occupied_by_patients_with_confirmed_COVID_19_past_week_average = NULL WHERE Staffed_inpatient_beds_occupied_by_patients_with_confirmed_COVID_19_past_week_average LIKE '%N/A%' OR Staffed_inpatient_beds_occupied_by_patients_with_confirmed_COVID_19_past_week_average LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Absolute_change_staffed_inpatient_beds_occupied_by_patients_with_confirmed_COVID_19_from_prior_week = NULL WHERE Absolute_change_staffed_inpatient_beds_occupied_by_patients_with_confirmed_COVID_19_from_prior_week LIKE '%N/A%' OR Absolute_change_staffed_inpatient_beds_occupied_by_patients_with_confirmed_COVID_19_from_prior_week LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Staffed_ICU_beds_occupied_by_patients_with_confirmed_COVID_19_past_week_average = NULL WHERE Staffed_ICU_beds_occupied_by_patients_with_confirmed_COVID_19_past_week_average LIKE '%N/A%' OR Staffed_ICU_beds_occupied_by_patients_with_confirmed_COVID_19_past_week_average LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Absolute_change_staffed_ICU_beds_occupied_by_patients_with_confirmed_COVID_19_from_prior_week = NULL WHERE Absolute_change_staffed_ICU_beds_occupied_by_patients_with_confirmed_COVID_19_from_prior_week LIKE '%N/A%' OR Absolute_change_staffed_ICU_beds_occupied_by_patients_with_confirmed_COVID_19_from_prior_week LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Percentage_of_deaths_due_to_COVID_19_in_past_week = NULL WHERE Percentage_of_deaths_due_to_COVID_19_in_past_week LIKE '%N/A%' OR Percentage_of_deaths_due_to_COVID_19_in_past_week LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Percent_change_percentage_of_deaths_due_to_COVID_19_in_past_week = NULL WHERE Percent_change_percentage_of_deaths_due_to_COVID_19_in_past_week LIKE '%N/A%' OR Percent_change_percentage_of_deaths_due_to_COVID_19_in_past_week LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Absolute_change_percentage_of_deaths_due_to_COVID_19_in_past_week = NULL WHERE Absolute_change_percentage_of_deaths_due_to_COVID_19_in_past_week LIKE '%N/A%' OR Absolute_change_percentage_of_deaths_due_to_COVID_19_in_past_week LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Deaths_in_the_Past_3_Months = NULL WHERE Deaths_in_the_Past_3_Months LIKE '%N/A%' OR Deaths_in_the_Past_3_Months LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Death_Rate_per_100000_for_the_Past_3_Months = NULL WHERE Death_Rate_per_100000_for_the_Past_3_Months LIKE '%N/A%' OR Death_Rate_per_100000_for_the_Past_3_Months LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Total_Deaths = NULL WHERE Total_Deaths LIKE '%N/A%' OR Total_Deaths LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Total_Death_rate_per_100000 = NULL WHERE Total_Death_rate_per_100000 LIKE '%N/A%' OR Total_Death_rate_per_100000 LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Percent_of_ED_visits_diagnosed_as_COVID_19 = NULL WHERE Percent_of_ED_visits_diagnosed_as_COVID_19 LIKE '%N/A%' OR Percent_of_ED_visits_diagnosed_as_COVID_19 LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Percent_change_in_of_visits_diagnosed_as_COVID_19_from_last_week_compared_to_prior_week = NULL WHERE Percent_change_in_of_visits_diagnosed_as_COVID_19_from_last_week_compared_to_prior_week LIKE '%N/A%' OR Percent_change_in_of_visits_diagnosed_as_COVID_19_from_last_week_compared_to_prior_week LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Test_positivity_in_past_week = NULL WHERE Test_positivity_in_past_week LIKE '%N/A%' OR Test_positivity_in_past_week LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Change_in_test_positivity_compared_with_prior_week = NULL WHERE Change_in_test_positivity_compared_with_prior_week LIKE '%N/A%' OR Change_in_test_positivity_compared_with_prior_week LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Test_positivity_in_past_2_weeks = NULL WHERE Test_positivity_in_past_2_weeks LIKE '%N/A%' OR Test_positivity_in_past_2_weeks LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Test_positivity_in_past_4_weeks = NULL WHERE Test_positivity_in_past_4_weeks LIKE '%N/A%' OR Test_positivity_in_past_4_weeks LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Test_volume_in_past_week = NULL WHERE Test_volume_in_past_week LIKE '%N/A%' OR Test_volume_in_past_week LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Test_volume_in_past_2_weeks = NULL WHERE Test_volume_in_past_2_weeks LIKE '%N/A%' OR Test_volume_in_past_2_weeks LIKE '%Data not available%';
UPDATE [PortfolioProject].[dbo].[us_covid19_deaths] SET Test_volume_in_past_4_weeks = NULL WHERE Test_volume_in_past_4_weeks LIKE '%N/A%' OR Test_volume_in_past_4_weeks LIKE '%Data not available%';

-- Preview the dataset and review columns to verify they've been updated
Select TOP 10 * from [PortfolioProject].[dbo].[us_covid19_deaths]

-- Let's see the number of people who tested positive for Covid 19 by State
Select
    State_Territory,
    CAST((Test_volume_in_past_week) AS INTEGER) as Past_Week_Positive_Tests
From [PortfolioProject].[dbo].[us_covid19_deaths]
Order by CAST((Test_volume_in_past_week) AS INTEGER) DESC

-- Let's see which region has the most Hospitalizations of patients with COVID 19 in the past week
Select
    State_Territory,
    HHS_Region,
    New_hospital_admissions_of_confirmed_COVID_19_past_week_total
From [PortfolioProject].[dbo].[us_covid19_deaths]
Order by New_hospital_admissions_of_confirmed_COVID_19_past_week_total DESC

-- OBESRVATION: The data is outputing the number of hospital admissions as strings, so the numbers are not able to sort in the correct order
--              Let's Cast the variable as an integer.
Select
    HHS_Region,
    SUM(CAST(New_hospital_admissions_of_confirmed_COVID_19_past_week_total AS INTEGER)) as Past_Week_Hospital_Admissions_by_Region
From [PortfolioProject].[dbo].[us_covid19_deaths]
Group by HHS_Region
Order by SUM(CAST(New_hospital_admissions_of_confirmed_COVID_19_past_week_total AS INTEGER)) DESC

-- OBESRVATION: Region 5 has the most New Hospital Admissions of Covid 19 this past week with 6,953 admissions.

-- Let's see which states are in Region 5 to determine where we need to support hospital staff
SELECT
    State_Territory
FROM [PortfolioProject].[dbo].[us_covid19_deaths]
WHERE HHS_Region = 'Region 5'

-- OBSERVATION: The following states are in Region 5:
-- Illinois
-- Indiana
-- Michigan
-- Minnesota
-- Ohio
-- Wisconsin

-- OBSERVATION: Looks like the Mid-west region has it the worst right now. 
--              Let's see who has the least admissions so we can potentially pull some resources to relocate to Region 5.
Select
    HHS_Region,
    SUM(CAST(New_hospital_admissions_of_confirmed_COVID_19_past_week_total AS INTEGER)) as Past_Week_Hospital_Admissions_by_Region
From [PortfolioProject].[dbo].[us_covid19_deaths]
Group by HHS_Region
Order by SUM(CAST(New_hospital_admissions_of_confirmed_COVID_19_past_week_total AS INTEGER)) ASC

-- OBSERVATION: Region 10 seems to have the least admissions with only 825 admissions. Let's see which states belong to Region 10.
SELECT
    State_Territory
FROM [PortfolioProject].[dbo].[us_covid19_deaths]
WHERE HHS_Region = 'Region 10'

-- OBSERVATION: The following states are in Region 10:
-- Alaska
-- Idaho
-- Oregon
-- Washington

-- OBSERVATION: It seems the upper left west-coast are experiencing fewer cases, or at least hospitalizations, of COVID 19.
--              We can recommend pulling some available resources and Covid medical supplies from their Region and assist Region 5.

-- Let's see the change in new hospital admissions over the prior week to see how much it's fluctuated in each region
SELECT
    HHS_Region,
    AVG(CAST(Change_in_new_hospital_admissions_of_confirmed_COVID_19_from_the_prior_week AS FLOAT)) as Change_in_Hospital_Admissions_by_Region
From [PortfolioProject].[dbo].[us_covid19_deaths]
Group by HHS_Region
Order by AVG(CAST(Change_in_new_hospital_admissions_of_confirmed_COVID_19_from_the_prior_week AS FLOAT)) DESC

-- OBSERVATION: It looks like Region 4 has the largest increase in confirmed cases over the prior week, meaning they
--              likely had an influx of people getting the virus either from travel or being in public spaces.
--              The Region with the least change is Region 7, likely indicating that more people are staying in their homes or
--              taking stronger preventitive measures when in public spaces and the virus could be dying out in that area.

-- Let's see which states are in that area to see if it's densely populated.
SELECT
    State_Territory
FROM [PortfolioProject].[dbo].[us_covid19_deaths]
WHERE HHS_Region = 'Region 4'

-- OBSERVATION: The following states are in Region 4:
-- Alabama
-- Florida
-- Georgia
-- Kentucky
-- Mississippi
-- North Carolina
-- South Carolina
-- Tennessee

-- OBERSVATION: These areas a fairly dense in population, though spread out in much of the state area. 
--              So it's more likely that the cause of the spread of the virus was due to state procedures 
--              and poorer regulations on safety measures in public spaces.

-- Let's find out which region has the most hospital admissions since early on in the Pandemic (Aug 2020)
Select
    HHS_Region,
    SUM(CAST(Total_hospital_admissions_of_confirmed_COVID_19_since_August_1_2020 AS INTEGER)) as Total_Hospital_Admissions_by_Region
From [PortfolioProject].[dbo].[us_covid19_deaths]
Group by HHS_Region
Order by SUM(CAST(Total_hospital_admissions_of_confirmed_COVID_19_since_August_1_2020 AS INTEGER)) DESC

-- OBSERVATION: Region 4 has the most hospital admissions due to Covid 19 since August, 2020, with Region 5 in close second.
--              So although Region 5 has the most this past week, Region 4 has the most overall cases.
--              Region 4 also had the highest change in covid cases this past week, which means the area is still heavily
--              infected with the Covid 19 virus. It could be likely that the area


-- Let's find out what percentage of these cases resulted in death during the past week by state
-- We'll exclude any with 'Counts 1-9' since those are states with data that's suppressed in accordance with the NCHS data confidentiality standards.
Select
    State_Territory,
    CAST(Percentage_of_deaths_due_to_COVID_19_in_past_week AS FLOAT) as Percentage_Deaths
From [PortfolioProject].[dbo].[us_covid19_deaths]
Where Percentage_of_deaths_due_to_COVID_19_in_past_week <> 'Counts 1-9'
Order by CAST(Percentage_of_deaths_due_to_COVID_19_in_past_week AS FLOAT) DESC

-- OBSERVATION: Only 37 state territories were returned.
--              Of these 37 state territories, 7 reported having 0% death rates this past week.
--              The states with the highest perctengages of death were Missouri, New Jersey, and Massachusetts with 6%+ rates.
--              These states are not connected and does not indicate any cross-border contamination.

-- Let's see the Death Rate over the last 3 months to get a bigger picture into recent events
Select
    State_Territory,
    CAST(Death_Rate_per_100000_for_the_Past_3_Months AS FLOAT) as Percentage_Deaths_Last_3_Months
From [PortfolioProject].[dbo].[us_covid19_deaths]
Where Death_Rate_per_100000_for_the_Past_3_Months <> 'Counts 1-9'
Order by CAST(Death_Rate_per_100000_for_the_Past_3_Months AS FLOAT) DESC

-- OBSERVATION: The last 3 months shows that the top percentage of deaths were in Main, Wyoming, and West Virginia with 6.6-7.1% death rates.
--              These were not listed in our prior week discovery, so that indicates that their rates are decreasing as of late.

-- Let's see what the Total Deaths are for each state to see if these 3 states have remained fairly consistent over the trajectory of this dataset.
Select
    State_Territory,
    CAST(Total_Deaths AS INTEGER) as Total_Deaths
From [PortfolioProject].[dbo].[us_covid19_deaths]
Order by CAST(Total_Deaths AS INTEGER) DESC

-- OBSERVATION: We see that California, Texas, and New York have the highest Total Death count in the USA. 
--              This indicates that their rates have dipped over the last 3 months and in the prior week,
--              but the other states we previously noted having higher death rates recently were some of the
--              ones with the lowest total death counts. This shows that the number of deaths from cases are slowing down.


-- Let's see the percentage of people who died of Covid 19 out of the people who tested positive for Covid 19 by State
Select
    State_Territory,
    CAST((Percentage_of_deaths_due_to_COVID_19_in_past_week) AS FLOAT) / CAST((Test_volume_in_past_week) AS FLOAT) as Percentage_Positive_Tests_Resulting_In_Death
From [PortfolioProject].[dbo].[us_covid19_deaths]
Order by CAST((Total_Deaths) AS INTEGER) / CAST((Test_volume_in_past_week) AS INTEGER) DESC

-- OBSERVATION: What we can see is that California has an exceedingly large percentage of deaths out of all positive test cases.
--              California surpasses the national average of 13% with 41% of Positive Results ending in Death.
--              This indicates that further precautionary measures should be put in place to control the spread of the infection.

