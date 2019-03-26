import os
import sys
import tarfile
from datetime import datetime
from urllib.request import urlretrieve

from PIL import Image

from libs.arbitrary_image_stylization.arbitrary_image_stylization_with_weights import console_entry_point
from libs.markov_img_gen.imggen import MarkovChain

MODEL_URL = "https://storage.googleapis.com/download.magenta.tensorflow.org/models/arbitrary_style_transfer.tar.gz"
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    model_url_basename = os.path.basename(MODEL_URL)
    model_folder = os.path.join(THIS_FOLDER, "pre-trained_models/arbitrary_style_transfer")
    model_download_folder = os.path.dirname(model_folder)
    model_download_path = os.path.join(model_download_folder, model_url_basename)
    if not os.path.isdir(model_folder):
        print("Downloading pre-trained model...")
        urlretrieve(MODEL_URL, model_download_path)
        print("Extracting pre-trained model...")
        tar = tarfile.open(model_download_path, "r:gz")
        tar.extractall(path=model_download_folder)
        tar.close()
        os.remove(model_download_path)

    chain = MarkovChain(bucket_size=1)
    content_img_path = os.path.join(THIS_FOLDER, sys.argv[1])
    style_img_path = os.path.join(THIS_FOLDER, sys.argv[2])
    content_img_name = os.path.splitext(os.path.basename(content_img_path))[0]
    style_img_name = os.path.splitext(os.path.basename(style_img_path))[0]
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    style_img_markov_path = os.path.join(THIS_FOLDER, "images/tmp/{}.png".format(timestamp))
    tmp_img_path = os.path.join(THIS_FOLDER, "images/tmp/{}_{}.jpg".format(content_img_name, timestamp))

    style_img = Image.open(style_img_path)
    print("Training Markov model...")
    chain.train(style_img)
    print("Generating markovified style...")
    style_img_markov = chain.generate(width=64, height=64)
    style_img_markov.save(style_img_markov_path)

    print("Combining styles...")
    console_entry_point([
        "arbitrary_image_stylization_with_weights",
        "--checkpoint",
        os.path.join(model_folder, "model.ckpt"),
        "--output_dir",
        os.path.join(THIS_FOLDER, "images/tmp/"),
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
        os.path.join(model_folder, "model.ckpt"),
        "--output_dir",
        os.path.join(THIS_FOLDER, "images/artifacts/"),
        "--style_images_paths",
        style_img_path,
        "--content_images_paths",
        tmp_img_path,
        "--logtostderr",
    ])
