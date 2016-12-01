#encoding utf-8
from PIL import Image
im=Image.open('lena.bmp')	
height,width=im.height,im.width

im2=Image.new('1',(66,66),0)
for i in range(64):
  for j in range(64):
    im2.putpixel((1+j,1+i),1 if im.getpixel((j*8,i*8))>=128 else 0)
#im2.show()
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
  def getpixels(j,i):
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
  l=[[0 for i in range(64)]for i in range(64)]
  for i in range(64):
    for j in range(64):
      p=getpixels(j+1,i+1)
      if p[0]:
        l[i][j]=f(h(p[0],p[1],p[6],p[2]),h(p[0],p[2],p[7],p[3]),h(p[0],p[3],p[8],p[4]),h(p[0],p[4],p[5],p[1]))
      else :
        l[i][j]=-1
#p=getpixels(10,1)
  #print p
  #print h(p[0],p[1],p[6],p[2]),h(p[0],p[2],p[7],p[3]),h(p[0],p[3],p[8],p[4]),h(p[0],p[4],p[5],p[1])
  #print f(h(p[0],p[1],p[6],p[2]),h(p[0],p[2],p[7],p[3]),h(p[0],p[3],p[8],p[4]),h(p[0],p[4],p[5],p[1]))
  return l
#for i in range(66):
#  for j in range(66):
#    print im2.getpixel((j,i)),
#  print

res=yokoi(im2)
with open('connectivity.txt','w+') as f:
  for item in res:
    for items in item:
      if items==-1:
        f.write(' ')
      else:
        f.write(str(items))
    f.write('\n')




