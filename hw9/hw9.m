clear all
clc
img=imread('lena.bmp');
imgsize=size(img);

%robert 
k1=[-1 0;0 1];
k2=[0 -1;1 0];
img =double(img);
%%
r1=zeros(imgsize(1)-1,imgsize(2)-1);
r2=zeros(imgsize(1)-1,imgsize(2)-1);
rob=zeros(imgsize(1)-1,imgsize(2)-1);
for i=1 :imgsize(1)-2
   for j =1 :imgsize(2)-1
       r1(i,j)=sum(sum(k1.*img(i:i+1,j:j+1)));
       r2(i,j)=sum(sum(k2.*img(i:i+1,j:j+1)));
       if sqrt(r1(i,j)^2+r2(i,j)^2) >=18
          rob(i,j)=0;
       else
          rob(i,j)=255;
       end
   end
end
imwrite(rob,'robert[thr=12].png');


%Prewitt
p1=[-1 -1 -1;
     0  0  0;
     1  1  1];
p2=[-1 0 1;
    -1 0 1;
    -1 0 1];
r1=zeros(imgsize(1)-1,imgsize(2)-1);
r2=zeros(imgsize(1)-1,imgsize(2)-1);
prewitt=zeros(imgsize(1)-1,imgsize(2)-1);
for i=1 :imgsize(1)-2
   for j =1 :imgsize(2)-2
       r1(i,j)=sum(sum(p1.*img(i:i+2,j:j+2)));
       r2(i,j)=sum(sum(p2.*img(i:i+2,j:j+2)));
       if sqrt(r1(i,j)^2+r2(i,j)^2) >=40
          prewitt(i,j)=0;
       else
          prewitt(i,j)=255;
       end
   end
end

imwrite(prewitt,'prewitt[thr=24].png');

%%
%Sobel 
s1=[-1 -2 -1;0 0 0;1 2 1];
s2=[-1 0 1;-2 0 2;-1 0 1];
r1=zeros(imgsize(1)-1,imgsize(2)-1);
r2=zeros(imgsize(1)-1,imgsize(2)-1);
sobel=zeros(imgsize(1)-1,imgsize(2)-1);
for i=1 :imgsize(1)-2
   for j =1 :imgsize(2)-2
       r1(i,j)=sum(sum(s1.*img(i:i+2,j:j+2)));
       r2(i,j)=sum(sum(s2.*img(i:i+2,j:j+2)));
       if sqrt(r1(i,j)^2+r2(i,j)^2) >=51
          sobel(i,j)=0;
       else
          sobel(i,j)=255;
       end
   end
end
imwrite(sobel,'sobel[thr=38].png');

%%
%Frei 
k1=[-1 -sqrt(2) -1;0 0 0;1 sqrt(2) 1];
k2=[-1 0 1;-sqrt(2) 0 sqrt(2);-1 0 1];
r1=zeros(imgsize(1)-1,imgsize(2)-1);
r2=zeros(imgsize(1)-1,imgsize(2)-1);
frei=zeros(imgsize(1)-1,imgsize(2)-1);
for i=1 :imgsize(1)-2
   for j =1 :imgsize(2)-2
       r1(i,j)=sum(sum(k1.*img(i:i+2,j:j+2)));
       r2(i,j)=sum(sum(k2.*img(i:i+2,j:j+2)));
       if sqrt(r1(i,j)^2+r2(i,j)^2) >=49
          frei(i,j)=0;
       else
          frei(i,j)=255;
       end
   end
end
imwrite(frei,'Frei[thr=30].png');
%%
%Kirsch
k1=[-3 -3 5;-3 0 5;-3 -3 5];
k2=[-3 5 5;-3 0 5;-3 -3 -3];
k3=[5 5 5;-3 0 -3;-3 -3 -3];
k4=[5 5 -3;5 0 -3;-3 -3 -3];
k5=[5 -3 -3;5 0 -3;5 -3 -3];
k6=[-3 -3 -3;5 0 -3;5 5 -3];
k7=[-3 -3 -3;-3 0 -3;5 5 5];
k8=[-3 -3 -3;-3 0 5;-3 5 5];
kirsch=zeros(imgsize(1)-1,imgsize(2)-1);
for i=1 :imgsize(1)-2
   for j =1 :imgsize(2)-2
       a=zeros(8,1);
       a(1,1)=sum(sum(k1.*img(i:i+2,j:j+2)));
       a(2,1)=sum(sum(k2.*img(i:i+2,j:j+2)));
       a(3,1)=sum(sum(k3.*img(i:i+2,j:j+2)));
       a(4,1)=sum(sum(k4.*img(i:i+2,j:j+2)));
       a(5,1)=sum(sum(k5.*img(i:i+2,j:j+2)));
       a(6,1)=sum(sum(k6.*img(i:i+2,j:j+2)));
       a(7,1)=sum(sum(k7.*img(i:i+2,j:j+2)));
       a(8,1)=sum(sum(k8.*img(i:i+2,j:j+2)));      
       if max(a(:)) >=155
          kirsch(i,j)=0;
       else
          kirsch(i,j)=255;
       end
   end
