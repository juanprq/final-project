CREATE TABLE flavors (
	"id" INTEGER,
	"name" VARCHAR (50)
);

CREATE TABLE products (
	"id" INTEGER,
	"brand" VARCHAR(50),
	"category" VARCHAR(50)
);

CREATE TABLE clients (
	"id" INTEGER,
	"name" VARCHAR(50)
);

CREATE TABLE points_of_sale (
	"id" INTEGER,
	"client_id" INTEGER,
	"name" VARCHAR (70)
);

CREATE TABLE distributors (
	"id" INTEGER,
	"name" VARCHAR (50)
);

CREATE TABLE locations (
	"name" VARCHAR (50),
	"id" INTEGER
);

CREATE TABLE sales (
	"product_id" INTEGER,
	"date" DATE,
	"units" INTEGER,
	"devolution_units" INTEGER,
	"sale_amount" FLOAT,
	"sale_discount" FLOAT,
	"sale_devolution" FLOAT,
	"incentive" BOOLEAN,
	"office_id" INTEGER,
	"warehouse_id" INTEGER,
	"distributor_id" INTEGER,
	"point_of_sale_id" FLOAT,
	"flavor_id" INTEGER
);
