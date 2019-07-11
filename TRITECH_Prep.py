
# Build for the Training Environment?
copyDisplayLayers = arcpy.GetParameterAsText(0)
copyStreets = arcpy.GetParameterAsText(1)
copyAddresses = arcpy.GetParameterAsText(2)
# Import arcpy module
import arcpy
import datetime
import os

# Set Geoprocessing environments:
arcpy.env.overwriteOutput = True
arcpy.gp.overwriteOutput = True

# Workspace Variables:
GDB_County = "C:\\Users\\robert.mabry\\Documents\\ArcGIS\\Williamson_TIPS.gdb"
GDB_Scratch = arcpy.env.scratchGDB
GDB_Display = "C:\\TriTech\\VisiCAD\\Data\\Maps\\MapDisplay\\Layers\\Display_Layers.gdb"
GDB_TriTech = "C:\\Users\\robert.mabry\\Documents\\ArcGIS\\TRITECH.gdb"
GDB_GISLink_Source = "G:\\Source\\TRITECH.gdb"
GDB_Static = "C:\\Users\\robert.mabry\\Documents\\ArcGIS\\StaticBase.gdb"
GDB_Network = r'C:\Users\robert.mabry\Documents\ArcGIS\Network\Network.gdb'
TIPS_Williamson = r'C:\Users\robert.mabry\Documents\ArcGIS\WILLIAMSON.gdb'
TIPS_Surround = r'C:\Users\robert.mabry\Documents\ArcGIS\WILLIAMSON_surrounding.gdb'
SDE_Brentwood = "C:\\Users\\robert.mabry\\AppData\\Roaming\\ESRI\\Desktop10.6\\ArcCatalog\\TriTech Shared.sde\\TritechGIS.DBO.BrentwoodCADLayers"

DateToday = str(datetime.date.today()).replace("-","")
addressDuplicateReport = r'C:\Users\robert.mabry\Documents\ArcGIS\TriTech Exports\address_duplicates_'+DateToday+r'.xls'

TRITECH_Geolocator = "C:\\Users\\robert.mabry\\Documents\\ArcGIS\\Static Base\\TRITECH_Geolocator"

# County Source Features:
williamson_lake_pond = GDB_County + "\\lake_pond_94"
williamson_riverpoly = GDB_County + "\\riverpoly_94"
williamson_streams = GDB_County + "\\stream_94"
williamson_rivers = GDB_County + "\\river_94"
williamson_parcels = GDB_County + "\\parcelsgpdata"
maury_parcels = GDB_County + '\\parcels_cama_a'
williamson_cityLimits = GDB_County + "\\corps"
springHill_cityLimits = GDB_County + '\\SH_City_Limits'
williamson_communities = GDB_County + "\\comunity_94"
williamson_sirens = GDB_County + "\\Tornado_Sirens"
williamson_railroad = GDB_County + "\\railroad"
williamson_parks = GDB_County + "\\parks"
williamson_centerlines = GDB_County + "\\Centerlines"
williamson_addresses = GDB_County + "\\Address"

# Display_Layers Features:
display_AED = GDB_Display + "\\AED_Locations"
display_Address = GDB_Display + "\\Address"
display_Buildings = GDB_Display + "\\Buildings"
display_Cable = GDB_Display + "\\CableTV"
display_CellTowers = GDB_Display + "\\Cell_Towers"
display_CityLimits = GDB_Display + "\\City_Limits"
display_Community = GDB_Display + "\\Community"
display_County = GDB_Display + "\\County"
display_EMS = GDB_Display + "\\EMS_Areas"
display_ESN = GDB_Display + "\\ESN"
display_Electric = GDB_Display + "\\ElectricCo"
display_FKFD = GDB_Display + "\\FKFD_Areas"
display_Lakes = GDB_Display + "\\Lakes_Rivers"
display_Neighborhoods = GDB_Display + "\\Neighborhoods"
display_Parcels = GDB_Display + "\\Parcels"
display_Parks = GDB_Display + "\\parks"
display_Radios = GDB_Display + "\\Radio_Coverage"
display_Railroad = GDB_Display + "\\railroad"
display_RiverMarkers = GDB_Display + "\\RiverMileMarkers"
display_Rivers = GDB_Display + "\\Rivers_Streams"
display_Sewer = GDB_Display + "\\Sewer"
display_Sirens = GDB_Display + "\\sirens"
display_SurroundStreets = GDB_Display + "\\Surrounding_Streets"
display_WaterDistricts = GDB_Display + "\\WaterDistricts"

#TRITECH Feature Layers:
tritech_LawAreas = GDB_TriTech + "\\Law_Response_Area"
tritech_Centerlines = GDB_TriTech + "\\Centerlines"
tritech_Addresses = GDB_TriTech + "\\Address"

#Static Data Feature Layers:
static_AED = GDB_Static + "\\AED_locations"
static_buildings = GDB_Static + "\\buildings"
static_catv = GDB_Static + "\\catv"
static_CenterlineSchema = GDB_Static + "\\Centerline_Schema"
static_CountyBorders = GDB_Static + "\\County_Borders"
static_electric = GDB_Static + "\\electric"
static_EMS = GDB_Static + "\\EMS_Poly"
static_Ramps = GDB_Static + "\\Exit_Ramps"
static_FKFD = GDB_Static + "\\FKFD_Poly"
static_SirenSectors = GDB_Static + "\\Tornado_Siren_Sectors"
static_Intersections = GDB_Static + "\\IntersectionPoints"
static_MileMarkers = GDB_Static + "\\Mile_Markers"
static_NatchezMM = GDB_Static + "\\Natchez_MM"
static_RiverMarkers = GDB_Static + "\\RiverMileMarkers"
static_septic = GDB_Static + "\\septic"
static_StreetBuffer = GDB_Static + "\\Surrounding_Street_Buffer"
static_watdist = GDB_Static + "\\watdist"
static_WOPS_Buff = GDB_Static + "\\WOPS_Buff"

#Network Analyst Features:
network_centerlines = GDB_Network + r'\Network\Centerlines'
network_dataset = GDB_Network + r'\Network\Network_ND'

# TIPS Downloaded Features (https://tngeo.app.box.com/v/NGDistrictDownloads):
TIPS_Addresses = TIPS_Surround + r'\NGlayers\Addresses'
TIPS_Centerlines = TIPS_Surround + r'\NGlayers\Centerlines'
TIPS_ESN = TIPS_Surround + r'\NGlayers\ESNs'
TIPS_surrTowers = TIPS_Surround + r'\ValueAdded\CellTowers'
TIPS_wcTowers = TIPS_Williamson + r'\ValueAdded\CellTowers'



