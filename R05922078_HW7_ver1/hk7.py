#encoding utf-8
from PIL import Image
im=Image.open('lena.bmp')
height,width=im.height,im.width

#downsampling
im2=Image.new('1',(66,66),0)
for i in range(64):
  for j in range(64):
    im2.putpixel((1+j,1+i),1 if im.getpixel((j*8,i*8))>=128 else 0)
im2.save('lena_down_bin.bmp')
def getpixels(j,i,img):
  ps=[0 for k in range(9)]
  ps[0]=img.getpixel((j,i))
  ps[1]=img.getpixel((j+1,i))
  ps[2]=img.getpixel((j,i-1))
  ps[3]=img.getpixel((j-1,i))
  ps[4]=img.getpixel((j,i+1))
  ps[5]=img.getpixel((j+1,i+1))
  ps[6]=img.getpixel((j+1,i-1))
  ps[7]=img.getpixel((j-1,i-1))
  ps[8]=img.getpixel((j-1,i+1))
  return ps

def img2list(img):
  res=[[0 for k in range(img.width)]for i in range(img.height)]
  for i in range(img.height):
    for j in range(img.width):
      res[i][j]=img.getpixel((j,i))
  return res

def checkimgsame(im1,im2):#base on img2list, it's not a efficient way to compare but convenient for testing
  im1list=img2list(im1)
  im2list=img2list(im2)
  for i in range(len(im1list)):
    for item1,item2 in zip(im1list[i],im2list[i]):
      if item1!=item2:
        return False
  return True



def yokoi(img):
  def h(b,c,d,e):
    #q=1,r=2,s=3
    if b == c:
      if d==b and e==b :
        return 2 #r
      elif d!=b or e!=b:
        return 1 #q
      return 0
    else :
      return 3   #s
  def f(a,b,c,d):
    cnt =0
    if a==b and b==c and c==d and d==2:
      return 5
    if a==1:
      cnt+=1
    if b==1:
      cnt+=1
    if c==1:
      cnt+=1
    if d==1:
      cnt+=1
    return cnt

  l=[[-1 for i in range(img.width)]for i in range(img.height)]


  for i in range(img.height-2):
    for j in range(img.width-2):
      l[i+1][j+1]=-1

  for i in range(img.height-2):
    for j in range(img.width-2):
      p=getpixels(j+1,i+1,img)
      if p[0]:
        l[i+1][j+1]=f(h(p[0],p[1],p[6],p[2]),h(p[0],p[2],p[7],p[3]),h(p[0],p[3],p[8],p[4]),h(p[0],p[4],p[5],p[1]))
      else :
        l[i+1][j+1]=-1
  return l


def prf(img,yk):
  h=lambda a:1 if a==1 else 0
  #deletable =1 else 0
  #q=0, p=1
  prlist=[[0 for i in range(img.width)]for j in range(img.height) ]
  #only do interior 64x64
  for s in range(img.height-2):
    for b in range(img.width-2):
      i,j=s+1,b+1
      #self y-num=1 and have at least one neighbor also have y-num=1
      if(yk[i][j]==1 and (yk[i][j+1]==1 or yk[i][j-1]==1 or yk[i+1][j]==1 or yk[i-1][j]==1)):
        prlist[i][j]=1
  return prlist

def shrink(img,mark):
  #tmp=img2list(img)
  tmp=img.copy()
  #resimg=Image.new('1',(tmp.width,tmp.height),0)
  def h(b,c,d,e):
    if( b==c and (d!=b or e!=b)):
      return 1
    else:
      return 0
  def f(a,b,c,d,x):
    if (a+b+c+d)==1 :
      return 0 #g=0
    else:
      return x

  #y=[[0 for k in range(7)]for i in range(6)]
  for i in range(img.height-2):
    for j in range(img.width-2):
      p=getpixels(j+1,i+1,tmp)#mark :border , marked: deletable?
      if p[0]  and  mark[i+1][j+1]==1:#only deletable pixel which is border could be delete
        val=f(
          h(p[0],p[1],p[6],p[2]),
          h(p[0],p[2],p[7],p[3]),
          h(p[0],p[3],p[8],p[4]),
          h(p[0],p[4],p[5],p[1]),
          p[0])
        tmp.putpixel((j+1,i+1),val)
        #resimg.putpixel((j+1,i+1),val)

  return tmp

def thin(img):
  im2=img.copy()
  im3=img.copy()
  cnt=1
  flag=False
  while not flag:
    print 'iteration %d..'%cnt
    cnt+=1
    yk=yokoi(im2)
    pr=prf(im2,yk)
    im3=shrink(im2,pr)
    flag=checkimgsame(im2,im3)
    im2=im3.copy()

  return im3

im3=thin(im2)
im3.show()
im3.save('lena_out.bmp')
