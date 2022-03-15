-- Table: public.SizeTable

-- DROP TABLE IF EXISTS public."SizeTable";

CREATE TABLE IF NOT EXISTS public."SizeTable"
(
    "SizePk" character(20) COLLATE pg_catalog."default" NOT NULL,
    "Top" integer NOT NULL DEFAULT 0,
    "Right" integer NOT NULL DEFAULT 0,
    "Bottom" integer NOT NULL DEFAULT 0,
    "Left" integer NOT NULL DEFAULT 0,
    CONSTRAINT "Size_pkey" PRIMARY KEY ("SizePk")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."SizeTable"
    OWNER to root;