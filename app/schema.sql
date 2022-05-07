DROP TABLE IF EXISTS propiedades;
DROP TABLE IF EXISTS imagenes;
CREATE TABLE "propiedades" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"whq"	TEXT NOT NULL,
	"nombre"	TEXT NOT NULL,
	"titulo"	TEXT NOT NULL,
	"frase"	TEXT NOT NULL,
	"direccion"	TEXT NOT NULL,
	"estado" TEXT NOT NULL,
	"documentos"	TEXT,
	"servicios"	TEXT,
	"medidas"	TEXT,
	"construccion"	TEXT,
	"lugares" TEXT,
	"latitud"	TEXT,
	"longitud"	TEXT
);

CREATE TABLE "imagenes" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"id_propiedad"	INTEGER NOT NULL,
	"url"	TEXT NOT NULL,
	"titulo" TEXT NOT NULL,
	"info" TEXT NULL
);