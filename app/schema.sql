DROP TABLE IF EXISTS propiedades;
CREATE TABLE "propiedades" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"titulo"	TEXT NOT NULL,
	"direccion"	TEXT NOT NULL,
	"documentacion"	TEXT,
	"servicios"	TEXT,
	"medidas"	TEXT,
	"ubicacion"	TEXT
);