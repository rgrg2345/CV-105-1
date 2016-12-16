clear all
clc
img=imread('lena.bmp');
imshow(img)
imgsize=size(img);
noise=randn(imgsize(1),imgsize(2));


%%gaussian noise
amp1=10;
amp2=30;

gassian10=zeros(imgsize(1),imgsize(2));
gassian30=zeros(imgsize(1),imgsize(2));

gassian10=uint8(plus(double(img),amp1*noise));
gassian30=uint8(plus(double(img),amp2*noise));

imwrite(gassian10,'gassian10.bmp');
imwrite(gassian30,'gassian30.bmp');



%%salt and pepper noise
noise=rand(imgsize(1),imgsize(2));
salt1=zeros(imgsize(1),imgsize(2));
salt2=zeros(imgsize(1),imgsize(2));
f1=0.05;
f2=0.1;

for i=1 :imgsize(1)
   for j =1 :imgsize(2)
       if noise(i,j) <f1/2
           salt1(i,j)=0;
       elseif  noise(i,j) > 1-(f1/2)
           salt1(i,j)=255;  
       else
           salt1(i,j)=img(i,j);   
       end
       if noise(i,j) <f2/2
           salt2(i,j)=0;
       elseif  noise(i,j) > 1-(f2/2)
           salt2(i,j)=255;  
       else
           salt2(i,j)=img(i,j);
       end
   end
end
salt1=uint8(salt1);
salt2=uint8(salt2);

imwrite(salt1,'saltpepper5.bmp');
imwrite(salt2,'saltpepper10.bmp');

%%box filter
box3=ones(3,3);
box5=ones(5,5);

  
g10box3=zeros(imgsize(1),imgsize(2));
g30box3=zeros(imgsize(1),imgsize(2)); 
g10box5=zeros(imgsize(1),imgsize(2));
g30box5=zeros(imgsize(1),imgsize(2)); 
sp5box3=zeros(imgsize(1),imgsize(2));
sp10box3=zeros(imgsize(1),imgsize(2));
sp5box5=zeros(imgsize(1),imgsize(2));
sp10box5=zeros(imgsize(1),imgsize(2));


%%box3x3
for i=1 :imgsize(1)%height 
   for j =1 :imgsize(2)%width
       %g10
       
       weightcnt=0;
       tmp=0;
       %calculate box
       for k=1:3
          for l=1:3% minus 2 is shift centrol to 2,2
              if (i+k-2>=1 & i+k-2<=imgsize(1) & j+l-2>=1& j+l-2<=imgsize(2))
                 weightcnt=weightcnt+box3(k,l);
                 tmp=tmp+uint16(gassian10(i+k-2,j+l-2)*box3(k,l));
              end
          end
       end
       g10box3(i,j)=tmp/weightcnt;
       
       %g30
       weightcnt=0;
       tmp=0;
       %calculate box
       for k=1:3
          for l=1:3% minus 2 is shift centrol to 2,2
              if (i+k-2>=1 & i+k-2<=imgsize(1) & j+l-2>=1& j+l-2<=imgsize(2))
                 weightcnt=weightcnt+box3(k,l);
                 tmp=tmp+uint16(gassian30(i+k-2,j+l-2)*box3(k,l));
              end
          end
       end
       g30box3(i,j)=tmp/weightcnt;

       %salt5
       weightcnt=0;
       tmp=0;
       %calculate box
       for k=1:3
          for l=1:3% minus 2 is shift centrol to 2,2
              if (i+k-2>=1 & i+k-2<=imgsize(1) & j+l-2>=1& j+l-2<=imgsize(2))
                 weightcnt=weightcnt+box3(k,l);
                 tmp=tmp+uint16(salt1(i+k-2,j+l-2)*box3(k,l));
              end
          end
       end
       sp5box3(i,j)=tmp/weightcnt;
       
       
       %salt10
       weightcnt=0;
       tmp=0;
       %calculate box
       for k=1:3
          for l=1:3% minus 2 is shift centrol to 2,2
              if (i+k-2>=1 & i+k-2<=imgsize(1) & j+l-2>=1& j+l-2<=imgsize(2))
                 weightcnt=weightcnt+box3(k,l);
                 tmp=tmp+uint16(salt2(i+k-2,j+l-2)*box3(k,l));
              end
          end
       end
       sp10box3(i,j)=tmp/weightcnt;
   end
