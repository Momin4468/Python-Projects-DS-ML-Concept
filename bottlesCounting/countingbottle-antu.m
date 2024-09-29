
%load image
image = imread("bottle_crate_10.png");
imshow(image)

% Determine Radius Range for Searching Circles
draw = drawline;
pos = draw.Position;
diffPos = diff(pos);
diameter = hypot(diffPos(1),diffPos(2))


%Initial Attempt to Find Circles
gray_image = im2gray(image);
imshow(gray_image)

%Increase Detection Sensitivity
[centersBright,radiiBright,metricBright] = imfindcircles(image,[20 30], ...
    "ObjectPolarity","bright","Sensitivity",0.92,"EdgeThreshold",0.1);


imshow(image)
h = viscircles(centersBright, radiiBright);

% length printing
text(100,20,strcat('Objects Found: ',num2str(length(centersBright))),'Color','green','FontSize',20)
