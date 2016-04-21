#!/usr/bin/env python

"""
Script to parse yeast and e.coli stocks, oligos and plasmids and to insert them into labstocks_db
"""
import pandas as pd
import peewee
import datetime
import sys
import labstocks
import os



def clean_db():
    # delete demo entries from DB
    labstocks.Strains.delete().execute()
    labstocks.PlFeatures.delete().execute()
    labstocks.Oligos.delete().execute()
    labstocks.EcoliStocks.delete().execute()
    labstocks.Plasmids.delete().execute()
    labstocks.LabMembers.delete().execute()
#    labstocks.EcoliStocks.delete().execute()

def create_users( user_list ):
    # create users
    for user in user_list:
        try:
            labstocks.LabMembers.insert( id=user ).execute()
        except peewee.IntegrityError, e:
            print e

def parse_date( date_string ):
    if pd.isnull(date_string):
        return None
    format_strings = [ '%d.%m.%y', '%d.%m.%Y', '%m/%d/%y', '%m/%d/%Y', '%m/%Y', '%m/%y', '%d-%m-%y', '%d-%m-%Y', '%d%m%y', '%d%m%Y' ]
    for f in format_strings:
        try:
            return datetime.datetime.strptime( date_string, f )
        except:
            pass
    return None


def create_oligos( csv_list, user ):
    # create oligo
    #primers = pd.read_excel( excel_list, header=2, date_parser=parse_date )
    primers = pd.read_csv( csv_list, header=2 )
    for pos,row in primers.iterrows():
        serial = seq = former = name = comment = ''
        date = None

        print row
        if pos==0:
            continue

        if not pd.isnull(row['serial No.']):
            serial = "{:0>4d}".format( int(row['serial No.']) )
        if not pd.isnull(row['sequence']):
            seq = row['sequence']
        if not pd.isnull(row[' order date']):
            #date = row[' order date']
            date = parse_date( row[' order date'] )
            print date
        if not pd.isnull(row['former No.']):
            former = row['former No.']
        if not pd.isnull(row['oligo name']):
            name = row['oligo name']
        if not pd.isnull(row['comments']):
            comment = row['comments']

        # if everything but serial no. is empty, skip row
        if seq=='' and date==None and name=='' and former=='' and comment=='':
            continue

        print serial, seq, date, former, name, comment
        print 
        labstocks.Oligos.insert( id = serial,
                                 sequence = seq,
                                 name=name,
                                 former_no=former,
                                 date_= date,
                                 author=user,
                                 description=comment ).execute()

def get_yeast_markers():
    return [r.type.encode('utf-8') for r in labstocks.PlYeastMarker.select().execute()]

def get_yeast_promoters():
    return [r.type.encode('utf-8') for r in labstocks.PlYeastPromoter.select().execute()]

def create_plasmids( csv_list ):
    # create plasmids
    plasmids = pd.read_csv( csv_list )

    # insert empty plasmid to be able to not select a plasmid in strain table
    labstocks.Plasmids.insert( ekp=0 ).execute()

    for pos,row in plasmids.iterrows():

        author = users[0]

        if not str(row['Date']).strip() == '"':
            date_ = None
            
        bacterial_selection = checkings = construction_description = insert_ = insert_type = ''
        marker_1 = marker_2 = name_ = promoter = reference_ = reporter = tags = type_ = ''
        #date_ = None

        ekb = markers = ''
        try:
            ekp = int(row['EKP No.']) 
        except:
            if row['EKP No.'] == '61a':
                ekp = 362

        if not pd.isnull(row['Vector']):
            name_ = row['Vector']
        if not pd.isnull(row['Insert']):
            insert_ = row['Insert']
        if not pd.isnull(row['EKB stock No.']):
            ekb = str(row['EKB stock No.'])
        if not pd.isnull(row['Features/ Marker']):
            markers = row['Features/ Marker']
        if not pd.isnull(row['Source/ Comments']):
            construction_description = row['Source/ Comments']
        if date_==None and not pd.isnull(row['Date']):
            date_ = parse_date(row['Date'])
        
        # parse bacterial marker
        if 'amp' in markers.lower() or 'ampr' in markers.lower():
            bacterial_selection = 'Amp'
        elif 'kan' in markers.lower():
            bacterial_selection = 'Kan'
        #elif '?'== markers.strip() or ''==markers.strip():
        else:
            bacterial_selection = ''

        if ekp==362: # weird entry. TODO: solve this prior to insertion
            construction_description = "!!! Attention: No. 61b !!!\n" + construction_description

        # parse yeast selection markers
        # get all possible markers
        all_markers = get_yeast_markers()
        all_markers.remove('')        
        try:
            ekb = int(ekb)
        except:
            ekb = None

        # parse promoters
        all_promoters = get_yeast_promoters()
        all_promoters.remove('')
        for p in all_promoters:
            if p.lower() in markers.lower():
                promoter = p

        labstocks.Plasmids.insert( ekp=ekp,
                                   name_ = name_,
                                   insert_ = insert_,
                                   ekb = ekb,
                                   construction_description=construction_description,
                                   bacterial_selection=bacterial_selection,
                                   date_=date_,
                                   markers=markers,
                                   promoter = promoter).execute()
        print
        print ekp
        print name_
        print insert_
        print ekb
        print markers
        print construction_description
        print date_


