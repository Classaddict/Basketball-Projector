import pandas as pd
import csv
import re

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
            age=line[1]
            minutes_pg=line[3]
            pra=float(line[4])+float(line[5])+float(line[8])
            stock=float(line[6])+float(line[7])
            sql="""
                INSERT INTO FAKE_PLAYER_DATA VALUES()
            """
        print(year)
        print(age)
        print(minutes_pg)
        print(pra)
        print(stock)
            

if __name__=="__main__":
    CSV_to_sql.main()
