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
