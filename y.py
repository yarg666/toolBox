
"""setup scene to manual mode
"""
def manual():
    import hou
    hou.setUpdateMode(hou.updateMode.Manual)

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


""" set the houdini desktop 
"""
def quatreCinqSix():
    import hou
    desktops_dict = dict((d.name(), d) for d in hou.ui.desktops())
    desktops_dict['Technical'].setAsCurrent()
	
    mode = hou.updateModeSetting().name()
    if mode == 'AutoUpdate':
        hou.setUpdateMode(hou.updateMode.Manual)


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

        #add create param for versionning and export format
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

def cacheAbc ():
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
        myFile = outNull.createOutputNode("alembic",getName.upper()+"_CACHE")
        myFile.setColor(pink)
        myFile.setParms({'fileName': '$HIP/cache/rop_sfx/abc/$OS/v`padzero(3,chs("/out/$OS/version"))`/$OS.abc'})
        #set write geo in out context
        myWriteGeo=out.createNode("alembic",getName.upper()+"_CACHE")
        #set parm
        myWriteGeo.setParms({"use_sop_path":1})
        myWriteGeo.setParms({"sop_path":"/obj/"+parentString+"/"+getName.upper()})
        myWriteGeo.setParms({"filename":"$HIP/cache/rop_sfx/abc/$OS/v`padzero(3, ch('version'))`/$OS.abc"})
        myWriteGeo.setParms({"trange":"normal"})
        #add create param for versionning
        parm_group = myWriteGeo.parmTemplateGroup()
        versionParm =hou.IntParmTemplate("version","Version",1)
        target_folder = ("Main")
        parm_group.appendToFolder(target_folder,versionParm)
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
        button.setTags({"script_callback_language":"python","script_callback":"exec(kwargs['node'].parm('pythonCode').eval())"})
        parm_folder.addParmTemplate(button)
        #multistring
        multistring=hou.StringParmTemplate("pythonCode","PythonCode",1)         
        multistring.setTags({"editor":"1","editorlang":"python"})
        parm_folder.addParmTemplate(multistring)
        #append param
        parm_group.append(parm_folder)
        pyNull.setParmTemplateGroup(parm_group)

def normalizeGeoVex ():
    import hou
    nodeSelect = hou.selectedNodes()
    pink=hou.Color ((0.9,0.304,0.9))

    for node in nodeSelect:
        wrangleSnippet=node.createOutputNode("attribwrangle","normalizeGeoVexByHeight")
        wrangleSnippet.setColor(pink)
        wrangleSnippet.setParms({"snippet":"""
//center geo
vector min, max;
getbbox(0, min, max);
vector centroid = (min+max)/2;;
@P+= centroid*-1;

@P*= 1/(max.y-min.y); //normalize by max height 
@P.y+=0.5; //normalize by max height

@P*=ch('realScale'); //real scale"""}) 
        print("--- Don't forget to just clic for create channels param in the wrangle node ---")


def camUvDelete ():
    import hou
    nodeSelect = hou.selectedNodes()
    pink=hou.Color ((0.9,0.304,0.9))

    for node in nodeSelect:
        wrangleSnippet=node.createOutputNode("attribwrangle","camUvDelete")
        wrangleSnippet.setColor(pink)
        wrangleSnippet.setParms({"snippet":"""
vector ndc=toNDC(chs("camPath"),@P);
@Cd = ndc; // viz
float secu = 0.1;
if(ndc.x+secu<0||ndc.x-secu>1||ndc.y+secu<0||ndc.y-secu>1||ndc.z>1){
removepoint(geoself(),@ptnum);
}"""}) 
        print("--- Don't forget to check the campath in camUvdelete ---")

