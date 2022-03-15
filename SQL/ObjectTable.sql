-- Table: public.ObjectTable

-- DROP TABLE IF EXISTS public."ObjectTable";

CREATE TABLE IF NOT EXISTS public."ObjectTable"
(
    "ObjPk" character(20) COLLATE pg_catalog."default" NOT NULL,
    "Label" character(20) COLLATE pg_catalog."default" NOT NULL,
    "Possition" double precision NOT NULL,
    "SizePk" character(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "ObjectTable_pkey" PRIMARY KEY ("ObjPk"),
    CONSTRAINT "fk_Size" FOREIGN KEY ("SizePk")
        REFERENCES public."SizeTable" ("SizePk") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."ObjectTable"
    OWNER to root;