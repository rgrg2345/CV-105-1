#encoding utf-8
from PIL import Image,ImageDraw
import random
def main():
  im=Image.open('lena.bmp')
  height,width=im.height,im.width

  im2=im.copy()
  #binarize
  for i in range(height):
    for j in range(width):
      im2.putpixel((j,i),255 if im2.getpixel((j,i))>=128 else 0)
  im2.save('lenabin.bmp')
  im2.save('lenabin.jpg')
  #im2.show()

  histogram=[0 for i in range(256)]
  #count
  for i in range(height):
    for j in range(width):
      histogram[im.getpixel((i,j))]+=1


  #connected component
  def get_min_neighbor(m,y,x,height,width):
    offsets=[[0,-1],[1,0],[0,1],[-1,0]]
    minn=m[y][x]
    for off in offsets:
      ix=x+off[1]
      iy=y+off[0]
      if ix<0 or ix>=width or iy<0 or iy>=height or m[iy][ix]==0:
        continue

      if m[iy][ix]<minn:
        minn=m[iy][ix]
    return minn


  #initialize
  maps=[[0 for j in range(width)]for i in range(height)]
  labelcnt=1
  for i in range(height):
    for j in range(width):
      if im2.getpixel((j,i))==255:
        maps[i][j]=labelcnt
        labelcnt+=1

  #iterative algorithm
  changed=True
  while changed==True:
    changed=False
    #top-down
    for i in range(height):
      for j in range(width):
        if maps[i][j]==0:
          continue
        minn=get_min_neighbor(maps,i,j,height,width)
        if maps[i][j]!=minn:
          maps[i][j]=minn
          changed=True

    #bottom-up
    for i in range(height):
      for j in range(width):
        x=width-j-1
        y=height-i-1
        if maps[y][x]==0:
          continue
        minn=get_min_neighbor(maps,y,x,height,width)
        if maps[y][x]!=minn:
          maps[y][x]=minn
          changed=True

  #bounding box
  boundlist=[]
  #find bound
  region=[0 for i in range(0,labelcnt)]
  centroid=[]
  for i in range(height):
    for j in range(width):
      region[maps[i][j]]+=1

  for r in range(1,labelcnt):
    if region[r]>=500:
      bottom,top,left,right=-1,width,height,-1
      sumx,sumy,cnt=0,0,0
      for y in range(height):
        for x in range(width):
          if(maps[y][x]==r):
            if x< left:
              left=x
            if y< top:
              top=y
            if y>bottom:
              bottom=y
            if x>right:
              right=x
            cnt+=1
            sumx+=x
            sumy+=y
      centroid.append([sumx/cnt,sumy/cnt])
      boundlist.append([left,top,right,bottom])

  im3=Image.new('RGBA',(width,height),(0,0,0,0))
  rgb_im=im.convert('RGB')

  for i in range(height):
    for j in range(width):
      pix=im2.getpixel((j,i))
      rgb_im.putpixel((j,i),(pix,pix,pix,0))
  draw = ImageDraw.Draw(rgb_im)
  for i in range(len(boundlist)):
    n=random.randrange(255)
    pix=(0,255,0,0)
    #draw bounding
    draw.line([boundlist[i][0],boundlist[i][1],boundlist[i][2],boundlist[i][1]],pix)
    draw.line([boundlist[i][0],boundlist[i][1],boundlist[i][0],boundlist[i][3]],pix)
    draw.line([boundlist[i][2],boundlist[i][1],boundlist[i][2],boundlist[i][3]],pix)
    draw.line([boundlist[i][0],boundlist[i][3],boundlist[i][2],boundlist[i][3]],pix)

    #draw centroid
    cx,cy=centroid[i][0],centroid[i][1]
    def find_end(c,m,b):
      for i in range(b):
        if m and c+(b-i)<m:
          return c+(b-i)
        if m==0 and c-(b-i)>=0:
          return c-(b-i)
      return c
    dx=find_end(cx,width,10)
    ux=find_end(cx,0,10)
    dy=find_end(cy,height,10)
    uy=find_end(cy,0,10)

    draw.line([ux,cy,dx,cy],pix)
    draw.line([cx,uy,cx,dy],pix)

  rgb_im.save('lenas.bmp')
  rgb_im.save('lenas.jpg')

if __name__=='__main__':
  main()