#Abbreviation Dictionaries:  These dictionaries show a list of all values for cities, counties, and street types. Each is made of two values: the original source value, and the "code" value or correct abbreviation for TriTech's databases.
CityList="""CityList={
    'ANTIOCH':'ANTIOCH',
    'ARRINGTON':'ARRINGTON',
    'ASHLAND  CITY':'ASHLAND',
    'ASHLAND CITY':'ASHLAND',
    'BELFAST':'BELFAST',
    'BELL BUCKLE':'BELLBUCKLE',
    'BON AQUA':'BONAQUA',
    'BRENTWOOD':'BRENTWOOD',
    'BURNS':'BURNS',
    'CEDAR HILL':'CEDARHILL',
    'CENTERVILLE':'CENTERVL',
    'CHAPEL HILL':'CHAPELHILL',
    'CHAPMANSBORO':'CHAPMANBRO',
    'CHARLOTTE':'CHARLOTTE',
    'CHEATHAM CO':'CHEATHAM',
    'CHEATHAM COUNTY':'CHEATHAM',
    'CHRISTIANA':'CHRISTIANA',
    'CLARKSVILLE':'CLARKSVL',
    'COLLEGE GROVE':'COLLEGEGRV',
    'COLUMBIA':'COLUMBIA',
    'CORNERSVILLE':'CORNERSVL',
    'CULLEOKA':'CULLEOKA',
    'CUMBELAND':'CUMBERLAND',
    'CUMBERLAND FURNACE':'CUMBERLAND',
    'CUNNINGHAM':'CUNNINGHAM',
    'DAVIDSON COUNTY':'DAVIDSON',
    'DICKSON':'DICKSON',
    'DICKSONCO':'DICKSONCO',
    'DUCK RIVER':'DUCKRIVER',
    'EAGLEVILLE':'EAGLEVILLE',
    'FAIRVIEW':'FAIRVIEW',
    'FOSTERVILLE':'FOSTERVL',
    'FRANKLIN':'FRANKLIN',
    'GILES':'GILES',
    'GOODLETTSVILLE':'GOODLETSVL',
    'HAMPSHIRE':'HAMPSHIRE',
    'HERMITAGE':'HERMITAGE',
    'HICKMANCO':'HICKMANCO',
    'HOHENWALD':'HOHENWALD',
    'JOELTON':'JOELTON',
    'KINGSTON SPRINGS':'KINGSTON',
    'LASCASSAS':'LASCASSAS',
    'LAVERGNE':'LAVERGNE',
    'LEBANON':'LEBANON',
    'LEWISBURG':'LEWISBURG',
    'LOBELVILLE':'LOBELVILLE',
    'LYLES':'LYLES',
    'LYNNVILLE':'LYNNVILLE',
    'MADISON':'MADISON',
    'MARSHALLCO':'MARSHALLCO',
    'MAURYCO':'MAURYCO',
    'MCEWEN':'MCEWEN',
    'MILTON':'MILTON',
    'MOUNT JULIET':'MTJULIET',
    'MT JULIET':'MTJULIET',
    'MT PLEASAN':'MTPLEASANT',
    'MT PLEASANT':'MTPLEASANT',
    'MURFREESBORO':'MURFBORO',
    'NASHVILLE':'NASHVILLE',
    'NIPPERS CO':'NIPPERS',
    'NOLENSVILLE':'NOLV',
    'NUNNELLY':'NUNNELLY',
    'OLD HICKORY':'OLDHICKORY',
    'ONLY':'ONLY',
    'PEGRAM':'PEGRAM',
    'PETERSBURG':'PETERSBURG',
    'PLEASANT VIEW':'PLEASANTV',
    'PRIMM SPRINGS':'PRIMMSPRGS',
    'READYVILLE':'READYVILLE',
    'RIDGETOP':'RIDGETOP',
    'ROCKVALE':'ROCKVALE',
    'RUTHERFORD COUNTY':'RUTHERFORD',
    'SANTA FE':'SANTAFE',
    'SMYRNA':'SMYRNA',
    'SOUTHSIDE':'SOUTHSIDE',
    'SPRING HIL':'SH',
    'SPRING HILL':'SH',
    'SUMMERTOWN':'SUMMERTOWN',
    'THOMPSONS STATION':'TH',
    'UNION HILL':'UNIONHILL',
    'UNIONVILLE':'UNIONVILLE',
    'VANLEER':'VANLEER',
    'VANLER':'VANLER',
    'WHITE  BLU':'WHITEBLUFF',
    'WHITE BLUF':'WHITEBLUFF',
    'WHITE BLUFF':'WHITEBLUFF',
    'WHITES CREEK':'WHITESCRK',
    'WILLIAMSON COUNTY':'WILLIAMSON',
    'WILLIAMSPORT':'WILLIAMSPT'
}"""
CountyList="""CountyList={
    'BEDFORD':'BEDFO',
    'CHEATHAM':'CHEAT',
    'DAVIDSON':'DV',
    'DICKSON':'DICKS',
    'GILES':'GILES',
    'HICKMAN':'HICKM',
    'HOUSTON':'HOUST',
    'LINCOLN':'LINCN',
    'MARSHALL':'MARSH',
    'MAURY':'MAURY',
    'RUTHERFORD':'RUTH',
    'WILLIAMSON':'WM',
    'WILSON':'WILSN'
}"""
StTypes="""StTypes={
    'ALLEE':'ALY',
    'ALLEY':'ALY',
    'ALLY':'ALY',
    'ALY':'ALY',
    'ANEX':'ANX',
    'ANNEX':'ANX',
    'ANNX':'ANX',
    'ANX':'ANX',
    'ARC':'ARC',
    'ARCADE':'ARC',
    'AV':'AVE',
    'AVE':'AVE',
    'AVEN':'AVE',
    'AVENU':'AVE',
    'AVENUE':'AVE',
    'AVN':'AVE',
    'AVNUE':'AVE',
    'BAYOO':'BYU',
    'BAYOU':'BYU',
    'BCH':'BCH',
    'BEACH':'BCH',
    'BEND':'BND',
    'BG':'BG',
    'BGS':'BGS',
    'BLF':'BLF',
    'BLFS':'BLFS',
    'BLUF':'BLF',
    'BLUFF':'BLF',
    'BLUFFS':'BLFS',
    'BLVD':'BLVD',
    'BND':'BND',
    'BOT':'BTM',
    'BOTTM':'BTM',
    'BOTTOM':'BTM',
    'BOUL':'BLVD',
    'BOULEVARD':'BLVD',
    'BOULV':'BLVD',
    'BR':'BR',
    'BRANCH':'BR',
    'BRDGE':'BRG',
    'BRG':'BRG',
    'BRIDGE':'BRG',
    'BRK':'BRK',
    'BRKS':'BRKS',
    'BRNCH':'BR',
    'BROOK':'BRK',
    'BROOKS':'BRKS',
    'BTM':'BTM',
    'BURG':'BG',
    'BURGS':'BGS',
    'BYP':'BYP',
    'BYPA':'BYP',
    'BYPAS':'BYP',
    'BYPASS':'BYP',
    'BYPS':'BYP',
    'BYU':'BYU',
    'CAMP':'CP',
    'CANYN':'CYN',
    'CANYON':'CYN',
    'CAPE':'CPE',
    'CAUSEWAY':'CSWY',
    'CAUSWA':'CSWY',
    'CEN':'CTR',
    'CENT':'CTR',
    'CENTER':'CTR',
    'CENTERS':'CTRS',
    'CENTR':'CTR',
    'CENTRE':'CTR',
    'CIR':'CIR',
    'CIRC':'CIR',
    'CIRCL':'CIR',
    'CIRCLE':'CIR',
    'CIRCLES':'CIRS',
    'CIRS':'CIRS',
    'CL':'CL',
    'CLB':'CLB',
    'CLF':'CLF',
    'CLFS':'CLFS',
    'CLIFF':'CLF',
    'CLIFFS':'CLFS',
    'CLOSE':'CL',
    'CLS':'CL',
    'CLUB':'CLB',
    'CMN':'CMN',
    'CMNS':'CMNS',
    'CMP':'CP',
    'CNTER':'CTR',
    'CNTR':'CTR',
    'CNYN':'CYN',
    'COMMON':'CMN',
    'COMMONS':'CMNS',
    'COR':'COR',
    'CORNER':'COR',
    'CORNERS':'CORS',
    'CORS':'CORS',
    'COURSE':'CRSE',
    'COURT':'CT',
    'COURTS':'CTS',
    'COVE':'CV',
    'COVES':'CVS',
    'CP':'CP',
    'CPE':'CPE',
    'CRCL':'CIR',
    'CRCLE':'CIR',
    'CREEK':'CRK',
    'CRES':'CRES',
    'CRESCENT':'CRES',
    'CREST':'CRST',
    'CRK':'CRK',
    'CROSSING':'XING',
    'CROSSROAD':'XRD',
    'CROSSROADS':'XRDS',
    'CRSE':'CRSE',
    'CRSENT':'CRES',
    'CRSG':'XING',
    'CRSNT':'CRES',
    'CRSSNG':'XING',
    'CRST':'CRST',
    'CSWY':'CSWY',
    'CT':'CT',
    'CTR':'CTR',
    'CTRS':'CTRS',
    'CTS':'CTS',
    'CURV':'CURV',
    'CURVE':'CURV',
    'CV':'CV',
    'CVS':'CVS',
    'CYN':'CYN',
    'DALE':'DL',
    'DAM':'DM',
    'DIV':'DV',
    'DIVIDE':'DV',
    'DL':'DL',
    'DM':'DM',
    'DR':'DR',
    'DRIV':'DR',
    'DRIVE':'DR',
    'DRIVES':'DRS',
    'DRS':'DRS',
    'DRV':'DR',
    'DV':'DV',
    'DVD':'DV',
    'ENT':'ENT',
    'ENTRANCE':'ENT',
    'EST':'EST',
    'ESTATE':'EST',
    'ESTATES':'ESTS',
    'ESTS':'ESTS',
    'EXP':'EXPY',
    'EXPR':'EXPY',
    'EXPRESS':'EXPY',
    'EXPRESSWAY':'EXPY',
    'EXPW':'EXPY',
    'EXPY':'EXPY',
    'EXT':'EXT',
    'EXTENSION':'EXT',
    'EXTENSIONS':'EXTS',
    'EXTN':'EXT',
    'EXTNSN':'EXT',
    'EXTS':'EXTS',
    'FALL':'FALL',
    'FALLS':'FLS',
    'FERRY':'FRY',
    'FIELD':'FLD',
    'FIELDS':'FLDS',
    'FLAT':'FLT',
    'FLATS':'FLTS',
    'FLD':'FLD',
    'FLDS':'FLDS',
    'FLS':'FLS',
    'FLT':'FLT',
    'FLTS':'FLTS',
    'FORD':'FRD',
    'FORDS':'FRDS',
    'FOREST':'FRST',
    'FORESTS':'FRST',
    'FORG':'FRG',
    'FORGE':'FRG',
    'FORGES':'FRGS',
    'FORK':'FRK',
    'FORKS':'FRKS',
    'FORT':'FT',
    'FRD':'FRD',
    'FRDS':'FRDS',
    'FREEWAY':'FWY',
    'FREEWY':'FWY',
    'FRG':'FRG',
    'FRGS':'FRGS',
    'FRK':'FRK',
    'FRKS':'FRKS',
    'FRRY':'FRY',
    'FRST':'FRST',
    'FRT':'FT',
    'FRWAY':'FWY',
    'FRWY':'FWY',
    'FRY':'FRY',
    'FT':'FT',
    'FWY':'FWY',
    'GARDEN':'GDN',
    'GARDENS':'GDNS',
    'GARDN':'GDN',
    'GATEWAY':'GTWY',
    'GATEWY':'GTWY',
    'GATWAY':'GTWY',
    'GDN':'GDN',
    'GDNS':'GDNS',
    'GLEN':'GLN',
    'GLENS':'GLNS',
    'GLN':'GLN',
    'GLNS':'GLNS',
    'GRDEN':'GDN',
    'GRDN':'GDN',
    'GRDNS':'GDNS',
    'GREEN':'GRN',
    'GREENS':'GRNS',
    'GRN':'GRN',
    'GRNS':'GRNS',
    'GROV':'GRV',
    'GROVE':'GRV',
    'GROVES':'GRVS',
    'GRV':'GRV',
    'GRVS':'GRVS',
    'GTWAY':'GTWY',
    'GTWY':'GTWY',
    'HARB':'HBR',
    'HARBOR':'HBR',
    'HARBORS':'HBRS',
    'HARBR':'HBR',
    'HAVEN':'HVN',
    'HBR':'HBR',
    'HBRS':'HBRS',
    'HEIGHTS':'HTS',
    'HIGHWAY':'HWY',
    'HIGHWY':'HWY',
    'HILL':'HL',
    'HILLS':'HLS',
    'HIWAY':'HWY',
    'HIWY':'HWY',
    'HL':'HL',
    'HLLW':'HOLW',
    'HLS':'HLS',
    'HOLLOW':'HOLW',
    'HOLLOWS':'HOLW',
    'HOLW':'HOLW',
    'HOLWS':'HOLW',
    'HRBOR':'HBR',
    'HT':'HTS',
    'HTS':'HTS',
    'HVN':'HVN',
    'HWAY':'HWY',
    'HWY':'HWY',
    'INLET':'INLT',
    'INLT':'INLT',
    'IS':'IS',
    'ISLAND':'IS',
    'ISLANDS':'ISS',
    'ISLE':'ISLE',
    'ISLES':'ISLE',
    'ISLND':'IS',
    'ISLNDS':'ISS',
    'ISS':'ISS',
    'JCT':'JCT',
    'JCTION':'JCT',
    'JCTN':'JCT',
    'JCTNS':'JCTS',
    'JCTS':'JCTS',
    'JUNCTION':'JCT',
    'JUNCTIONS':'JCTS',
    'JUNCTN':'JCT',
    'JUNCTON':'JCT',
    'KEY':'KY',
    'KEYS':'KYS',
    'KNL':'KNL',
    'KNLS':'KNLS',
    'KNOB':'KNOB',
    'KNOL':'KNL',
    'KNOLL':'KNL',
    'KNOLLS':'KNLS',
    'KY':'KY',
    'KYS':'KYS',
    'LAKE':'LK',
    'LAKES':'LKS',
    'LAND':'LAND',
    'LANDING':'LNDG',
    'LANE':'LN',
    'LCK':'LCK',
    'LCKS':'LCKS',
    'LDG':'LDG',
    'LDGE':'LDG',
    'LF':'LF',
    'LGT':'LGT',
    'LGTS':'LGTS',
    'LIGHT':'LGT',
    'LIGHTS':'LGTS',
    'LK':'LK',
    'LKS':'LKS',
    'LN':'LN',
    'LNDG':'LNDG',
    'LNDNG':'LNDG',
    'LOAF':'LF',
    'LOCK':'LCK',
    'LOCKS':'LCKS',
    'LODG':'LDG',
    'LODGE':'LDG',
    'LOOP':'LOOP',
    'LOOPS':'LOOP',
    'MALL':'MALL',
    'MANOR':'MNR',
    'MANORS':'MNRS',
    'MDW':'MDWS',
    'MDWS':'MDWS',
    'MEADOW':'MDW',
    'MEADOWS':'MDWS',
    'MEDOWS':'MDWS',
    'MEWS':'MEWS',
    'MILL':'ML',
    'MILLS':'MLS',
    'MISSION':'MSN',
    'MISSN':'MSN',
    'ML':'ML',
    'MLS':'MLS',
    'MNR':'MNR',
    'MNRS':'MNRS',
    'MNT':'MT',
    'MNTAIN':'MTN',
    'MNTN':'MTN',
    'MNTNS':'MTNS',
    'MOTORWAY':'MTWY',
    'MOUNT':'MT',
    'MOUNTAIN':'MTN',
    'MOUNTAINS':'MTNS',
    'MOUNTIN':'MTN',
    'MSN':'MSN',
    'MSSN':'MSN',
    'MT':'MT',
    'MTIN':'MTN',
    'MTN':'MTN',
    'MTNS':'MTNS',
    'MTWY':'MTWY',
    'NCK':'NCK',
    'NECK':'NCK',
    'OPAS':'OPAS',
    'ORCH':'ORCH',
    'ORCHARD':'ORCH',
    'ORCHRD':'ORCH',
    'OVAL':'OVAL',
    'OVERPASS':'OPAS',
    'OVL':'OVAL',
    'PARK':'PARK',
    'PARKS':'PARK',
    'PARKWAY':'PKWY',
    'PARKWAYS':'PKWY',
    'PARKWY':'PKWY',
    'PASS':'PASS',
    'PASSAGE':'PSGE',
    'PATH':'PATH',
    'PATHS':'PATH',
    'PIKE':'PIKE',
    'PIKES':'PIKE',
    'PINE':'PNE',
    'PINES':'PNES',
    'PKE':'PIKE',
    'PKWAY':'PKWY',
    'PKWY':'PKWY',
    'PKWYS':'PKWY',
    'PKY':'PKWY',
    'PL':'PL',
    'PLACE':'PL',
    'PLAIN':'PLN',
    'PLAINS':'PLNS',
    'PLAZA':'PLZ',
    'PLN':'PLN',
    'PLNS':'PLNS',
    'PLZ':'PLZ',
    'PLZA':'PLZ',
    'PNE':'PNE',
    'PNES':'PNES',
    'POINT':'PT',
    'POINTE':'PT',
    'POINTS':'PTS',
    'PORT':'PRT',
    'PORTS':'PRTS',
    'PR':'PR',
    'PRAIRIE':'PR',
    'PRK':'PARK',
    'PRR':'PR',
    'PRT':'PRT',
    'PRTS':'PRTS',
    'PSGE':'PSGE',
    'PT':'PT',
    'PTS':'PTS',
    'RAD':'RADL',
    'RADIAL':'RADL',
    'RADIEL':'RADL',
    'RADL':'RADL',
    'RAMP':'RAMP',
    'RANCH':'RNCH',
    'RANCHES':'RNCH',
    'RAPID':'RPD',
    'RAPIDS':'RPDS',
    'RD':'RD',
    'RDG':'RDG',
    'RDGE':'RDG',
    'RDGS':'RDGS',
    'RDS':'RDS',
    'REST':'RST',
    'RETREAT':'RTT',
    'RIDGE':'RDG',
    'RIDGES':'RDGS',
    'RISE':'RISE',
    'RIV':'RIV',
    'RIVER':'RIV',
    'RIVR':'RIV',
    'RNCH':'RNCH',
    'RNCHS':'RNCH',
    'ROAD':'RD',
    'ROADS':'RDS',
    'ROUTE':'RTE',
    'ROW':'ROW',
    'RPD':'RPD',
    'RPDS':'RPDS',
    'RST':'RST',
    'RTE':'RTE',
    'RTT':'RTT',
    'RUE':'RUE',
    'RUN':'RUN',
    'RVR':'RIV',
    'SHCT':'SHCT',
    'SHL':'SHL',
    'SHLS':'SHLS',
    'SHOAL':'SHL',
    'SHOALS':'SHLS',
    'SHOAR':'SHR',
    'SHOARS':'SHRS',
    'SHORE':'SHR',
    'SHORES':'SHRS',
    'SHR':'SHR',
    'SHRS':'SHRS',
    'SKWY':'SKWY',
    'SKYWAY':'SKWY',
    'SMT':'SMT',
    'SPG':'SPG',
    'SPGS':'SPGS',
    'SPNG':'SPG',
    'SPNGS':'SPGS',
    'SPRING':'SPG',
    'SPRINGS':'SPGS',
    'SPRNG':'SPG',
    'SPRNGS':'SPGS',
    'SPUR':'SPUR',
    'SPURS':'SPUR',
    'SQ':'SQ',
    'SQR':'SQ',
    'SQRE':'SQ',
    'SQRS':'SQS',
    'SQS':'SQS',
    'SQU':'SQ',
    'SQUARE':'SQ',
    'SQUARES':'SQS',
    'ST':'ST',
    'STA':'STA',
    'STATION':'STA',
    'STATN':'STA',
    'STN':'STA',
    'STR':'ST',
    'STRA':'STRA',
    'STRAV':'STRA',
    'STRAVEN':'STRA',
    'STRAVENUE':'STRA',
    'STRAVN':'STRA',
    'STREAM':'STRM',
    'STREET':'ST',
    'STREETS':'STS',
    'STREME':'STRM',
    'STRM':'STRM',
    'STRT':'ST',
    'STRVN':'STRA',
    'STRVNUE':'STRA',
    'STS':'STS',
    'SUMIT':'SMT',
    'SUMITT':'SMT',
    'SUMMIT':'SMT',
    'TER':'TER',
    'TERR':'TER',
    'TERRACE':'TER',
    'THROUGHWAY':'TRWY',
    'TPKE':'TPKE',
    'TRACE':'TRCE',
    'TRACES':'TRCE',
    'TRACK':'TRAK',
    'TRACKS':'TRAK',
    'TRAFFICWAY':'TRFY',
    'TRAIL':'TRL',
    'TRAILER':'TRLR',
    'TRAILS':'TRL',
    'TRAK':'TRAK',
    'TRC':'TRCE',
    'TRCE':'TRCE',
    'TRFY':'TRFY',
    'TRK':'TRAK',
    'TRKS':'TRAK',
    'TRL':'TRL',
    'TRLR':'TRLR',
    'TRLRS':'TRLR',
    'TRLS':'TRL',
    'TRNPK':'TPKE',
    'TRWY':'TRWY',
    'TUNEL':'TUNL',
    'TUNL':'TUNL',
    'TUNLS':'TUNL',
    'TUNNEL':'TUNL',
    'TUNNELS':'TUNL',
    'TUNNL':'TUNL',
    'TURNPIKE':'TPKE',
    'TURNPK':'TPKE',
    'UN':'UN',
    'UNDERPASS':'UPAS',
    'UNION':'UN',
    'UNIONS':'UNS',
    'UNS':'UNS',
    'UPAS':'UPAS',
    'VALLEY':'VLY',
    'VALLEYS':'VLYS',
    'VALLY':'VLY',
    'VDCT':'VIA',
    'VIA':'VIA',
    'VIADCT':'VIA',
    'VIADUCT':'VIA',
    'VIEW':'VW',
    'VIEWS':'VWS',
    'VILL':'VLG',
    'VILLAG':'VLG',
    'VILLAGE':'VLG',
    'VILLAGES':'VLGS',
    'VILLE':'VL',
    'VILLG':'VLG',
    'VILLIAGE':'VLG',
    'VIS':'VIS',
    'VIST':'VIS',
    'VISTA':'VIS',
    'VL':'VL',
    'VLG':'VLG',
    'VLGS':'VLGS',
    'VLLY':'VLY',
    'VLY':'VLY',
    'VLYS':'VLYS',
    'VST':'VIS',
    'VSTA':'VIS',
    'VW':'VW',
    'VWS':'VWS',
    'WALK':'WALK',
    'WALKS':'WALK',
    'WALL':'WALL',
    'WAY':'WAY',
    'WAYS':'WAYS',
    'WELL':'WL',
    'WELLS':'WLS',
    'WL':'WL',
    'WLS':'WLS',
    'WY':'WAY',
    'XING':'XING',
    'XRD':'XRD',
    'XRDS':'XRDS'
}"""