end
imwrite(kirsch,'Kirsch[thr=135].png');
%%
%Robinson
r0 = [-1 0 1; -2 0 2; -1 0 1];
r1 = [0 1 2; -1 0 1; -2 -1 0];
r2 = [1 2 1; 0 0 0; -1 -2 -1];
r3 = [2 1 0; 1 0 -1; 0 -1 -2];
r4 = [1 0 -1; 2 0 -2; 1 0 -1];
r5 = [0 -1 -2; 1 0 -1; 2 1 0];
r6 = [-1 -2 -1; 0 0 0; 1 2 1];
r7 = [-2 -1 0; -1 0 1; 0 1 2];

robinson=zeros(imgsize(1)-1,imgsize(2)-1);
for i=1 :imgsize(1)-2
   for j =1 :imgsize(2)-2
       a=zeros(8,1);
       a(1,1)=sum(sum(r1.*img(i:i+2,j:j+2)));
       a(2,1)=sum(sum(r2.*img(i:i+2,j:j+2)));
       a(3,1)=sum(sum(r3.*img(i:i+2,j:j+2)));
       a(4,1)=sum(sum(r4.*img(i:i+2,j:j+2)));
       a(5,1)=sum(sum(r5.*img(i:i+2,j:j+2)));
       a(6,1)=sum(sum(r6.*img(i:i+2,j:j+2)));
       a(7,1)=sum(sum(r7.*img(i:i+2,j:j+2)));
       a(8,1)=sum(sum(r0.*img(i:i+2,j:j+2)));      
       if max(a(:)) >=43
          robinson(i,j)=0;
       else
          robinson(i,j)=255;
       end
   end
end
imwrite(robinson,'Robinson[thr=43].png');
%%
%Nevatia
nb0 =   [100 100 100 100 100;
    100 100 100 100 100;
    0 0 0 0 0;
    -100 -100 -100 -100 -100;
    -100 -100 -100 -100 -100];
nb30 =  [100 100 100 100 100; 100 100 100 78 -32; 100 92 0 -92 -100; 32 -78 -100 -100 -100; -100 -100 -100 -100 -100];
nb60 =  [100 100 100 32 -100; 100 100 92 -78 -100; 100 100 0 -100 -100; 100 78 -92 -100 -100; 100 -32 -100 -100 -100];
nb_90 = [-100 -100 0 100 100; -100 -100 0 100 100; -100 -100 0 100 100; -100 -100 0 100 100; -100 -100 0 100 100];
nb_60 = [-100 32 100 100 100; -100 -78 92 100 100; -100 -100 0 100 100; -100 -100 -92 78 100; -100 -100 -100 -32 100];
nb_30 = [100 100 100 100 100; -32 78 100 100 100; -100 -92 0 92 100; -100 -100 -100 -78 32; -100 -100 -100 -100 -100];
nb=zeros(imgsize(1)-1,imgsize(2)-1);
for i=1 :imgsize(1)-4
   for j =1 :imgsize(2)-4
       a=zeros(6,1);
       a(1,1)=sum(sum(nb0.*img(i:i+4,j:j+4)));
       a(2,1)=sum(sum(nb30.*img(i:i+4,j:j+4)));
       a(3,1)=sum(sum(nb60.*img(i:i+4,j:j+4)));
       a(4,1)=sum(sum(nb_90.*img(i:i+4,j:j+4)));
       a(5,1)=sum(sum(nb_60.*img(i:i+4,j:j+4)));
       a(6,1)=sum(sum(nb_30.*img(i:i+4,j:j+4)));  
       if max(a(:)) >=12500
          nb(i,j)=0;
       else
          nb(i,j)=255;
       end
   end
end
imwrite(nb,'NevatiaAndBabu[thr=12500].png');