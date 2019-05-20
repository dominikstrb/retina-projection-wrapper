clear all;
close all;
addpath('./functionsAux/');
fprintf('Loading windowed image and initializing parameters...\n');
%%interpolation method used in the t-form
interpolation_method = 'bicubic';

%coordinates of the center of the patch in angles
epsilon = 30;
chi = 180;
r = 8.3350;

fov = 120;%field of view covered by the initial image
img_size = [5954, 5954];%initial image size in pixels

%windowed_img = imread('/data/forest-scenes/2019-04-26_09:35/ecc0_polar0/screen_0.png'); %window planar image
%windowed_img = rgb2gray(windowed_img);
windowed_img = imread('grid.png');
windowed_img = double(windowed_img);

   
[planar_sample_frame, spherical_sample, spherical_abrr_sample] = transform_sample(windowed_img, r, epsilon, chi, fov, img_size, interpolation_method);
plot_sample(windowed_img, planar_sample_frame, spherical_sample, spherical_abrr_sample)

















