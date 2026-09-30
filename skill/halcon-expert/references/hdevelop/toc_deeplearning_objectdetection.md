## Advanced Object Detection

List of Sections ↓

This chapter explains how to use **advanced object detection**
based on deep learning.

With **advanced object detection**, the goal is to find different objects
within an image and assign them to a class.
Multiple objects may appear in the same image and may partially overlap
while still being detected as distinct objects.
This is illustrated in the following schema.

![figure](../assets/be1375dc20e536f1.svg)

A possible example for advanced object detection: Within the input image
three objects are found and assigned to a class.

Unlike image classification, which assigns a single label to an entire image,
advanced object detection performs both object localization and
classification within a single network.

It is based on an efficient detection architecture that
improves robustness and performance compared to previous approaches.
In particular, the detection of objects of different sizes is improved
and robustness against varying image conditions is increased.

The model predicts bounding boxes indicating the position of potential
objects in the image.

As output, the model returns the following information for each
detected object:

- An axis-aligned bounding box (instance type *`'rectangle1'`*)
- A class assignment
- A confidence value

The confidence value denotes a model-dependent score that reflects the
relative certainty of the network that the predicted bounding box corresponds
to an object of the assigned class.

Advanced object detection supports exclusively the instance type
*`'rectangle1'`*.
Therefore, all bounding boxes are axis-aligned rectangles.

For object detection with oriented bounding boxes,
see the chapter [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md).

In HALCON, advanced object detection is implemented within the
general deep learning framework.
For more information on the deep learning model in general, see the
chapter [Deep Learning / Model](toc_deeplearning_model.md).

The following sections describe the general workflow needed for advanced
object detection, information related to the involved data,
and explanations to the network output.

### General Workflow

In this paragraph, we describe the general workflow for an advanced object
detection task based on deep learning.

The preprocessing and data augmentation are defined using a transform
pipeline. The pipeline specifies a sequence of transformations that are
applied to the input images before they are processed by the model.

The general workflow for advanced object detection is subdivided
into the following four parts:

- Loading of the model and configuration of the transform pipeline
- Training of the model
- Evaluation of the trained model
- Inference on new images

Here, we assume, your dataset is already labeled, see also the
section “Data” below.

Have a look at the HDevelop example
`dl_advanced_detection_workflow.hdev` for a complete workflow.
The example series `detect_pills_deep_learning_*.hdev`
illustrates the individual workflow steps using the advanced object
detection approach.

For details on defining and configuring transform pipelines,
including data augmentation, see the dedicated HDevelop example
`dl_transform_pipeline.hdev`.

- **Loading of the model and configuration of the transform pipeline** —

  This part covers the preparation of the dataset and the creation
  of a transform pipeline used to preprocess and augment the data.

  1. Load a pretrained detection model using the operator

     - [`read_dl_model`](read_dl_model.md).
  2. Read the dataset containing the images and annotations into
     a dictionary `DLDataset`.
  3. Split the dataset represented by the dictionary
     `DLDataset`. This can be done using the procedure

     - `split_dl_dataset`.
  4. Create individual transform methods defining the desired
     preprocessing and augmentation steps.
     Typical transformations include random perspective
     transformations, flipping,
     normalization, and resizing.

     Typical transform methods are created using operators such as:

     - [`create_dl_transform_flip`](create_dl_transform_flip.md)
     - [`create_dl_transform_random_hsv`](create_dl_transform_random_hsv.md)
     - [`create_dl_transform_normalize`](create_dl_transform_normalize.md)
     - [`create_dl_transform_resize`](create_dl_transform_resize.md)
  5. Combine the individual transforms into a transform pipeline
     using the operator

     - [`create_dl_transform_pipeline`](create_dl_transform_pipeline.md).
  6. Store the resulting pipeline in the dictionary `DLDataset`.
     Separate pipelines can be defined for training, validation,
     and test data.
     Typically, data augmentation is applied only during training,
     while for validation and test data only deterministic
     preprocessing steps are used.
- **Training of the model** —

  In this part the model is trained using the prepared dataset.

  1. Set the training parameters and store them in the dictionary
     `TrainParam`.
  2. Train the model using the procedure

     - `train_dl_model`.

     During training, the transform pipeline is applied to the input
     data. This allows performing data augmentation and other
     preprocessing steps before the images are processed by the
     network.
- **Evaluation of the trained model** —

  In this part, the trained model is evaluated.

  1. Evaluate the model using the procedure

     - `evaluate_dl_model`.
  2. The evaluation results can be visualized using the procedure

     - `dev_display_detection_detailed_evaluation`.
- **Inference on new images** —

  This part covers the application of the trained detection model.

  1. Generate a data dictionary `DLSample` for each input
     image using the procedure

     - `gen_dl_samples_from_images`.
  2. Apply the transform pipeline defined for test data to the generated
     samples using the operator

     - [`transform_dl_sample_batch`](transform_dl_sample_batch.md).

     The applied pipeline depends on the dataset configuration.
  3. Apply the model using the operator

     - [`apply_dl_model`](apply_dl_model.md).
  4. Retrieve the detection results from the dictionary
     *`'DLResultBatch'`*.

### Data

We distinguish between data used for training and evaluation and
data used for inference.
Training and evaluation data consist of images together with
annotations describing the object, whereas inference
data consist of images only.

As a basic concept, the model handles data over dictionaries,
meaning it receives the input data over a dictionary `DLSample`
and returns results in dictionaries such as `DLResult`.
More information on the data handling can be found in the chapter
[Deep Learning / Model](toc_deeplearning_model.md).