# Codeblocks:
AddrLabel = """def LabelOut(UNIT_NUM, STREET, STNUM, STNUMSUF, BLDG, UNIT_TYPE):
    STREET = STREET.strip()
    STNUM = STNUM.strip()
    BLDG = BLDG.strip()
    UNIT_TYPE = UNIT_TYPE.strip()
    UNIT_NUM = UNIT_NUM.strip()
    Labout = STREET +' '+ STNUM
    if (STREET =='ANCIENT CREST CIR') and (int(STNUM) >9999) and (int(STNUM) <15000) and (UNIT_NUM is not None and UNIT_NUM <> ''):
        Labout = STREET +' '+ UNIT_NUM
    else:
        if (STNUMSUF is not None and STNUMSUF <> ''):
            Labout = Labout + STNUMSUF
        if (BLDG is not None and BLDG <> ''):
            Labout = Labout +' '+ BLDG
        if (UNIT_TYPE is not None and UNIT_NUM is not None):
            Labout = Labout +' '+ UNIT_TYPE +' '+ UNIT_NUM
    Labout = Labout.strip()
    while '  ' in Labout:
        Labout = Labout.replace('  ',' ')
    return Labout"""

BldgNum = """def BldgNum(BUILDING, UNIT_TYPE, UNIT_NUM):
    if BUILDING is None:
        BldgVal = ''
    else:
        BldgVal = BUILDING
    if (UNIT_TYPE=='BLDG' or UNIT_TYPE=='BLGD'):
        BldgVal = UNIT_NUM
    elif 'BUILDING' in BldgVal:
        BldgVal = BldgVal.replace('BUILDING','').strip()
    elif 'BLDG' in BldgVal:
        BldgVal = BldgVal.replace('BLDG','').strip()
    if ' ' in BldgVal or len(BldgVal )>4:
        BldgVal = ''
    return BldgVal"""

UnitType = """def UnitType(UNIT_TYPE):
    if UNIT_TYPE is None:
        TypeVal = ''
    else:
        TypeVal = UNIT_TYPE
        if ('BLDG' in TypeVal or 'BLGD' in TypeVal or 'BUILDING' in TypeVal):
            TypeVal = ''
    return TypeVal"""

UnitNum = """def UnitNum(UNIT_TYPE, UNIT_NUM):
    if (UNIT_TYPE is None or UNIT_NUM is None):
        UnitVal = ''
    else:
        TypeVal = UNIT_TYPE
        UnitVal = UNIT_NUM
        if ('BLDG' in TypeVal or 'BLGD' in TypeVal or 'BUILDING' in TypeVal):
            UnitVal = ''
    return UnitVal"""

BWStreetNames = """def BWStreetNames(StreetName):
    StreetName = StreetName.strip()
    if StreetName.endswith(' CLOSE'):
        StreetName = StreetName.replace(' CLOSE',' CL')
    return StreetName"""

City_Codes = CityList + "\\n" + """def myCity(cityVal):
    cityVal = cityVal.upper()
    cityCode = CityList.get(cityVal, cityVal[:10])
    return cityCode"""

County_Codes = CountyList + "\\n" + """def myCounty(countyVal):
    countyVal = countyVal.upper()
    CountyCode = CountyList.get(countyVal, countyVal[:5])
    return CountyCode"""

GetLawCode = """def GetLawCode(SPAEK,OIRID):
    LawCode = SPAEK
    if (OIRID[:5] <> 'WILLI'):
        TowCode = ''
    elif ('LFK' in LawCode):
        TowCode = 'TOW_FRANKLIN'
    elif ('LFV' in LawCode):
        TowCode = 'TOW_FAIRVIEW'
    elif ('LNV' in LawCode):
        TowCode = 'TOW_NOLV'
    elif ('LSH' in LawCode):
        TowCode = 'TOW_SH'
    elif ('LWCZ2' in LawCode):
        TowCode = 'TOW_WC2'
    else:
        TowCode = 'TOW_WC'
    return TowCode"""

GetGeoName = """def GetName(PREDIR='',PRETYPE='',NAME='',TYPE='',SUFDIR='',DIRECTION='',CFCC='',EXITNUM='',RAMPDIR=''):
    if (PRETYPE.strip() == 'I'):
        SName=(PREDIR+PRETYPE+NAME+DIRECTION).strip()
        if (CFCC == 'A63'):
            SName = (SName+' '+EXITNUM+' '+RAMPDIR).strip()
    elif (CFCC == 'A63'):
            SName = (PREDIR+' '+PRETYPE+' '+NAME+' '+TYPE+' '+SUFDIR+' '+DIRECTION+' '+EXITNUM+' '+RAMPDIR).strip()
    elif ((NAME + ' ' + TYPE).strip() in ['NAME NM','ALLEY ALY','ACCESS RD','ACCESS'] or TYPE.strip() == 'EMAC'):
        SName='UNNAMED STREET'
    else:
        SName= (PREDIR+' '+ PRETYPE+' '+ NAME+' '+ TYPE+' '+ SUFDIR).strip()
    if ( NAME[:6] == 'MOUNT '):
        SName = SName.replace('MOUNT ','MT ')
    if ('HIGHWAY' in SName):
        SName = SName.replace('HIGHWAY','HWY')
    if ('CLOSE CL' in SName):
        SName = SName.replace('CLOSE CL','CL')
    while ('  ' in SName):
        SName = SName.replace('  ',' ')
    return SName"""

