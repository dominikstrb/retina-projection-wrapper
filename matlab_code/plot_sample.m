function plot_sample(windowed_img, planar_sample_frame, spherical_sample, spherical_abrr_sample)
%PLOT_SAMPLE Summary of this function goes here
%   Detailed explanation goes here
    fprintf('Plotting\n');
    figure()
    subplot(2,2,1)
    imagesc(windowed_img);
    axis('square')
    title('Planar Windowed Image')
    subplot(2,2,2);
    imagesc(planar_sample_frame)
    axis('square')
    title('Planar Sample (with Frame)')
    subplot(2,2,3)
    imagesc(spherical_sample);
    axis('square')
    title('Spherical Sample')
    subplot(2,2,4);
    imagesc(spherical_abrr_sample);
    axis('square')
    title('Naturalistic Sample')
    colormap gray

end

