-- SEA Instructores UNA BASE DE DATOS, CON SUS RESPECTIVOS DATOS Y COLUMNAS:

SELECT * FROM Instructores;
SELECT Id, Name, Age, Status FROM Instructores; --Recibir todos los datos, o ciertas columnas.

SELECT * FROM Instructores WHERE Name='Juan';
SELECT * FROM Instructores WHERE Age<25;
SELECT * FROM Instructores WHERE Status<>'Inactive'; -- Recibir todos los datos con restricciones.

SELECT COUNT(*) FROM Instructores WHERE Age<25; --Contar numeros de fila.

SELECT DISTINCT Name FROM Instructores; --Devuelve los valores unicos.

SELECT * FROM Instructores LIMIT 5;
SELECT * FROM Instructores LIMIT 5 OFFSET 3; --Limite de filas, y para "saltear" cierta cantidad.

INSERT INTO Instructores
(Id, Name, Age, Status)
VALUES(NewId, 'Agustin', 20, 'Active'),(NewId, 'Agustin1', 21, 'Active'); --Insetar 1 o mas filas.

UPDATE Instructores
SET Status='Inactive'
WHERE Name='Agustin'; --Actualizar filas.

DELETE FROM Instructores
WHERE Status='Inactive' --Borra todas las coincidencias. 