
%load image
image = imread("C:\Users\z2m09\Desktop\files\ruhi apu\bottles\inputs\bottle_crate_22.png");
imshow(image)

% Determine Radius Range for Searching Circles
draw = drawline;
position = draw.Position;
diffPos = diff(position);
diameter = hypot(diffPos(1),diffPos(2))

%Initial Attempt to Find Circles
gray_image = im2gray(image);
imshow(gray_image)

%Increase Detection Sensitivity
[centers,radii] = imfindcircles(image,[10 25], "ObjectPolarity","dark","Sensitivity",0.85)
imshow(image)
darkCircles = viscircles(centers,radii);

%Detecting the Missing circles, which is white (Bright)
[centersBright,radiiBright] = imfindcircles(image,[10 25],"ObjectPolarity","bright","Sensitivity",0.8);
imshow(image)
brightCircles = viscircles(centersBright, radiiBright,"Color","b");


%Detecting All Circles
AllCircles = viscircles(centers,radii);



% length printing
text(100,20,strcat('Objects Found: ',num2str(length(centersBright))),'Color','green','FontSize',20)


