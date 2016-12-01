#encoding utf-8
from PIL import Image
def main():
  im = Image.open("lena.bmp")
  height,width=im.height,im.width
  print height,width
  im2=im.copy()

  def swapPixel(im,c1,c2):
    tmp=im.getpixel(c2)
    im.putpixel(c2,im.getpixel(c1))
    im.putpixel(c1,tmp)

  #upside-down
  for i in range(height/2):
    for j in range(width):
      swapPixel(im2,(j,i),(j,height-i-1))
  im2.save('lenaud.bmp')
  #im2.show()


  #right-side-left
  im3=im.copy()

  for i in range(width/2):
    for j in range(height):
      swapPixel(im3,(i,j),(width-i-1,j))
  im3.save('lenarl.bmp')
  #im3.show()

  #diagonally mirrored
  im4=im.copy()
  for i in range(height):
    for j in range(i,width):
      swapPixel(im4,(i,j),(j,i))
  im4.save('lenediagonal.bmp')
  #im4.show()

  im5=im.rotate(-45)
  im5.save('lenerotate.bmp')

  for i in range(width):
    for j in range(height):
      im.putpixel((i,j),255 if im.getpixel((i,j))>=128 else 0)
  im.save('lenabin.bmp')

if __name__=='__main__':
  main()


