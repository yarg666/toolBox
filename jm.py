"""bound defini le bound box et le centroid d'un node"""

def bound ():
    import hou
    nodeSelect = hou.selectedNodes()
    black=hou.Color((0,0,0))
    pink=hou.Color((0.9,0.304,0.9))

    for node in nodeSelect:
        getName = node.name()
        outNull = node.createOutputNode("null",getName+"_IN_BOUND")
        outNull.setPosition(node.position())
        outNull.move([0, -1])
        outNull.setColor(black)
        outBound= outNull.createOutputNode("null",getName+"_BOUND_CENTROID")
        outBound.setColor(pink)
        #add create param to outBound
        parm_group = outBound.parmTemplateGroup()
        parm_folder = hou.FolderParmTemplate("folder","Bound_Centroid")
        parm_folder.addParmTemplate(hou.FloatParmTemplate("bound","Bound",3))
        parm_folder.addParmTemplate(hou.FloatParmTemplate("centroid","Centroid",3))
        parm_group.append(parm_folder)
        outBound.setParmTemplateGroup(parm_group)

        outBound.parm('boundx').setExpression('bbox("../",D_XSIZE)')
        outBound.parm('boundy').setExpression('bbox("../",D_YSIZE)')
        outBound.parm('boundz').setExpression('bbox("../",D_ZSIZE)')

        outBound.parm('centroidx').setExpression('centroid("../",D_X)')
        outBound.parm('centroidy').setExpression('centroid("../",D_Y)')
        outBound.parm('centroidz').setExpression('centroid("../",D_Z)')

""" cache creer un rop output dans /out et le recharge dans le context d'origine
cela permet d'enchainer les depandences dans /out et de les relirent automatiquement
dans dans le contexte d'origine
"""

def cache ():
    import hou
    nodeSelect = hou.selectedNodes()
    black=hou.Color((0,0,0))
    pink=hou.Color((0.9,0.304,0.9))
    out= hou.node("/out")

    for node in nodeSelect:
        parent = node.parent()  #hou.node("..")
        parentString =parent.name()    
        getName = node.name()
        connectNode = node.outputs()
        outNull = node.createOutputNode("null",getName.upper())
        outNull.setPosition(node.position())
        outNull.move([0, -.75])
        outNull.setColor(black)
        #set read node to read myWriteGeo
        myFile = outNull.createOutputNode("file",getName.upper()+"_CACHE")
        myFile.setColor(pink)
        myFile.setParms({"file": "$"+"HIP/geo/$OS/"+"$"+"HIPNAME."+"$"+"OS."+"$"+"F.bgeo.sc"})
        #set myWriteGeo to cache the myFile
        myWriteGeo= out.createNode("geometry",getName.upper()+"_CACHE")
        myWriteGeo.setParms({"soppath":"/obj/"+parentString+"/"+getName.upper()})
        myWriteGeo.setParms({"sopoutput":"$HIP/geo/$OS/$HIPNAME.$OS.$F.bgeo.sc"})
        myWriteGeo.setParms({"trange":"normal"})

""" filecache cree un super node filecache 
qui ecrit la geo sans ce soucier du nom de fichier courant"""

def filecache ():
	import hou
	nodeSelect = hou.selectedNodes()
	pink=hou.Color ((0.9,0.304,0.9))

	for node in nodeSelect:
		getName = node.name()
		myFileCache = node.createOutputNode("filecache",getName.upper()+"_CACHE")
		myFileCache.setParms({"file":"$HIP/geo/$OS.$F.bgeo.sc"})
		myFileCache.setParms({"loadfromdisk":True})
		myFileCache.setColor(pink)

def pywy ():
    import hou
    nodeSelect = hou.selectedNodes()
    pink=hou.Color ((0.9,0.304,0.9))

    for node in nodeSelect:
        #create node from selected node
        pyNull = node.createOutputNode("null","pythonRunCode")
        pyNull.setColor(pink)
        #prepa param
        parm_group = pyNull.parmTemplateGroup()
        parm_folder = hou.FolderParmTemplate("folder","pywy")
        #button run code
        button=hou.ButtonParmTemplate("runcode","Run_Code")
        button.setTags({"script_callback_language":"python","script_callback":"exec(kwargs['node'].parm('parm').eval())"})
        parm_folder.addParmTemplate(button)
        #multistring
        multistring=hou.StringParmTemplate("pythonCode","PythonCode",1)         
        multistring.setTags({"editor":"1","editorlang":"python"})
        parm_folder.addParmTemplate(multistring)
        #append param
        parm_group.append(parm_folder)
        pyNull.setParmTemplateGroup(parm_group)













