-- Best Employees by Revenue and Orders Handled

SELECT e.FirstName || ' ' || e.LastName AS Employee,
       CONCAT(ROUND(SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)), 2), '$') AS Revenue,
       COUNT(DISTINCT o.OrderID) AS 'Orders Handled'
FROM Employees e
JOIN Orders o ON e.EmployeeID = o.EmployeeID
JOIN OrderDetails od ON o.OrderID = od.OrderID
GROUP BY Employee
ORDER BY Revenue DESC;