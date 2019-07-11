# -*- coding: utf-8 -*-
# Set the necessary product code
#import arceditor

# Import arcpy module
import arcpy
import datetime
import os
import shutil
import errno

# Workspace Variables:
Q_Maps = "Q:\\TriTech\\VisiCAD\\Data\\Maps\\MapDisplay"
Q_MXD_Folder = r"Q:\TriTech\VisiCAD\Data\SystemMapThemes"
GDB_TriTech = "C:\\Users\\robert.mabry\\Documents\\ArcGIS\\TRITECH.gdb"
Address_Dif = r"G:\Differences\Differences.gdb\Address"
Street_Dif = r"G:\Differences\Differences.gdb\Streets"

LocalData = r"C:\TriTech\VisiCAD\Data"
HostName = os.getenv('COMPUTERNAME')
MapDisplay = os.path.join(LocalData, r"Maps\MapDisplay")
MXD_Folder = os.path.join(LocalData, HostName, r"Maps\MapDisplay\GEO_MXD")
MXD_file = os.path.join(MXD_Folder, "Williamson_GEO.mxd")
Q_MXD = os.path.join(Q_MXD_Folder, "Williamson_GEO.mxd")
DateToday = str(datetime.date.today()).replace("-","")
GDB_Scratch = "C:\\Users\\robert.mabry\\Documents\\ArcGIS\\Default.gdb"

SDE_Williamson = "C:\\Users\\robert.mabry\\AppData\\Roaming\\ESRI\\Desktop10.5\\ArcCatalog\\TriTech Shared.sde\\TritechGIS.DBO.WilliamsonCADLayers"
TriTechSDE_WC_Centerlines = SDE_Williamson + "\\TritechGIS.DBO.WM_Centerlines"
TriTechSDE_WM_Address = SDE_Williamson + "\\TritechGIS.DBO.WM_Address"
Centerlines = GDB_Scratch + "\\Centerlines_Named"
Merged_Addresses = GDB_TriTech + "\\Address"
Address_Select = GDB_Scratch + "\\Address_Select"
Address_Report = r'C:\Users\robert.mabry\Documents\ArcGIS\TriTech Exports\address_updates_'+DateToday+r'.xls'
Street_Report = r'C:\Users\robert.mabry\Documents\ArcGIS\TriTech Exports\street_updates_'+DateToday+r'.xls'

# Fuctions:
def copy(src, dest):
    arcpy.AddMessage("Copying {0} to {1}".format(src, dest))
    if os.path.exists(dest):
        shutil.rmtree(dest)
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        if (e.errno == errno.ENOTDIR or e.errno == errno.EINVAL):
            try:
                shutil.copyfile(src, dest)
            except:
                arcpy.AddError("Could not copy. Error: %s" % e)
        else:
            arcpy.AddError("Directory not copied. Error: %s" % e)


# Process:
arcpy.env.overwriteOutput = True
arcpy.gp.overwriteOutput = True

mxd = arcpy.mapping.MapDocument(MXD_file)
saveName = str(mxd.filePath).replace("GEO.mxd","GEO-"+DateToday+".mxd")
copyName = str(Q_MXD).replace("GEO.mxd","GEO-"+DateToday+".mxd")
backupName = os.path.join(MXD_Folder, "BACKUPS", "Williamson_GEO-"+DateToday+".mxd")
arcpy.AddMessage("Saving {0} as 10.1 MXD".format(saveName))
mxd.saveACopy(saveName,"10.1")
del mxd
if (os.path.isfile(copyName)):
  os.remove(copyName)
copy(saveName, copyName)
os.remove(saveName)
if (os.path.isfile(backupName)):
  os.remove(backupName)
copy(Q_MXD, backupName)
copy(Q_Maps+"\\Layers",MapDisplay+"\\Backup\\"+DateToday+"\\Layers")
copy(Q_Maps+"\\Streets",MapDisplay+"\\Backup\\"+DateToday+"\\Streets")
copy(MapDisplay+"\\Layers", Q_Maps+"\\Layers")
copy(MapDisplay+"\\Streets", Q_Maps+"\\Streets")

# Process: Export MSAG Changes to Excel
arcpy.MakeFeatureLayer_management(Address_Dif,"Address_Export","CountyCode ='WM' AND (SrcRwState='A' OR (SrcRwState='M' AND (AttrMod LIKE '%LocationName%' OR AttrMod LIKE '%CityCode%')))")
arcpy.MakeFeatureLayer_management(Street_Dif,"Street_Export","(LeftCountyCode ='WM' OR RightCountyCode='WM') AND (SrcRwState='A' OR (SrcRwState='M' AND AttrMod LIKE '%StreetName%'))")

arcpy.TableToExcel_conversion("Address_Export",Address_Report,"ALIAS","DESCRIPTION")
arcpy.TableToExcel_conversion("Street_Export",Street_Report,"ALIAS","DESCRIPTION")
arcpy.AddWarning('Do not forget to forward the changes spreadsheets to MSAG Coordinator and Locution Manager:\n'+Address_Report+'  and  '+Street_Report)
os.startfile(Street_Report)
os.startfile(Address_Report)

# Process: Update SDE Centerlines

arcpy.AddMessage("Starting Update SDE Centerlines")
try:
    if arcpy.Exists(TriTechSDE_WC_Centerlines):
        arcpy.DeleteFeatures_management(TriTechSDE_WC_Centerlines)
        arcpy.AddMessage("Completed Delete Successfully")
        arcpy.Append_management(Centerlines, TriTechSDE_WC_Centerlines, "NO_TEST")
        arcpy.AddMessage("Completed Upload Successfully")
except:
    arcpy.AddWarning("Could not connect to SDE.  Bypassing step...")

    
# Process: Update SDE Addresses

arcpy.AddMessage("Starting Update SDE Addresses")
arcpy.Select_analysis(Merged_Addresses, Address_Select, "ExternalKey LIKE 'WILLIAM%' OR (ExternalKey LIKE 'MM%' AND CountyCode='WM') OR CountyCode = 'MAUSH'")
arcpy.AddMessage("Completed Extract County Addresses for SDE Successfully")
try:
    if arcpy.Exists(TriTechSDE_WM_Address):
        arcpy.DeleteFeatures_management(TriTechSDE_WM_Address)
        arcpy.AddMessage("Completed Delete Successfully")
        arcpy.Append_management(Address_Select, TriTechSDE_WM_Address, "NO_TEST")
        arcpy.AddMessage("Completed Update Successfully")
except:
    arcpy.AddWarning("Could not connect to SDE.  Bypassing step...")