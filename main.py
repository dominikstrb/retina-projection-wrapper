from transform import transform_sample
from plot_sample import plot_sample
import imageio
import os


def transform_samples(input_dir="screenshots", output_dir="output"):
    directories = next(os.walk(input_dir))[1]
    for dir in directories:
        ecc, polar = [
            float("".join(x for x in name if x.isdigit())) for name in dir.split("_")
        ]
        filenames = next(os.walk(os.path.join(input_dir, dir)))[2]
        for filename in filenames:
            filepath = os.path.join(input_dir, dir, filename)

            print("Loading {} at ecc = {}, polar = {}".format(filename, ecc, polar))
            img = imageio.imread(filepath, as_gray=True)

            r = 8.3350

            fov = 120.0
            img_size = [5954.0, 5954.0]

            planar_sample_frame, spherical_sample, spherical_abrr_sample = transform_sample(
                windowed_img=img,
                r=r,
                epsilon=ecc,
                chi=polar,
                fov=fov,
                img_size=img_size,
            )

            output_path = os.path.join(output_dir, dir, filename)
            if not os.path.exists(os.path.join(output_dir, dir)):
                os.makedirs(os.path.join(output_dir, dir))
            imageio.imwrite(output_path, spherical_abrr_sample)

            """
            plot_sample(
                img, planar_sample_frame, spherical_sample, spherical_abrr_sample
            )
            """


if __name__ == "__main__":
    transform_samples(input_dir="screenshots", output_dir="output")
