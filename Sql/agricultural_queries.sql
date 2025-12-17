1.Year-wise Trend of Rice Production Across States (Top 3)
--------------------------------------------------------------------

SELECT
    Year,
    State_Name,
    SUM(RICE_PRODUCTION) AS Total_Rice_Production
FROM agricultural_data
WHERE State_Name IN(
    SELECT State_Name
    FROM agricultural_data
    GROUP BY State_Name
    ORDER BY SUM(RICE_PRODUCTION) DESC
    LIMIT 3
)    

GROUP BY YEAR, State_Name
ORDER BY YEAR;


2.Top 5 Districts by Wheat Yield Increase  (Last 5 Years)
------------------------------------------------------------------

SELECT
    Dist_Name,
    (MAX(WHEAT_YIELD) - MIN (WHEAT_YIELD)) AS Yield_Increase
FROM agricultural_data
WHERE Year >= (SELECT MAX(Year) - 5 FROM agricultural_data)
GROUP BY Dist_Name
ORDER BY Yield_Increase DESC 
LIMIT 5;


3.States with the Highest Growth in Oilseed Production (5-Year Growth)
-------------------------------------------------------------------------

SELECT
    State_Name,
    (MAX(OILSEEDS_PRODUCTION) - MIN (OILSEEDS_PRODUCTION)) AS
Growth
FROM agricultural_data
WHERE Year >= (SELECT MAX(Year) - 5 FROM agricultural_data)
GROUP BY State_Name
ORDER BY Growth DESC;


4.District-wise Area VS Production (Rice, Wheat, and Maize)
--------------------------------------------------------------
SELECT
    Dist_Name,
     SUM(RICE_AREA + WHEAT_AREA + MAIZE_AREA) AS Total_Area,
      SUM(RICE_PRODUCTION + WHEAT_PRODUCTION + MAIZE_PRODUCTION) AS Total_Production
FROM agricultural_data
GROUP BY Dist_Name;


5.Yearly Cotton Production Growth (Top 5 States)
-----------------------------------------------------------
SELECT
    Year,
    State_Name,
    SUM(COTTON_PRODUCTION) AS Total_Cotton_Production
FROM agricultural_data
WHERE  State_Name IN (
    SELECT State_Name
    FROM agricultural_data
    GROUP BY State_Name
    ORDER BY SUM(COTTON_PRODUCTION) DESC
    LIMIT 5
)
GROUP BY Year, State_Name
ORDER BY Year;


6.Districts with the Highest Groundnut Production in 2017
-----------------------------------------------------------------
SELECT
    Dist_Name,
     SUM(RGROUNDNUT_PRODUCTION) AS Total_Groundnut
FROM agricultural_data
WHERE Year = 2017
GROUP BY Dist_Name
ORDER BY Total_Groundnut DESC;


7.Annual Average Maize Yield Across All States
----------------------------------------------------
SELECT
    Year,
    AVG(MAIZE_YIELD) AS Avg_Maize_Yield
FROM agricultural_data
GROUP BY Year
ORDER BY Year;


8.Total Area Cultivated for Oilseeds in Each State
-------------------------------------------------------
SELECT
    State_Name,
    SUM(OILSEEDS_AREA) AS Total_Oilseed_Area
FROM agricultural_data
GROUP BY State_Name
ORDER BY Total_Oilseed_Area DESC;


9.Districts with the Highest Rice Yield
----------------------------------------------
SELECT
    Dist_Name,
    MAX(RICE_YIELD) AS Highest_Rice_Yield
FROM agricultural_data
GROUP BY Dist_Name
ORDER BY Highest_Rice_Yield DESC;


10.Compare Wheat vs Rice Production (Top 5 States - Last 10 Years)
------------------------------------------------------------------------
SELECT
    Year,
    State_Name,
    SUM(RICE_PRODUCTION) AS Rice_Production,
    SUM(WHEAT_PRODUCTION) AS Wheat_Production
FROM agricultural_data
WHERE State_Name IN(
    SELECT State_Name
    FROM agricultural_data
    GROUP BY State_Name
    ORDER BY SUM(RICE_PRODUCTION + WHEAT_PRODUCTION) DESC
    LIMIT 5
)    
AND Year >= (SELECT MAX(Year) - 10 FROM agricultural_data)
GROUP BY YEAR, State_Name
ORDER BY YEAR;

















