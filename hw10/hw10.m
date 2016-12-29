clear all
clc
img=imread('lena.bmp');
[h,w]=size(img);

laplk=[0 1 0;
       1 -4 1;
       0 1 0
];

%% task1
laplacian=zeros(h-2,w-2);
tmp=zeros(h-2,w-2);
for i =1 :w-2
    for j = 1 :h-2
        tmp(i,j)=convolution(img(i:i+2,j:j+2),laplk);
    end    
end
for i =1 :w-2
    for j = 1 :h-2
        if( tmp(i,j)>=15 && zerocross(tmp,i,j,1,15) == 1)
           laplacian(i,j)=0;
        else
            laplacian(i,j)=255;
        end
    end    
end
imwrite(uint8(laplacian),'laplacian.png');

%% task2
mvlaplk=[2 -1 2;
       -1 -4 -1;
        2 -1 2
];
mvlaplacian=zeros(h-2,w-2);
tmp=zeros(h-2,w-2);
for i =1 :w-2
    for j = 1 :h-2
        tmp(i,j)=convolution(img(i:i+2,j:j+2),mvlaplk)/3;
    end    
end
for i =1 :w-2
    for j = 1 :h-2
        if( tmp(i,j)>=20 && zerocross(tmp,i,j,1,20) == 1)
           mvlaplacian(i,j)=0;
        else
            mvlaplacian(i,j)=255;
        end
    end    
end
imwrite(uint8(mvlaplacian),'min_vari_laplacian.png');

%% task3
laogker=[0 0 0 -1 -1 -2 -1 -1 0 0 0 ;
         0 0 -2 -4 -8 -9 -8 -4 -2 0 0;
         0 -2 -7 -15 -22 -23 -22 -15 -7 -2 0;
         -1 -4 -15 -24 -14 -1 -14 -24 -15 -4 -1;
         -1 -8 -22 -14 52 103 52 -14 -22 -8 -1;
         -2, -9, -23, -1, 103, 178, 103, -1, -23, -9, -2;
         -1 -8 -22 -14 52 103 52 -14 -22 -8 -1;
         -1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1;
         0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0;
         0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0;
         0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0
        ];
laplaofgaus=zeros(h-10,w-10);
tmp=zeros(h-10,w-10);
for i =1 :w-10
    for j = 1 :h-10
        tmp(i,j)=convolution(img(i:i+10,j:j+10),laogker);
    end    
end
for i =1 :w-10
    for j = 1 :h-10
        if( tmp(i,j)>=3000 && zerocross(tmp,i,j,1,3000) == 1)
           laplaofgaus(i,j)=0;
        else
            laplaofgaus(i,j)=255;
        end
    end    
end
imwrite(uint8(laplaofgaus),'laplaceofGaus.png');

%% task4
h1 = fspecial('gaussian', [11 11], 3);
h2 = fspecial('gaussian', [11 11], 1);
dofgaus=zeros(h-10,w-10);
dofgaus2=zeros(h-10,w-10);
dofgausimg=zeros(h-10,w-10);
for i =1 :w-10
    for j = 1 :h-10
        val1=convolution(img(i:i+10,j:j+10),h1);
        dofgaus(i,j)=val1;
        val2=convolution(img(i:i+10,j:j+10),h2);
        dofgaus2(i,j)=val2;
        if val1-val2 >=2.5
            dofgausimg(i,j)=0;
        else
            dofgausimg(i,j)=255;
        end
    end    
end
dofgaus=dofgaus-dofgaus2;
imwrite(dofgausimg,'dofGaus.png');
sum(sum(h2))
%% output
fileID = fopen('result.txt','w+');
fprintf(fileID,'Laplacian :\n threshold=%d\n',15);
fprintf(fileID,' kernel=%s\n',m2str(laplk));
fprintf(fileID,'Minimum variance Laplacian :\n threshold=%d\n',20);
fprintf(fileID,' kernel=%s\n',m2str(mvlaplk));
fprintf(fileID,'Laplace of Gaussian :\n threshold=%d\n',3500);
fprintf(fileID,' kernel=%s\n',m2str(laogker));
fprintf(fileID,'Difference of Gaussian :\n threshold=%d\n',2.5);
fprintf(fileID,' kernel1(alpha=3)=%s\n',m2str(h1));
fprintf(fileID,' kernel1(alpha=1)=%s\n',m2str(h2));
%% output function
function str=m2str(mat)
   str=sprintf('[\n');
   [h w]=size(mat);
   for i=1:h
       for j=1:w
           str=sprintf('%s%f ',str,mat(i,j));
       end
       str=sprintf('%s\n',str);
   end
   str=sprintf('%s]',str);
end

function val=convolution(imgmat,kernel)
    [kh,kw]=size(kernel);
    val=double(0);
    for i =1:kh
        for j =1 :kw
           val=val+double(imgmat(i,j))*kernel(kh-i+1,kw-j+1);
        end
    end
end
%% type 0 :find negative, 1:find positive
function cross=zerocross(img,i,j,type,t)
    [h,w]=size(img);
    dx=[-1 0 1 -1  1 -1 0 1];
    dy=[-1 -1 -1 0 0 1 1 1];
    cross=0;
    for k =1 :8
        if( i+dy(k)>0 && i+dy(k)<=w && j+dx(k)>0 && j+dx(k)<=h )
           if type==0
               if img(i+dy(k),j+dx(k)) >=t
                   cross=1;
               end
           else
               if img(i+dy(k),j+dx(k)) <=-t
                   cross=1;
               end
           end
        end
    end
end

