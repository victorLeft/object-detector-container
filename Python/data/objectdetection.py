#!/usr/bin/python
from ntpath import join
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import psycopg2
import requests
import random
import os
from sqlite3 import Timestamp
from tokenize import String
from turtle import position
from cvlib.object_detection import draw_bbox
from configparser import ConfigParser


#Read the Database conf for connection
def possitionsig(filename='database.ini', section='postgresql'):
    '''create a parser'''
    parser = ConfigParser()
    '''read possitionsig file'''
    parser.read(filename)
  
    '''get section, default to postgresql'''
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
  
    return db


'''Insert values into table'''
def sql_query(sql_query):
    try:
        # read connection parameters
        params = possitionsig()
  
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        conn.autocommit = True
          
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        print('Executting query:')
        print("    "+sql_query)
        cur.execute(sql_query)
        query_result = cur.fetchall()
        cur.close()
        return query_result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def last_row(tabla:str,columna:str):
    return sql_query("SELECT \""+columna+"\" from \""+tabla+"\" ORDER BY \""+columna+"\" DESC LIMIT 1;")

def insert_value(tabla:str,columns:list[str],values:list[str]):
    return sql_query("INSERT INTO  \""+tabla+"\" ("+",".join(columns)+") VALUES ("+",".join(values)+")")

def extractImage():
    cam = str(random.randint(10,1000))
    url = 'https://infocar.dgt.es/etraffic/data/camaras/'+cam+'.jpg'
    date = str(Timestamp.now())
    filename = cam+'_'+date
    r = requests.get(url, allow_redirects=True)
    open("input/"+filename+".jpg", 'wb').write(r.content)
    return filename

imagename = extractImage()
inputpath = "input/"+imagename+".jpg"
outputpath = "output/"+imagename+".png"
#Load image and detect the common objects within
im = cv2.imread(inputpath)
sizes, labels, possitions = cv.detect_common_objects(im)

print("CV detected")
output_image = draw_bbox(im, sizes, labels, possitions)

plt.imshow(output_image)
plt.imsave(outputpath,output_image, format='png')

if os.path.exists(inputpath):
  os.remove(inputpath)
else:
  print("The file does not exist")

last_obj = last_row("ObjectTable","ObjPk")
if last_obj:
    for raw in last_obj:
        obj = "".join(raw)
        n:int = int(obj[3:])+1
else:
    n = 1
       

last_size = last_row("ObjectTable","SizePk")
if last_size:
    for raw in last_size:
        obj = "".join(raw)
        r:int = int(obj[4:])+1
else:
    r = 1

filename = imagename.split("_")
insert_value("ImageTable",["\"Cam\"","\"Date\"","\"Path\""],[filename[0],"'"+filename[1]+"'","'"+outputpath+"'"])
for label, size, possition in zip(labels,sizes,possitions):
    obj_pk = "Obj"+str(n)
    size_pk = "Size"+str(r)
    insert_value("SizeTable",["\"SizePk\"","\"Top\"","\"Right\"","\"Bottom\"","\"Left\""],["'"+size_pk+"'",str(size[0]),str(size[1]),str(size[2]),str(size[3])])
    insert_value("ObjectTable",["\"ObjPk\"","\"Label\"","\"Possition\"","\"SizePk\""],["'"+obj_pk+"'","'"+label+"'","'"+str(possition)+"'","'"+size_pk+"'"])
    insert_value("ImageObjectTable",["\"Cam\"","\"Date\"","\"ObjPk\""],[filename[0],"'"+filename[1]+"'","'"+obj_pk+"'"])
    n = n+1
    r = r+1