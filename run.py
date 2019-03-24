import os
import sys
from datetime import datetime

from PIL import Image

from magenta.models.arbitrary_image_stylization.arbitrary_image_stylization_with_weights import console_entry_point
from markov import MarkovChain

if __name__ == "__main__":
    chain = MarkovChain(bucket_size=16, four_neighbour=True)
    content_img_path = sys.argv[1]
    style_img_path = sys.argv[2]
    content_img_name = os.path.splitext(os.path.basename(content_img_path))[0]
    style_img_name = os.path.splitext(os.path.basename(style_img_path))[0]
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    style_img_markov_path = "images/tmp/{}.png".format(timestamp)
    tmp_img_path = "images/tmp/{}_{}.jpg".format(content_img_name, timestamp)

    style_img = Image.open(style_img_path)
    print("Training Markov model...")
    chain.train(style_img)
    print("Generating Markov style...")
    style_img_markov = chain.generate()
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    style_img_markov.save(os.path.join(THIS_FOLDER, style_img_markov_path))

    print("Combining styles...")
    console_entry_point([
        "arbitrary_image_stylization_with_weights",
        "--checkpoint",
        "magenta/models/arbitrary_image_stylization/model/model.ckpt",
        "--output_dir",
        "images/tmp/",
        "--style_images_paths",
        style_img_markov_path,
        "--content_images_paths",
        content_img_path,
        "--interpolation_weights",
        "[0.5]",
        "--logtostderr",
    ])
    console_entry_point([
        "arbitrary_image_stylization_with_weights",
        "--checkpoint",
        "magenta/models/arbitrary_image_stylization/model/model.ckpt",
        "--output_dir",
        "images/artifacts/",
        "--style_images_paths",
        style_img_path,
        "--content_images_paths",
        tmp_img_path,
        "--logtostderr",
    ])
