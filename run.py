import os
import sys
from datetime import datetime

from PIL import Image

from libs.arbitrary_image_stylization.arbitrary_image_stylization_with_weights import console_entry_point
from libs.markov_img_gen.imggen import MarkovChain

if __name__ == "__main__":
    chain = MarkovChain(bucket_size=1)
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
    print("Generating markovified style...")
    style_img_markov = chain.generate(width=64, height=64)
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    style_img_markov.save(os.path.join(THIS_FOLDER, style_img_markov_path))

    print("Combining styles...")
    console_entry_point([
        "arbitrary_image_stylization_with_weights",
        "--checkpoint",
        "pre-trained_models/arbitrary_style_transfer/model.ckpt",
        "--output_dir",
        "images/tmp/",
        "--style_images_paths",
        style_img_markov_path,
        "--content_images_paths",
        content_img_path,
        "--interpolation_weights",
        "[0.35]",
        "--logtostderr",
    ])
    console_entry_point([
        "arbitrary_image_stylization_with_weights",
        "--checkpoint",
        "pre-trained_models/arbitrary_style_transfer/model.ckpt",
        "--output_dir",
        "images/artifacts/",
        "--style_images_paths",
        style_img_path,
        "--content_images_paths",
        tmp_img_path,
        "--logtostderr",
    ])
