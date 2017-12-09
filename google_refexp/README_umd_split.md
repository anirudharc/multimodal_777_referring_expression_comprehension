# Google Refexp (Referring Expressions) dataset - UMD split
The original partitions provided by Mao et al. were created by randomly selecting 
5000 objects for validation. This resulted in overlapping images between training and 
validation sets.

We create a different split since we train on negative and context regions 
in an image and that information should not leak into the test stage.
Our training partition contains 23199 images with 67996 objects and 85408 referring 
expressions. The validation partition contains 2600 images with 7623 objects 
and 9602 referring expressions.

We also provide MCG region candidates for all the images in training and validation.
The region candidates are filtered in the same way as Mao et al. 
We first obtain top 100 proposals for an image using MCG and evaluate scores 
for the 80 categories in the MS-COCO dataset. We then discard boxes with low values. 
The category scores are obtained using the 16 layers VGGNet CNN fine-tuned using 
Fast RCNN. 

## Citation

If you find this dataset useful in your research, please consider citing:

    @inproceedings{mao2016generation,
      title={Generation and Comprehension of Unambiguous Object Descriptions},
      author={Mao, Junhua and Huang, Jonathan and Toshev, Alexander and Camburu, Oana and Yuille, Alan and Murphy, Kevin},
      booktitle={CVPR},
      year={2016}
    }
    
If you use the UMD split, please consider citing:

    @inproceedings{nagaraja16refexp,
      title={Modeling Context Between Objects for Referring Expression Understanding},
      author={Varun K. Nagaraja and Vlad I. Morariu and Larry S. Davis},
      booktitle={ECCV},
      year={2016}
    }

If you are using the multibox proposals ("region_candidates" field), please also
consider citing:

    @inproceedings{erhan2014scalable,
      title={Scalable object detection using deep neural networks},
      author={Erhan, Dumitru and Szegedy, Christian and Toshev, Alexander and Anguelov, Dragomir},
      booktitle={CVPR},
      pages={2155--2162},
      year={2014},
    }

If you are using the MCG proposals, please cite:

    @inproceedings{APBMM2014,
      author = {Arbel\'{a}ez, P. and Pont-Tuset, J. and Barron, J. and Marques, F. and Malik, J.},
      title = {Multiscale Combinatorial Grouping},
      booktitle = {CVPR},
      year = {2014}
    }

## Terms of use:

The annotations in this dataset belong to Google and are licensed under a Creative Commons Attribution 4.0 License (see license.txt file).  See also http://mscoco.org/terms_of_use/ for terms of use for the MS-COCO dataset.
