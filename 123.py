
obj = hou.node("/obj")
cam = obj.createNode("cam","myCam")
cam.setParms({"resx":1920,"resy":1080})
cam.setParms({"tz":3,"ty":1.7})
