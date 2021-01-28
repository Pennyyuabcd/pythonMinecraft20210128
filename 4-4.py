from mcpi.minecraft import Minecraft
PY=Minecraft.create()
list2 = [[12,41,14],[35,73,86]]
myID = PY.getPlayerEntityId("APE_41")
x,y,z = PY.entity.getTilePos(myID)
startX = x
for i in list2:
    for j in i:
        PY.setBlock(x,y,z,j)
        x = x+1
    x = startX
    z = z-1