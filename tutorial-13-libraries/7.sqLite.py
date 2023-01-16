import json
import sqlite3
from pathlib import Path

products = json.loads(Path("ecommerce/products.json").read_text())
# print(products)

# --------writing to a database
with sqlite3.connect("products-db.sqlite3") as connection:
    command = "INSERT INTO Products VALUES()"

    for product in products:
        connection.execute(command, tuple(product.values()))

    connection.commit()
