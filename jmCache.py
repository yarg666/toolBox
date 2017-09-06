
def cache ()

	import hou
	nodeSelect = hou.selectedNodes()
	black=hou.Color((0,0,0))
	pink=hou.Color((0.9,0.304,0.9))
	out= hou.node("/out")

	for node in nodeSelect:
	    parent = hou.parent()
	    parentString = parent.name()      
	    getName = node.name()
	    connectNode = node.outputs()
	    outNull = node.createOutputNode("null",getName.upper())
	    outNull.setPosition(node.position())
	    outNull.move([0, -.75])
	    outNull.setColor(black)
	    #set read node to read myWriteGeo
	    myFile = outNull.createOutputNode("file",getName.upper()+"_CACHE")
	    myFile.setColor(pink)
	    myFile.setParms({"file": "$"+"HIP/geo/"+"$"+"HIPNAME."+"$"+"OS."+"$"+"F.bgeo.sc"})
	    #set myWriteGeo to cache the myFile
	    myWriteGeo= out.createNode("geometry",getName.upper()+"_CACHE")
	    myWriteGeo.setParms({"soppath":"/obj/"+parentString+"/"+getName.upper()})
	    myWriteGeo.setParms({"trange":"normal"})
