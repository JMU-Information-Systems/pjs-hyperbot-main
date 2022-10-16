# EXTRACT data from Logger DB
# coding=utf-8
from datetime import datetime
import sqlite3
import shutil
import os
from pathlib import Path
from tarfile import ENCODING
import psycopg2
import json


def main():
    #Reading the information about a record (userid) from postgres into a cursor
    sqlread='''WITH al AS (
           SELECT DISTINCT applog.id, applog.userid, applog.applicationname, applog.windowtitle, applog.url, applog.analysisid
           FROM processanalyzer.applog WHERE applog.applicationname IS NOT NULL AND applog.applicationname::text <> ''::text
           )
           SELECT DISTINCT uilog.clickpositionx, uilog.clickpositiony, uilog.userid AS uilog_userid,
                  uilog.appid AS uilog_appid, uilog.automationid, uilog.name, uilog.type, uilog.eventtype,
                  uilog.positionx, uilog.positiony, uilog.width, uilog.height, uilog."timestamp" AS eventtime,
                  uilog.analysisid, uilog.relativeclickx, uilog.relativeclicky, 0, uilog.unifiedlabel,
                  uilog.value, uilog.elementclass, al.userid AS applog_userid, al.applicationname, al.windowtitle, al.url
           FROM processanalyzer.uilog
           LEFT JOIN al ON uilog.userid::text = al.userid::text AND uilog.appid = al.id AND uilog.analysisid = al.analysisid
           WHERE uilog.userid='%s' 
           ORDER BY uilog."timestamp"; '''
    sqlinsert='''INSERT INTO logger (clickpositionx, clickpositiony, u_userid, u_appid, automationid, u_name, u_type, u_eventtype,
    positionx, positiony, u_width, u_height, eventtime, analysisid, relativeclickx, relativeclicky, u_time, unifiedlabel, u_value, elementclass, 
    a_userid, a_applicationname, a_windowtitle, a_url) VALUES
    (''' 

    #read json file for extraction of userid and intallationtime (for filename)
    jfile="C:\\ProgramData\\RecorderService\\Settings\\applicationsettings.json"

    #Reading the UserID and installation time
    with open(jfile, "r") as json_datei:
        json_liste= json.load(json_datei)
        userid=(str(json_liste['AnonymousUserId']))
        filename=str(json_liste['InstallationTimeUtc']).replace('-','').replace(':','').replace('T','_')[:15]    
    sqlread = sqlread.replace('%s',userid)
    fpath=os.path.dirname(__file__)
    sfile=Path(fpath + '\\' + 'rpatemplate.sqlite3') #templatedb in sqlite (source)
    dfile=Path(fpath + '\\' + filename + '.sqlite3') #Recordingdb in sqlite (target)
    shutil.copy(sfile,dfile)

    try:
        #Connect to postgres
        conp=psycopg2.connect(
            host="132.187.102.173", #Host-IP
            database="processanalyzer", #name of DB
            user="postgres", #user
            password="postgres") #password
        cursor=conp.cursor()
    except psycopg2.Error as error:  #Error handling
        print("DB-Error ", error)
        exit

    try:
        #connect to sqlite3
        cons=sqlite3.connect(dfile,check_same_thread=False)
        curs=cons.cursor()
    except sqlite3.Error as e:
        print(e)
        exit

    #Filling the cursor from postgres of the recording
    cursor.execute(sqlread) 

    #Inserting the rows from the cursor into the sqlitedb(record)
    row = cursor.fetchone() 
    while row:
        sqlcmd=sqlinsert
        for i in range(24):
            if i > 0:
                sqlcmd=sqlcmd+','
            if str(row[i]).isnumeric():
                sqlcmd=sqlcmd+str(row[i])
            else:
                sqlcmd=sqlcmd+'\''+str(row[i])+'\'' 
        sqlcmd=sqlcmd+')'
        try:
            curs.execute(sqlcmd)
            cons.commit()
            curs.close
        except sqlite3.Error as e:
            print(e)
            exit
        row = cursor.fetchone()

    cursor.close

if __name__ == '__main__':
    main()