GetTriTechName = """def GetName(PRETYPE,STREET,DIRECTION,CFCC):
    SName = STREET
    DIRECTION = (DIRECTION or '').strip()
    if (PRETYPE.strip()<>'I' and CFCC<>'A63' and SName<>'UNNAMED STREET' and DIRECTION <>''):
        SName = (SName+' '+DIRECTION).strip()
        while ('  ' in SName):
            SName = SName.replace('  ',' ')
    return SName"""

LocName = """def LocName(StreetName, Address, Apartment):
    Labout = StreetName.strip()+' '+ str(Address)+' '+ Apartment.strip()
    while ('  ' in Labout):
        Labout = Labout.replace('  ',' ')
    return Labout"""

RouteStr = """def RouteStr(Ref_ID, ROUTINGSTR, County):
    if (County!='WM' and County!='MAUSH'):
        return ''
    else:
        output = ROUTINGSTR
        if ((output is None or output.strip() =='' or output == '-1' or len(output)>36) ):
            output = Ref_ID
        elif not (output.startswith('WILLIAMSON_')):
            output = Ref_ID
        if ((output is None or output.strip() =='' or output == '-1' or len(output)>36) ):
            output = ''
        return output"""

Street_Names = StTypes + """
def GetType(StrType,StrName):
    StrType=StrType.strip().upper()
    StrName=StrName.strip().upper()
    for typename in StTypes:
        if (StTypes.get(typename) == StTypes.get(StrType)):
            if StrName.endswith(' '+typename):
                StrName=StrName.replace(' '+typename,'')
                break
    StrName=StrName.strip()
    return StrName"""

Street_Types = StTypes + """
def GetType(StrType,StrName):
    StrType=StrType.strip().upper()
    StrName=StrName.strip().upper()
    if (StrType in StTypes):
        StrType = StTypes.get(StrType)
    elif (StrType == '' or StrType == 'None'):
        for type in StTypes:
            if StrName.endswith(' '+type):
                StrType = StTypes.get(type)
                break
    if StrType == 'None':
        StrType = ''
    return StrType"""

StreetName = """def StreetName(PREDIR, PRETYPE, NAME, TYPE, SUFDIR):
    SName = PREDIR.strip()+' '+PRETYPE.strip()+' '+ NAME.strip()+' '+ TYPE.strip()+' '+ SUFDIR.strip()
    SName = SName.strip()
    if (SName[:6] == 'MOUNT '):
        SName = SName.replace('MOUNT ', 'MT ')
    if ('HIGHWAY' in SName):
        SName = SName.replace('HIGHWAY', 'HWY')
    if ('MACK HATCHER PKWY' in SName):
        SName = SName.replace('MACK HATCHER PKWY','MACK HATCHER MEMORIAL PKWY')
    while ('  ' in SName):
        SName = SName.replace('  ',' ')
    return SName"""

# Custom Functions:
def FieldMap(feature):
    fieldMappings = arcpy.FieldMappings()
    fieldMappings.removeAll()
    if (feature == "WaterPoly"):
        # Feature classes to be merged
        lakes = williamson_lake_pond
        rivers = williamson_riverpoly
        # Add input fields "STREET_NAM" & "NM" into new output field
        fldMap = arcpy.FieldMap()
        fldMap.removeAll()
        fldMap.addInputField(lakes,"LAKE_NAME")
        fldMap.addInputField(rivers,"RIVER_NAME")
        # Set name of new output field "Street_Name"
        fldName = fldMap.outputField
        fldName.name = "NAME"
        fldName.aliasName = fldName.name
        fldMap.outputField = fldName
        # Add output field to field mappings object
        fieldMappings.addFieldMap(fldMap)
    elif (feature == "WaterLine"):
        # Feature classes to be merged
        streams = williamson_streams
        rivers = williamson_rivers
        # Add all fields from both streams and rivers
        fieldMappings.addTable(streams)
        fieldMappings.addTable(rivers)
        # Add input fields "STREET_NAM" & "NM" into new output field
        fldMap = arcpy.FieldMap()
        fldMap.removeAll()
        fldMap.addInputField(streams,"WTR_NM")
        fldMap.addInputField(rivers,"RIVER_NAME")
        # Set name of new output field "Street_Name"
        fldName = fldMap.outputField
        fldName.name = "NAME"
        fldName.aliasName = fldName.name
        fldMap.outputField = fldName
        # Add output field to field mappings object
        fieldMappings.addFieldMap(fldMap)
        # Remove all output fields from the field mappings, except fields "Street_Class", "Street_Name", & "Distance"
        for field in fieldMappings.fields:
            if field.name <> "NAME":
                fieldMappings.removeFieldMap(fieldMappings.findFieldMapIndex(field.name))
    elif (feature == "Ramps"):
        # Feature classes to be merged
        streets = GDB_Scratch + "\\Centerlines_Merged"
        ramps = static_Ramps
        # Add all fields from both streets and ramps
        fieldMappings.addTable(streets)
        fieldMappings.addTable(ramps)
        # Remove all output fields from the field mappings, except fields "Street_Class", "Street_Name", & "Distance"
        for field in fieldMappings.fields:
            if field.name not in ["OIRID","SEGID","L_F_ADD","L_T_ADD","R_F_ADD","R_T_ADD","PREDIR","PRETYPE","NAME","TYPE","SUFDIR","LABEL","VANITY","CFCC","ZIP_L","ZIP_R","CITY_L","CITY_R","COUNTY_L","COUNTY_R","STATE_L","STATE_R","SPDLIMIT","ONEWAY","T_ELEV","F_ELEV","STREET","LEFT_ZONE","RIGHT_ZONE","DIRECTION","SUBNAME","EXITNUM","RAMPDIR"]:
                fieldMappings.removeFieldMap(fieldMappings.findFieldMapIndex(field.name))
    elif (feature == "Mile Markers"):
        mmI = static_MileMarkers
        mmN = static_NatchezMM
        fieldMappings.addTable(mmI)
        fieldMappings.addTable(mmN)
    elif (feature == "Neighborhood"):
        fieldMappings.addTable(GDB_Scratch + "\\Neighborhoods")
        fldMap = arcpy.FieldMap()
        fldMap.removeAll()
        fldMap.addInputField(GDB_Scratch + "\\Neighborhoods", "L_Neighborhood")
        fldMap.addInputField(GDB_Scratch + "\\Neighborhoods", "R_Neighborhood")
        fldMap.mergeRule = "First"
        fldOut = fldMap.outputField
        fldOut.name = "Neighborhood"
        fldOut.aliasName = fldOut.name
        fldOut.type = "Text"
        fldOut.length = 50
        fldMap.outputField = fldOut
        fieldMappings.addFieldMap(fldMap)
        for field in fieldMappings.fields:
            if (field.name <> "Neighborhood"):
                fieldMappings.removeFieldMap(fieldMappings.findFieldMapIndex(field.name))
    elif (feature == "Law_RA"):
        # Feature classes to be merged
        streets = GDB_Scratch + "\\Centerlines_SpatialJoin"
        lawRAs = tritech_LawAreas
        # Add all fields from both streets and lawRAs
        fieldMappings.addTable(streets)
        fieldMappings.addTable(lawRAs)
        # Add input fields "STREET_NAM" & "NM" into new output field
        fldMap = arcpy.FieldMap()
        fldMap.removeAll()
        fldMap.addInputField(lawRAs,"Code")
        fldMap.joinDelimiter = ";"
        fldMap.mergeRule = "Join"
        # Set name of new output field "Street_Name"
        fldName = fldMap.outputField
        fldName.name = "LeftServiceProviderAreaExtKey"
        fldName.aliasName = fldName.name
        fldName.type = "Text"
        fldName.length = 36
        fldMap.outputField = fldName
        # Add output field to field mappings object
        fieldMappings.addFieldMap(fldMap)
        # Add input fields "STREET_NAM" & "NM" into new output field
        fldMap = arcpy.FieldMap()
        fldMap.removeAll()
        fldMap.addInputField(lawRAs,"Code")
        # Set name of new output field "Street_Name"
        fldName = fldMap.outputField
        fldName.name = "RightServiceProviderAreaExtKey"
        fldName.aliasName = fldName.name
        fldName.type = "Text"
        fldName.length = 36
        fldMap.outputField = fldName
        # Add output field to field mappings object
        fieldMappings.addFieldMap(fldMap)
        # Remove all output fields from the field mappings, except fields "Street_Class", "Street_Name", & "Distance"
        for field in fieldMappings.fields:
            if field.name not in ["OIRID","SEGID","L_F_ADD","L_T_ADD","R_F_ADD","R_T_ADD","ADDR_TYPE","PREDIR","PRETYPE","NAME","TYPE","SUFDIR","POSTMOD","LABEL","VANITY","NAMETYPE","CFCC","ESN_L","ESN_R","ZIP_L","ZIP_R","CITY_L","CITY_R","COUNTY_L","COUNTY_R","STATE_L","STATE_R","SPDLIMIT","ONEWAY","LANES","T_ELEV","F_ELEV","TFCOST","FTCOST","EDITOR","GEOMOD","GEOSRCE","GEODATE","ATTMOD","ATTSRCE","ATTDATE","STATUS","CLASS","STREET","LEFT_ZONE","RIGHT_ZONE","ALT_NAME","ALT_NAME2","ALT_NAME3","SID","NOTES","ROUTE_NO","ROUTE_STAT","GEO_STAT","ID","STRAITNESS","ERRORCODE","IG_ERRORCO","VERTEX","SUBNETSIZE","SUBNETID","X_DN_P_SN","ODD","PLID","DIRECTION","TRITECH_ALIAS","SUBNAME","EXITNUM","RAMPDIR","LeftServiceProviderAreaExtKey","RightServiceProviderAreaExtKey"]:
                fieldMappings.removeFieldMap(fieldMappings.findFieldMapIndex(field.name))
    elif (feature == "Centerline_Rename"):
        # Feature classes to be merged
        schema = static_CenterlineSchema
        streets = GDB_Scratch + "\\Centerlines_Merge"
        # Add all fields from both schema and streets
        fieldMappings.addTable(schema)
        fieldMappings.addTable(streets)
        for fldMap in fieldMappings.fieldMappings:
            newMap = fldMap
            removeFld = 0
            if (newMap.outputField.name == "ExternalStreetKey"):
                newMap.addInputField(streets,"OIRID")
            elif (newMap.outputField.name == "StreetName"):
                newMap.addInputField(streets,"StreetName")
            elif (newMap.outputField.name == "LeftFromAddress"):
                newMap.addInputField(streets,"L_F_ADD")
            elif (newMap.outputField.name == "LeftToAddress"):
                newMap.addInputField(streets,"L_T_ADD")
            elif (newMap.outputField.name == "RightFromAddress"):
                newMap.addInputField(streets,"R_F_ADD")
            elif (newMap.outputField.name == "RightToAddress"):
                newMap.addInputField(streets,"R_T_ADD")
            elif (newMap.outputField.name == "LeftParity"):
                {}
            elif (newMap.outputField.name == "RightParity"):
                {}
            elif (newMap.outputField.name == "LeftCityCode"):
                newMap.addInputField(streets,"CITY_L")
            elif (newMap.outputField.name == "RightCityCode"):
                newMap.addInputField(streets,"CITY_R")
            elif (newMap.outputField.name == "LeftZipCode"):
                newMap.addInputField(streets,"ZIP_L")
            elif (newMap.outputField.name == "RightZipCode"):
                newMap.addInputField(streets,"ZIP_R")
            elif (newMap.outputField.name == "LeftServiceProviderAreaExtKey"):
                newMap.addInputField(streets,"LeftServiceProviderAreaExtKey")
            elif (newMap.outputField.name == "RightServiceProviderAreaExtKey"):
                newMap.addInputField(streets,"RightServiceProviderAreaExtKey")
            elif (newMap.outputField.name == "LeftCountyCode"):
                newMap.addInputField(streets,"COUNTY_L")
            elif (newMap.outputField.name == "RightCountyCode"):
                newMap.addInputField(streets,"COUNTY_R")
            elif (newMap.outputField.name == "LeftState"):
                newMap.addInputField(streets,"STATE_L")
            elif (newMap.outputField.name == "RightState"):
                newMap.addInputField(streets,"STATE_R")
            elif (newMap.outputField.name == "FeatureTypeCode"):
                newMap.addInputField(streets,"CFCC")
            elif (newMap.outputField.name == "SpeedLimit"):
                newMap.addInputField(streets,"SPDLIMIT")
            elif (newMap.outputField.name == "OneWayCode"):
                newMap.addInputField(streets,"ONEWAY")
            elif (newMap.outputField.name == "FromElevation"):
                newMap.addInputField(streets,"F_ELEV")
            elif (newMap.outputField.name == "ToElevation"):
                newMap.addInputField(streets,"T_ELEV")
            elif (newMap.outputField.name == "LocationName"):
                {}
            elif (newMap.outputField.name == "RoutingStreetExtKey"):
                newMap.addInputField(streets,"SEGID")
            elif (newMap.outputField.name == "L_Neighborhood"):
                newMap.addInputField(streets,"SUBNAME")
            elif (newMap.outputField.name == "R_Neighborhood"):
                newMap.addInputField(streets,"SUBNAME")
            elif (newMap.outputField.name == "PRETYPE"):
                {}
            elif (newMap.outputField.name == "DIRECTION"):
                {}
            else:
                removeFld = 1
            if (removeFld == 1):
                #arcpy.AddMessage("        Removing {0} field from Centerlines Field Map (index {1})".format(fldMap.outputField.name,fieldMappings.findFieldMapIndex(fldMap.outputField.name)))
                fieldMappings.removeFieldMap(fieldMappings.findFieldMapIndex(fldMap.outputField.name))
            else:
                #arcpy.AddMessage("        Including {0} field in Centerlines Field Map".format(fldMap.outputField.name))
                fieldMappings.replaceFieldMap(fieldMappings.findFieldMapIndex(fldMap.outputField.name),newMap)
    elif (feature == "Addresses"):
        # Feature classes to be merged
        bwAddr = GDB_Scratch + "\\BW_Address_CopyFeatures"
        milemarkers = GDB_Scratch + "\\Mile_Markers_Merge"
        wcAddr = GDB_Scratch + "\\County_Addr"
        surrAddr = GDB_Scratch + "\\surround_addr"
        # Add all fields
        fieldMappings.addTable(bwAddr)
        fieldMappings.addTable(milemarkers)
        fieldMappings.addTable(wcAddr)
        fieldMappings.addTable(surrAddr)
        for fldMap in fieldMappings.fieldMappings:
            newMap = fldMap
            removeFld = 0
            if (newMap.outputField.name == "ExternalKey"):
                newMap.addInputField(surrAddr,"OIRID")
                newMap.addInputField(wcAddr,"OIRID")
            elif (newMap.outputField.name == "StreetName"):
                newMap.addInputField(surrAddr,"STREET")
                newMap.addInputField(wcAddr,"STREET")
            elif (newMap.outputField.name == "Address"):
                newMap.addInputField(surrAddr,"STNUM")
                newMap.addInputField(wcAddr,"STNUM")
            elif (newMap.outputField.name == "Building"):
                newMap.addInputField(surrAddr,"BUILDING")
                newMap.addInputField(wcAddr,"BUILDING")
            elif (newMap.outputField.name == "Apartment"):
                newMap.addInputField(surrAddr,"UNIT_NUM")
                newMap.addInputField(wcAddr,"UNIT_NUM")
            elif (newMap.outputField.name == "CityCode"):
                newMap.addInputField(surrAddr,"CITY")
                newMap.addInputField(wcAddr,"CITY")
            elif (newMap.outputField.name == "ZipCode"):
                newMap.addInputField(surrAddr,"ZIP")
                newMap.addInputField(wcAddr,"ZIP")
            elif (newMap.outputField.name == "ServiceProviderAreaExtKey"):
                {}
            elif (newMap.outputField.name == "CountyCode"):
                newMap.addInputField(surrAddr,"COUNTY")
                newMap.addInputField(wcAddr,"COUNTY")
            elif (newMap.outputField.name == "State"):
                newMap.addInputField(surrAddr,"STATE")
                newMap.addInputField(wcAddr,"STATE")
            elif (newMap.outputField.name == "LocationName"):
                newMap.addInputField(surrAddr,"LABEL")
                newMap.addInputField(wcAddr,"LABEL")
            elif (newMap.outputField.name == "RoutingStreetExtKey"):
                newMap.addInputField(surrAddr,"R_SEGID")
                newMap.addInputField(wcAddr,"R_SEGID")
            elif (newMap.outputField.name == "Neighborhood"):
                newMap.addInputField(surrAddr,"SUBNAME")
                newMap.addInputField(wcAddr,"SUBNAME")
            elif (newMap.outputField.name == "MajorRoad"):
                newMap.addInputField(wcAddr,"MajorRoad")
            else:
                removeFld = 1
            if (removeFld == 1):
                #arcpy.AddMessage("        Removing {0} field from Addresses Field Map (index {1})".format(fldMap.outputField.name,fieldMappings.findFieldMapIndex(fldMap.outputField.name)))
                fieldMappings.removeFieldMap(fieldMappings.findFieldMapIndex(fldMap.outputField.name))
            else:
                #arcpy.AddMessage("        Including {0} field in Addresses Field Map".format(fldMap.outputField.name))
                fieldMappings.replaceFieldMap(fieldMappings.findFieldMapIndex(fldMap.outputField.name),newMap)
    elif (feature == "Parcels"):
        # Feature classes to be merged
        wc_parcel = williamson_parcels
        maury_parcel = GDB_County + r'\parcels_cama_a'
        # Add all fields from both
        fieldMappings.addTable(wc_parcel)
        fieldMappings.addTable(maury_parcel)
        for fldMap in fieldMappings.fieldMappings:
            newMap = fldMap
            removeFld = False
            updFld = newMap.outputField
            if (newMap.outputField.name == "ADDRESS"):
                updFld.length = 68
                newMap.addInputField(maury_parcel,"ADDRESS")
            elif (newMap.outputField.name == "owner1"):
                updFld.length = 40
                newMap.addInputField(maury_parcel,"OWNER")
            elif (newMap.outputField.name == "owner2"):
                updFld.length = 40
                newMap.addInputField(maury_parcel,"OWNER2")
            elif (newMap.outputField.name == "own_street"):
                updFld.length = 80
                newMap.addInputField(maury_parcel,"MAILADDR")
            elif (newMap.outputField.name == "own_city"):
                updFld.length = 40
                newMap.addInputField(maury_parcel,"MAILCITY")
            elif (newMap.outputField.name == "own_state"):
                newMap.addInputField(maury_parcel,"STATE")
            elif (newMap.outputField.name == "own_zip"):
                updFld.length = 10
                newMap.addInputField(maury_parcel,"ZIP")
            else:
                removeFld = True
            newMap.outputField = updFld
            if (removeFld):
                #arcpy.AddMessage("        Removing {0} field from Parcel Field Map (index {1})".format(fldMap.outputField.name,fieldMappings.findFieldMapIndex(fldMap.outputField.name)))
                fieldMappings.removeFieldMap(fieldMappings.findFieldMapIndex(fldMap.outputField.name))
            else:
                #arcpy.AddMessage("        Including {0} field in Parcel Field Map".format(fldMap.outputField.name))
                fieldMappings.replaceFieldMap(fieldMappings.findFieldMapIndex(fldMap.outputField.name),newMap)
    else:
        print "Feature Field Map Not Found For Feature \""+feature+"\""
        arcpy.AddError("Feature Field Map Not Found For {0}".format(feature))
    return fieldMappings
