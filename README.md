Replication Instructions:

# Vesuvius Scroll Challenge - Ink Detection

https://github.com/lucyellu/inkception-3d

This repository contains training and inference code based on an I3D architecture to detect ink from image stacks.

The easiest way is to clone the repo and open the jupyter notebooks in a colab environment. Then simply run the cells of interest. 

```
git clone https://github.com/lucyellu/inkception-3d.git


```

Otherwise- to install and run locally:

### Set up a python environment. Tested with python 3.10

```
conda create --name python310 python=3.10
conda activate python310
git clone https://github.com/lucyellu/inkception-3d.git
cd inkception-3d
pip install -r requirements.txt


```
note the following packages need to be installed

```
pytorch-lightning   
typed-argument-parser   
segmentation_models_pytorch   
albumentations   
warmup_scheduler   
```

#if you run into cudaa or other compatibility issues, try installing with no version requirements

```
pip install -r requirements_noversions.txt


```

## Download Data
Download the segments that you want to inference or train with. ([paths](http://dl.ash2txt.org/full-scrolls/Scroll1.volpkg/paths/)).   

Submission segments include: 
    20230702185753 
    20231012184423 
    20231005123336 
    20231106155351
    20231022170901
    
Place the downloaded segment folders in the inkception-3d folder:
    Place inference segments in /eval_segments
    Place training segments in /training_segments
    
Make sure each {segmentid}_mask.png and {segmentid}_inklabel.png (if training) file is in its appropriate segment folder.

### Inference
Place the segment data you want to inference into ./eval_segments or adjust accordingly.
The inference_stride32 script runs a checkpoint model based on inception-3d. It saves progress images in a folder designated in outputs path at 2% intervals. Adjust as needed. 

Arguments found within the InferenceArgumentParser class.

Download Youseff's checkpoint [here](https://drive.google.com/file/d/1fAGZbVPHW6q1hNiI2E2NKzf6TyELzOC4/view?usp=sharing) 

```
python inference_stride32.py --segment_id 20230702185753 --model_path '/content/drive/MyDrive/inkception-3d/models/valid_20230827161847_0_fr_i3depoch=7.ckpt'
```

###
Some example outputs found at [Segment Browser](https://vesuvius.virtual-void.net/) 

### Training

Adjust the CFG class in 64x64_256stride_i3d.py
These are the parameters you can adjust per inference or training run. 

I found the default backbone setting to be different for the inference (efficientnet0) and training files (set to resnet) so make sure you select the one you want. 

```
python 64x64_256stride_i3d.py
