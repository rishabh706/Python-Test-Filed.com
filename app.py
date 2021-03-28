from flask import Flask,jsonify,request
import datetime
from sqlite import *
import sqlite3
import json

app=Flask(__name__)


# Creating Table in Database
table=Database()

table.create_table()

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

            elif audio_file_type=="podcast":
                unique_id = int(audio_meta_data["ID"])
                podcast_name = str(audio_meta_data["NAME"])
                podcast_duration = int(audio_meta_data["DURATION"])
                uploaded_time = datetime.datetime.now()
                host=str(audio_meta_data["HOST"])
                participants=list(audio_meta_data["PARTICIPANTS"])
                if len(participants)<=10:
                    participants=json.dumps(participants)
                    cursor.execute("INSERT INTO PODCAST(ID,NAME,DURATION,UPLOADED_TIME,HOST,PARTICIPANTS) VALUES(?,?,?,?,?,?)",
                                   (unique_id, podcast_name, podcast_duration, uploaded_time,host,participants))
                    cursor.close()
                else:
                    return jsonify("The request is invalid"),400

            else:
                unique_id = int(audio_meta_data["ID"])
                title = str(audio_meta_data["TITLE"])
                author = str(audio_meta_data["AUTHOR"])
                narrator=str(audio_meta_data["NARRATOR"])
                duration=int(audio_meta_data["DURATION"])
                uploaded_time = datetime.datetime.now()
                cursor.execute("INSERT INTO AUDIOBOOK(ID,TITLE,AUTHOR,NARRATOR,DURATION,UPLOADED_TIME) VALUES(?,?,?,?,?,?)",
                               (unique_id,title,author,narrator,duration,uploaded_time))
                cursor.close()


    return jsonify("STATUS OK"),200



if __name__=="__main__":
    app.run(debug=True)

