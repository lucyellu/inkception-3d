# inkception-3d: ink detection in carbonized Herculaneum scrolls

Code from about a year on the [Vesuvius Challenge](https://scrollprize.org/): detecting ink in 3D
X-ray scans of papyrus scrolls carbonized by Vesuvius in 79 AD.

**What I found:** reversing the order of the scan layers changes what the model sees (credit to
Johannes Rudolph's [segment browser](https://vesuvius.virtual-void.net/) for pointing this out).
Stacking the reversed and normal predictions with targeted masking suppressed distracting
artifacts, both from segmentation and from non-ink texture in the papyrus.

**Built on:** the 2023 Grand Prize-winning I3D model (Youssef Nader, Luke Farritor and Julian Schilliger)
([GP colab](https://colab.research.google.com/drive/11gF1YEAAknr_bTvBKp8eX7GSSjs9WQgN?usp=sharing)),
with modifications to the inference-specific layers.

![Scroll 1 segments near the end of the scroll](images/scroll1_title.jpg)
*Scroll 1 segments near the end of the scroll.*

## Replicate

The easiest way to replicate is to clone the repo and open the jupyter notebooks in a colab environment. 
Then simply run the cells of interest. 

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
pip install -r install/requirements.txt


```
note the following packages need to be installed

```
pytorch-lightning   
typed-argument-parser   
segmentation_models_pytorch   
albumentations   
warmup_scheduler   
```

If you run into CUDA or other compatibility issues, try installing with no version requirements

```
pip install -r install/requirements_noversions.txt


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
The `inference_v32_suffix.py` script runs a checkpoint model based on inception-3d. It saves progress images in a folder designated in outputs path at 2% intervals. Adjust as needed. 

Arguments found within the InferenceArgumentParser class.

Download Youseff's checkpoint [here](https://drive.google.com/file/d/1fAGZbVPHW6q1hNiI2E2NKzf6TyELzOC4/view?usp=sharing) 

```
python inference_v32_suffix.py --segment_id 20230702185753 --model_path '/content/drive/MyDrive/inkception-3d/models/valid_20230827161847_0_fr_i3depoch=7.ckpt'
```

### Example outputs
Some example outputs found at [Segment Browser](https://vesuvius.virtual-void.net/) 

### Training

Adjust the CFG class in `code/64x64_256stride_i3d.py`.
These are the parameters you can adjust per inference or training run. 

I found the default backbone setting to be different for the inference (efficientnet0) and training files (set to resnet) so make sure you select the one you want. 

```
python code/64x64_256stride_i3d.py
```
