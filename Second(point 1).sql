ALTER TABLE Departament RENAME COLUMN name TO name_dep;
ALTER TABLE

SELECT name_dep
FROM (SELECT dp.id, dp.name_dep, p.id_dep
		FROM Departament dp
		INNER JOIN Personal p ON p.id_dep=dp.id)
WHERE name_dep=(SELECT MAX(COUNT(id_dep) FROM Personal)