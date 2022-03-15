-- Table: public.ImageObjectTable

-- DROP TABLE IF EXISTS public."ImageObjectTable";

CREATE TABLE IF NOT EXISTS public."ImageObjectTable"
(
    "Cam" integer NOT NULL,
    "Date" character(20) COLLATE pg_catalog."default" NOT NULL,
    "ObjpK" character(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "ImageObjectTable_pk" PRIMARY KEY ("Cam", "Date", "ObjpK"),
    CONSTRAINT "fk_Image" FOREIGN KEY ("Cam", "Date")
        REFERENCES public."ImageTable" ("Cam", "Date") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "fk_Objeto" FOREIGN KEY ("ObjpK")
        REFERENCES public."ObjectTable" ("ObjPk") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."ImageObjectTable"
    OWNER to root;