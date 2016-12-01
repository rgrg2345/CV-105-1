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



def markInter_Border(img):
  #only do interior region
  #border=1, interior =2, other=0

  #initialize list
  mark=[ [0 for j in range(img.width-2)]for i in range(img.height-2)]
  for i in range(img.height-2):
    for j in range(img.width-2):
      p=getpixels(j+1,i+1,img)
      if p[0]:
        cnt=0
        for k in range(1,5):
          cnt+=p[k]
        if cnt==4:#
          mark[i][j]=2
        else:
          mark[i][j]=1
  return mark

#get 'b' 'i'


#for test interior /border
'''
for i in range(len(mark)):
  for j in range(len(mark[0])):
    if mark[i][j]==0:
      print ' ',
    elif mark[i][j]==1:
      print 'b',
    else:
      print 'i',
  print
'''

#vulnerable code but easy to write
def boundborder(mark):
  marked=[ [0 for i in range(len(mark[0]))]for j in range(len(mark))]

  #8-connectivity
  #surround=[[-1,-1],[0,-1],[1,-1],
  #        [-1,0],        [1,0],
  #        [-1,1],[0,1]  ,[1,1]]

  #4-connectivity
  surround=[[-1,0],[1,0],[0,-1],[0,1]]


  #mark b pixel next to i
  for i in range(len(mark)):
    for j in range(len(mark[0])):
      if mark[i][j]==2:#interior pixel
        for item in surround:
          if mark[i+item[1]][j+item[0]]==1: #must be border to marked
            marked[i+item[1]][j+item[0]]=1
  return marked
'''
#for test
for i in range(len(marked)):
  for j in range(len(marked[0])):
    if marked[i][j]:
      print 'b',
    else:
      print ' ',
  print
'''
#yk=yokoi(im2)
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

#doesn't need to do it
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


def checkimgsame(im1,im2):
  im1list=img2list(im1)
  im2list=img2list(im2)
  for i in range(len(im1list)):
    for item1,item2 in zip(im1list[i],im2list[i]):
      if item1!=item2:
        return False
  return True
def thin(img):
  im3=img.copy()
  im4l=img2list(img)
  for i in range(len(im4l)):
    for item in im4l[i]:
      print item,
    print
  cnt=1
  flag=False
  while not flag:
    print 'iteration %d..'%cnt
    cnt+=1
    yk=yokoi(img)
    pr=prf(img,yk)
    im3=shrink(img,pr)
    flag=checkimgsame(img,im3)
    img=im3.copy()

    '''
    for i in range(len(mark)):
      for item in mark[i]:
        if item==2:
          print 'i',
        elif item==1:
          print 'b',
        else:
          print ' ',
      print
    '''
    print 'yk %d'%len(yk)
    for i in range(len(yk)):
      for item in yk[i]:
        if item==-1:
          print ' ',
        else:
          print item,
      print

    for i in range(len(pr)):
      for item in pr[i]:
        if item:
          print 'd',
        else:
          print ' ',
      print
    im4l=img2list(img)
    for i in range(len(im4l)):
      for item in im4l[i]:
        print item,
      print
  return img

im4=im2.copy()
im3=thin(im2)
im3.show()
im3.save('lena_out.bmp')

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

for i in range(len(seq)):
  im3.putpixel((i%8,i/8),seq[i])
mark=[[1 for i in range(8)]for j in range(9)]
im4=thin(im3)
im4.show()

'''


'''


im3=Image.new('1',(9,8),0)
seq=[0,0,0,0,0,0,0,0,0,
     0,1,1,1,1,1,1,0,0,
     0,1,1,1,1,1,1,0,0,
     0,1,1,1,1,1,1,1,0,
     0,1,0,0,1,1,1,1,0,
     0,1,0,0,0,1,1,1,0,
     0,1,0,0,0,0,0,1,0,
     0,0,0,0,0,0,0,0,0
     ]

for i in range(len(seq)):
  im3.putpixel((i%9,i/9),seq[i])
mark=markInter_Border(im3)
im3.show()

#for test interior /border
for i in range(len(mark)):
  for j in range(len(mark[0])):
    if mark[i][j]==0:
      print ' ',
    elif mark[i][j]==1:
      print 'b',
    else:
      print 'i',
  print

print

print
yk=yokoi(im3)
for i in range(len(yk)):
  for item in yk[i]:
    if item==-1:
      print ' ',
    else:
      print item,
  print

pr=prf(im3,yk)
marked=boundborder(mark)
delete=deletable(marked,pr)
#for test
for i in range(len(delete)):
  for item,i2 in zip(delete[i],mark[i]):
    if i2:
      if item:
        print 'p',
      else:
        print 'q',
    else:
      print ' ',
  print

im4=shrink(im3,delete)
im4.show()
'''

'''


def zthin(img):
  tmp=img.copy()
  def A(j,i):
    flag=False
    #clockwiseq=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    clockwiseq=[[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1]]
    p=getpixels(j,i,img)

    cnt=0
    for k in range(1,9):
      cnt+=p[k]
    cnt1to0=0
    prev=p[2]
    print '\n(%d,%d):'%(j,i),
    for item in clockwiseq:
      now=img.getpixel((j+item[0],i+item[1]))
      print '%d - %d '%(prev,now),
      if prev-now==1:
        cnt1to0+=1
      prev=now
    if cnt1to0==1:
      print ' v',
    if (p[2]*p[1]*p[4]==0 and p[1]*p[4]*p[3]==0 and 2<=cnt<=6 and cnt1to0==1):
      return True
    else:
      return False
  def B(j,i):
    flag=False
    clockwiseq=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    p=getpixels(j,i,img)

    cnt=0
    for k in range(1,9):
      cnt+=p[k]
    cnt1to0=0
    prev=p[2]
    print '\n(%d,%d):'%(j,i),
    for item in clockwiseq:
      now=img.getpixel((j+item[0],i+item[1]))
      print '%d - %d '%(prev,now),
      if prev-now==1:
        cnt1to0+=1
      prev=now
    if cnt1to0==1:
      print ' v',
    if (p[3]*p[2]*p[1]==0 and p[4]*p[3]*p[2]==0 and 2<=cnt<=6 and cnt1to0==1):
      return True
    else:
      return False

  for i in range(img.height-2):
    for j in range(img.width-2):
      p=getpixels(j+1,i+1,img)
      if p[0]:
        if A(j+1,i+1):
          tmp.putpixel((j+1,i+1),0)

  for i in range(img.height-2):
    for j in range(img.width-2):
      p=getpixels(j+1,i+1,img)
      if p[0]:
        if B(j+1,i+1):
          tmp.putpixel((j+1,i+1),0)

  tmp.show()
im3=Image.new('1',(9,8),0)
seq=[0,0,0,0,0,0,0,0,0,
     0,1,1,1,1,1,1,0,0,
     0,1,1,1,1,1,1,0,0,
     0,1,1,1,1,1,1,1,0,
     0,1,0,0,1,1,1,1,0,
     0,1,0,0,0,1,1,1,0,
     0,1,0,0,0,0,0,1,0,
     0,0,0,0,0,0,0,0,0
     ]

for i in range(len(seq)):
  im3.putpixel((i%9,i/9),seq[i])
im3.show()
zthin(im3)
'''