def camUvDeleteAnim ():
    import hou
    nodeSelect= hou.selectedNodes()
    pink=hou.Color ((0.9,0.304,0.9))
    black=hou.Color ((0,0,0))

    for node in nodeSelect:
        parent = node.parent()
        parentString= parent.name()
        getName= node.name()
        connectNode = node.outputs()
        outNull = node.createOutputNode("null","inCamDeleteAnim")
        outNull.setPosition(node.position())
        outNull.move([0, -.75])
        outNull.setColor(black)
        #create left branch
        blackColor= outNull.createOutputNode("color","black")
        blackColor.move([-.75, -.75])
        blackColor.setParms({"colorr":0,"colorg":0,"colorb":0})
        #create right branch
        wrangleSnippet=outNull.createOutputNode("attribwrangle","camUvDelete")
        wrangleSnippet.setColor(pink)
        wrangleSnippet.setParms({"snippet":"""
vector ndc=toNDC("/obj/root/transform/camera/cambaked/ppCam/ppCamShape",@P); // DONT FORGET TO FILL CAM PATH
@Cd = ndc; // viz
float secu = 0.1;
if(ndc.x+secu<0||ndc.x-secu>1||ndc.y+secu<0||ndc.y-secu>1||ndc.z>1){
removepoint(geoself(),@ptnum);
}"""}) 
        wrangleSnippet.move([0.75, -.75])
        redColor= wrangleSnippet.createOutputNode("color","red")
        redColor.move([0, -.35])
        redColor.setParms({"colorr":1,"colorg":0,"colorb":0}) 
        #create solver
        mysolver = blackColor.createOutputNode("solver","transferColor")
        solverName = mysolver.name()
        mysolver.move([0, -1.5]) 
        mysolver.setInput(1,redColor)
        mytransfert = hou.node('/obj/'+parentString+'/'+solverName+'/d/s').createNode('attribtransfer','transferUv')
        hou.node('/obj/'+parentString+'/'+solverName+'/d/s/transferUv').setInput(0,hou.node('/obj/'+parentString+'/'+solverName+'/d/s/Prev_Frame'))
        hou.node('/obj/'+parentString+'/'+solverName+'/d/s/transferUv').setInput(1,hou.node('/obj/'+parentString+'/'+solverName+'/d/s/Input_2'))
        mytransfert.setDisplayFlag(True) #set display flag true
        mytransfert.setParms({"thresholddist":0.1})
        time = mysolver.createOutputNode("timeshift","Fend")
        time.parm("frame").deleteAllKeyframes()
        time.setParms({"frame":240})
        
        removePointVex=time.createOutputNode("attribwrangle","deleteGeo")
        removePointVex.setColor(pink)
        removePointVex.setParms({"snippet":"""
if(@Cd.x<0.5)removepoint(0,@ptnum);
"""}) 
        removePointVex.setDisplayFlag(True)

        print("--- Don't forget to check the campath in camUvdelete ---")

def fillHoles ():
    import hou
    nodeSelect = hou.selectedNodes()
    pink=hou.Color ((0.9,0.304,0.9))

    for node in nodeSelect:
        wrangleSnippet=node.createOutputNode("attribwrangle","simpleFillHoles")
        wrangleSnippet.setColor(pink)
        wrangleSnippet.setParms({"snippet":"""
float searchrad=ch("searchrad");
float mindist=ch("mindist");
int maxpoints=chi("maxpoints");
int fillpoints=chi("fillpts");

vector clpos;
int handle=pcopen(0,"P",@P,searchrad,maxpoints+1);
int i=0;
while(pciterate(handle))
{
    if (i==0) // the first point found should be the closest, in this case, itself. We want to skip it.
    {
        i++;
        continue;
    }
    pcimport(handle,"P",clpos);
    if (length(@P-clpos)>mindist)
    {
        vector pointstep=(clpos-@P)/(fillpoints*2+1); // this ensures there are no duplicate point
                                                     // at the cost of doubling the fill points number
        for (int t=0;t<fillpoints;t++)
            addpoint(0,@P+(pointstep*float(t+1)));
    }
}

}"""}) 
        print("--- Don't forget to create the channel ---")


def inputColor ():
    import hou
    nodeSelect = hou.selectedNodes()
    
    for node in nodeSelect:
        inputNode = node.inputs()
        currentColor = node.color()
        for n in inputNode:
            n.setColor(currentColor)