def create_strains( txt_path, user ):
    skip = [ '135' ] # weird entries that should be skipped
    df = parse_yeast_stock( txt_path )
    for pos,row in df.iterrows():
        if row.ID in skip:
            continue
        
        if 'mata/alpha' in row.genotype.lower():
            mating = 'MATa/MATalpha'
        elif 'mata' in row.genotype.lower() and not 'matalpha' in row.genotype.lower():
            mating = 'MATa'
        elif 'matalpha' in row.genotype.lower():
            mating = 'MATalpha'
        else:
            mating = ''

        his3 = leu2 = met15 = ura3 = ''
        
        if 'BY4741' in str(row['name']) or 'BY4741' in str(row.parental) or 'BY 4741' in str(row.parental) or 'EKY 281' in str(row.parental) or 'EKY 266' in str(row.parental):
            pass
            his3 = u"\u0394" + '1'
            leu2 = u"\u0394" + '1'
            met15 = u"\u0394" + '0'
            ura3 = u"\u0394" + '0'
            matring = 'MATa'

        if pd.isnull(row.date):
            date = None
        else:
            date = row.date
        labstocks.Strains.insert( eky = row.ID,
                                  author = user,
                                  comments = row.comments,
                                  phenotype = row.phenotype,
                                  genotype = row.genotype,
                                  growth_req = row.growth_req,
                                  obtained_by = row.source,
                                  #storage_fridges = row.storage,
                                  date_ = date,
                                  name_ = row['name'],
                                  mating_type = mating,
                                  parental_strain = row.parental,
                                  reference_ = row.reference,
                                  #relevant_plasmids = row.plasmid,
                                  his3 = his3,
                                  leu2 = leu2,
                                  met15 = met15,
                                  ura3 = ura3 ).execute()



def create_ecoli_stocks( txt_path ):
    skip = [135] # weird entries that should be skipped
    df = parse_ecoli_stock( txt_path )
    print df.axes
    print df.index
    print df.columns

    for row in df.index:
#        row = row.split('\t')
#        print len(row)
        print row
        if row in skip:
             continue

        if row in [180, 181]:
            author = users[6]
        else:
            author = users[0]

        if pd.isnull(df.loc[row, 'Date']):
            datum = None
        else:
            datum = df.loc[row, 'Date']
            tmp = datum.split("/")
            datum = tmp[1] + "-" + tmp[0] + "-01"

        if pd.isnull(df.loc[row, 'Comments']):
            comment = None
        else:                                                                                                                                                                                                
            comment = df.loc[row, 'Comments']

        if pd.isnull(df.loc[row, 'EKP No.']):
            plasmid = None
        else:
            plasmid = df.loc[row, 'EKP No.']

        print row, df.loc[row, 'E.coli strain'], datum, plasmid, df.loc[row, 'Source'], df.loc[row, 'Features/ Marker'], author, comment

        labstocks.EcoliStocks.insert( ekb = row, 
                                      name_ = df.loc[row, 'E.coli strain'],
                                      date_ = datum,
                                      plasmid = plasmid,
#                                       insertion = df.loc[row, 'Insert'],
                                       source = df.loc[row, 'Source'],
                                       features_marker = df.loc[row, 'Features/ Marker'],
                                       author = author,
                                       comments = comment ).execute()


