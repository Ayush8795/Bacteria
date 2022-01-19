This is repository with the code used to generate synthetic microbiological dataset in the paper "Generation of microbial colonies dataset with deep learning style transfer" [1].
During neneration we use images from AGAR [2] -- a recently introduced large microbiological dataset.

Prerequisites:

- before synthesis one has to downoad the input data. We used 100 images from the higher-resolution AGAR subset; it can be downloaded here together with the images containing empty dishes (on which colonies will be placed) + images that carries style (used to style transfer).
- set up environment (we recommend conda, and python 3.7) -> requirements.txt

Usage:

- to extact microbial colonies from the input images of Petri dish:
python get_patches.py -i ./input_data -o ./colonies
-i  : directory containing input images
-o  : ditectory to store extracted colonies

- to generate synthetic patches -- fragments of dish with placed (previously extracted) colonies and applied style transfer:
python grow_colonies.py -c ./colonies -e ./empty_dishes -s ./style_dishes -o ./generated
-c  : directory containing colonies that will be used during generation
-e  : directory containing images of empty dishes used during generation
-s  : directory containing images carrying style to be transferred during the stylization stage
-o  : ditectory to store generated patches

Notes:

- labels for the each generated patch are stored in *.json file in COCO format
- instance segmentation masks are stored in .npy files
- it is important to use scikit-image in version 0.17.2
- style transfer part is based on the repository provided in [3]
- if you find this repository useful, please cite us :)

Literature:

[1] Pawłowski, J., Majchrowska, S., & Golan, T. Generation of microbial colonies dataset with deep learning style transfer. arXiv preprint arXiv:2111.03789 (2021).
[2] Majchrowska, S. et al. AGAR a microbial colony dataset for deep learning detection. arXiv preprint arXiv:2108.01234 (2021).
[3] Li, M., Ye, C. & Li, W. High-resolution network for photorealistic style transfer. arXiv preprint arXiv:1904.11617 (2019).
