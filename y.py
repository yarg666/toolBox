

""" setup une start scene basique
"""

def unDeuxTrois():
    import hou
    obj = hou.node("/obj")

    cam = obj.createNode("cam","myCam")
    cam.setParms({"resx":1920,"resy":1080})
    cam.setParms({"tz":3,"ty":1.7})

    geo1 = obj.createNode ("geo","myGeo")
    geo1.move([0, -2])
    file1 = hou.node("/obj/myGeo/file1")
    file1.destroy()
      
    env = obj.createNode("envlight","myEnv")
    env.setParms ({"env_map":"$HFS/houdini/pic/DOSCH_SKIESV2_01SN_lowres.rat"})
    env.move([0, 1])

    out = hou.node("/out")
    mantra = out.createNode("ifd","myMantra")
    mantra.setParms({"vm_renderengine":"pbrraytrace","camera":"/obj/myCam"})

    shop = hou.node("/shop")
    mat = shop.createNode("principledshader","myMat")
    mat.setParms({"basecolorr":1,"basecolorg":1,"basecolorb":1}) 


""" setup the houdini desktop 
"""
def quatreCinqSix():
    import hou
    desktops_dict = dict((d.name(), d) for d in hou.ui.desktops())
    desktops_dict['Technical'].setAsCurrent()

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

        outBound.parm('boundx').setExpression("bbox(opinputpath('.',0),D_XSIZE)")
        outBound.parm('boundy').setExpression("bbox(opinputpath('.',0),D_YSIZE)")
        outBound.parm('boundz').setExpression("bbox(opinputpath('.',0),D_ZSIZE)")

        outBound.parm('centroidx').setExpression("centroid(opinputpath('.',0),D_X)")
        outBound.parm('centroidy').setExpression("centroid(opinputpath('.',0),D_Y)")
        outBound.parm('centroidz').setExpression("centroid(opinputpath('.',0),D_Z)")

""" cache cree un rop output dans /out et le recharge dans le context d'origine
cela permet d'enchainer les depandences dans /out et de les relirent automatiquement
dans dans le contexte d'origine
"""

def cacheBgeo ():
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
        myFile.setParms({'file': '$HIP/cache/rop_sfx/bgeo.sc/$OS/v`padzero(3,chs("/out/$OS/version"))`/$OS.$F5.bgeo.sc'})
        myWriteGeo= out.createNode("geometry",getName.upper()+"_CACHE")
        myWriteGeo.setParms({"soppath":"/obj/"+parentString+"/"+getName.upper()})
        myWriteGeo.setParms({"sopoutput":"$HIP/cache/rop_sfx/bgeo.sc/$OS/v`padzero(3, ch('version'))`/$OS.$F5.bgeo.sc"})
        myWriteGeo.setParms({"trange":"normal"})

        #add create param for versionning
        parm_group = myWriteGeo.parmTemplateGroup()
        parm_folder = hou.FolderParmTemplate("folder","version")
        parm_folder.addParmTemplate(hou.IntParmTemplate("version","Version",1))
        parm_group.append(parm_folder)
        myWriteGeo.setParmTemplateGroup(parm_group)


def cacheVdb ():
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
        myFile.setParms({'file': '$HIP/cache/rop_sfx/vdb/$OS/v`padzero(3,chs("/out/$OS/version"))`/$OS.$F5.vdb'})
        myWriteGeo= out.createNode("geometry",getName.upper()+"_CACHE")
        myWriteGeo.setParms({"soppath":"/obj/"+parentString+"/"+getName.upper()})
        myWriteGeo.setParms({"sopoutput":"$HIP/cache/rop_sfx/vdb/$OS/v`padzero(3, ch('version'))`/$OS.$F5.vdb"})
        myWriteGeo.setParms({"trange":"normal"})

        #add create param for versionning
        parm_group = myWriteGeo.parmTemplateGroup()
        parm_folder = hou.FolderParmTemplate("folder","version")
        parm_folder.addParmTemplate(hou.IntParmTemplate("version","Version",1))
        parm_group.append(parm_folder)
        myWriteGeo.setParmTemplateGroup(parm_group)
        

"""
y.pywy genere un node python pour tester des scripts avec un bouton run script et c'est pratique
"""

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













