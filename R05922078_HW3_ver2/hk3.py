#encoding uft-8
from PIL import Image
def main():
  im=Image.open('lena.bmp')
  height,width=im.height,im.width
  r=[0 for i in range(256)]
  s=[0 for i in range(256)]

  for i in range(height):
    for j in range(width):
      #decrease the luminance
      im.putpixel((j,i),im.getpixel((j,i))/3)
      #ori histogram
      r[im.getpixel((j,i))]+=1
  #print r
  im.show()

  '''formula
     sk= 255*sumation 0 to k(nl/N)
  '''
  for i in range(256):
    tmp=0
    for j in range(i+1):
      tmp+=r[j]
    tmp*=255
    tmp=tmp/float(height*width)
    s[i]=int(round(tmp))
    #print "%d,"%s[i],


  #new image
  for i in range(height):
    for j in range(width):
      im.putpixel((j,i),s[im.getpixel((j,i))])
  im.save('lena_histogram_equalization.bmp')
  im.save('lena_histogram_equalization.jpg')

  his=[0 for i in range(256)]
  #output histogram
  for i in range(height):
    for j in range(width):
      his[im.getpixel((j,i))]+=1


if __name__=='__main__':
  main()
