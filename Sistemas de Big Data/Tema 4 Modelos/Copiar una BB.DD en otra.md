### Copiar una BB.DD en otra.

Para copiar una base de datos a otra con un nombre distinto en MySQL, hay varias formas de hacerlo dependiendo de tus herramientas y requisitos. A continuación, te detallo las opciones más comunes:

---

### **1. Usando `mysqldump` en línea de comandos**
Esta es una de las formas más comunes y eficientes. Implica exportar la base de datos original a un archivo y luego importarlo en una nueva base de datos.

#### Paso 1: Exportar la base de datos original
Usa el comando `mysqldump` para crear un archivo SQL con la estructura y los datos de la base de datos original:

```bash
mysqldump -u [usuario] -p [nombre_base_origen] > backup.sql
```

Por ejemplo:
```bash
mysqldump -u root -p sakila > sakila_backup.sql
```

#### Paso 2: Crear la nueva base de datos
Entra en MySQL y crea una base de datos vacía con el nuevo nombre:

```sql
CREATE DATABASE [nombre_base_nueva];
```

Por ejemplo:
```sql
CREATE DATABASE sakila_copy;
```

#### Paso 3: Importar los datos a la nueva base de datos
Usa el archivo SQL exportado para poblar la nueva base de datos:

```bash
mysql -u [usuario] -p [nombre_base_nueva] < backup.sql
```

Por ejemplo:
```bash
mysql -u root -p sakila_copy < sakila_backup.sql
```

---

### **2. Usando un script SQL**
Si estás trabajando desde una herramienta como MySQL Workbench o cualquier cliente SQL, puedes clonar la base de datos directamente escribiendo consultas.

#### Paso 1: Crear la nueva base de datos
```sql
CREATE DATABASE [nombre_base_nueva];
```

Por ejemplo:
```sql
CREATE DATABASE sakila_copy;
```

#### Paso 2: Copiar tablas y datos
Por cada tabla en la base de datos original, puedes usar `CREATE TABLE ... AS` para copiar su estructura y datos:

```sql
USE [nombre_base_origen];

SET @original_db = '[nombre_base_origen]';
SET @new_db = '[nombre_base_nueva]';

-- Obtener lista de tablas
SET group_concat_max_len = 32768;

SELECT GROUP_CONCAT(
    CONCAT('CREATE TABLE ', @new_db, '.', table_name, ' LIKE ', @original_db, '.', table_name, '; ',
           'INSERT INTO ', @new_db, '.', table_name, ' SELECT * FROM ', @original_db, '.', table_name, ';')
) INTO @copy_query
FROM information_schema.tables
WHERE table_schema = @original_db;

-- Ejecutar el script generado
PREPARE stmt FROM @copy_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

Este método genera y ejecuta dinámicamente las consultas para copiar todas las tablas y sus datos.

---

### **3. Usando herramientas gráficas**
Si prefieres una herramienta con interfaz gráfica, puedes usar **MySQL Workbench** o cualquier cliente gráfico de MySQL.

1. **Exportar e importar con Workbench:**
   - Haz clic derecho en la base de datos que quieres copiar.
   - Selecciona `Data Export`.
   - Exporta la base de datos a un archivo SQL.
   - Ve al menú `Data Import/Restore`.
   - Importa el archivo SQL a la nueva base de datos.

2. **Clonar directamente con Workbench:**
   - Haz clic derecho en la base de datos y selecciona `Copy Database`.
   - Elige la base de datos de destino con el nuevo nombre.

---

### Consideraciones
1. **Privilegios:** Asegúrate de que tu usuario de MySQL tenga los permisos adecuados (`SELECT`, `CREATE`, `INSERT`, etc.).
2. **Espacio:** El tamaño de la base de datos puede influir en el tiempo que tome la copia, especialmente para bases grandes.
3. **Integridad:** Si tienes claves foráneas, índices, o triggers, asegúrate de que la copia sea consistente.

¿Quieres que te ayude a crear un script SQL para tu caso específico?

--------------------------------
If you enjoy using this GPT and need something more powerful, want to be a beta tester for new versions, or just wish to support us, please check out our new [SQL Expert PRO GPT](https://chatgpt.com/g/g-6740a711568c819189f561c15e0707e6-beta-sql-expert-pro) with a monthly subscription and follow GPT creator profile on LinkedIn [https://linkedin.com/in/khanukov/](https://linkedin.com/in/khanukov/)