def parse_yeast_stock( txt_path ):
    # convert our yeast stock word file to a pandas dataframe

    skip = [ 135 ] 
    chars_to_remove = ['\t', '\n', '\r']

    key_external = [ 'Parental strain', 'Genotype', 'Phenotype', 'Plasmid', 'Source', 'Date Obtained', 'Storage', 'Growth Req.', 'Reference', 'Comments' ]
    key_internal = [ 'parental',        'genotype', 'phenotype', 'plasmid', 'source', 'date',          'storage',  'growth_req', 'reference', 'comments' ]

    df = pd.DataFrame( columns = ['ID', 'name'] + key_internal )
    f = open( txt_path, 'r' )

    buff = ''
    eky = []

    # first separate the different entries
    for l in f.readlines():
        if l.strip().startswith( 'EKY' ):
            if buff != '':
                eky.append(buff)
                buff = ''
        buff += l

    # next parse the information for each strain
    for ID, strain in enumerate(eky, 1):
        if ID in skip:
            continue
        rest = strain
        for c in chars_to_remove:
            rest = rest.replace(c, '')
        parsed = []
        
        for pos,key in enumerate(key_external):
            this, rest = rest.split( key, 1)
            this = this.strip()
            while this.startswith(':'): 
                this = this[1:]
            parsed.append( this.strip() )
        parsed.append( rest.strip() )
        d = dict( zip( ['EKY']+key_internal, parsed ) )
        d['ID'] = ID
        eky, name = d['EKY'].split( str(ID) + '.', 1 )
        d['name'] = name.strip()
        d['date'] = parse_date( d['date'] )
        
        df = df.append( d, ignore_index=True )
    return df


def parse_ecoli_stock( txt_path ):
    skip = []#[ 135 ]
    chars_to_remove = ['\n', '\r']

    key_external = ['EKB No.', 'E.coli strain', 'Plasmid', 'Insert', 'Source', 'Features/ Marker', 'Date', 'Comments', 'EKP No.']
    key_internal = ['ekb_no',  'name',          'plasmid', 'insert', 'source', 'features_marker',  'date', 'comments', 'ekp_no']
    parsed = []

#    df = pd.read_excel( txt_path, ignore_index=True, columns=key_internal )
    df = pd.read_excel( txt_path, index_col='EKB No.', columns=key_internal )
#    print df
    for line in df:
        for c in chars_to_remove:
            line = line.replace(c, '')
                                                                        
    return df


def convert_yeast_stock_excel( path ):

    df = parse_yeast_stock( path  )
    df['general_background'] = ''
    for i,row in df.iterrows():
        if 'BY4741' in str(row['name']) or 'BY4741' in str(row.parental) or 'BY 4741' in str(row.parental) or 'EKY 281' in str(row.parental) or 'EKY 266' in str(row.parental):
            df.loc[i, 'general_background'] = 'BY4741'
        elif 'W303' in str(row['name']) or 'W303' in str(row.parental) or 'W 303' in str(row.parental):
            df.loc[i, 'general_background'] = 'W303'
    return df

if __name__=='__main__':

    data_dir = '../../../data/' # when Jannis updates
    #data_dir = '/home/jwodke/Desktop/job/projects/labDB/jannis/lab_db2/data/' # on my computer!

    df = convert_yeast_stock_excel( os.path.join( data_dir, 'TBP_yeast_stocks.txt' )  )
    df.to_csv( 'strains_exp.csv' )

    labstocks.database.connect_kwargs['passwd'] = sys.argv[1]
    # connect DB
    labstocks.database.connect()

    clean_db()

    users = ["Gabi", "Bjorn", "Lotte", "Severin", "Jannis", "Paula", "Christiane", "Lisa"]
    create_users( users )
    
    create_oligos( os.path.join( data_dir, 'TBP_all_primers.csv' ), users[0] )

    create_plasmids( os.path.join( data_dir, 'TBP_plasmids.csv' ) )

    create_strains( os.path.join( data_dir, 'TBP_yeast_stocks.txt' ), users[0] )

    create_ecoli_stocks( os.path.join( data_dir, 'TBP_Ecoli_stocks_20160420.xlsx' ) )
