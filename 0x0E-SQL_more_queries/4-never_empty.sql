-- creates table with specific description
-- creates the table where id defaults to 1
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1,
  name VARCHAR(256)
  );
