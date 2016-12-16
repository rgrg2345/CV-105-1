#encoding utf-8
from PIL import Image,ImageDraw

def main():
  im=Image.open('lena.bmp')
  height,width=im.height,im.width
  im2=im.copy()
  kernel=[[0,255,255,255,0],
         [255,255,255,255,255],
         [255,255,255,255,255],
         [255,255,255,255,255],
         [0,255,255,255,0]
         ]

  kwidth,kheight=len(kernel[0]),len(kernel)
  def checkbound(x,y,j,i):
    if x+j<0 or y+i<0 or x+j>=width or y+i >=height:
      return False
    return True

  def dilation(y,x,src,dst):
    if src.getpixel((x,y)):
      maxval=0
      for i in range(kheight):
        for j in range(kwidth):
          if(checkbound(x,y,j-2,i-2)):
            val=src.getpixel((x+j-2,y+i-2))
            if val >maxval:
              maxval=val
      dst.putpixel((x,y),maxval)

  for i in range(height):
    for j in range(width):
      dilation(i,j,im,im2)

  #im2.show()


  def erosion(y,x,src,dst):
    if src.getpixel((x,y)):
      minval=255
      for i in range(kheight):
        for j in range(kwidth):
          if(checkbound(x,y,j-2,i-2)):
            val=src.getpixel((x+j-2,y+i-2))
            if val <minval:
              minval=val
      dst.putpixel((x,y),minval)
  im3=im.copy()

  for i in range(height):
    for j in range(width):
      erosion(i,j,im,im3)
  #im3.show()
  im3.save('lenaErosion.jpg')


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
  im4=opening(im)
  #im4.show()
  im4.save('lenaOpening.jpg')

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

  im5=closing(im)
  #im5.show()
  im5.save('lenaClosing.jpg')

  def opening2closing(src):
    tmp=src.copy()
    op=opening(tmp)
    res=closing(op)
    return res

  g10=Image.open('gassian10.bmp')
  g30=Image.open('gassian30.bmp')
  sp5=Image.open('saltpepper5.bmp')
  sp10=Image.open('saltpepper10.bmp')
  g10f=opening2closing(g10)
  g30f=opening2closing(g30)
  sp5f=opening2closing(sp5)
  sp10f=opening2closing(sp10)

  g10f.save('gassian10open-close.bmp')
  g30f.save('gassian30open-close.bmp')
  sp5f.save('saltpepper5open-close.bmp')
  sp10f.save('saltpepper10open-close.bmp')


if __name__=='__main__':
    main()
