#encoding utf-8
from PIL import Image
im=Image.open('lena.bmp')
height,width=im.height,im.width

im2=Image.new('1',(66,66),0)
for i in range(64):
  for j in range(64):
    im2.putpixel((1+j,1+i),1 if im.getpixel((j*8,i*8))>=128 else 0)
#im2.show()
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

  l=[[-1 for i in range(66)]for i in range(66)]

  for i in range(64):
    for j in range(64):
      l[i+1][j+1]=0

  for i in range(64):
    for j in range(64):
      p=getpixels(j+1,i+1,img)
      if p[0]:
        l[i+1][j+1]=f(h(p[0],p[1],p[6],p[2]),h(p[0],p[2],p[7],p[3]),h(p[0],p[3],p[8],p[4]),h(p[0],p[4],p[5],p[1]))
      else :
        l[i+1][j+1]=-1
  return l
yk=yokoi(im2)
'''
for i in range(66):
  for j in range(66):
    if yk[i][j]!=-1:
      print yk[i][j],
    else:
      print ' ',
  print
'''
def prf(yk,img):
  h=lambda a:1 if a==1 else 0
  #q=1 p=-1
  tmpimg=Image.new('1',(len(yk[1]),len(yk)),0)
  for i in range(tmpimg.height-2):
    for j in range(tmpimg.width-2):
      p=getpixels(j+1,i+1,img)

      cnt=0
      for k in range(1,5):
        cnt+=p[k]
      if p[0] and cnt:
        tmpimg.putpixel((j+1,i+1),1)
  return tmpimg

def img2list(img):
  res=[[0 for k in range(img.width)]for i in range(img.height)]
  for i in range(img.height):
    for j in range(img.width):
      res[i][j]=img.getpixel((j,i))
  return res
def shrink(img):
  tmp=img2list(img)
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
      p=getpixels(j+1,i+1,img)
      if p[0]:
        val=f(
          h(p[0],p[1],p[6],p[2]),
          h(p[0],p[2],p[7],p[3]),
          h(p[0],p[3],p[8],p[4]),
          h(p[0],p[4],p[5],p[1]),
          p[0])
        img.putpixel((j+1,i+1),val)
  return tmp
'''
sh=shrink(im2)
for i in range(64):
  for j in range(64):
    if sh[i][j]==1:
      print '*',
    else:
      print ' ',
  print
'''

im3=Image.new('1',(8,9),0)
seq=[0,0,0,0,0,0,0,0,
     0,0,0,1,1,0,0,0,
     0,0,1,1,1,1,0,0,
     0,1,1,1,1,1,1,0,
     0,0,1,1,0,1,1,0,
     0,0,0,1,0,1,1,0,
     0,0,0,1,0,1,1,0,
     0,0,0,1,0,1,1,0,
     0,0,0,0,0,0,0,0
     ]
'''
for i in range(len(seq)):
  im3.putpixel((i%8,i/8),seq[i])
  print seq[i],
  if i%8==7:
    print
'''

'''

'''

im3=prf(yk,im2)
im3.show()

shrink(im3)
sk=img2list(im3)
for i in range(im3.height):
  for j in range(im3.width):
    if sk[i][j]:
      print '*',
    else:
      print ' ',
  print
im3.show()

