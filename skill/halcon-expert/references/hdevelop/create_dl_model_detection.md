# create_dl_model_detection (Operator)

## Name

`create_dl_model_detection` — Create a deep learning network for object detection or instance segmentation.

## Signature

`create_dl_model_detection( : : Backbone, NumClasses, DLModelDetectionParam : DLModelHandle)`

## Description

With the operator `create_dl_model_detection` a deep learning network
for object detection or instance segmentation is created.
See the chapter [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md) for further
information on instance segmentation and object detection based on
deep learning.
The handle of this network is returned in *`DLModelHandle`*.

You can specify your model and its architecture over the parameters listed
below.
To successfully create a detection model, you need to specify its backbone
and the number of classes the model shall be able to distinguish.
The first information is handed over through the parameter
*`Backbone`* which is explained below in the section
“Possible Backbones”.
The second information is given through the parameter *`NumClasses`*.
Note, this parameter fixes the number of classes the network will
distinguish and therewith also the number of entries in
*'class_ids'* and *'class_names'*.

The values of all other applicable parameters can be specified using
the dictionary *`DLModelDetectionParam`*.
Such a parameter is e.g., the *'instance_type'*, determining which
kind of bounding boxes the model handles.
To create a deep learning network for instance segmentation the parameter
*'instance_segmentation'* has to be set to *'true'*.
The full list of parameters that can be set is given below in the section
“Settable Parameters”. Some parameters are only available for instance
segmentation.
In case a parameter is not specified, the default value is taken to create
the model.
Note, parameters influencing the network architecture will not be changeable
anymore once the network has been created.
All the other parameters can still be set or changed using the operator
[`set_dl_model_param`](set_dl_model_param.md).
An overview, how parameters can be set is given in
[`get_dl_model_param`](get_dl_model_param.md), where also a description of the specific
parameters is provided.
After creating the object detection model, the *'type'* will
automatically be set to *'detection'*.

### Possible Backbones

The parameter *`Backbone`* determines the backbone your
network will use. See the chapter [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md)
for more information to the backbone. In short, the backbone consists of a
pretrained classifier, from which only the layers necessary to generate
the feature maps are kept.
Hence, there are no fully connected layers anymore in the network.
This implies that you read in a classifier as feature extractor for
the subsequent detection network.
For this you can read in a classifier in the HALCON format or a model
in the ONNX format, see [`read_dl_model`](read_dl_model.md) for more information.

`create_dl_model_detection` attaches the feature pyramid on
different levels of the backbone.
More precisely, the backbone has for different levels a layer specified
as docking layer. When creating a detection
model, the feature pyramid is attached on the corresponding docking layer.
The pretrained classifiers provided by HALCON have already
specified docking layers. But when you use a self-provided classifier as
backbone, you have to specify them yourself.
You can set `backbone_docking_layers` as part of the classifier
using the operator [`set_dl_model_param`](set_dl_model_param.md) or the backbone as such
using this operator.

The docking layers are from different levels and therefore the feature
maps used in the feature pyramid are of different size.
More precisely, in the feature pyramid the feature map lengths are halved
with every level.
By implication, the input image lengths need to be halved for every level.
This means, the network architectures allow changes concerning the image
dimensions, but the dimensions *'image_width'* and
*'image_height'*
need to be an integer multiple of
$2^{level}$.
Here, $level$ is the highest level up to which the feature
pyramid is built.
This value depends on the attached networks as well as on the docking
layers. For the provided classifiers the list below mentions, up to which
levels the feature pyramid is built using default settings.

HALCON provides the following pretrained classifiers you can read in
as backbone:

