# -*- coding: utf-8 -*-
# Set the necessary product code
#import arceditor

# Import arcpy module
import arcpy, os, time

# Workspace Variables:
C_Maps = r'C:\TriTech\VisiCAD\Data\Maps'
VisiData = r'Q:\TriTech\VisiCAD\Data'
Q_Maps = VisiData + '\\Maps'
MXD_file = arcpy.GetParameterAsText(0)
#what the heck

# Feature Variables:
QStreets = Q_Maps + "\\Routing\\Streets.shp"
DisplayStreets = C_Maps + r'\MapDisplay\Streets\Display_Streets.gdb\Streets_D1'

arcpy.env.overwriteOutput = True
arcpy.gp.overwriteOutput = True

# Process: Dissolve DisplayStreets
arcpy.AddMessage("Dissolving Streets...")
arcpy.Dissolve_management(QStreets, DisplayStreets, "STREETNAME;SEGTYPE;ONEWAY", "","SINGLE_PART","DISSOLVE_LINES")
arcpy.AddMessage("Dissolving Completed.")

mxd = arcpy.mapping.MapDocument(MXD_file)
df = arcpy.mapping.ListDataFrames(mxd, "Inform CAD GEO")[0]
lyr = arcpy.mapping.ListLayers(mxd, "Neighborhoods", df)[0]
lyrTemp = arcpy.env.scratchFolder + '\\Neighborhoods.lyr'

if lyr.symbologyType == "UNIQUE_VALUES":
    lyr.symbology.addAllValues()
lyr.saveACopy(lyrTemp, "10.1")
arcpy.mapping.UpdateLayer(df, lyr, arcpy.mapping.Layer(lyrTemp), True)
mxd.save()

os.startfile(mxd.filePath)

arcpy.AddMessage("")
arcpy.AddMessage("MXD OPEN FOR QUALITY CHECK.")
arcpy.AddMessage("VERIFY ALL CHANGES BEFORE EXECUTING NEXT SCRIPT.")