end
g10box3=uint8(g10box3);
g30box3=uint8(g30box3);
sp5box3=uint8(sp5box3);
sp10box3=uint8(sp10box3);

imwrite(g10box3,'gassain10Box3.bmp');
imwrite(g30box3,'gassain30Box3.bmp');
imwrite(sp5box3,'saltpepper5Box3.bmp');
imwrite(sp10box3,'saltpepper10Box3.bmp');




%box 5x5
for i=1 :imgsize(1)%height 
   for j =1 :imgsize(2)%width
       %g10
       
       weightcnt=0;
       tmp=0;
       %calculate box
       for k=1:5
          for l=1:5% minus 3 is shift centrol to 3,3
              if (i+k-3>=1 & i+k-3<=imgsize(1) & j+l-3>=1& j+l-3<=imgsize(2))
                 weightcnt=weightcnt+box5(k,l);
                 tmp=tmp+uint16(gassian10(i+k-3,j+l-3)*box5(k,l));
              end
          end
       end
       g10box5(i,j)=tmp/weightcnt;
       
       %g30
       weightcnt=0;
       tmp=0;
       %calculate box
       for k=1:5
          for l=1:5% minus 3 is shift centrol to 3,3
              if (i+k-3>=1 & i+k-3<=imgsize(1) & j+l-3>=1& j+l-3<=imgsize(2))
                 weightcnt=weightcnt+box5(k,l);
                 tmp=tmp+uint16(gassian30(i+k-3,j+l-3)*box5(k,l));
              end
          end
       end
       g30box5(i,j)=tmp/weightcnt;

       %salt5
       weightcnt=0;
       tmp=0;
       %calculate box
       for k=1:5
          for l=1:5% minus 3 is shift centrol to 3,3
              if (i+k-3>=1 & i+k-3<=imgsize(1) & j+l-3>=1& j+l-3<=imgsize(2))
                 weightcnt=weightcnt+box5(k,l);
                 tmp=tmp+uint16(salt1(i+k-3,j+l-3)*box5(k,l));
              end
          end
       end
       sp5box5(i,j)=tmp/weightcnt;
       
       
       %salt10
       weightcnt=0;
       tmp=0;
       %calculate box
       for k=1:5
          for l=1:5% minus 3 is shift centrol to 3,3
              if (i+k-3>=1 & i+k-3<=imgsize(1) & j+l-3>=1& j+l-3<=imgsize(2))
                 weightcnt=weightcnt+box5(k,l);
                 tmp=tmp+uint16(salt2(i+k-3,j+l-3)*box5(k,l));
              end
          end
       end
       sp10box5(i,j)=tmp/weightcnt;
   end
end
g10box5=uint8(g10box5);
g30box5=uint8(g30box5);
sp5box5=uint8(sp5box5);
sp10box5=uint8(sp10box5);

imwrite(g10box5,'gassain10Box5.bmp');
imwrite(g30box5,'gassain30Box5.bmp');
imwrite(sp5box5,'saltpepper5Box5.bmp');
imwrite(sp10box5,'saltpepper10Box5.bmp');


%%median filter


g10m3=zeros(imgsize(1),imgsize(2));
g30m3=zeros(imgsize(1),imgsize(2)); 
g10m5=zeros(imgsize(1),imgsize(2));
g30m5=zeros(imgsize(1),imgsize(2)); 
sp5m3=zeros(imgsize(1),imgsize(2));
sp10m3=zeros(imgsize(1),imgsize(2));
sp5m5=zeros(imgsize(1),imgsize(2));
sp10m5=zeros(imgsize(1),imgsize(2));