- ***'pretrained_dl_classifier_alexnet.hdl'*:** —

  This neural network is designed for simple classification tasks.
  It is characterized by its convolution kernels in the first
  convolution layers, which are larger than in other networks with
  comparable classification performance
  (e.g., *'pretrained_dl_classifier_compact.hdl'*).
  This may be beneficial for feature extraction.

  This backbone expects the images to be of the type `real`.
  Additionally, the backbone is designed for certain image properties.
  The corresponding values can be retrieved with
  [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
  which the classifier has been trained:

  - —

    *'image_width'*: 224
  - —

    *'image_height'*: 224
  - —

    *'image_num_channels'*: 3
  - —

    *'image_range_min'*: -127.0
  - —

    *'image_range_max'*: 128.0

  The default feature pyramid built on this backbone goes up to level 4.
- ***'pretrained_dl_classifier_compact.hdl'*:** —

  This neural network is designed to be memory and runtime efficient.

  This backbone expects the images to be of the type `real`.
  Additionally, the backbone is designed for certain image properties.
  The corresponding values can be retrieved with
  [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
  which the classifier has been trained:

  - —

    *'image_width'*: 224
  - —

    *'image_height'*: 224
  - —

    *'image_num_channels'*: 3
  - —

    *'image_range_min'*: -127.0
  - —

    *'image_range_max'*: 128.0

  The default feature pyramid built on this backbone goes up to level 4.
- ***'pretrained_dl_classifier_enhanced.hdl'*:** —

  This neural network has more hidden layers than
  *'pretrained_dl_classifier_compact.hdl'* and is therefore
  assumed to be better suited for more complex tasks. But this comes
  at the cost of being more time and memory demanding.

  This backbone expects the images to be of the type `real`.
  Additionally, the backbone is designed for certain image properties.
  The corresponding values can be retrieved with
  [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
  which the classifier has been trained:

  - —

    *'image_width'*: 224
  - —

    *'image_height'*: 224
  - —

    *'image_num_channels'*: 3
  - —

    *'image_range_min'*: -127.0
  - —

    *'image_range_max'*: 128.0

  The default feature pyramid built on this backbone goes up to level 5.
- ***'pretrained_dl_classifier_mobilenet_v2.hdl'*:** —

  This classifier is a small and low-power model, and hence it is more
  suitable for mobile and embedded vision applications.

  This backbone expects the images to be of the type `real`.
  Additionally, the backbone is designed for certain image properties.
  The corresponding values can be retrieved with
  [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
  which the classifier has been trained:

  - —

    *'image_width'*: 224
  - —

    *'image_height'*: 224
  - —

    *'image_num_channels'*: 3
  - —

    *'image_range_min'*: -127.0
  - —

    *'image_range_max'*: 128.0

  The default feature pyramid built on this backbone goes up to level 4.
- ***'pretrained_dl_classifier_mobilenet_v4_small.hdl'*,
  *'pretrained_dl_classifier_mobilenet_v4_medium.hdl'*,
  *'pretrained_dl_classifier_mobilenet_v4_large.hdl'*:** —

  Selection of efficient classification models, offering low runtimes at high
  accuracies on a wide range of hardware platforms (see reference below).
  All models were pretrained with the following default values:

  - —

    *'image_width'*: 224
  - —

    *'image_height'*: 224
  - —

    *'image_num_channels'*: 3
  - —

    *'image_range_min'*: -127.0
  - —

    *'image_range_max'*: 128.0

  The default feature pyramid built on this backbone goes up to level 4.
- ***'pretrained_dl_classifier_resnet18.hdl'*:** —

  As the network *'pretrained_dl_classifier_enhanced.hdl'*,
  this network is suited for more complex tasks.
  But its structure differs, bringing the advantage of making the
  training more stable and being internally more robust. Compared to
  the neural network *'pretrained_dl_classifier_resnet50.hdl'*
  it is less complex and has faster inference times.

  This backbone expects the images to be of the type `real`.
  Additionally, the backbone is designed for certain image properties.
  The corresponding values can be retrieved with
  [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
  which the classifier has been trained:

  - —

    *'image_width'*: 224
  - —

    *'image_height'*: 224
  - —

    *'image_num_channels'*: 3
  - —

    *'image_range_min'*: -127.0
  - —

    *'image_range_max'*: 128.0

  The default feature pyramid built on this backbone goes up to level 5.
- ***'pretrained_dl_classifier_resnet50.hdl'*:** —

  As the network *'pretrained_dl_classifier_enhanced.hdl'*,
  this network is suited for more complex tasks.
  But its structure differs, bringing the advantage of making the
  training more stable and being internally more robust.

  This backbone expects the images to be of the type `real`.
  Additionally, the backbone is designed for certain image properties.
  The corresponding values can be retrieved with
  [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
  which the classifier has been trained:

  - —

    *'image_width'*: 224
  - —

    *'image_height'*: 224
  - —

    *'image_num_channels'*: 3
  - —

    *'image_range_min'*: -127.0
  - —

    *'image_range_max'*: 128.0

  The default feature pyramid built on this backbone goes up to level 5.

### Settable Parameters

Parameters you can set for your model when creating it using
`create_dl_model_detection` (see [`get_dl_model_param`](get_dl_model_param.md) for
explanations):

- *'anchor_angles'*
- *'anchor_aspect_ratios'* (legacy: *'aspect_ratios'*)
- *'anchor_num_subscales'* (legacy: *'num_subscales'*)
- *'backbone_docking_layers'*
- *'bbox_heads_weight'*, *'class_heads_weight'*
- *'capacity'*
- *'class_ids'*
- *'class_ids_no_orientation'*
- *'class_names'*
- *'class_weights'*
- *'freeze_backbone_level'*
- *'ignore_direction'*
- *'image_dimensions'*
- *'image_height'*, *'image_width'*
- *'image_num_channels'*
- *'instance_segmentation'*
- *'instance_type'*
- *'mask_head_weight'*

  Restriction:
   only instance segmentation
- *'max_level'*, *'min_level'*
- *'max_num_detections'*
- *'max_overlap'*
- *'max_overlap_class_agnostic'*
- *'min_confidence'*
- *'optimize_for_inference'*

## Attention

To successfully set *'gpu'* parameters, cuDNN and cuBLAS are
required, i.e., to set the parameter `GenParamName`
*'runtime'* to *'gpu'*.
For further details, please refer to the `“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Backbone`** (input_control)  filename.read `→`  (string)

Deep learning classifier, used as backbone network.

Default:
'pretrained_dl_classifier_compact.hdl'

List of values:
'pretrained_dl_classifier_alexnet.hdl', 'pretrained_dl_classifier_compact.hdl', 'pretrained_dl_classifier_enhanced.hdl', 'pretrained_dl_classifier_mobilenet_v2.hdl', 'pretrained_dl_classifier_mobilenet_v4_large.hdl', 'pretrained_dl_classifier_mobilenet_v4_medium.hdl', 'pretrained_dl_classifier_mobilenet_v4_small.hdl', 'pretrained_dl_classifier_resnet18.hdl', 'pretrained_dl_classifier_resnet50.hdl'

File extension:
.`hdl`

**`NumClasses`** (input_control)  integer `→`  (integer)

Number of classes.

Default:
3

**`DLModelDetectionParam`** (input_control)  dict `→`  (handle)

Parameters for the object detection model.

Default:
[]

**`DLModelHandle`** (output_control)  dl_model `→`  (handle)

Deep learning model for object detection.

## Result

If the parameters are valid, the operator `create_dl_model_detection`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`set_dl_model_param`,
`get_dl_model_param`,
`apply_dl_model`,
`train_dl_model_batch`

## Alternatives

`read_dl_model`

## References

D. Qin et al.,
"MobileNetV4: Universal Models for the Mobile Ecosystem". In
European Conference on Machine Vision, pp. 78-96, Sept. 2024,
https://doi.org/10.1007/978-3-031-73661-2_5

## Module

Deep Learning Professional
