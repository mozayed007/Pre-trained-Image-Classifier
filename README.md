
# Dog Breeds Images Classifier

This is a pre-trained dog breed image classifier. It uses different architectures like Resnet, Alexnet, and VGG for classification.

## Prerequisites

Make sure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

## Requirements

This project requires the following Python libraries:

- ast
- PIL (Python Imaging Library)
- torchvision
- torch

You can install these libraries using pip:

```bash
pip install ast
pip install pillow
pip install torchvision
pip install torch
```

## Usage

You can use the classifier with the following commands:

For Resnet architecture:

```bash
python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > resnet_pet-images.txt
```

For Alexnet architecture:

```bash
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt
```

For VGG architecture:

```bash
python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt > vgg_pet-images.txt
```

## Parameters

- `--dir`: Directory of the pet images.
- `--arch`: The architecture to be used for the classifier. It can be `resnet`, `alexnet`, or `vgg`.
- `--dogfile`: The file containing the names of the dog breeds.

The output of the classifier will be saved in a text file.

---

If you need more specific information or have any other requirements, please let me know.
