clear all
BW = imread('lena_down_bin.bmp');

imshow(BW);
BW2 = bwmorph(BW,'thin',Inf);
figure
imshow(BW2)