%%median filter3x3
for i=1 :imgsize(1)%height 
   for j =1 :imgsize(2)%width
       %g10
       cnt=0;
       tmp=zeros(9,1);
       %calculate box
       for k=1:3
          for l=1:3% minus 2 is shift centrol to 2,2
              if (i+k-2>=1 & i+k-2<=imgsize(1) & j+l-2>=1& j+l-2<=imgsize(2))
                 cnt=cnt+1;
                 tmp(cnt,1)=gassian10(i+k-2,j+l-2)*box3(k,l);
              end
          end
       end
       sortp=sort(tmp);
       g10m3(i,j)=sortp(5);
       
       %g30
       cnt=0;
       tmp=zeros(9,1);
       %calculate box
       for k=1:3
          for l=1:3% minus 2 is shift centrol to 2,2
              if (i+k-2>=1 & i+k-2<=imgsize(1) & j+l-2>=1& j+l-2<=imgsize(2))
                 cnt=cnt+1;
                 tmp(cnt,1)=gassian30(i+k-2,j+l-2)*box3(k,l);
              end
          end
       end
       sortp=sort(tmp);
       g30m3(i,j)=sortp(5);
       
       %salt5
       cnt=0;
       tmp=zeros(9,1);
       %calculate box
       for k=1:3
          for l=1:3% minus 2 is shift centrol to 2,2
              if (i+k-2>=1 & i+k-2<=imgsize(1) & j+l-2>=1& j+l-2<=imgsize(2))
                 cnt=cnt+1;
                 tmp(cnt,1)=salt1(i+k-2,j+l-2)*box3(k,l);
              end
          end
       end
       sortp=sort(tmp);
       sp5m3(i,j)=sortp(5);
       
       %salt10
       cnt=0;
       tmp=zeros(9,1);
       %calculate box
       for k=1:3
          for l=1:3% minus 2 is shift centrol to 2,2
              if (i+k-2>=1 & i+k-2<=imgsize(1) & j+l-2>=1& j+l-2<=imgsize(2))
                 cnt=cnt+1;
                 tmp(cnt,1)=salt2(i+k-2,j+l-2)*box3(k,l);
              end
          end
       end
       sortp=sort(tmp);
       sp10m3(i,j)=sortp(5);
   end
end
g10m3=uint8(g10m3);
g30m3=uint8(g30m3);
sp5m3=uint8(sp5m3);
sp10m3=uint8(sp10m3);

imwrite(g10m3,'gassain10median3.bmp');
imwrite(g30m3,'gassain30median3.bmp');
imwrite(sp5m3,'saltpepper5median3.bmp');
imwrite(sp10m3,'saltpepper10median3.bmp');

%%median filter5x5
for i=1 :imgsize(1)%height 
   for j =1 :imgsize(2)%width
       %g10
       cnt=0;
       tmp=zeros(25,1);
       %calculate box
       for k=1:5
          for l=1:5% minus 3 is shift centrol to 3,3
              if (i+k-3>=1 & i+k-3<=imgsize(1) & j+l-3>=1& j+l-3<=imgsize(2))
                 cnt=cnt+1;
                 tmp(cnt,1)=gassian10(i+k-3,j+l-3)*box5(k,l);
              end
          end
       end
       sortp=sort(tmp);
       g10m5(i,j)=sortp(13);
       
       %g30
       cnt=0;
       tmp=zeros(25,1);
       %calculate box
       for k=1:5
          for l=1:5% minus 3 is shift centrol to 3,3
              if (i+k-3>=1 & i+k-3<=imgsize(1) & j+l-3>=1& j+l-3<=imgsize(2))
                 cnt=cnt+1;
                 tmp(cnt,1)=gassian30(i+k-3,j+l-3)*box5(k,l);
              end
          end
       end
       sortp=sort(tmp);
       g30m5(i,j)=sortp(13);
       
       %salt5
       cnt=0;
       tmp=zeros(25,1);
       %calculate box
       for k=1:5
          for l=1:5% minus 3 is shift centrol to 3,3
              if (i+k-3>=1 & i+k-3<=imgsize(1) & j+l-3>=1& j+l-3<=imgsize(2))
                 cnt=cnt+1;
                 tmp(cnt,1)=salt1(i+k-3,j+l-3)*box5(k,l);
              end
          end
       end
       sortp=sort(tmp);
       sp5m5(i,j)=sortp(13);
       
       %salt10
       cnt=0;
       tmp=zeros(25,1);
       %calculate box
       for k=1:5
          for l=1:5% minus 3 is shift centrol to 3,3
              if (i+k-3>=1 & i+k-3<=imgsize(1) & j+l-3>=1& j+l-3<=imgsize(2))
                 cnt=cnt+1;
                 tmp(cnt,1)=salt2(i+k-3,j+l-3)*box5(k,l);
              end
          end
       end
       sortp=sort(tmp);
       sp10m5(i,j)=sortp(13);
   end
