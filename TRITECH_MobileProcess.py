
# Import arcpy module
import arcpy
import datetime
import shutil
import glob

# Workspace Variables:
GDB_Scratch = arcpy.env.scratchGDB
GDB_Static = r"C:\Users\robert.mabry\Documents\ArcGIS\StaticBase.gdb"
SQL_CAD = r"Database Connections\CAD Database.sde\System.dbo.Hydrant_Info"

G_Streets = r"G:\Exports\MapData\Streets\Streets_D1.*"
Street_Dir = r"C:\TriTech\MobileMap\Streets"
CAD_Streets = r"C:\TriTech\MobileMap\Streets\Streets_D1.shp"
DisplayStreets = r"C:\TriTech\MobileMap\Streets\Streets_D1_Dissolve.shp"
MXD_file = r"C:\TriTech\MobileMap\Williamson_Mobile_Map.mxd"
mapPackage = r"C:\TriTech\MobileMap\Williamson_Mobile_Map.mpk"
CityLimit_mxd = r"C:\TriTech\MobileMap\Williamson_City_Limits.mxd"
CityLimit_pkg = r"C:\TriTech\MobileMap\Williamson_City_Limits.mpk"
RespArea_mxd = r"C:\TriTech\MobileMap\Williamson_Response_Areas.mxd"
RespArea_pkg = r"C:\TriTech\MobileMap\Williamson_Response_Areas.mpk"
MobileLoc = r"C:\TriTech\MobileMap\MobileLocator"
MobileLocPkg = r"C:\TriTech\MobileMap\MobileLocatorPackage.gcpk"
StreetNameMobileLoc = r"C:\TriTech\MobileMap\StreetNameMobileLocator"
StreetNameMobileLocPkg = r"C:\TriTech\MobileMap\StreetNameMobileLocatorPackage.gcpk"
DateToday = str(datetime.date.today()).replace("-","")

# Process:
arcpy.env.overwriteOutput = True
arcpy.gp.overwriteOutput = True

for file in glob.glob(r"C:\TriTech\MobileMap\*.*"):
    arcpy.AddMessage("Backing Up {0}".format(file))
    shutil.copy(file, r"C:\TriTech\MobileMap\Backup")

for file in glob.glob(G_Streets):
    shutil.copy(file, Street_Dir)

arcpy.AddMessage("Dissolving Streets...")
arcpy.Dissolve_management(CAD_Streets, DisplayStreets, "Label;FeatTpCode;OneWayCode", "","SINGLE_PART","DISSOLVE_LINES")

arcpy.AddMessage("Updating Hydrants...")
arcpy.TableToTable_conversion(SQL_CAD,GDB_Scratch,'Hydrants_Table')
arcpy.AddField_management(GDB_Scratch+'\\Hydrants_Table',"Longitude","DOUBLE",9,6)
arcpy.AddField_management(GDB_Scratch+'\\Hydrants_Table',"Latitude","DOUBLE",9,6)
arcpy.CalculateField_management(GDB_Scratch+'\\Hydrants_Table',"Longitude","!Lon!*-0.000001","PYTHON_9.3")
arcpy.CalculateField_management(GDB_Scratch+'\\Hydrants_Table',"Latitude","!Lat!*0.000001","PYTHON_9.3")
arcpy.MakeXYEventLayer_management(GDB_Scratch+'\\Hydrants_Table',"Longitude","Latitude","Hydrants_Layer")
arcpy.FeatureClassToFeatureClass_conversion("Hydrants_Layer",GDB_Scratch,'Hydrants')
spatial_ref = arcpy.Describe(GDB_Static+'\\Hydrants').spatialReference
arcpy.Project_management(GDB_Scratch+'\\Hydrants',GDB_Static+'\\Hydrants',spatial_ref)

arcpy.AddMessage("Saving Williamson_Mobile_Map Package...")
arcpy.PackageMap_management(MXD_file, mapPackage, "CONVERT", "CONVERT_ARCSDE", "#","ALL","RUNTIME","NOT_REFERENCED","10.2")
arcpy.AddMessage("Saving Williamson_City_Limits Package...")
arcpy.PackageMap_management(CityLimit_mxd, CityLimit_pkg, "CONVERT", "CONVERT_ARCSDE", "#","ALL","RUNTIME","NOT_REFERENCED","10.2")
arcpy.AddMessage("Saving Williamson_Response_Areas Package...")
arcpy.PackageMap_management(RespArea_mxd, RespArea_pkg, "CONVERT", "CONVERT_ARCSDE", "#","ALL","RUNTIME","NOT_REFERENCED","10.2")

arcpy.AddMessage("Building Address Locators...")
arcpy.RebuildAddressLocator_geocoding(MobileLoc)
arcpy.RebuildAddressLocator_geocoding(StreetNameMobileLoc)
arcpy.AddMessage("Saving Address Locator Packages...")
arcpy.PackageLocator_geocoding(MobileLoc, MobileLocPkg)
arcpy.PackageLocator_geocoding(StreetNameMobileLoc, StreetNameMobileLocPkg)
