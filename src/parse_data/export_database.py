#!/usr/bin/env python

import pandas as pd
import numpy as np
import labstocks
import peewee
import json
import time

class LabDBExporter:
	def __init__(self, password, specify_tables):
		labstocks.database.connect_kwargs['passwd'] = password
		labstocks.database.connect()
		self._specify_tables = specify_tables

	def get_table_as_pandas(self, table_name, full=False):
		query = getattr(labstocks, table_name).select().execute()
		if full:
			column_names = [cm.name for cm in query.column_meta]
		else:
			column_names = self._specify_tables[table_name]
		for pos, cm in enumerate(query.column_meta):
			if isinstance(cm, peewee.PrimaryKeyField):
				column_names[column_names.index(cm.name)] = cm.name.upper()
		df = pd.DataFrame(columns=column_names)
		for row in query:
			values = [row.__getattribute__(attr.lower()) for attr in column_names]
			values = [v.get_id() if isinstance(v, labstocks.BaseModel) else v for v in values]
			df.loc[len(df)] = values
		return df

	def write_table_as_excel(self, table_name, full=False):
		df = self.get_table_as_pandas(table_name, full)
		f_name = '%s_%s.xls' %(table_name, time.strftime("%H%M_%d%h%y"))
		df.to_excel(f_name)
		print 'Table %s exported to %s.' %(table_name, f_name)

	def write_table_as_text(self, table_name, full=False):
		df = self.get_table_as_pandas(table_name, full)
		txt = u''
		for index, row in df.iterrows():
			for key in df:
				if row[key] is None or pd.isnull(row[key]):
					elem = ''
				elif isinstance(row[key], float):
					elem = int(row[key])
				else:
					elem = row[key]
				txt += key + ': ' + unicode(elem) + '\n'
			txt += '\n'
		f_name = '%s_%s.txt' %(table_name, time.strftime("%H%M_%d%h%y"))
		with open(f_name, 'w') as f:
			f.write(txt.encode('utf8'))
		print 'Table %s exported to %s' %(table_name, f_name)

	def write_all_tables(self, kind='text', full=False):
		if not kind in ['text', 'excel']:
			raise Exception('Unkown export type. %s' %kind)
		for table_name in self._specify_tables.keys():
			getattr(self, 'write_table_as_' + kind)(table_name, full)

	@staticmethod
	def _df_float_to_int(df):
		""" convert all float columns in a pandas dataframe to int """
		positions_to_cast = [pos for (pos, dtype) in enumerate(df.dtypes) if dtype==float]
		print df.dtypes
		print df.columns
		print positions_to_cast
		for pos in positions_to_cast:
			print df.iloc[:, pos]
			df.iloc[:, pos] = df.iloc[:, pos].astype(np.int)
		return df



if __name__ == '__main__':
	import optparse
	import sys

	parser = optparse.OptionParser(usage='usage: %prog [options]')

	parser.add_option('-k', '--kind', metavar='kind', default='text',
                      dest='kind', help='export type: excel or text (default)')
	parser.add_option('-d', '--tabledef', metavar='tabledef', default='table_columns_to_export.json',
                      dest='tabledef', help='path to json file defining tables and columns to export (default: table_columns_to_export.json')
	parser.add_option('-t', '--table', metavar='table', default='all',
                     dest='table', help='specify name of a single table to export. (default is export of all tables mentioned in tabledef file.')
	parser.add_option('-a', '--all_columns', action='store_true', default=False,
                     dest='all_columns', help='export all columns instead of the ones specified in tabledef file')



	(options,args) = parser.parse_args()

	with open(options.tabledef, 'r') as f:
		tabledef_file = json.load(f)

	pwd = raw_input("Enter password for mysql database: ")
	ldb_exporter = LabDBExporter(pwd, tabledef_file)

	if options.table == 'all':
		ldb_exporter.write_all_tables(kind=options.kind, full=options.all_columns)
	else:
		if options.kind == 'text':
			ldb_exporter.write_table_as_text(options.table, full=options.all_columns)
		else:
			ldb_exporter.write_table_as_excel(options.table, full=options.all_columns)