def RemoveNULL(feature):
    fieldList = arcpy.ListFields(feature)
    for field in fieldList:
        #arcpy.AddMessage("        Removing NULL values from field {0} in feature {1}".format(field.name, arcpy.Describe(feature).name))
        if (field.type == "String"):
            expression = """(!{}! or "").strip()""".format(field.name)
            arcpy.CalculateField_management(feature, field.name, expression, "PYTHON_9.3")
        elif (field.type == "Integer"):
            expression = "noNull(!{}!)".format(field.name)
            codeblock = """def noNull(value):
                if value is None:
                    return 0
                else:
                    return value"""
            arcpy.CalculateField_management(feature, field.name, expression, "PYTHON_9.3", codeblock)
    return

# Processing:
if (copyDisplayLayers == 'true'):
    arcpy.AddMessage("Copying sources to Display Layers...")
    # Process: Copy Water Districts to Display_Layers
    arcpy.AddMessage("    Copying Water Districts to Display_Layers")
    arcpy.Dissolve_management(static_watdist, display_WaterDistricts, "WATER_UTIL", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy Sewer to Display_Layers
    arcpy.AddMessage("    Copying Sewer to Display_Layers")
    arcpy.Dissolve_management(static_septic, display_Sewer, "SEPTIC_TEX", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy Electric Co to Display_Layers
    arcpy.AddMessage("    Copying Electric Co to Display_Layers")
    arcpy.Dissolve_management(static_electric, display_Electric, "ELECTRIC_U", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy Cable TV to Display_Layers
    arcpy.AddMessage("    Copying Cable TV to Display_Layers")
    arcpy.Dissolve_management(static_catv, display_Cable, "CABLE_TEXT", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy City_Limits to Display_Layers
    arcpy.AddMessage("    Copying City_Limits to Display_Layers")
    arcpy.CopyFeatures_management(GDB_County + "\\corps", GDB_Scratch + r'\corps')
    arcpy.CopyFeatures_management(GDB_County + r'\SH_City_Limits', GDB_Scratch + r'\corps_SH')
    arcpy.MakeFeatureLayer_management(GDB_Scratch + r'\corps','SPRING HILL',"NAME = 'SPRING HILL'")
    arcpy.DeleteFeatures_management('SPRING HILL')
    arcpy.AlignFeatures_edit(GDB_Scratch + r'\corps', GDB_Scratch + r'\corps_SH', '75 Feet', '#')
    arcpy.Merge_management([GDB_Scratch + r'\corps', GDB_Scratch + r'\corps_SH'], GDB_Scratch + r'\corps_merge', 'NAME "NAME" true true false 40 Text 0 0 ,First,#,corps,NAME,-1,-1')
    arcpy.CalculateField_management(GDB_Scratch + r'\corps_merge',"NAME","'SPRING HILL' if (!NAME! is None) else !NAME!","PYTHON_9.3")
    arcpy.Dissolve_management(GDB_Scratch + r'\corps_merge', display_CityLimits, "NAME", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy ESN to Display_Layers
    arcpy.AddMessage("    Copying ESN to Display_Layers")
    arcpy.AddSpatialIndex_management(TIPS_ESN, 0, 0, 0)
    arcpy.Dissolve_management(TIPS_ESN, display_ESN, "ESN;PSAPID;LE;FD;EMS", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy RiverMileMarkers to Display_Layers
    arcpy.AddMessage("    Copying RiverMileMarkers to Display_Layers")
    arcpy.Dissolve_management(static_RiverMarkers, display_RiverMarkers, "Id;MILE;Type;Notes", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy Communities to Display_Layers
    arcpy.AddMessage("    Copying Communities to Display_Layers")
    arcpy.Dissolve_management(GDB_County + "\\comunity_94", display_Community, "COMMUNITY", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy EMS/Fire Areas to Display_Layers
    arcpy.AddMessage("    Copying EMS Areas to Display_Layers")
    arcpy.Dissolve_management(static_EMS, display_EMS, "Primary;Alternate;Supervisor", "", "SINGLE_PART", "DISSOLVE_LINES")
    arcpy.Dissolve_management(static_FKFD, display_FKFD, "Name;Code;Color", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy Sirens to Display_Layers
    arcpy.AddMessage("    Copying Sirens to Display_Layers")
    arcpy.SpatialJoin_analysis(williamson_sirens, static_SirenSectors, GDB_Scratch + r'\Sirens',"JOIN_ONE_TO_ONE","KEEP_ALL","#","WITHIN")
    arcpy.Dissolve_management(GDB_Scratch + r'\Sirens', display_Sirens, "Id;NUMBER;NAME;LOCATION;OTHER;ENTITY;SECTOR", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy AED Locations to Display_Layers
    arcpy.AddMessage("    Copying AED Locations to Display_Layers")
    arcpy.Dissolve_management(static_AED, display_AED, "Make;Model;Facility_Park;Address;Physical_Location;Notes;Serial_Num;Contact_Name;Phone_Number;Email", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy Cell Towers to Display_Layers
    arcpy.AddMessage("    Copying Cell Towers to Display_Layers")
    arcpy.Merge_management([TIPS_wcTowers, TIPS_surrTowers], GDB_Scratch + "\\cell_towers")
    arcpy.Integrate_management(GDB_Scratch + "\\cell_towers", '300 Feet')
    arcpy.Dissolve_management(GDB_Scratch + "\\cell_towers", display_CellTowers, 'CT_Cell_Company;CT_Address', 'CT_Lat MEAN;CT_Long MEAN', 'SINGLE_PART', 'DISSOLVE_LINES')
    # Process: Copy Lakes_Rivers to Display_Layers
    arcpy.AddMessage("    Copying Lakes_Rivers to Display_Layers")
    arcpy.Merge_management([GDB_County + "\\lake_pond_94", GDB_County + "\\riverpoly_94"], GDB_Scratch + "\\Lakes_Rivers", FieldMap("WaterPoly"))
    arcpy.Dissolve_management(GDB_Scratch + "\\Lakes_Rivers", display_Lakes, "NAME", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy Rivers_Streams to Display_Layers
    arcpy.AddMessage("    Copying Rivers_Streams to Display_Layers")
    arcpy.Merge_management([GDB_County + "\\stream_94", GDB_County + "\\river_94"] , GDB_Scratch + "\\Rivers_Streams", FieldMap("WaterLine"))
    arcpy.Dissolve_management(GDB_Scratch + "\\Rivers_Streams", display_Rivers, "NAME", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy Railroad to Display_Layers
    arcpy.AddMessage("    Copying Railroad to Display_Layers")
    arcpy.Dissolve_management(williamson_railroad, display_Railroad, "RAILROAD_N", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy Parks to Display_Layers
    arcpy.AddMessage("    Copying Parks to Display_Layers")
    arcpy.Dissolve_management(williamson_parks, display_Parks, "NAME;PROP_STREE", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy Parcels to Display_Layers
    arcpy.AddMessage("    Copying Parcels to Display_Layers")
    arcpy.MakeFeatureLayer_management(GDB_County + r'\parcels_cama_a', "Spring_Hill_Parcels")
    arcpy.SelectLayerByLocation_management("Spring_Hill_Parcels","WITHIN_A_DISTANCE",display_CityLimits,'1 Mile',"NEW_SELECTION")
    arcpy.Merge_management([GDB_County + "\\parcelsgpdata", "Spring_Hill_Parcels"], display_Parcels, FieldMap('Parcels'))
    # Process: Copy County Boundary to Display_Layers
    arcpy.AddMessage("    Copying County Boundary to Display_Layers")
    arcpy.Dissolve_management(static_CountyBorders, display_County, "NAME", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy Buildings to Display_Layers
    arcpy.AddMessage("    Copying Buildings to Display_Layers")
    arcpy.Dissolve_management(static_buildings, display_Buildings, "BUILDINGS_;BUILDING_1", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Copy Radio Coverage to Display_Layers
    arcpy.AddMessage("    Copying Radio Coverage to Display_Layers")
    arcpy.Dissolve_management(static_WOPS_Buff, display_Radios, "WOPS", "", "SINGLE_PART", "DISSOLVE_LINES")

if (copyStreets == 'true'):
    arcpy.AddMessage("\n\nPreparing Centerlines...")
    # Process: Repair Geometry
    arcpy.AddMessage("    Repairing Surrounding Centerline Geometry")
    arcpy.AddSpatialIndex_management(TIPS_Centerlines, 0, 0, 0)
    arcpy.RepairGeometry_management(TIPS_Centerlines, "DELETE_NULL")
    # Process: Copy Non-Brentwood Streets
    arcpy.AddMessage("    Copying Non-Brentwood Streets from Surrounding Centerlines")
    arcpy.Select_analysis(TIPS_Centerlines, GDB_Scratch + "\\Surrounding_Streets", "\"OIRID\" NOT LIKE 'BRENTWOOD%' AND \"CFCC\" NOT LIKE 'B%'")
    # Process: Set Labels
    arcpy.AddMessage("    Starting Set Surrounding Centerline Labels")
    arcpy.CalculateField_management(GDB_Scratch + "\\Surrounding_Streets", "LABEL", "GetName(!PREDIR!,!PRETYPE!, !NAME!, !TYPE!,!SUFDIR!)", "PYTHON_9.3", GetGeoName)
    # Process: Merge WC Centerlines and Surrounding Margin
    arcpy.AddMessage("    Merging WC Centerlines and Surrounding Margin")
    arcpy.Snap_edit(static_StreetBuffer,[[williamson_centerlines,  "END", "25 Feet"]])
    arcpy.Merge_management([williamson_centerlines, static_StreetBuffer] , GDB_Scratch + "\\Centerlines_Merged")
    # Process: Spatial Join
    arcpy.AddMessage("    Collecting Ramp Label Fields")
    arcpy.SpatialJoin_analysis(GDB_Scratch + "\\Centerlines_Merged", static_Ramps, GDB_Scratch + "\\Centerlines_SpatialJoin", "JOIN_ONE_TO_ONE", "KEEP_ALL",FieldMap("Ramps"),"HAVE_THEIR_CENTER_IN")
    # Process: Calculate Tow Provider
    arcpy.AddMessage("    Calculating Tow Provider")
    arcpy.SpatialJoin_analysis(GDB_Scratch + "\\Centerlines_SpatialJoin", tritech_LawAreas, GDB_Scratch + "\\Centerlines_Merge", "JOIN_ONE_TO_ONE", "KEEP_ALL", FieldMap("Law_RA"),"HAVE_THEIR_CENTER_IN")
    arcpy.CalculateField_management(GDB_Scratch + "\\Centerlines_Merge", "LeftServiceProviderAreaExtKey", "GetLawCode(!LeftServiceProviderAreaExtKey!,!OIRID!)", "PYTHON_9.3", GetLawCode)
    arcpy.CalculateField_management(GDB_Scratch + "\\Centerlines_Merge", "RightServiceProviderAreaExtKey", "!LeftServiceProviderAreaExtKey!", "PYTHON_9.3", "")
    # Process: Convert City Names to City Codes
    arcpy.AddMessage("    Converting Street City Names to City Codes")
    arcpy.CalculateField_management(GDB_Scratch + "\\Centerlines_Merge", "CITY_L", "myCity(!CITY_L!)", "PYTHON_9.3", City_Codes)
    arcpy.CalculateField_management(GDB_Scratch + "\\Centerlines_Merge", "CITY_R", "myCity(!CITY_R!)", "PYTHON_9.3", City_Codes)
    # Process: Convert County Names to County Codes
    arcpy.AddMessage("    Converting Street County Names to County Codes")
    arcpy.MakeFeatureLayer_management(GDB_Scratch + "\\Centerlines_Merge", "Maury_Streets", "COUNTY_L='MAURY' OR COUNTY_R='MAURY'")
    arcpy.MakeFeatureLayer_management(GDB_Display + "\\County", "Maury_SH", "NAME='MAURY*'")
    arcpy.SelectLayerByLocation_management("Maury_Streets","HAVE_THEIR_CENTER_IN","Maury_SH","","NEW_SELECTION")
    arcpy.CalculateField_management("Maury_Streets","COUNTY_L",'"MAUSH" if !COUNTY_L! == "MAURY" else !COUNTY_L!',"PYTHON_9.3","")
    arcpy.CalculateField_management("Maury_Streets","COUNTY_R",'"MAUSH" if !COUNTY_R! == "MAURY" else !COUNTY_R!',"PYTHON_9.3","")
    arcpy.CalculateField_management(GDB_Scratch + "\\Centerlines_Merge", "COUNTY_L", "myCounty(!COUNTY_L!)", "PYTHON_9.3", County_Codes)
    arcpy.CalculateField_management(GDB_Scratch + "\\Centerlines_Merge", "COUNTY_R", "myCounty(!COUNTY_R!)", "PYTHON_9.3", County_Codes)
    # Process: Add StreetName Field
    arcpy.AddMessage("    Fixing Centerline Street Name Fields")
    FieldList = ["PREDIR","PRETYPE","NAME","TYPE","SUFDIR","DIRECTION","CFCC","EXITNUM","RAMPDIR"]
    for field in FieldList:
        arcpy.CalculateField_management(GDB_Scratch + "\\Centerlines_Merge", field, """(!{}! or "").strip()""".format(field), "PYTHON_9.3")
    arcpy.AddField_management(GDB_Scratch + "\\Centerlines_Merge", "StreetName", "TEXT", "", "", "150", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.CalculateField_management(GDB_Scratch + "\\Centerlines_Merge", "TYPE", "GetType( !TYPE!, !NAME!)", "PYTHON_9.3", Street_Types)
    arcpy.CalculateField_management(GDB_Scratch + "\\Centerlines_Merge", "NAME", "GetType( !TYPE!, !NAME!)", "PYTHON_9.3", Street_Names)
    arcpy.CalculateField_management(GDB_Scratch + "\\Centerlines_Merge", "StreetName", "GetName(!PREDIR!,!PRETYPE!, !NAME!, !TYPE!,!SUFDIR!,!DIRECTION!,!CFCC!,!EXITNUM!,!RAMPDIR!)", "PYTHON_9.3", GetGeoName)
    # Process: Rename Centerline Fields
    arcpy.AddMessage("    Starting Rename Centerline Fields")
    arcpy.Merge_management([static_CenterlineSchema, GDB_Scratch + "\\Centerlines_Merge"], GDB_Scratch + "\\Centerlines_Named", FieldMap("Centerline_Rename"))
    # Process: Calculate Parity
    arcpy.AddMessage("    Setting Street Parity Values")
    arcpy.CalculateField_management(GDB_Scratch + "\\Centerlines_Named", "LeftParity", "\"R\"", "PYTHON_9.3", "")
    arcpy.CalculateField_management(GDB_Scratch + "\\Centerlines_Named", "RightParity", "\"R\"", "PYTHON_9.3", "")
    # Process: Copy Brentwood Streets from SDE
    arcpy.AddMessage("    Copying Brentwood Streets from SDE")
    try:
        if arcpy.Exists(SDE_Brentwood + "\\TritechGIS.DBO.BW_Centerlines"):
            arcpy.Copy_management(SDE_Brentwood + "\\TritechGIS.DBO.BW_Centerlines", GDB_Scratch + "\\BW_Streets", "FeatureClass")
    except:
        if arcpy.Exists(GDB_Scratch + "\\BW_Streets"):
            arcpy.AddWarning("        Could not connect to SDE - using previous feature class.")
        else:
            arcpy.AddError("SDE Could not be reached and no local copy was found.")
    # Process: Brentwood Field Recalculate
    arcpy.AddMessage("    Starting Brentwood Field Recalculations")
    arcpy.CalculateField_management(GDB_Scratch + "\\BW_Streets", "LeftServiceProviderAreaExtKey", "\"TOW_BRENTWOOD\"", "PYTHON_9.3", "")
    arcpy.CalculateField_management(GDB_Scratch + "\\BW_Streets", "RightServiceProviderAreaExtKey", "\"TOW_BRENTWOOD\"", "PYTHON_9.3", "")
    arcpy.CalculateField_management(GDB_Scratch + "\\BW_Streets", "StreetName","BWStreetNames(!StreetName!)","PYTHON_9.3", BWStreetNames)
    # Process: Snap To Intersection Points
    arcpy.AddMessage("    Starting Snap To Intersection Points")
    arcpy.Snap_edit(GDB_Scratch + "\\Centerlines_Named",[[static_Intersections, "END", "8 Feet"]])
    arcpy.Snap_edit(GDB_Scratch + "\\BW_Streets",[[static_Intersections, "END", "8 Feet"]])
    # Process: Merge County & Brentwood Centerlines
    arcpy.AddMessage("    Starting Merge County & Brentwood Centerlines")
    arcpy.Merge_management([GDB_Scratch + "\\Centerlines_Named", GDB_Scratch + "\\BW_Streets"] , tritech_Centerlines)
    arcpy.DeleteField_management(tritech_Centerlines,"StreetID")
    arcpy.CalculateField_management(tritech_Centerlines, "RoutingStreetExtKey", "'' if !RoutingStreetExtKey! == !ExternalStreetKey! else !RoutingStreetExtKey!", "PYTHON_9.3")
    RemoveNULL(tritech_Centerlines)
    # Process: Output Geolocator Source
    arcpy.AddMessage("    Building Address Geolocator")
    arcpy.CopyFeatures_management(tritech_Centerlines,GDB_Scratch + "\\Centerlines_Geolocator")
    arcpy.MakeFeatureLayer_management(GDB_Scratch + "\\Centerlines_Geolocator", 'Unroutables',"SpeedLimit < 1")
    arcpy.DeleteFeatures_management('Unroutables')
    arcpy.RebuildAddressLocator_geocoding(TRITECH_Geolocator)
    # Process: Calculate TRITECH Street Name
    arcpy.AddMessage("    Starting Calculate TRITECH Street Name")
    arcpy.CalculateField_management(tritech_Centerlines,"DIRECTION","""(!DIRECTION! or "").strip()""", "PYTHON_9.3")
    arcpy.CalculateField_management(tritech_Centerlines,"PRETYPE","""(!PRETYPE! or "").strip()""", "PYTHON_9.3")
    arcpy.CalculateField_management(tritech_Centerlines, "StreetName", "GetName(!PRETYPE!,!StreetName!,!DIRECTION!,!FeatureTypeCode!)", "PYTHON_9.3", GetTriTechName)
    arcpy.DeleteField_management(tritech_Centerlines,["DIRECTION","PRETYPE","Fire_Grid"])
    # Process: Snap
    arcpy.AddMessage("    Snapping Surrounding Streets to Final Centerlines")
    arcpy.Snap_edit(GDB_Scratch + "\\Surrounding_Streets",[[tritech_Centerlines, "END", "20 Feet"]])
    arcpy.Snap_edit(GDB_Scratch + "\\Surrounding_Streets",[[tritech_Centerlines, "EDGE", "5 Feet"]])
    # Process: Remove Surrounding Street Overlap
    arcpy.AddMessage("    Removing Surrounding Street Overlap")
    arcpy.MakeFeatureLayer_management(GDB_Scratch + "\\Surrounding_Streets", "Surrounding_Streets_Layer")
    arcpy.Buffer_analysis(tritech_Centerlines, GDB_Scratch + "\\Brentwood_Street_Buffer", "35 Feet", "FULL", "ROUND", "ALL", "", "PLANAR")
    arcpy.SelectLayerByLocation_management("Surrounding_Streets_Layer", "HAVE_THEIR_CENTER_IN", GDB_Scratch + "\\Brentwood_Street_Buffer", "", "NEW_SELECTION", "NOT_INVERT")
    arcpy.DeleteFeatures_management("Surrounding_Streets_Layer")
    # Process: Dissolve
    arcpy.AddMessage("    Simplifying Surrounding Streets")
    arcpy.Dissolve_management(GDB_Scratch + "\\Surrounding_Streets", display_SurroundStreets, "LABEL;VANITY;SUBNAME;CFCC;ZIP_L;ZIP_R;CITY_L;CITY_R;COUNTY_L;COUNTY_R;SPDLIMIT;ONEWAY", "", "SINGLE_PART", "DISSOLVE_LINES")
    arcpy.Generalize_edit(display_SurroundStreets, "0.5 Feet")
    # Process: Simplify Neighborhood Field
    arcpy.AddMessage("    Starting Simplify Neighborhoods")
    arcpy.Select_analysis(tritech_Centerlines, GDB_Scratch + "\\Neighborhoods", "(\"L_Neighborhood\" IS NOT NULL AND \"L_Neighborhood\"<>'') OR (\"R_Neighborhood\" IS NOT NULL AND \"R_Neighborhood\"<>'')")
    arcpy.Merge_management(GDB_Scratch + "\\Neighborhoods", GDB_Scratch + "\\Neighborhoods_Diss",FieldMap("Neighborhood"))
    arcpy.Dissolve_management(GDB_Scratch + "\\Neighborhoods_Diss", display_Neighborhoods, "Neighborhood", "", "SINGLE_PART", "DISSOLVE_LINES")


if (copyAddresses == 'true'):
    arcpy.AddMessage("\n\nPreparing Address Points...")
    # Process: Copy Brentwood Addresses
    arcpy.AddMessage("    Copying Brentwood Addresses from SDE")
    try:
        if arcpy.Exists(SDE_Brentwood + "\\TritechGIS.DBO.BW_Address"):
            arcpy.CopyFeatures_management(SDE_Brentwood + "\\TritechGIS.DBO.BW_Address", GDB_Scratch + "\\BW_Address_CopyFeatures", "DEFAULTS", "0", "0", "0")
    except:
        if arcpy.Exists(GDB_Scratch + "\\BW_Address_CopyFeatures"):
            arcpy.AddWarning("        Could not connect to SDE - using previous feature class.")
        else:
            arcpy.AddError("SDE Could not be reached and no local copy was found.")
    # Process: Set LocationName to Street, Address, Apartment
    arcpy.AddMessage("    Setting Brentwood LocationName to Street, Address, Apartment")
    arcpy.CalculateField_management(GDB_Scratch + "\\BW_Address_CopyFeatures","StreetName","BWStreetNames(!StreetName!)","PYTHON_9.3", BWStreetNames)
    arcpy.CalculateField_management(GDB_Scratch + "\\BW_Address_CopyFeatures", "LocationName", "LocName(!StreetName!, !Address!, !Apartment!)", "PYTHON_9.3", LocName)
    # Process: Merge Mile_Markers
    arcpy.AddMessage("    Starting Merge Mile_Markers")
    arcpy.Merge_management([static_MileMarkers, static_NatchezMM], GDB_Scratch + "\\Mile_Markers_Merge", FieldMap("Mile Markers") )
    # Process: Select
    arcpy.AddMessage("    Starting Select")
    arcpy.AddSpatialIndex_management(TIPS_Addresses, 0, 0, 0)
    arcpy.Select_analysis(TIPS_Addresses, GDB_Scratch + "\\SiteAddress_select", "\"OIRID\" NOT LIKE 'BRENT%' AND SUBSTRING(\"STNUM\" FROM 1 FOR 1) >= '1' AND SUBSTRING(\"STNUM\" FROM 1 FOR 1) <= '9' ")
    # Process: Merge County & Surrounding Addresses
    arcpy.AddMessage("    Starting Merge County & Surrounding Addresses")
    arcpy.Merge_management([williamson_addresses, GDB_Scratch + "\\SiteAddress_select"] , GDB_Scratch + "\\Merged_Addresses")
    # Process: Fix Address Street Types
    arcpy.AddMessage("    Starting Fix Address Street Types")
    FieldList = ["PREDIR","PRETYPE","NAME","TYPE","SUFDIR", "STNUM", "STNUMSUF", "BUILDING", "UNIT_NUM", "SECUNTNUM", "UNIT_TYPE"]
    for field in FieldList:
        arcpy.CalculateField_management(GDB_Scratch + "\\Merged_Addresses", field, """(!{}! or "").strip()""".format(field), "PYTHON_9.3")
    arcpy.CalculateField_management(GDB_Scratch + "\\Merged_Addresses", "TYPE", "GetType(!TYPE!,!NAME!)", "PYTHON_9.3", Street_Types)
    # Process: Fix Address Street Names
    arcpy.AddMessage("    Starting Fix Address Street Names")
    arcpy.CalculateField_management(GDB_Scratch + "\\Merged_Addresses", "NAME", "GetType(!TYPE!,!NAME!)", "PYTHON_9.3", Street_Names)
    # Process: Replace STREET field with concatenated values
    arcpy.AddMessage("    Starting Replace STREET field with concatenated values")
    arcpy.CalculateField_management(GDB_Scratch + "\\Merged_Addresses", "STREET", "StreetName(!PREDIR!, !PRETYPE!, !NAME!, !TYPE!, !SUFDIR!)", "PYTHON_9.3", StreetName)
    # Process: Save STNUM as Digits Only
    arcpy.AddMessage("    Starting Save STNUM as Digits Only")
    arcpy.CalculateField_management(GDB_Scratch + "\\Merged_Addresses", "STNUM", "''.join([i for i in !STNUM! if i.isdigit()])", "PYTHON_9.3")
    # Process: Get BUILDING from BLDG Units
    arcpy.AddMessage("    Starting Get BUILDING from BLDG Units")
    arcpy.CalculateField_management(GDB_Scratch + "\\Merged_Addresses", "BUILDING", "BldgNum(!BUILDING!, !UNIT_TYPE!, !UNIT_NUM!)", "PYTHON_9.3", BldgNum)
    arcpy.CalculateField_management(GDB_Scratch + "\\Merged_Addresses", "UNIT_NUM", "UnitNum(!UNIT_TYPE!, !UNIT_NUM!)", "PYTHON_9.3", UnitNum)
    arcpy.CalculateField_management(GDB_Scratch + "\\Merged_Addresses", "UNIT_TYPE", "UnitType(!UNIT_TYPE!)", "PYTHON_9.3", UnitType)
    # Process: Merge Unit and SecUnit as Apartment
    arcpy.AddMessage("    Starting Merge Unit and SecUnit as Apartment")
    arcpy.CalculateField_management(GDB_Scratch + "\\Merged_Addresses", "UNIT_NUM", "(!UNIT_NUM!+!SECUNTNUM!).strip()", "PYTHON_9.3")
    # Process: Create LABEL with Address & Apartment
    arcpy.AddMessage("    Starting Create LABEL with Address & Apartment")
    arcpy.CalculateField_management(GDB_Scratch + "\\Merged_Addresses", "LABEL", "LabelOut(!UNIT_NUM!, !STREET!, !STNUM!, !STNUMSUF!, !BUILDING!, !UNIT_TYPE!)", "PYTHON_9.3", AddrLabel)
    # Process: Convert City Names to City Codes
    arcpy.AddMessage("    Starting Convert City Names to City Codes")
    arcpy.CalculateField_management(GDB_Scratch + "\\Merged_Addresses", "CITY", "myCity(!CITY!)", "PYTHON_9.3", City_Codes)
    # Process: Convert County Names to County Codes
    arcpy.AddMessage("    Starting Convert County Names to County Codes")
    arcpy.MakeFeatureLayer_management(GDB_Scratch + "\\Merged_Addresses", "Maury_Addr", "County='MAURY'")
    arcpy.MakeFeatureLayer_management(GDB_Display + "\\County", "Maury_SH", "NAME='MAURY*'")
    arcpy.SelectLayerByLocation_management("Maury_Addr","WITHIN","Maury_SH","","NEW_SELECTION")
    arcpy.CalculateField_management("Maury_Addr","COUNTY",'"MAUSH"',"PYTHON_9.3","")
    arcpy.CalculateField_management(GDB_Scratch + "\\Merged_Addresses", "COUNTY", "myCounty(!COUNTY!)", "PYTHON_9.3", County_Codes)
    # Process: Remove Address Fields
    arcpy.AddMessage("    Starting Remove Address Fields")
    arcpy.Dissolve_management(GDB_Scratch + "\\Merged_Addresses", GDB_Scratch + "\\Merged_Addresses_Dissolve", "OIRID;R_SEGID;A_SEGID;STNUM;BUILDING;UNIT_NUM;LABEL;SUBNAME;CITY;COUNTY;STATE;ZIP;STREET", "", "SINGLE_PART", "DISSOLVE_LINES")
    # Process: Extract County Addresses
    arcpy.AddMessage("    Starting Extract County Addresses")
    arcpy.Select_analysis(GDB_Scratch + "\\Merged_Addresses_Dissolve", GDB_Scratch + "\\County_Addr", " \"COUNTY\"='WM' OR \"COUNTY\" = 'MAUSH'")
    # Process: Add Street Address Field
    arcpy.AddMessage("    Starting Add Street Address Field")
    arcpy.AddField_management(GDB_Scratch + "\\County_Addr", "StAddress", "TEXT", "", "", "150", "Address", "NULLABLE", "NON_REQUIRED", "")
    arcpy.CalculateField_management(GDB_Scratch + "\\County_Addr", "StAddress", "!STNUM!.strip()+\" \"+!STREET!.strip()", "PYTHON_9.3", "")
    # Process: Geocode Addresses
    arcpy.AddMessage("    Starting Geocode Addresses")
    arcpy.GeocodeAddresses_geocoding(GDB_Scratch + "\\County_Addr", TRITECH_Geolocator, "'Street or Intersection' StAddress VISIBLE NONE;'City or Placename' City VISIBLE NONE;State State VISIBLE NONE;'ZIP Code' ZIP VISIBLE NONE", GDB_Scratch + "\\Address_geocode", "STATIC", '#', '#')
    arcpy.Merge_management([GDB_Scratch + "\\County_Addr",GDB_Scratch + "\\Address_geocode"], GDB_Scratch + '\\Address_Lines_Points','#')
    arcpy.PointsToLine_management(GDB_Scratch + '\\Address_Lines_Points',GDB_Scratch + '\\Address_Lines','OIRID','LABEL')
    arcpy.AddMessage("    Starting Find Nearest Major Road")
    arcpy.DeleteFeatures_management(network_centerlines)
    arcpy.Append_management(GDB_Scratch + "\\Centerlines_Geolocator",network_centerlines,"NO_TEST")
    arcpy.BuildNetwork_na(network_dataset)
    outNALayer = arcpy.na.MakeODCostMatrixLayer(network_dataset, 'OD_Matrix',"Length",10560,1,"#","ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY","#","NO_HIERARCHY","#","STRAIGHT_LINES","#")
    outNALayer = outNALayer.getOutput(0)
    subLayerNames = arcpy.na.GetNAClassNames(outNALayer)
    originsLayerName = subLayerNames["Origins"]
    destinationsLayerName = subLayerNames["Destinations"]
    arcpy.MakeFeatureLayer_management(GDB_Scratch + "\\Centerlines_Geolocator","Centerlines_Major","(FeatureTypeCode LIKE 'A2%' OR FeatureTypeCode LIKE 'A3%') AND (StreetName NOT LIKE 'UNNAMED%')")
    arcpy.GeneratePointsAlongLines_management('Centerlines_Major', GDB_Scratch + '\\Centerlines_Merged_near', 'PERCENTAGE', '#', '49', 'NO_END_POINTS')
    arcpy.na.AddFieldToAnalysisLayer(outNALayer, destinationsLayerName,"MajorRoad", "TEXT")
    fieldMappings = arcpy.na.NAClassFieldMappings(outNALayer, destinationsLayerName)
    fieldMappings["MajorRoad"].mappedFieldName = "StreetName"
    arcpy.na.AddLocations(outNALayer, destinationsLayerName, GDB_Scratch + '\\Centerlines_Merged_near',fieldMappings,append='CLEAR')
    arcpy.MakeFeatureLayer_management(GDB_Scratch + "\\Address_geocode","Geocoded_Addresses","Score > 0")
    arcpy.na.AddFieldToAnalysisLayer(outNALayer, originsLayerName,"ADDR_UID", "TEXT")
    fieldMappings = arcpy.na.NAClassFieldMappings(outNALayer, originsLayerName)
    fieldMappings["ADDR_UID"].mappedFieldName = "OIRID"
    arcpy.na.AddLocations(outNALayer,originsLayerName,"Geocoded_Addresses",fieldMappings,append="CLEAR")
    arcpy.na.Solve(outNALayer)
    subLayers = dict((lyr.datasetName, lyr) for lyr in arcpy.mapping.ListLayers(outNALayer)[1:])
    OriginsSubLayer = subLayers["Origins"]
    DestinationsSubLayer = subLayers["Destinations"]
    LinesSubLayer = subLayers["ODLines"]
    arcpy.CopyFeatures_management(LinesSubLayer,GDB_Scratch+"\\ODLines")
    arcpy.JoinField_management(GDB_Scratch+"\\ODLines", "OriginID", OriginsSubLayer, "ObjectID", "ADDR_UID")
    arcpy.JoinField_management(GDB_Scratch+"\\ODLines", "DestinationID", DestinationsSubLayer, "ObjectID", "MajorRoad")
    arcpy.JoinField_management(GDB_Scratch + "\\Address_geocode","OIRID",GDB_Scratch+"\\ODLines","ADDR_UID","MajorRoad")
    # Process: Join Field
    arcpy.AddMessage("    Starting Join Field")
    arcpy.JoinField_management(GDB_Scratch + "\\County_Addr", "OIRID", GDB_Scratch + "\\Address_geocode", "OIRID", ["Ref_ID","MajorRoad"])
    with arcpy.da.SearchCursor(GDB_Scratch + "\\County_Addr", ["LABEL","OIRID"], "Ref_ID = '-1'") as cursor:
        for row in cursor:
            arcpy.AddMessage("        No centerline found to geocode {0} ({1})".format(row[0], row[1]))
    with arcpy.da.SearchCursor(GDB_Scratch + "\\County_Addr", ["LABEL","Ref_ID","A_SEGID","OIRID"], arcpy.AddFieldDelimiters(GDB_Scratch + "\\County_Addr", "Ref_ID")+"<> '-1' AND "+arcpy.AddFieldDelimiters(GDB_Scratch + "\\County_Addr", "A_SEGID")+" <> "+arcpy.AddFieldDelimiters(GDB_Scratch + "\\County_Addr", "Ref_ID")) as cursor:
        for row in cursor:
            if row[2].strip() <> '':
                arcpy.AddMessage("A_SEGID ({0}) and Geocoded centerline ({1}) don't match for {2} ({3})".format(row[2],row[1],row[0],row[3]))
    # Process: Fill RoutingStreetExtKey in Addresses
    arcpy.AddMessage("    Starting Fill RoutingStreetExtKey in Addresses")
    arcpy.CalculateField_management(GDB_Scratch + "\\County_Addr", "R_SEGID", "RouteStr(!Ref_ID!, !R_SEGID!,!COUNTY!)", "PYTHON_9.3", RouteStr)
    # Process: Extract All Other Addresses
    arcpy.AddMessage("    Starting Extract All Other Addresses")
    arcpy.Select_analysis(GDB_Scratch + "\\Merged_Addresses_Dissolve", GDB_Scratch + "\\surround_addr", "\"COUNTY\"<>'WM' AND \"COUNTY\" <> 'MAUSH'")
    arcpy.CalculateField_management(GDB_Scratch + "\\surround_addr", "R_SEGID", "RouteStr('', !R_SEGID!,!COUNTY!)", "PYTHON_9.3", RouteStr)
    # Process: Merge
    arcpy.AddMessage("    Starting Merge")
    arcpy.Merge_management([GDB_Scratch + "\\BW_Address_CopyFeatures", GDB_Scratch + "\\Mile_Markers_Merge", GDB_Scratch + "\\County_Addr", GDB_Scratch + "\\surround_addr"], GDB_Scratch + "\\Address_Select_all", FieldMap("Addresses"))
    arcpy.Select_analysis(GDB_Scratch + "\\Address_Select_all",tritech_Addresses,"Address > 0")
    # Process: Find nearest major road to addresses
    arcpy.AddMessage("    Starting Find Nearest Major Road (Pass 2)")
    arcpy.MakeFeatureLayer_management(tritech_Addresses,"Address","(CountyCode = 'WM' OR CountyCode = 'MAUSH') AND MajorRoad IS NULL")
    fieldMappings = arcpy.na.NAClassFieldMappings(outNALayer, originsLayerName)
    fieldMappings["ADDR_UID"].mappedFieldName = "ExternalKey"
    arcpy.na.AddLocations(outNALayer,originsLayerName,"Address",fieldMappings,append="CLEAR")
    arcpy.na.Solve(outNALayer)
    subLayers = dict((lyr.datasetName, lyr) for lyr in arcpy.mapping.ListLayers(outNALayer)[1:])
    OriginsSubLayer = subLayers["Origins"]
    DestinationsSubLayer = subLayers["Destinations"]
    LinesSubLayer = subLayers["ODLines"]
    arcpy.CopyFeatures_management(LinesSubLayer,GDB_Scratch+"\\ODLines2")
    arcpy.JoinField_management(GDB_Scratch+"\\ODLines2", "OriginID", OriginsSubLayer, "ObjectID", "ADDR_UID")
    arcpy.JoinField_management(GDB_Scratch+"\\ODLines2", "DestinationID", DestinationsSubLayer, "ObjectID", "MajorRoad")
    arcpy.JoinField_management("Address","ExternalKey",GDB_Scratch+"\\ODLines2","ADDR_UID","MajorRoad")
    arcpy.CalculateField_management("Address", "MajorRoad","!MajorRoad_1!","PYTHON_9.3")
    arcpy.DeleteField_management(tritech_Addresses,"MajorRoad_1")
    arcpy.CalculateField_management(tritech_Addresses, 'MajorRoad', "'' if ( !StreetName!== !MajorRoad!) else !MajorRoad!", 'PYTHON_9.3', '#')
    # Process: Remove NULL from Addresses
    arcpy.AddMessage("    Starting Remove NULL from Addresses")
    RemoveNULL(tritech_Addresses)
    # Process: Copy Features to Display_Layers
    arcpy.AddMessage("    Copying Features to Display_Layers")
    arcpy.CopyFeatures_management(tritech_Addresses, display_Address, "DEFAULTS", "0", "0", "0")
    
    # Process: Report Duplicate Address Points
    arcpy.AddMessage("    Generating Duplicate Address Report...")
    arcpy.Select_analysis(display_Address, GDB_Scratch+'\\County_Addresses', "CountyCode='WM'")
    arcpy.FindIdentical_management(GDB_Scratch+'\\County_Addresses', GDB_Scratch+'\\Address_Duplicates', 'Shape;LocationName', '1 Feet', '0', 'ONLY_DUPLICATES')
    arcpy.MakeTableView_management(GDB_Scratch+'\\Address_Duplicates','Duplicate_Table')
    arcpy.AddJoin_management('Duplicate_Table',"IN_FID",GDB_Scratch+'\\County_Addresses',"OBJECTID","KEEP_ALL")
    arcpy.TableToExcel_conversion('Duplicate_Table',addressDuplicateReport,"ALIAS","DESCRIPTION")
    os.startfile(addressDuplicateReport)

if (copyAddresses == 'true' or copyStreets == 'true'):
    # Process: Copy results to GISLink Folder
    arcpy.AddMessage("    Copying TriTech GDB to GISLink Source Folder")
    arcpy.Copy_management(GDB_TriTech, GDB_GISLink_Source)







