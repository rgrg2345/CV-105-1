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
  im2.save('lenaDilation.jpg')


  def erosion(y,x,src,dst):
    if src.getpixel((x,y)):
      minval=255
      for i in range(kheight):
        for j in range(kwidth):
          if(checkbound(x,y,j-2,i-2)):
            val=src.getpixel((x+j-2,y+i-2))
            if val <minval:
              minval=va
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

  #for i in range(height):
  #  for j in range(width):
  #    tmp=abs(im5.getpixel((j,i))-im4.getpixel((j,i)))
  #    im5.putpixel((j,i),tmp)
  #im5.show()


if __name__=='__main__':
    main()