- **Data for training and evaluation** —

  The dataset consists of images and corresponding annotations.
  For each object, the class label and its location within
  the image must be provided.

  Each object requires the following information:

  - The coordinates of the upper left corner
    (*`'bbox_row1'`*, *`'bbox_col1'`*)
  - The coordinates of the lower right corner
    (*`'bbox_row2'`*, *`'bbox_col2'`*)
  - A corresponding class label

  These parameters define an axis-aligned bounding box and are
  consistent with the operator [`gen_rectangle1`](gen_rectangle1.md).

  The dataset is organized in a dictionary `DLDataset`,
  which stores the images together with their annotations and
  additional information required for training and evaluation.

  The example `detect_pills_deep_learning_1.hdev`
  illustrates how to prepare and structure such a dataset.
- **Images** —

  The network imposes requirements on the input images, such as the
  image dimensions and value ranges.
  These requirements depend on the model and can be queried using
  the operator

  - [`get_dl_model_param`](get_dl_model_param.md).

  The required preprocessing and data augmentation steps are defined
  using a transform pipeline.
  The transformations are applied to the images at runtime before they
  are processed by the model and are not stored in the dataset.
- **Data for inference** —

  For inference, only the images are required.
  The same transform pipeline as defined for the model should be
  applied to ensure consistent preprocessing.

### Model Parameters and Hyperparameters

Next to the general deep learning hyperparameters explained in
[Deep Learning](toc_deeplearning.md), there are further hyperparameters relevant
for object detection.

- *`'bbox_heads_weight'`*
- *`'class_heads_weight'`*

These hyperparameters influence the weighting of the respective
loss components during training.

For an advanced object detection model, several model parameters influence
the predictions and, consequently, the evaluation results:

- *`'max_num_detections'`*
- *`'max_overlap'`*
- *`'max_overlap_class_agnostic'`*
- *`'min_confidence'`*

In advanced object detection, the model may predict multiple overlapping
bounding boxes for the same object.
To reduce such duplicate detections, non-maximum suppression (NMS)
is applied.

The suppression behavior can be controlled using the parameters
*`'max_overlap'`* and
*`'max_overlap_class_agnostic'`*.

The parameter *`'max_overlap'`* defines the maximum allowed
overlap between bounding boxes of the same class.
If the overlap exceeds this threshold, only the bounding box with
the highest confidence is kept.

The parameter *`'max_overlap_class_agnostic'`* extends this
suppression to bounding boxes of different classes.

These parameters influence the final detection results and,
consequently, the evaluation.

The parameters can be set when creating the model or afterwards
using the operator [`set_dl_model_param`](set_dl_model_param.md).
For more information, see the operator [`get_dl_model_param`](get_dl_model_param.md).

### Evaluation Measures

For advanced object detection, the following evaluation measures are supported
in HALCON.
Note that for computing such a measure for an image, the related ground
truth information is needed.

- Mean average precision, `mAP` and average precision (AP)
  of a class for an IoU threshold, `ap_iou_classname`

  The AP value is an average of maximum precision at different recall
  values.
  In simple words it tells us, if the objects predicted for this class
  are generally correct detections or not.
  Thereby we pay more attention to the predictions with high confidence
  values. The higher the value, the better.

  To count a prediction as a hit, we want both correct, its
  top-1 classification and its localization.
  The measure, telling us the correctness of the localization is the
  intersection over union, IoU: an instance is localized correctly if
  the IoU is higher than the demanded threshold.
  The IoU is explained in more detail below.
  For this reason, the AP value depends on the class and on the IoU
  threshold.

  You can obtain the specific AP values, the averages over the classes,
  the averages over the IoU thresholds, and the average over both, the
  classes and the IoU thresholds.
  The latter one is the mean average precision, mAP, a measure to tell
  us how well instances are found and classified.
- True Positives, False Positives, False Negatives

  The concept of true positive, false positives, and false negatives
  is explained in [Deep Learning](toc_deeplearning.md).
  It applies for object detection with the exception that there are
  different kinds of false positives, as e.g.:

  - An instance got classified wrongly.
  - An instance was found where there is only background.
  - An instance was localized badly, meaning the IoU between the
    instance and its ground truth is lower than the evaluation IoU
    threshold.
  - There is a duplicate, thus at least two instances overlap mainly
    with the same ground truth bounding box, but they overlap not more
    than *`'max_overlap'`* with each other, so none of them got
    suppressed.

  Note, these values are only available from the detailed evaluation.
  This means, in `evaluate_dl_model` the parameter
  `detailed_evaluation` has to be set to *`'true'`*.

Before mentioned measures use the intersection over union (IoU).
The IoU is a measure for the accuracy of an
object detection. For a proposed bounding box it compares
the ratio between area of intersection and the area of overlap with
the ground truth bounding box.
A visual example is shown in the following schema.

|  |  |
| --- | --- |
| ![figure](../assets/24bb7a02f4c77c4b.svg) | ![figure](../assets/fc62427e397ffb0e.svg) |
| ( 1) | ( 2) |

Visual example of the IoU, illustrated for instance type
*`'rectangle1'`*.
(1) The input image with the ground truth bounding box (orange)
and the predicted bounding box (light blue).
(2) The IoU is the ratio between the area intersection and the
area overlap.

### Limitations

Currently, advanced object detection supports only axis-aligned
bounding boxes (*`'rectangle1'`*).

---

#### List of Sections
