0707070000010000000006660000000000000000010000001326363346200000700000000237.start fplayback -i on -r off -f 1 -e on -h on -t on -a on -k on -s 1
tcur 0
fps 24
tset 0 10
frange 1 240
unitlength 1
unitmass 1
prompt '`strcat(oppwf(), " -> ")`'
0707070000010000000006660000000000000000010000001326363346200001300000000767.variables set -g ACTIVETAKE = 'Main'
set -g E = '2.7182818284590452354'
set -g EYE = 'stereo'
set -g HIP = '/run/media/jmargelin/ok/toolBox'
set -g HIPFILE = '/run/media/jmargelin/ok/toolBox/sopTools.hip'
set -g HIPNAME = 'sopTools'
set -g JOB = '/users/jmargelin'
set -g PI = '3.1415926535897932384'
set -g POSE = '/users/jmargelin/houdini16.0/poselib'
set -g _HIP_SAVEPLATFORM = 'linux-x86_64-gcc4.8'
set -g _HIP_SAVETIME = 'Thu Apr 12 12:38:42 2018'
set -g _HIP_SAVEVERSION = '16.0.504.20'
set -g status = '0'
0707070000010000000006660000000000000000010000001326363346200001100000000310.aliases alias bye 'quit'
alias cd 'opcf'
alias cp 'opcp'
alias h 'history'
alias hython 'python'
alias ls 'opls'
alias matramp 'opramp'
alias opcd 'opcf'
alias oppwd 'oppwf'
alias pwd 'oppwf'
alias rm 'oprm'
0707070000010000000006660000000000000000010000001326363346200001400000000021.takeconfig takename -g take
0707070000010000000006660000000000000000010000001326363346200001500000000000.hou.session 0707070000010000000006660000000000000000010000001326363346200001500000000000.OPlibraries 0707070000010000000006660000000000000000010000001326363346200001700000000000.OPpreferences 0707070000010000000006660000000000000000010000001326363346200002000000000012expression.func # 0 bytes
0707070000010000000006660000000000000000010000001326363346200001000000000665vex.def comment ""
position 5.5 2.5
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1523529477
  modify 1523529478
  author jmargelin@ws102.prs.vfx.int
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001326363346200001100000000020vex.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001326363346200001500000000044vex.userdata     ___Version___    16.0.504.200707070000010000000006660000000000000000010000001326363346200001000000000663mat.def comment ""
position 5 1.5
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1523529477
  modify 1523529478
  author jmargelin@ws102.prs.vfx.int
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001326363346200001100000000020mat.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001326363346200001500000000044mat.userdata     ___Version___    16.0.504.200707070000010000000006660000000000000000010000001326363346200001000000000657obj.def comment ""
position 5 2
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display on render on highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1523529477
  modify 1523529482
  author jmargelin@ws102.prs.vfx.int
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001326363346200001100000000020obj.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001326363346200001500000000044obj.userdata     ___Version___    16.0.504.200707070000010000000006660000000000000000010000001326363346200001000000000002obj.net 1
0707070000010000000006660000000000000000010000001326363346200001000000000663out.def comment ""
position 5 0.5
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1523529477
  modify 1523529478
  author jmargelin@ws102.prs.vfx.int
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001326363346200001100000000020out.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001326363346200001500000000044out.userdata     ___Version___    16.0.504.200707070000010000000006660000000000000000010000001326363346200001000000000002out.net 1
0707070000010000000006660000000000000000010000001326363346200001100000000666part.def comment ""
position 5.5 1.5
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed off
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1523529477
  modify 1523529479
  author jmargelin@ws102.prs.vfx.int
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001326363346200001200000000020part.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001326363346200001600000000044part.userdata     ___Version___    16.0.504.200707070000010000000006660000000000000000010000001326363346200001100000000002part.net 1
0707070000010000000006660000000000000000010000001326363346200000700000000663ch.def comment ""
position 4.5 1
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1523529477
  modify 1523529478
  author jmargelin@ws102.prs.vfx.int
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001326363346200001000000000020ch.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001326363346200001400000000044ch.userdata     ___Version___    16.0.504.200707070000010000000006660000000000000000010000001326363346200000700000000002ch.net 1
0707070000010000000006660000000000000000010000001326363346200001100000000661shop.def comment ""
position 5 3
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1523529477
  modify 1523529478
  author jmargelin@ws102.prs.vfx.int
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001326363346200001200000000020shop.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001326363346200001600000000044shop.userdata     ___Version___    16.0.504.200707070000010000000006660000000000000000010000001326363346200001100000000002shop.net 1
0707070000010000000006660000000000000000010000001326363346200001000000000665img.def comment ""
position 4.5 2.5
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1523529477
  modify 1523529479
  author jmargelin@ws102.prs.vfx.int
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001326363346200001100000000020img.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001326363346200001500000000044img.userdata     ___Version___    16.0.504.200707070000010000000006660000000000000000010000001326363346200001700000000032img/comp1.init type = img
matchesdef = 0
0707070000010000000006660000000000000000010000001326363346200001600000000661img/comp1.def comment ""
position 0 0
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1523529478
  modify 1523529478
  author jmargelin@ws102.prs.vfx.int
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001326363346200001700000000020img/comp1.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001326363346200002300000000044img/comp1.userdata     ___Version___    16.0.504.200707070000010000000006660000000000000000010000001326363346200001600000000002img/comp1.net 1
0707070000010000000006660000000000000000010000001326363346200001000000000002img.net 1
0707070000010000000006660000000000000000010000001326363346200001000000000002vex.net 1
0707070000010000000006660000000000000000010000001326363346200001000000000002mat.net 1
0707070000010000000006660000000000000000010000001326363346200002600000000000.scenefilevisualizers 0707070000010000000006660000000000000000010000001326363346200000700000000060.takes HoudiniTakeFile 1.0
take name Main kids 0
   e
0707070000010000000006660000000000000000010000001326363346200001000000000007.styles NSJb{}0707070000010000000006660000000000000000010000001326363346200000500000000024.cwd opcf /
takeset Main
0707070000010000000006660000000000000000010000001326363346200001300000000000TRAILER!!! 