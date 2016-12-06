#!/usr/bin/env python

"""
Script to dump strains from labDB into excel file
"""
import pandas as pd
import peewee
import datetime
import sys
import labstocks
import os
import time


def get_strains_as_data_frame():
	"""
	convert all data in strains table in database into pandas dataframe
	"""
	columns = [ 'eky', 'name_', 'date_', 'genotype', 'phenotype', 'growth_req', 'original_no', 'comments', 'general_background', 'author', 'cytoplasmic_character',  'his3', 'ade2', 'ho_', 'leu2', 'lys2', 'met15', 'mating_type', 'obtained_by', 'parental_strain',  'plasmid', 'reference_', 'sgd', 'trp1', 'ura3', 'clone_no', 'labbook_reference', 'locus1', 'locus2', 'locus3', 'storage_box' ]
	df = pd.DataFrame(columns= columns)
	for row in labstocks.Strains.select().execute():	
		values = [row.__getattribute__(attr) for attr in columns]
		values = [v.get_id() if isinstance(v, labstocks.BaseModel) else v for v in values]
		df.loc[len(df)] = values
	return df

if __name__ == '__main__':
	pwd = raw_input("Enter password for mysql database: ")
	labstocks.database.connect_kwargs['passwd'] = pwd
	# connect DB
	labstocks.database.connect()

	df = get_strains_as_data_frame()
	f_name = 'yeast_strains_%s.xls' % time.strftime("%H%M_%d%h%y")
	df.to_excel(f_name)
	print 'Strain data written to %s' % f_name