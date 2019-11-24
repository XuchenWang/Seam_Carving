# Xuchen Wang - CIS 581 Project 2

This project shrinks the images' size without affecting the main objects in the image. The result will be in a gif animation. 

## Getting Started

The folder contains pictures and scripts: 

"1_result.gif" the image carving results from the source image, "1_try.jpg". "2_result.gif" is the carving result from the source image, "2_try.jpg". The 'infile' and the 'outfile' are the first and the last images in the animation, respectively.

For scripts, imageCarving.py is the main file that puts everything together. carv.py does the dynamic programming and find the optimal seam to cut. genEngMap.py is the python file provided by the TA that calculates the energy map. cumMinEngHor.py and cumMinEngVer.py find all the possible seam horizontally or vertically and rmHorSeam.py and rmVerSeam.py remove the seam from the image.

## Running the tests

Go to imageCarving.py. Change variables 'nr' and 'nc' to the number of seams you would like to remove. Change the image path to the image you would like to modify. 

Run imageCarving.py and check your folder for the gif, 'eval_morphimg.gif'.

## Acknowledgments

* Collaberated with Yuezhan Tao for this project.

