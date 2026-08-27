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
        with open("Docs/nash.csv",encoding="utf-8") as f:
            lines=f.readline()
        rows=[CSV_to_sql.parse_line(line) for line in lines[:]]
        rows=[r for r in rows if r is not None]
        print(lines)

if __name__=="__main__":
    CSV_to_sql.main()
