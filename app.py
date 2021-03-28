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

        try:

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
                        return jsonify("Any error: 500 internal server error"),500

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


            return jsonify("Action is successful: 200 OK"),200

        except Exception as e:

            return jsonify("Any error: 500 internal server error"),500

@app.route("/delete/<audioFileType>/<audioFileID>",methods=['GET','POST'])
def delete(audioFileType,audioFileID):

    with sqlite3.connect('database.db') as con:

        cursor=con.cursor()

        if request.method=="POST":
            id=int(audioFileID)

            if audioFileType=="song":
                print('executed')
                cursor.execute("DELETE FROM SONG WHERE ID=(?)",(id,))
                con.commit()



            elif audioFileType=="podcast":
                cursor.execute("DELETE FROM PODCAST WHERE ID=(?)", (id,))
                con.commit()

            else:
                cursor.execute("DELETE FROM AUDIOBOOK WHERE ID=(?)", (id,))
                con.commit()

        cursor.close()

    return jsonify("Action is successful: 200 OK"),200

@app.route("/update/<audioFileType>/<audioFileID>",methods=['GET','POST'])
def update(audioFileType,audioFileID):

    with sqlite3.connect('database.db') as con:

        cursor=con.cursor()

        if request.method=="POST":
            data=request.get_json()
            audio_meta_data = data["audioFileMetadata"]
            id = int(audioFileID)

            if audioFileType=="song":
                song_name = str(audio_meta_data["NAME"])
                song_duration = int(audio_meta_data["DURATION"])
                uploaded_time = datetime.datetime.now()
                cursor.execute("UPDATE SONG SET NAME=(?),DURATION=(?),UPLOADED_TIME=(?)",
                               (song_name, song_duration, uploaded_time))
                cursor.close()

            elif audioFileType=="podcast":
                podcast_name = str(audio_meta_data["NAME"])
                podcast_duration = int(audio_meta_data["DURATION"])
                uploaded_time = datetime.datetime.now()
                host = str(audio_meta_data["HOST"])
                participants = list(audio_meta_data["PARTICIPANTS"])
                if len(participants) <= 10:
                    participants = json.dumps(participants)
                    cursor.execute(
                        "UPDATE PODCAST SET NAME=(?),DURATION=(?),UPLOADED_TIME=(?),HOST=(?),PARTICIPANTS=(?)",
                        (podcast_name, podcast_duration, uploaded_time, host, participants))
                    cursor.close()
                else:
                    return jsonify("Any error: 500 internal server error"), 500

            else:
                title = str(audio_meta_data["TITLE"])
                author = str(audio_meta_data["AUTHOR"])
                narrator = str(audio_meta_data["NARRATOR"])
                duration = int(audio_meta_data["DURATION"])
                uploaded_time = datetime.datetime.now()
                cursor.execute(
                    "UPDATE AUDIOBOOK SET TITLE=(?),AUTHOR=(?),NARRATOR=(?),DURATION=(?),UPLOADED_TIME=(?)",
                    (title, author, narrator, duration, uploaded_time))
                cursor.close()

    return jsonify("Action is successful: 200 OK"),200


if __name__=="__main__":
    app.run(debug=True)

