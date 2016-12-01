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
  #im2.show()
  kernel=[[0,255,255,255,0],
          [255,255,255,255,255],
          [255,255,255,255,255],
          [255,255,255,255,255],
          [0,255,255,255,0]
    ]
  kwidth,kheight=len(kernel[0]),len(kernel)
  """
  for i in range(kheight):
    for j in range(kwidth):
      print kernel[i][j],
    print
  """
  def checkbound(x,y):
    if x-2<0 or y-2<0 or x+2>=width or y+2 >=height:
      return False
    return True
  def dilation(y,x,src,dst):
    if checkbound(x,y):
      if src.getpixel((x,y))==kernel[2][2]:
        for i in range(kheight):
          for j in range(kwidth):
            if dst.getpixel((x+j-2,y+i-2))==0:
              dst.putpixel((x+j-2,y+i-2),kernel[i][j])
  im3=im2.copy()

  for i in range(height):
    for j in range(width):
      dilation(i,j,im2,im3)
  im3.save('lenaDilation.bmp')
  im3.save('lenaDilation.jpg')

  def erosion(y,x,src,dst):
    def checkmatch():
      for i in range(kheight):
        for j in range(kwidth):
          if kernel[i][j] and src.getpixel((x+j-2,y+i-2)) != kernel[i][j]:
            return False
      return True
    if checkbound(x,y)== False or checkmatch() ==False:
      dst.putpixel((x,y),0)
    else :
      dst.putpixel((x,y),255)
  im4=im2.copy()

  for i in range(height):
    for j in range(width):
      erosion(i,j,im2,im4)
  im4.save('lenaErosion.bmp')
  im4.save('lenaErosion.jpg')
  def opening(src):
    tmp=src.copy()
    for i in range(height):
      for j in range(width):
        erosion(i,j,src,tmp)
    res=tmp.copy()
    for i in range(height):
      for j in range(width):
        dilation(i,j,tmp,res)
    return res

    """
    def checkmatch():
      for i in range(kheight):
        for j in range(kwidth):
          if kernel[i][j] and src.getpixel((x+j-2,y+i-2)) != kernel[i][j]:
            return False
      return True
    if checkbound(x,y)== False or checkmatch() ==False:
      dst.putpixel((x,y),0)
    else :
      for i in range(kheight):
        for j in range(kwidth):
          if kernel[i][j]:
            dst.putpixel((x+j-2,y+i-2),255)
    """
  im5=opening(im2)
  im5.save('lenaOpening.bmp')
  im5.save('lenaOpening.jpg')
  def closing(src):
    tmp=src.copy()
    for i in range(height):
      for j in range(width):
        dilation(i,j,src,tmp)
    res=tmp.copy()
    for i in range(height):
      for j in range(width):
        erosion(i,j,tmp,res)
    return res
  im6=closing(im2)
  im6.save('lenaClosing.bmp')
  im6.save('lenaClosing.jpg')

  kernel2=[[255,255],
            [0,255]
            ]
  def erosion2(y,x,src,dst,mode):
    def checkmatch():
      for i in range(2):
        for j in range(2):
          if mode ==0:
            if kernel2[i][j] and src.getpixel((x+j-1,y+i)) != kernel2[i][j]:
              return False
          else:
            if kernel2[i][j] and src.getpixel((x+j,y+i-1)) != kernel2[i][j]:
              return False
      return True
    chb=True
    if mode==0 :
      if x-1<0 or y<0 or x>=width or y+1 >=height:
        chb=False
    else:
      if x<0 or y-1<0 or x+1>=width or y>=height:
        chb=False
    if chb== False or checkmatch() ==False:
      dst.putpixel((x,y),0)
    else :
      dst.putpixel((x,y),255)
  def erosion3(y,x,src,dst,mode):
    def checkmatch():
      for i in range(kheight):
        for j in range(kwidth):
          if mode ==0:
            if kernel2[i][j] and src.getpixel((x+j-2,y+i-2)) != kernel2[i][j]:
              return False
          else:
            if kernel3[i][j] and src.getpixel((x+j-2,y+i-2)) != kernel3[i][j]:
              return False
      return True
    if checkbound(x,y)== False or checkmatch() ==False:
      dst.putpixel((x,y),0)
    else :
      dst.putpixel((x,y),255)


  im7=im2.copy()

  for i in range(height):
      for j in range(width):
        erosion2(i,j,im2,im7,0)

  #make complement
  im8=im2.copy()
  for i in range(height):
    for j in range(width):
      im8.putpixel((j,i),0 if im8.getpixel((j,i)) else 255)
  im9=im8.copy()
  for i in range(height):
    for j in range(width):
      erosion2(i,j,im8,im9,1)
  im9.show()


  for i in range(height):
    for j in range(width):
      im7.putpixel((j,i), 255 if (im7.getpixel((j,i)) and im9.getpixel((j,i))) else 0)
  im7.show()
  im7.save('lenaHit-and-Miss.bmp')
  im7.save('lenaHit-and-Miss.jpg')



if __name__=='__main__':
  main()
