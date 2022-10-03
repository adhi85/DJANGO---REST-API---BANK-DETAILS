import pandas as pd

from django.core.management.base import BaseCommand
from base.models import Bank
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = "Add data from excel "

    def handle(self, *args,**options):
        
        files = 'bank_branches.csv'
        df = pd.read_csv(files)
        
        engine = create_engine('sqlite:///db.sqlite3')

        df.to_sql(Bank._meta.db_table, if_exists='replace' ,con = engine, index=True)