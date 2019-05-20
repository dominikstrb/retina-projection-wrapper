import matplotlib.pyplot as plt


def plot_sample(
        windowed_img, planar_sample_frame, spherical_sample, spherical_abrr_sample
):
    """
    Plot the original sample, the actually relevant area of the sample,
    the sample projected onto the sphere and the blurred spherical sample

    Args:
        windowed_img: original (input) sample, planar
        planar_sample_frame: planar sample, relevant region with frame
        spherical_sample: spherical sample
        spherical_abrr_sample: spherical sample with blurring

    Returns:
        f, axes: pyplot figure and axes objects
    """
    f, axes = plt.subplots(2, 2)
    axes[0, 0].imshow(windowed_img, cmap="gray")
    axes[0, 0].set_title("Planar Windowed Image")

    axes[0, 1].imshow(planar_sample_frame, cmap="gray")
    axes[0, 1].set_title("Planar Sample (with Frame)")

    axes[1, 0].imshow(spherical_sample, cmap="gray")
    axes[1, 0].set_title("Spherical Sample")

    axes[1, 1].imshow(spherical_abrr_sample, cmap="gray")
    axes[1, 1].set_title("Naturalistic Sample")

    return f, axes
