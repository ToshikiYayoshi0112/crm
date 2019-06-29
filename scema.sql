--customersテーブルが既存の場合にさくじょする
DROP TABLE IF EXISTS customers;
--customersテーブルをつくる
CREATE TABLE customers (
    name TEXT,
    age INTEGER
);

INSERT INTO customers
    (name, age)
VALUES
    ('Bob', 15),
    ('Tom', 57),
    ('Ken', 73)
;
