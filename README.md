# Python-Test-Filed.com

# Instructions For Using the API

1.Clone the respository using ```git clone https://github.com/rishabh706/Python-Test-Filed.com.git```

2.cd Python-Test-Filed.com

3.Start the Flask server using ```python3 app.py```

4.To insert data into the table enter the following command in the terminal ```curl -X POST -H "Content-Type: application/json" -d '{"audioFileType":"song","audioFileMetadata":{"ID":"1","NAME":"song","DURATION":"2"}}' http://127.0.0.1:5000/create```

5.To update data into the table enter the following command in the terminal ```curl -X POST -H "Content-Type: application/json" -d '{"audioFileType":"song","audioFileMetadata":{"NAME":"song2","DURATION":"4"}}' http://127.0.0.1:5000/update/song/1```

6.To delete data from the table enter the following command in the terminal ```curl -X POST -H  http://127.0.0.1:5000/delete/song/1```

7.To get data from table enter the following commands ```

curl -X POST -H "Content-Type: application/json"  http://127.0.0.1:5000/get/song/
curl -X POST -H "Content-Type: application/json"  http://127.0.0.1:5000/get/song/1

```

# Instruction for Testing the Table

1.To get all the records from the specific table enter the following command in the terminal ```python3 sqlite.py song```

2.To list all the table names in the database enter the following command in the terminal ```python3 sqlite.py```





