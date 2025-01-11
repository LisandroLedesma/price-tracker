CREATE TABLE Ecommerce (
    id_ecommerce SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Products (
    id_product SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    image_url VARCHAR(255),
    id_user VARCHAR(255) NOT NULL,
    id_ecommerce INT NOT NULL
    FOREIGN KEY (id_ecommerce) REFERENCES Ecommerce(id_ecommerce)
);

CREATE TABLE PriceHistory (
    id_history SERIAL PRIMARY KEY,
    id_product INT NOT NULL,
    query_date TIMESTAMP NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    is_offer BOOLEAN NOT NULL,
    FOREIGN KEY (id_product) REFERENCES Products(id_product)
);

CREATE TABLE Tracker (
    id_tracker SERIAL PRIMARY KEY,
    id_product INT NOT NULL,
    execution_date TIMESTAMP NOT NULL,
    is_active BOOLEAN NOT NULL,
    FOREIGN KEY (id_product) REFERENCES Products(id_product)
);
