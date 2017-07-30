nodeSelect = hou.selectedNodes()
black=hou.Color((0,0,0))
pink=hou.Color((0.9,0.304,0.9))
out= hou.node("/out")

for node in nodeSelect:
    parent = hou.parent()
    print parent
    getName = node.name()
    connectNode = node.outputs()
    outNull = node.createOutputNode("null",getName.upper())
    outNull.setPosition(node.position())
    outNull.move([0, -.75])
    outNull.setColor(black)
    myfile = outNull.createOutputNode("file",getName.upper()+"_CACHE")
    myfile.setColor(pink)
    myWriteGeo= out.createNode("geometry",getName.upper()+"_CACHE")
    myWriteGeo.setParms({"soppath":"/obj/"+getName.upper()})
 
