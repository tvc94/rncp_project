USE watches_website;

SELECT * from Watches;

-- Query 1

SELECT AVG(Price) from Watches;

-- Query 2

SELECT w.Brand, w.Model_Name, w.Model, w.Price
FROM Watches w
JOIN Special_Edition se ON w.Special_Edition_ID = se.ID
WHERE se.Description = 'Special Edition';

-- Query 3
SELECT 
    w.Brand, 
    w.Model_Name, 
    w.Model, 
    w.Price, 
    se.Description AS Special_Edition_Status, 
    av.Description AS Availability_Status, 
    cpo.Description AS Certified_Pre_Owned_Status
FROM Watches w
JOIN Special_Edition se ON w.Special_Edition_ID = se.ID
JOIN Availability av ON w.Availability_ID = av.ID
JOIN Certified_Pre_Owned cpo ON w.Certified_Pre_Owned_ID = cpo.ID
WHERE w.Brand = 'Cartier';

-- Query 4
SELECT AVG(w.Price) AS Mean_Price
FROM Watches w
WHERE w.Brand = 'Cartier';


-- Query 5
SELECT 
    w.Brand, 
    w.Model_Name, 
    w.Model, 
    w.Price, 
    av.Description AS Availability_Status,
    COUNT(w.Brand) AS NumberOfAvailableWatches
FROM Watches AS w
JOIN Availability av ON w.Availability_ID = av.ID
WHERE av.Description = 'In Stock'
GROUP BY w.Brand, w.Model_Name, w.Model, w.Price, av.Description;



