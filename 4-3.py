from mcpi.minecraft import Minecraft
PY=Minecraft.create()
from random import randrange
for i in range(10):
    x,y,z=PY.player.getTilePos()
    z=z+i
    for j in range(10):
        color=randrange(0,16)
        x=x+1
        PY.setBlock(x,y,z,35,color)
ans=randrange(0,16)
while True:
    hits=PY.events.pollBlockHits()
    if len(hits)>0:
        h=hits[0]
        block=PY.getBlockWithData(h.pos)
        data=block.data
        if data == ans:
            PY.postToChat("恭喜你找到啦!")
            PY.setBlock(h.pos,57)
            break
        elif data<ans:
            PY.postToChat("找錯囉~~~找大點的吧!")
        elif data>ans:
            PY.postToChat("找錯囉~~~找小點的吧!")
            
                         