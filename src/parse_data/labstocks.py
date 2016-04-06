from peewee import *

database = MySQLDatabase('test_labstocks_db', **{'host': 'localhost', 'user': 'superuser'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class AbAvail(BaseModel):
    type = CharField(db_column='Type', primary_key=True)

    class Meta:
        db_table = 'ab_avail'

class AbHost(BaseModel):
    host = CharField(db_column='Host', primary_key=True)

    class Meta:
        db_table = 'ab_host'

class AbMonopoly(BaseModel):
    type = CharField(db_column='Type', primary_key=True)

    class Meta:
        db_table = 'ab_monopoly'

class AbSupplier(BaseModel):
    supplier = CharField(db_column='Supplier', primary_key=True)

    class Meta:
        db_table = 'ab_supplier'

class AbType(BaseModel):
    type = CharField(db_column='Type', primary_key=True)

    class Meta:
        db_table = 'ab_type'

class Antibodies(BaseModel):
    antigen = CharField(db_column='Antigen')
    batch_reference = CharField(db_column='Batch_Reference', null=True)
    comments = TextField(db_column='Comments', null=True)
    date = DateField(db_column='Date', null=True)
    dilution_wb = TextField(db_column='Dilution-WB')
    host = CharField(db_column='Host', null=True)
    instock = CharField(db_column='InStock')
    location = CharField(db_column='Location')
    ordered_by = CharField(db_column='Ordered_by', index=True, null=True)
    productid = CharField(db_column='ProductID')
    supplier = CharField(db_column='Supplier')
    type = CharField(db_column='Type')
    volume_chip = TextField(db_column='Volume-ChIP')
    storage_fridges = CharField(null=True)
    storage_minus20freezers = CharField(null=True)
    storage_minus80freezers = CharField(null=True)
    storage_rooms = CharField(null=True)

    class Meta:
        db_table = 'antibodies'

class ClName(BaseModel):
    author = CharField(db_column='Author', null=True)
    description = TextField(null=True)
    name = CharField(primary_key=True)
    origin = TextField(null=True)
    type = CharField(null=True)

    class Meta:
        db_table = 'cl_name'

class ClPassages(BaseModel):
    author = CharField(db_column='Author', null=True)
    id = PrimaryKeyField(db_column='ID')
    date_of_freezing = DateField(null=True)
    name = CharField(null=True)
    passage = TextField(null=True)

    class Meta:
        db_table = 'cl_passages'

class ClStorage(BaseModel):
    id = PrimaryKeyField(db_column='ID')
    box = CharField(null=True)
    cl_passages = IntegerField(null=True)
    container = CharField(null=True)
    field_x = CharField(null=True)
    field_y = CharField(null=True)
    rack = CharField(null=True)

    class Meta:
        db_table = 'cl_storage'

class ClType(BaseModel):
    type = CharField(primary_key=True)

    class Meta:
        db_table = 'cl_type'

class LabMembers(BaseModel):
    id = CharField(primary_key=True)

    class Meta:
        db_table = 'lab_members'

class Plasmids(BaseModel):
    author = ForeignKeyField(db_column='Author', null=True, rel_model=LabMembers, to_field='id')
    bacterial_selection = CharField(db_column='Bacterial_selection', null=True)
    checkings = CharField(db_column='Checkings', null=True)
    construction_description = TextField(db_column='Construction_Description', null=True)
    ekb = IntegerField(db_column='EKB', null=True)
    insert_ = CharField(db_column='Insert_', null=True)
    insert_type = CharField(db_column='Insert_Type', null=True)
    link_to_file = CharField(db_column='Link_to_file', null=True, unique=True)
    markers = CharField(db_column='Markers', null=True)
    name_ = CharField(db_column='Name_', null=True)
    other_names = CharField(db_column='Other_names', null=True)
    promoter = CharField(db_column='Promoter', null=True)
    reference_ = CharField(db_column='Reference_', null=True)
    reporter = CharField(db_column='Reporter', null=True)
    tags = CharField(db_column='Tags', null=True)
    type_ = CharField(db_column='Type_', null=True)
    date_ = DateField(null=True)
    image_file = CharField(null=True)
    parent_vector = CharField(null=True)
    sequence = TextField(null=True)
    storage_fridges = CharField(null=True)
    storage_minus20freezers = CharField(null=True)
    storage_minus80freezers = CharField(null=True)
    storage_rooms = CharField(null=True)

    class Meta:
        db_table = 'plasmids'

class EcoliStocks(BaseModel):
    author = ForeignKeyField(db_column='Author', null=True, rel_model=LabMembers, to_field='id')
    comments = TextField(db_column='Comments', null=True)
    date_ = DateField(db_column='Date_', null=True)
    ekb_no = PrimaryKeyField(db_column='EKB_no')
    features_marker = CharField(db_column='Features_Marker', null=True)
    insert = CharField(db_column='Insert', null=True)
    name_ = CharField(db_column='Name_')
    original_no = IntegerField(db_column='Original_no', null=True)
    plasmid = ForeignKeyField(db_column='Plasmid', null=True, rel_model=Plasmids, to_field='id')
    source = CharField(db_column='Source', null=True)

    class Meta:
        db_table = 'ecoli_stocks'

class Notebooks(BaseModel):
    author = CharField(db_column='Author', index=True)
    begin_date = DateField(db_column='Begin_Date', null=True)
    end_date = DateField(db_column='End_Date', null=True)
    id = PrimaryKeyField(db_column='ID')
    serial_number = CharField(db_column='Serial_Number', unique=True)

    class Meta:
        db_table = 'notebooks'

class OligPurif(BaseModel):
    type = CharField(primary_key=True)

    class Meta:
        db_table = 'olig_purif'

class Oligos(BaseModel):
    author = ForeignKeyField(db_column='Author', null=True, rel_model=LabMembers, to_field='id')
    date_ = DateField(db_column='Date_', null=True)
    description = TextField(db_column='Description', null=True)
    name = CharField(db_column='Name', null=True)
    pcr_conditions_predicted = TextField(db_column='PCR_conditions_predicted', null=True)
    purif = CharField(db_column='Purif')
    sequence = CharField(db_column='Sequence')
    former_no = CharField(null=True)
    id = CharField(primary_key=True)
    storage_fridges = CharField(null=True)
    storage_minus20freezers = CharField(null=True)
    storage_minus80freezers = CharField(null=True)
    storage_rooms = CharField(null=True)

    class Meta:
        db_table = 'oligos'

class PipEvents(BaseModel):
    events = CharField(db_column='Events', primary_key=True)

    class Meta:
        db_table = 'pip_events'

class PipGenericUser(BaseModel):
    user = CharField(db_column='User', primary_key=True)

    class Meta:
        db_table = 'pip_generic_user'

class PipHistory(BaseModel):
    comments = TextField(db_column='Comments')
    date = DateField(db_column='Date')
    event_type = CharField(db_column='Event_Type')
    id = PrimaryKeyField(db_column='ID')
    owner_fromnowon = CharField(db_column='Owner_fromNowOn')
    serial_number = CharField(db_column='Serial_Number')
    usage_fromnowon = CharField(db_column='Usage_fromNowOn')

    class Meta:
        db_table = 'pip_history'

class PipMarque(BaseModel):
    marque = CharField(db_column='Marque', primary_key=True)

    class Meta:
        db_table = 'pip_marque'

class PipNonusers(BaseModel):
    user = CharField(db_column='User', primary_key=True)

    class Meta:
        db_table = 'pip_nonusers'

class PipStock(BaseModel):
    id = PrimaryKeyField(db_column='ID')
    marque = CharField(db_column='Marque')
    serial_number = CharField(db_column='Serial_Number', unique=True)
    type = CharField(db_column='Type')

    class Meta:
        db_table = 'pip_stock'

class PipType(BaseModel):
    type = CharField(db_column='Type', primary_key=True)

    class Meta:
        db_table = 'pip_type'

class PipUsage(BaseModel):
    usage = CharField(db_column='Usage', primary_key=True)

    class Meta:
        db_table = 'pip_usage'

class PipUsers(BaseModel):
    user = CharField(db_column='User', primary_key=True)

    class Meta:
        db_table = 'pip_users'

class PlBacterialSelection(BaseModel):
    type = CharField(primary_key=True)

    class Meta:
        db_table = 'pl_bacterial_selection'

class PlFeatures(BaseModel):
    author = ForeignKeyField(db_column='Author', null=True, rel_model=LabMembers, to_field='id')
    category = CharField(db_column='Category')
    comments = TextField(db_column='Comments')
    date_ = DateField(db_column='Date_', null=True)
    description = TextField(db_column='Description', null=True)
    sequence = TextField(db_column='Sequence', unique=True)

    class Meta:
        db_table = 'pl_features'

class PlFeaturesCatname(BaseModel):
    category = CharField(db_column='Category', primary_key=True)
    name = CharField(db_column='Name', null=True)

    class Meta:
        db_table = 'pl_features_catname'

class PlTag(BaseModel):
    type = CharField(primary_key=True)

    class Meta:
        db_table = 'pl_tag'

class PlType(BaseModel):
    type = CharField(primary_key=True)

    class Meta:
        db_table = 'pl_type'

class PlYeastMarker(BaseModel):
    type = CharField(primary_key=True)

    class Meta:
        db_table = 'pl_yeast_marker'

class PlYeastPromoter(BaseModel):
    type = CharField(primary_key=True)

    class Meta:
        db_table = 'pl_yeast_promoter'

class StAde2(BaseModel):
    alleles = CharField(primary_key=True)

    class Meta:
        db_table = 'st_ADE2'

class StHis3(BaseModel):
    alleles = CharField(primary_key=True)

    class Meta:
        db_table = 'st_HIS3'

class StLeu2(BaseModel):
    alleles = CharField(primary_key=True)

    class Meta:
        db_table = 'st_LEU2'

class StLys2(BaseModel):
    alleles = CharField(primary_key=True)

    class Meta:
        db_table = 'st_LYS2'

class StMat(BaseModel):
    alleles = CharField(primary_key=True)

    class Meta:
        db_table = 'st_MAT'

class StMet15(BaseModel):
    alleles = CharField(primary_key=True)

    class Meta:
        db_table = 'st_MET15'

class StTrp1(BaseModel):
    alleles = CharField(primary_key=True)

    class Meta:
        db_table = 'st_TRP1'

class StUra3(BaseModel):
    alleles = CharField(primary_key=True)

    class Meta:
        db_table = 'st_URA3'

class StGeneralBackgrounds(BaseModel):
    background = CharField(primary_key=True)

    class Meta:
        db_table = 'st_general_backgrounds'

class StSpecies(BaseModel):
    species = CharField(primary_key=True)

    class Meta:
        db_table = 'st_species'

class StorageFridges(BaseModel):
    name = CharField(primary_key=True)

    class Meta:
        db_table = 'storage_fridges'

class StorageMinus20Freezers(BaseModel):
    name = CharField(primary_key=True)

    class Meta:
        db_table = 'storage_minus20freezers'

class StorageMinus80Freezers(BaseModel):
    name = CharField(primary_key=True)

    class Meta:
        db_table = 'storage_minus80freezers'

class StorageRooms(BaseModel):
    name = CharField(primary_key=True)

    class Meta:
        db_table = 'storage_rooms'

class Strains(BaseModel):
    ade2 = CharField(db_column='ADE2', null=True)
    author = ForeignKeyField(db_column='Author', null=True, rel_model=LabMembers, to_field='id')
    comments = TextField(db_column='Comments', null=True)
    cytoplasmic_character = CharField(db_column='Cytoplasmic_Character', null=True)
    date_ = DateField(db_column='Date_', null=True)
    general_background = CharField(db_column='General_Background')
    genotype = CharField(db_column='Genotype', null=True)
    growth_req = CharField(db_column='Growth_req', null=True)
    his3 = CharField(db_column='HIS3', null=True)
    ho_ = CharField(db_column='HO_', null=True)
    leu2 = CharField(db_column='LEU2', null=True)
    lys2 = CharField(db_column='LYS2', null=True)
    met15 = CharField(db_column='MET15', null=True)
    mating_type = CharField(db_column='Mating_Type', null=True)
    name_ = CharField(db_column='Name_')
    obtained_by = CharField(db_column='Obtained_by', null=True)
    parental_strain = CharField(db_column='Parental_strain', null=True)
    phenotype = CharField(db_column='Phenotype', null=True)
    plasmid = ForeignKeyField(db_column='Plasmid', null=True, rel_model=Plasmids, to_field='id')
    reference_ = CharField(db_column='Reference_', null=True)
    sgd = CharField(db_column='SGD_ID', null=True)
    trp1 = CharField(db_column='TRP1', null=True)
    ura3 = CharField(db_column='URA3', null=True)
    clone_no = IntegerField(null=True)
    labbook_reference = CharField(null=True)
    locus1 = CharField(null=True)
    locus2 = CharField(null=True)
    locus3 = CharField(null=True)
    original_no = IntegerField(null=True)
    storage_box = CharField(null=True)

    class Meta:
        db_table = 'strains'

class Visitors(BaseModel):
    login = CharField(primary_key=True)
    mode = CharField()
    pwd = CharField()
    target_table = CharField()

    class Meta:
        db_table = 'visitors'

class Websession(BaseModel):
    id_session = CharField(primary_key=True)
    login = CharField(index=True)
    mode = CharField(null=True)
    target_table = CharField(null=True)
    time_limit = DecimalField()

    class Meta:
        db_table = 'websession'

