import speech_recognition as sr
import pyttsx3
import pandas as pd
import mysql.connector as sql
import os
import pywhatkit
import datetime
import wikipedia

mysql_cn = sql.connect(host='localhost', port=3306, user='root', passwd='Sujith@123', db='project',
                       auth_plugin='mysql_native_password')
listner = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 120)
try:
    with sr.Microphone() as source:
        engine.say('please speak with me now')
        engine.runAndWait()
        print('speak')
        voice = listner.listen(source)
        command = listner.recognize_google(voice)
        command = command.lower()
        if 'what is your name' in command:
            engine.say('my name is bobb. ')
            engine.runAndWait()
        elif 'bob' in command:
            engine.say('things you spoke to me is..')
            engine.say(command)
            print(command)
            engine.runAndWait()
            if 'marry' in command:
                engine.say('i will complaint to head of the department about you')
                engine.runAndWait()
            elif 'who are you' in command:
                engine.say('my name is bobb')
                engine.say('your personalised voice assistant ')
                engine.runAndWait()
            if 'shut down' in command:
                os.system("shutdown /s /t 1")
            elif 'restart' in command:
                os.system("shutdown /r /t 1")
            elif 'logout' in command:
                os.system("shutdown -l")
            elif 'play' in command:
                command = command.replace('bob play', "")
                engine.say('playing' + command)
                pywhatkit.playonyt(command)
                engine.runAndWait()
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                engine.say(time)
                engine.runAndWait()
            elif 'info' in command:
                command = command.replace('bob give me info about', "")
                info = wikipedia.summary(command, 5)
                print(info)
                engine.say(info)
                engine.runAndWait()
            if 'student profile' in command:
                command= command.replace('bob student profile ',"")

                command=command.replace('',"")

                query = ("SELECT * FROM O16CSE WHERE ID = %s;" % command)
                df_mysql1 = pd.read_sql(query, con=mysql_cn)
                print(df_mysql1)
                engine.say('student details')
                query1 = ("SELECT ID FROM O16CSE WHERE ID = %s;" % command)
                df_mysql2 = pd.read_sql(query1, con=mysql_cn)
                query2 = ("SELECT NAME FROM O16CSE WHERE ID = %s;" % command)
                df_mysql3 = pd.read_sql(query2, con=mysql_cn)
                query3 = ("SELECT BRANCH FROM O16CSE WHERE ID = %s;" % command)
                df_mysql4 = pd.read_sql(query3, con=mysql_cn)
                engine.say(df_mysql2)
                engine.say(df_mysql3)
                engine.say(df_mysql4)
                engine.runAndWait()
            elif 'topper of cse' in command:
                topper = (
                    "SELECT ID,NAME,BRANCH FROM project.o16cse WHERE TOTAL = (SELECT MAX(TOTAL) FROM project.o16cse)")
                topper_marks = pd.read_sql(topper, con=mysql_cn)
                print(topper_marks)
                engine.say(topper_marks)
                engine.runAndWait()
            elif 'top attendance' in command:
                attd = (
                    "SELECT ID,NAME,BRANCH FROM project.o16cse WHERE ATTDANCE= (SELECT MAX(ATTDANCE) FROM project.o16cse)")
                m_attd = pd.read_sql(attd, con=mysql_cn)
                print(m_attd)
                engine.say(m_attd)
                engine.runAndWait()
            elif 'less attendance' in command:
                lattd = (
                    "SELECT ID,NAME,BRANCH FROM project.o16cse WHERE ATTDANCE= (SELECT MIN(ATTDANCE) FROM project.o16cse)")
                l_attd = pd.read_sql(lattd, con=mysql_cn)
                print(l_attd)
                engine.say(l_attd)
                engine.runAndWait()
            elif 'subject' in command:
                if 'less' in command:
                    if 'se' in command:
                        SEL = (
                            "SELECT ID,NAME,BRANCH FROM project.o16cse WHERE ATTDANCE= (SELECT MIN(SE) FROM project.o16cse)")
                        SEM = pd.read_sql(SEL, con=mysql_cn)
                        print(SEM)
                        engine.say(SEM)
                        engine.runAndWait()
                    elif 'cn' in command:
                        CNL = (
                            "SELECT ID,NAME,BRANCH FROM project.o16cse WHERE ATTDANCE= (SELECT MIN(CN) FROM project.o16cse)")
                        CNM = pd.read_sql(CNL, con=mysql_cn)
                        print(CNM)
                        engine.say(CNM)
                        engine.runAndWait()
                    elif 'dbms' in command:
                        DBMSL = (
                            "SELECT ID,NAME,BRANCH FROM project.o16cse WHERE ATTDANCE= (SELECT MIN(DBMS) FROM project.o16cse)")
                        DBMSM = pd.read_sql(DBMSL, con=mysql_cn)
                        print(DBMSM)
                        engine.say(DBMSM)
                        engine.runAndWait()
                elif 'top' in command:
                    if 'se' in command:
                        SEL = (
                            "SELECT ID,NAME,BRANCH FROM project.o16cse WHERE ATTDANCE= (SELECT MAX(SE) FROM project.o16cse)")
                        SEM = pd.read_sql(SEL, con=mysql_cn)
                        print(SEM)
                        engine.say(SEM)
                        engine.runAndWait()
                    elif 'cn' in command:
                        CNL = (
                            "SELECT ID,NAME,BRANCH FROM project.o16cse WHERE ATTDANCE= (SELECT MAX(CN) FROM project.o16cse)")
                        CNM = pd.read_sql(CNL, con=mysql_cn)
                        print(CNM)
                        engine.say(CNM)
                        engine.runAndWait()
                    elif 'dbms' in command:
                        DBMSL = (
                            "SELECT ID,NAME,BRANCH FROM project.o16cse WHERE ATTDANCE= (SELECT MAX(DBMS) FROM project.o16cse)")
                        DBMSM = pd.read_sql(DBMSL, con=mysql_cn)
                        print(DBMSM)
                        engine.say(DBMSM)
                        engine.runAndWait()




except:

    engine.say('Some thing went Wrong with system your program is terminating')
