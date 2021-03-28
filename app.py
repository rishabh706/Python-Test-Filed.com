from flask import Flask,jsonify,request
import datetime
from sqlite import *
import sqlite3

app=Flask(__name__)


# Creating Table in Database
create_table()

# table_names, table_information = list_tables()

@app.route("/create",methods=['GET','POST'])
def create():

    with sqlite3.connect('database.db') as con:

        cursor=con.cursor()

        if request.method=="POST":
            data=request.get_json()
            audio_file_type=data["audioFileType"]
            audio_meta_data=data["audioFileMetadata"]

            if audio_file_type=="song":
                unique_id=int(audio_meta_data["ID"])
                song_name=str(audio_meta_data["NAME"])
                song_duration=int(audio_meta_data["DURATION"])
                uploaded_time=datetime.datetime.now()
                cursor.execute("INSERT INTO SONG(ID,NAME,DURATION,UPLOADED_TIME) VALUES(?,?,?,?)",(unique_id,song_name,song_duration,uploaded_time))
                cursor.close()

    return jsonify(200)


if __name__=="__main__":
    app.run(debug=True)

