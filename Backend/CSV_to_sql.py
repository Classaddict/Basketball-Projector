import pandas as pd
import csv
import re
from server import *
#TO DO: add controller to get player ID so it doesn't need to be hardcoded. 
class CSV_to_sql:
    @staticmethod
    def parse_line(line):
        line=line.strip()
        if not line:
            return None
        fields=line.split("\t")
        return fields

    @staticmethod
    def main():
        sql="""
            INSERT INTO FAKE_PLAYER_DATA VALUES();
        """
        with open("Docs/nash.csv",encoding="utf-8") as f:
            lines=f.readlines()
        rows=[CSV_to_sql.parse_line(line) for line in lines[:]]
        rows=[r for r in rows if r is not None]
        headers=rows[0]
        rows.pop(0)
        print(headers)
        for line in rows:
            line=line[0]
            line=line.split(",")
            year=line[0]
            year=int(year[:4])
            age=line[1]
            minutes_pg=line[3]
            pra=round(float(line[4])+float(line[5])+float(line[8]),2)
            stock=round(float(line[6])+float(line[7]),2)
            try:
                player_eff=float(line[9])
                usg=float(line[10])
                ts=float(line[11])
                drtg=float(line[12])
            except Exception as e:
                player_eff=0
                usg=0
            
            sql="""
                INSERT INTO PLAYER_DATA(player,season,age,pra,stock,ts,useage,mins,per,drtg)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            exec_commit(sql,(1,year,age,pra,stock,ts,usg,minutes_pg,player_eff,drtg))
            

if __name__=="__main__":
    CSV_to_sql.main()
