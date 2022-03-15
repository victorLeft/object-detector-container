-- Table: public.ImageTable

-- DROP TABLE IF EXISTS public."ImageTable";

CREATE TABLE IF NOT EXISTS public."ImageTable"
(
    "Cam" integer NOT NULL,
    "Date" character(20) COLLATE pg_catalog."default" NOT NULL,
    "Path" character varying(250) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "ImageTable_pk" PRIMARY KEY ("Cam", "Date")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."ImageTable"
    OWNER to root;