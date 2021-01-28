from mcpi.minecraft import Minecraft
PY=Minecraft.create()
import random
x,y,z=PY.player.getTilePos()
for i in range(20):
    r = random.randrange(1,7)
    if r == 1:
        PY.setBlocks(x,y,z,x,y,z+4,95)
        z=z+4
    if r == 2:
        PY.setBlocks(x,y,z,x,y,z-4,57)
        z=z-4
    if r == 3:
        PY.setBlocks(x,y,z,x+4,y,z,56)
        x=x+4
    if r == 4:
         PY.setBlocks(x,y,z,x-4,y,z,41)
         x=x-4
    if r == 5:
        PY.setBlocks(x,y,z,x,y+4,z,35)
        y=y+4
    if r == 6:
        PY.setBlocks(x,y,z,x,y-4,z,88)
        y=y-4