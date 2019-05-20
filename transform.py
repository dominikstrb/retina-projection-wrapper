import numpy as np
import matlab.engine

eng = matlab.engine.start_matlab()

eng.addpath("matlab_code")
eng.addpath("matlab_code/functionsAux/")


def transform_sample(
        windowed_img, r, epsilon, chi, fov, img_size, interpolation_method="bicubic"
):
    """ Transform a sample on the image plane to a sample on the retina's tangential plane
    at a given eccentricity and polar angle

    This function simply passes the input arguments to the matlab function transform_sample.m
    from the code provided by Pamplona et al. 2013

    Args:
        windowed_img: input sample (np.array)
        r: radius of the eyeball (float)
        epsilon: eccentricity in degrees (float)
        chi: polar angle in degrees (float)
        fov: total field of view (float)
        img_size: total size of the image (2-element list of int)
        interpolation_method: interpolation for the transformations (default "bicubic")

    Returns:
        planar_sample_frame, spherical_sample, spherical_abrr_sample
        - sample on the image plane with a frame around it
        - sample on the tangential plane at (epsilon, chi)
        - sample on the tangential plane, blurred
    """
    result = eng.transform_sample(
        matlab.double(windowed_img),
        r,
        epsilon,
        chi,
        fov,
        matlab.double(img_size),
        interpolation_method,
        nargout=3,
    )
    return (np.array(x) for x in result)


if __name__ == "__main__":
    # do the projection for a test sample
    import imageio
    from plot_sample import plot_sample

    img = imageio.imread("spherical/IMG200.png", as_gray=True)

    epsilon = 50.0
    chi = 45.0
    r = 8.3350

    fov = 120.0
    img_size = [5954.0, 5954.0]

    planar_sample_frame, spherical_sample, spherical_abrr_sample = transform_sample(
        img, r, epsilon, chi, fov, img_size
    )

    plot_sample(img, planar_sample_frame, spherical_sample, spherical_abrr_sample)