end

g10m5=uint8(g10m5);
g30m5=uint8(g30m5);
sp5m5=uint8(sp5m5);
sp10m5=uint8(sp10m5);

imwrite(g10m5,'gassain10median5.bmp');
imwrite(g30m5,'gassain30median5.bmp');
imwrite(sp5m5,'saltpepper5median5.bmp');
imwrite(sp10m5,'saltpepper10median5.bmp');

g10opcl=imread('gassian10open-close.bmp');
g30opcl=imread('gassian30open-close.bmp');
sp5opcl=imread('saltpepper5open-close.bmp');
sp10opcl=imread('saltpepper10open-close.bmp');
fileID = fopen('SNR.txt','w+');

%calculate snr by using psnr
fprintf(fileID,'SNRs :\n');
fprintf(fileID,'gaussian 10:%f\n',calSNR(img,gassian10));
fprintf(fileID,'gaussian 10 box3:%f\n',calSNR(img,g10box3));
fprintf(fileID,'gaussian 10 box5:%f\n',calSNR(img,g10box5));
fprintf(fileID,'gaussian 10 median3:%f\n',calSNR(img,g10m3));
fprintf(fileID,'gaussian 10 median5:%f\n',calSNR(img,g10m5));
fprintf(fileID,'gaussian 10 open-close:%f\n',calSNR(img,g10opcl));

fprintf(fileID,'gaussian 30:%f\n',calSNR(img,gassian30));
fprintf(fileID,'gaussian 30 box3:%f\n',calSNR(img,g30box3));
fprintf(fileID,'gaussian 30 box5:%f\n',calSNR(img,g30box5));
fprintf(fileID,'gaussian 30 median3:%f\n',calSNR(img,g30m3));
fprintf(fileID,'gaussian 30 median5:%f\n',calSNR(img,g30m5));
fprintf(fileID,'gaussian 30 open-close:%f\n',calSNR(img,g30opcl));

fprintf(fileID,'salt & pepper 5:%f\n',calSNR(img,salt1));
fprintf(fileID,'salt & pepper 5 box3:%f\n',calSNR(img,sp5box3));
fprintf(fileID,'salt & pepper 5 box5:%f\n',calSNR(img,sp5box5));
fprintf(fileID,'salt & pepper 5 median3:%f\n',calSNR(img,sp5m3));
fprintf(fileID,'salt & pepper 5 median5:%f\n',calSNR(img,sp5m5));
fprintf(fileID,'salt & pepper 5 open-close:%f\n',calSNR(img,sp5opcl));

fprintf(fileID,'salt & pepper 10:%f\n',calSNR(img,salt2));
fprintf(fileID,'salt & pepper 10 box3:%f\n',calSNR(img,sp10box3));
fprintf(fileID,'salt & pepper 10 box5:%f\n',calSNR(img,sp10box5));
fprintf(fileID,'salt & pepper 10 median3:%f\n',calSNR(img,sp10m3));
fprintf(fileID,'salt & pepper 10 median5:%f\n',calSNR(img,sp10m5));
fprintf(fileID,'salt & pepper 10 open-close:%f\n',calSNR(img,sp10opcl));

fclose(fileID);

function SNR = calSNR(Img, noiseImg)
    
    [ImgH, ImgW] = size(Img);
    n = ImgH * ImgW;
    
    sum = 0.0;
    sumN = 0.0;
    for i = 1 : ImgH
        for j = 1 : ImgW
            sum = sum + double(Img(i, j));
            sumN = sumN + noiseImg(i, j) - Img(i, j);
        end
    end
    miu = double(sum / n);
    miuN = double(sumN / n);
    
    sum = 0.0;
    sumN = 0.0;
    for i = 1 : ImgH
        for j = 1 : ImgW
            sum = sum + power(double(Img(i, j)) - miu, 2.0);
            sumN = sumN + power(double(noiseImg(i, j)) - double(Img(i, j)) - miuN, 2.0);
        end
    end
    VS = double(sum / n);
    VN = double(sumN / n);
    
    SNR = 20.0 * log10(sqrt(VS) / sqrt(VN));
end