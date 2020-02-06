# Arabic Letters Classification Deep Learning
A model that can recognize the alphabets of Arabic letters using deep learning.

# Model
RESNET18: https://pytorch.org/hub/pytorch_vision_resnet/

Accuracy: 98%

# Dataset
The dataset can be found at:

https://www.kaggle.com/rashwan/arabic-chars-mnist

The dataset isn't organized so we must group the letters into their corresponding folder which will require a lot of copying & pasting.

To solve this problem you can run the `organize_data.py` script which is explained in the section below.

## Organizing the data's script:

__Please note that the files `organize_data.py` and `run_the_script.bat` must be placed in the same folder as the unzipped data.__

__The script expects to see a `train` and a `test` folder in the same directory.__

### using cmd or bash:
run cmd or bash and type the following commands:

` cd '$REPLACE_WITH_YOUR_WORKING_DIRECTORY' `

` python organize_data.py `

### Or Using the bat file:
Copy the `organize_data.py` & `run_the_script.bat` files into your working directory.

Launch the run_the_script.bat file.
