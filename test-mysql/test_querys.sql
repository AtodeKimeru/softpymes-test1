/* 
Teniendo en cuenta los archivos:
- softpymes_test.png
- softpymes_test.sql
Generar scripts que realicen las siguientes consultas:
*/

/* 1. Consultar los items que pertenezcan a la compañia con ID #3 (debe utilizar INNER JOIN) */

SELECT i.id, i.name, c.name AS color, cost, price
FROM items AS i
INNER JOIN companies AS cp
    ON i.companyId = cp.id
INNER JOIN colors AS c
    ON i.colorId = c.id
WHERE i.companyId = 3
GROUP BY i.id;

/* 2. Mostrar los items para los cuales su precio se encuentre en el rango 70000 a 90000*/

SELECT i.id, i.name, c.name AS color, cp.name AS company, cost, price
FROM items AS i
INNER JOIN companies AS cp
    ON i.companyId = cp.id
INNER JOIN colors AS c
    ON i.colorId = c.id
WHERE price BETWEEN 70000 AND 90000
GROUP BY i.id;

/* 3. Mostrar los items que en el nombre inicien con la letra "A" */

SELECT i.id, i.name, c.name AS color, cp.name AS company, cost, price
FROM items AS i
INNER JOIN companies AS cp
    ON i.companyId = cp.id
INNER JOIN colors AS c
    ON i.colorId = c.id
WHERE i.name LIKE 'A%'
GROUP BY i.id;

/* 4. Mostrar los items que tengan relacionado el color Rojo */

SELECT i.id, i.name, c.name AS color, cp.name AS company, cost, price
FROM items AS i
INNER JOIN companies AS cp
    ON i.companyId = cp.id
INNER JOIN colors AS c
    ON i.colorId = c.id
WHERE c.name = 'ROJO'
GROUP BY i.id;

/* 5. Se requiere asignar un precio a los items cuyo precio sea NULL, 
el precio a agregar debe ser calculado de la siguiente forma: costo del item + 10.000*/

UPDATE items
SET 
    price = cost + 10000
WHERE
    price IN (NULL, 0);

/* 6. Incrementar el precio de los items en un 20% */

UPDATE items SET price = price*1.2;

/* 7. Consultar los items que terminen en la letra "A" en el nombre, y anteponer la 
palabra "Nuevo" */

SELECT i.id, CONCAT('"Nuevo" ',i.name) AS name,
    c.name AS color, cp.name AS company, cost, price
FROM items AS i
INNER JOIN companies AS cp
    ON i.companyId = cp.id
INNER JOIN colors AS c
    ON i.colorId = c.id
WHERE i.name LIKE '%A'
GROUP BY i.id
ORDER BY i.id;

/* 8. Eliminar los items que pertenezcan a la compañía con ID #1 */

BEGIN;
DELETE FROM items WHERE companyID = 1;
COMMIT;

/* 9. Eliminar los items que tengan el costo menor a 10.000 */

BEGIN;
DELETE FROM items WHERE cost < 10000;
COMMIT;

/* 10. Cree una función que permita insertar registros en la tabla colores*/

DELIMITER $$
CREATE FUNCTION insertColor(code_color VARCHAR(3), color VARCHAR(25))
    RETURNS VARCHAR(14)
    DETERMINISTIC
    BEGIN
        INSERT INTO colors (code, `name`) VALUES (code_color, UPPER(color));
        RETURN 'register added';
    END $$
DELIMITER ;

/* 11. Eliminar todos los datos de la tabla colores */

ALTER TABLE items DROP FOREIGN KEY items_ibfk_1;
BEGIN;
TRUNCATE colors;
COMMIT;

/* 12. Agregar un campo llamado "description" en la tabla items, que permita ser NULL, 
y que tenga un máximo de 200 caracteres */

ALTER TABLE items ADD COLUMN `description` VARCHAR(200);