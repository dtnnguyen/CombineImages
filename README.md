# CombineImages
CombineImages.py takes in two inputs: "input_image" and "drop_in_image". combineImages() will blur "input_image" and 
sharpen the "drop_in_image", which is then pasted onto "input_image".

## Set up
Download PyCharm here: https://www.jetbrains.com/pycharm/
Start pycharm, create a new project, insert combineimages.py to project.

In terminal on the bottom panel of PyCharm, install these packages:
  - Upgrade to pip3:                               pip install --upgrade pip   
  - Install PILLOW for image processing library:   pip3 install Pillow   
  - To parse, read and write ole file:             pip3 install olefile    
  
## References
Scikit-image can also be used to manipulate images: https://scikit-image.org/download.html

ole file:                                           https://pypi.org/project/olefile/

## Finished Image
![Finished Image](https://github.com/dtnnguyen/CombineImages/blob/master/combineImages.gif)
