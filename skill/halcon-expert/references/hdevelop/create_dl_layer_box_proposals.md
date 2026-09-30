# create_dl_layer_box_proposals (Operator)

## Name

`create_dl_layer_box_proposals` — Create a layer for generating box proposals.

## Signature

`create_dl_layer_box_proposals( : : DLLayerClassScore, DLLayerBoxDelta, DLLayerBox, DLLayerInputImage, LayerName, GenParamName, GenParamValue : DLLayerBoxProposals)`

## Description

The operator `create_dl_layer_box_proposals` creates a layer for
generating box proposals whose handle is returned in
*`DLLayerBoxProposals`*.

This layer expects several feeding input layers:

- *`DLLayerClassScore`*: Contains the predicted score for
  each input box and class,
- *`DLLayerBoxDelta`* (optional): Contains the box delta values
  predicted by a box regression layer (see
  [`create_dl_layer_box_targets`](create_dl_layer_box_targets.md)),
- *`DLLayerBox`*: Contains the input box coordinates, and
- *`DLLayerInputImage`*: Contains the image feeding layer of
  the network or any other layer that has the same dimensions (regarding
  `width` and `height`) as the input images.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The box proposal layer processes the input boxes in the following steps
(see also the detailed description of generic parameters below):

- **Apply scores:** —

  For each input box in *`DLLayerBox`*, the
  corresponding score in *`DLLayerClassScore`* is set as box
  confidence. If *`DLLayerClassScore`* contains scores for more than
  one class, one box is created for each class where the score exceeds the
  *'min_confidence'* and the class ID belonging to the
  class index is set as output class ID.
  All boxes with a score smaller than *'min_confidence'* are removed.
  During training, the score threshold *'min_confidence_train'* is
  used instead of *'min_confidence'*. A lower value allows to
  forward more boxes to consecutive stages of the network. At most
  *'max_num_pre_nms'* boxes per input with highest score are kept
  for the following steps.
- **Apply box deltas:** —

  If box deltas are given in
  *`DLLayerBoxDelta`* and *'apply_box_regression'* is
  *'true'*, box deltas are applied to the input boxes given by
  *`DLLayerBox`*. Before being applied, the box deltas are
  transformed by the inverse function as their targets are transformed in
  [`create_dl_layer_box_targets`](create_dl_layer_box_targets.md). All coordinates shall be given
  subpixel-precisely. If *`DLLayerBoxDelta`* is set to an empty
  tuple, box coordinates are kept as given in *`DLLayerBox`*.
- **Class specific non-maximum-suppression (NMS):** —

  For each box *B*
  that has not been suppressed by another box, all other boxes *B'*
  that are not suppressed, have the same class ID, have a lower score and
  have an intersection over union (IoU) of at least *'max_overlap'*
  with *B* are suppressed.
- **Class agnostic NMS:** —

  For each box *B* that has not been
  suppressed by another box, all other boxes *B'* that are not
  suppressed, have a lower score and have an IoU of at least
  *'max_overlap_class_agnostic'* with *B* are suppressed.
- **Set outputs:** —

  After NMS was applied, the at most
  *'max_num_post_nms'* boxes (in total for all inputs) with the
  highest scores that have not been suppressed are given as output. If
  less than *'max_num_post_nms'* boxes are present within one batch
  item, the remaining output values are filled up with zeros.

For each box the output contains its parameters, its class index, and its
score in this order. The box parameters depend on the
*'instance_type'*:
4 for *'rectangle1'* (`row1`, `column1`,
`row2`, `column2`), and
5 for *'rectangle2'* (`row`, `column`, `phi`,
`length1`, `length2`) respectively.
Hence, the output `depth` equals the maximum number of output boxes
per batch item *'max_num_post_nms'*, the `height` equals the
number of box parameters plus two (for class index and score), and the
`width` equals one.
The subpixel-precise coordinates (pixel-centered, see
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md)) of the output boxes are given
with respect to the input image dimensions.

After creating a network with [`create_dl_model`](create_dl_model.md) and setting the
model type to *'detection'* via [`set_dl_model_param`](set_dl_model_param.md),
the last box proposals layer within the network is used as the box
output layer: Its outputs are given in tuples within the result
dictionary of the model, similar to the outputs given by a detection
model that has been created by [`create_dl_model_detection`](create_dl_model_detection.md).
The output dictionary contains:

- box parameters. Depending on the *'instance_type'* the keys are:

  - `'bbox_row1'`, `'bbox_col1'`, `'bbox_row2'`,
    and `'bbox_col2'` for
    *'instance_type'* = *'rectangle1'*.
  - `'bbox_row'`, `'bbox_col'`, `'bbox_length1'`,
    `'bbox_length2'`, and `'bbox_phi'` for
    *'instance_type'* = *'rectangle2'*.
- class IDs. Key: `'bbox_class_id'`
- scores. Key: `'bbox_confidence'`

For a created model with type set to *'detection'*, the following
parameters (see their explanation below) of the last box proposal layer
within the network can be set with the operators [`set_dl_model_param`](set_dl_model_param.md)
or [`set_dl_model_layer_param`](set_dl_model_layer_param.md):

- *'max_num_detections'* (overwrites
  *'max_num_post_nms'*),
- *'max_overlap'*,
- *'max_overlap_class_agnostic'*,
- *'min_confidence'*, and
- *'nms_pre_top_n_per_level'* (overwrites
  *'max_num_pre_nms'*).

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'apply_box_regression'*:** —

  If set to *'false'*, box
  regression is not applied.

  Default:
   *'true'*.
- ***'box_cls_specific'*:** —

  Should be set to *'true'*,
  if the box deltas are calculated class-specifically, see
  [`create_dl_layer_box_targets`](create_dl_layer_box_targets.md).

  Default:
   *'false'*.
- ***'clip_boxes'*:** —

  If set to *'true'*, output boxes are
  clipped to the image boundaries.

  Restriction:
   Only for *'instance_type'*
  *'rectangle1'*.

  Default:
   *'false'*.
- ***'ignore_direction'*:** —

  If set to *'false'*, the
  orientation of *'rectangle2'* boxes is in the range
  $(-\pi,\pi]$, else in the range
  $(-\pi/2,\pi/2]$.

  Restriction:
   Only for *'instance_type'*
  *'rectangle2'*.

  Default:
   *'false'*.
- ***'input_mode'*:** —

  Type of the underlying box inputs and
  box deltas. The following types can be set:

  - ***'anchors'*:** —

    The input boxes given by
    *`DLLayerBox`* are anchors, e.g., generated with
    [`create_dl_layer_anchors`](create_dl_layer_anchors.md). In this case, both the score inputs
    and the optional box delta inputs shall have the same `width` and
    `height` as the anchors.

    The `depth` of the score inputs
    corresponds to the anchor type and class index. Hence, if *k* is
    the number of anchor types (the number of subscales times the number of
    aspect ratios times the number of angles) and *n* is the number of
    classes, the `depth` shall be *k* times *n*.
    The ordering is the same as given in the class target output
    of the box target layer, i.e.,
    (anchor type 0, class index 0),
    (anchor type 0, class index 1), ...,
    (anchor type 0, class index *n*-1), ...,
    (anchor type *k*-1, class index 0),
    (anchor type *k*-1, class index 1), ...,
    (anchor type *k*-1, class index *n*).

    The `depth` of the box delta inputs corresponds to the number of
    anchor types times the number of box parameters (NBP),
    i.e. *k* * NBP.
    NBP depends on the *'instance_type'*: there are
    4 parameters for *'rectangle1'* (`row1`, `column1`,
    `row2`, `column2`), and
    5 parameters for *'rectangle2'* (`row`, `column`,
    `phi`, `length1`, `length2` ) respectively.
    Hence the box delta inputs and the input anchors shall be equal in
    `depth` and ordered in the same way.
    If [`create_dl_layer_box_targets`](create_dl_layer_box_targets.md) was used to generate the score and
    box delta targets, the correct order is already on hand.

    *`DLLayerBox`*, *`DLLayerClassScore`*, and
    *`DLLayerBoxDelta`* can be tuples of layers of the
    same length to be processed simultaneously. For example, each input can
    correspond to one level in a Feature Pyramid Network (see the references
    given below).
  - ***'dense'*:** —

    The input boxes given by
    *`DLLayerBox`* are box proposals, e.g., generated with another box
    proposals layer. In this case, the batch size of the score and box
    delta inputs shall be the same as the batch size of the box inputs
    times the `depth` of the box inputs. This change of batch size is
    achieved by a ROI pooling layer ([`create_dl_layer_roi_pooling`](create_dl_layer_roi_pooling.md))
    that uses the box proposals as input.

    The `depth` of the score inputs shall be the number of classes plus
    one, since the first index is interpreted as background class.

    The `depth` of the box delta inputs shall be the number of
    box parameters NBP, if *'box_cls_specific'* is set to
    *'false'*, or NBP times the number of classes if
    *'box_cls_specific'* is set to *'true'*.

    If [`create_dl_layer_box_targets`](create_dl_layer_box_targets.md) was used to generate the score and
    box delta targets, here as well, the correct order is already on hand.

  Default:
   *'anchors'*.
- ***'inside_angle_weight'*:** —

  Inside weight multiplier for
  box angle coordinates (phi). Box angle deltas are divided
  by this value to account for the inside box weights in the box targets
  layer. Hence, the values should match the corresponding values that
  are set in the box targets layer.

  Restriction:
   Only for *'instance_type'*
  *'rectangle2'*.
  Default:
   *1.0*.
- ***'inside_center_weight'*:** —

  Inside weight multiplier for
  box center coordinates (row and column). Box center deltas are divided
  by this value to account for the inside box weights in the box targets
  layer. Hence, the values should match the corresponding values that
  are set in the box targets layer.

  Default:
   *1.0*.
- ***'inside_dimension_weight'*:** —

  Inside weight multiplier for
  box dimension (width and height). Box dimension deltas are divided
  by this value to account for the inside box weights in the box targets
  layer. Hence, the values should match the corresponding values that
  are set in the box targets layer.

  Default:
   *1.0*.
- ***'instance_type'*:** —

  Instance type of the generated boxes.
  Possible values:

  - *'rectangle1'*: axis-aligned rectangles.
  - *'rectangle2'*: oriented rectangles.

  Default:
   *'rectangle1'*.
- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*
- ***'max_num_post_nms'*:** —

  Maximal number of detections after
  applying NMS. If the number of inputs in *`DLLayerClassScore`*
  times *'max_num_pre_nms'* is higher, this value is taken.

  Restriction:
   Must be an integer larger than zero.

  Default:
   *1000*.
- ***'max_num_pre_nms'*:** —

  Maximum number of detections per
  *`DLLayerClassScore`* input before applying NMS.

  Restriction:
   Must be an integer larger than zero.

  Default:
   *10000*.
- ***'max_overlap'*:** —

  The maximal allowed intersection over
  union (IoU) between two boxes of the same class. Class specific NMS
  can be switched off by setting this value to *1.0*.

  Default:
   *0.7*.
- ***'max_overlap_class_agnostic'*:** —

  The maximum allowed IoU
  between two boxes of any class. Class agnostic NMS can be switched
  off by setting this value to *1.0*.

  Default:
   *1.0*.
- ***'max_side_length'*:** —

  Boxes with at least one of the
  side-length larger than this value are discarded. Possible values:

  - ***'default'* or *0.0*:** —

    For *'instance_type'*
    *'rectangle1'* the thresholds are set to 1.5 times the image
    height for the box height and 1.5 times the image width for the box
    width.

    For *'instance_type'* *'rectangle2'* the threshold
    is set to two times the maximum of the image width and height for both
    the box width and height.
  - **Number:** —

    Determines the maximum side length that is allowed.
  - ***'none'*:** —

    No thresholding is used.

  Restriction:
   Needs to be larger or equal to zero or
  *'default'* or *'none'*.

  Default:
   *'default'*.
- ***'min_confidence'*:** —

  Boxes with a confidence smaller than
  this value are discarded during inference.

  Default:
   *0.5*.
- ***'min_confidence_train'*:** —

  Boxes with a confidence
  smaller than this value are discarded during training.

  Default:
   *0.05*.
- ***'min_side_length'*:** —

  Boxes with at least one side length
  smaller than this value are discarded.

  Restriction:
   Shall be larger or equal to zero.

  Default:
   *0.0*.
- ***'nms_mode'*:** —

  Determines which IoU is used for the NMS
  calculation. Possible values:

  - ***'exact'*:** —

    Exact IoU.
  - ***'arIoU'*:** —

    Angle-related IoU. The angle-related IoU is defined
    for two *'rectangle2'* boxes *A* and *B* as the
    cosine of their intermediate angle times the *'rectangle1'*
    IoU of $\overline{A}$ ![figure](../assets/310ff61e2cd9208a.svg) and *B*, where $\overline{A}$ ![figure](../assets/310ff61e2cd9208a.svg) is the box
    *A* aligned to the box *B*.
    See also [`create_dl_layer_box_targets`](create_dl_layer_box_targets.md).

  Restriction:
   Only applicable for *'instance_type'*
  *'rectangle2'*.

  Default:
   *'exact'*.
- ***'nms_type'*:** —

  Determines which type of NMS is used. Possible values:

  - ***'standard'*:** —

    A box is discarded if it overlaps with another
    box with higher score.
  - ***'soft'*:** —

    Soft NMS is applied. This means that a box is not
    discarded if it overlaps with another box with higher score.
    Instead, its score is reduced depending on the value of the IoU with the
    higher scoring box, see *'soft_nms_type'* and the references below.

  Default:
   *'standard'*.
- ***'soft_nms_type'*:** —

  Defines how the scores are updated in case
  of *'nms_type'* *'soft'*. Possible values:

  - ***'linear'*:** —

    The confidence of a box is scaled by a
    factor 1 - IoU if its IoU with another higher scoring box is greater
    than *'max_overlap'* or *'max_overlap_class_agnostic'*,
    respectively.
  - ***'gaussian'*:** —

    Iteratively each box causes a scaling of the
    box confidence of all other boxes with lower confidence by a factor
    $$e^{-\\frac{\\lVert \\mathrm{IoU} \\rVert}{\\sigma}}$$ ![figure](../assets/4264787ea1a73c09.svg)
    where $\sigma$ is given as *'max_overlap'* and
    *'max_overlap_class_agnostic'*, respectively.

  Default:
   *'linear'*.

Certain parameters of layers created using this operator
`create_dl_layer_box_proposals` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Internal Parameters | `set` | `get` |
| --- | --- | --- |
| *'input_layer'* (*`DLLayerClassScore`*, *`DLLayerBoxDelta`*, *`DLLayerBox`*, and/or *`DLLayerInputImage`*) |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerBoxProposals`*) |  | `x` |
| *'shape'* |  | `x` |
| *'type'* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'apply_box_regression'* | `x` | `x` |
| *'box_cls_specific'* |  | `x` |
| *'clip_boxes'* | `x` | `x` |
| *'has_box_regression_inputs'* |  | `x` |
| *'ignore_direction'* |  | `x` |
| *'input_mode'* |  | `x` |
| *'inside_angle_weight'* |  | `x` |
| *'inside_center_weight'* |  | `x` |
| *'inside_dimension_weight'* |  | `x` |
| *'is_inference_output'* | `x` | `x` |
| *'instance_type'* |  | `x` |
| *'max_overlap'* | `x` | `x` |
| *'max_overlap_class_agnostic'* | `x` | `x` |
| *'max_num_post_nms'* |  | `x` |
| *'max_num_pre_nms'* | `x` | `x` |
| *'max_overlap'* | `x` | `x` |
| *'max_overlap_class_agnostic'* | `x` | `x` |
| *'max_num_post_nms'* |  | `x` |
| *'max_num_pre_nms'* | `x` | `x` |
| *'max_side_length'* | `x` | `x` |
| *'min_confidence'* | `x` | `x` |
| *'min_confidence_train'* | `x` | `x` |
| *'min_side_length'* | `x` | `x` |
| *'nms_mode'* |  | `x` |
| *'nms_type'* | `x` | `x` |
| *'num_class_ids_no_orientation'* |  | `x` |
| *'num_trainable_params'* |  | `x` |
| *'soft_nms_type'* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerClassScore`** (input_control)  dl_layer(-array) `→`  (handle)

Feeding layers with classification scores.

**`DLLayerBoxDelta`** (input_control)  dl_layer(-array) `→`  (handle)

Feeding layers with bounding box regression values.

**`DLLayerBox`** (input_control)  dl_layer(-array) `→`  (handle)

Feeding layers with anchors or input box proposals.

**`DLLayerInputImage`** (input_control)  dl_layer `→`  (handle)

Feeding layer with the network input image.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'apply_box_regression', 'box_cls_specific', 'clip_boxes', 'ignore_direction', 'input_mode', 'inside_angle_weight', 'inside_center_weight', 'inside_dimension_weight', 'instance_type', 'is_inference_output', 'max_num_post_nms', 'max_num_pre_nms', 'max_overlap', 'max_overlap_class_agnostic', 'max_side_length', 'min_confidence', 'min_confidence_train', 'min_side_length', 'nms_mode', 'nms_type', 'soft_nms_type'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Generic input parameter values.

Default:
[]

Suggested values:
'rectangle1', 'rectangle2', 'dense', 'anchors', 'standard', 'soft', 'exact', 'arIoU', 'linear', 'gaussian', 'true', 'false', 'default', 'none', 0.05, 0.5, 1.0, 0.7, 10.0, 5.0, 2000

**`DLLayerBoxProposals`** (output_control)  dl_layer `→`  (handle)

BoxProposals layer.

## Example (HDevelop)

```
* Minimal example for the usage of layers
*  - create_dl_layer_box_proposals
*  - create_dl_layer_box_targets
* for creating and training a model to perform object detection.
*
dev_update_off ()
NumClasses := 1
AnchorAspectRatios := 1.0
AnchorNumSubscales := 1
* Define the input image layer.
create_dl_layer_input ('image', [224,224,3], [], [], DLLayerInputImage)
* Define the input ground truth box layers.
create_dl_layer_input ('bbox_row1', [1, 1, 10], ['allow_smaller_tuple'], \
                       ['true'], DLLayerInputRow1)
create_dl_layer_input ('bbox_row2', [1, 1, 10], ['allow_smaller_tuple'], \
                       ['true'], DLLayerInputRow2)
create_dl_layer_input ('bbox_col1', [1, 1, 10], ['allow_smaller_tuple'], \
                       ['true'], DLLayerInputCol1)
create_dl_layer_input ('bbox_col2', [1, 1, 10], ['allow_smaller_tuple'], \
                       ['true'], DLLayerInputCol2)
create_dl_layer_input ('bbox_label_id', [1, 1, 10], \
                       ['allow_smaller_tuple'], ['true'], \
                       DLLayerInputLabelID)
create_dl_layer_class_id_conversion (DLLayerInputLabelID, \
                                     'class_id_conversion', \
                                     'from_class_id', [], [], \
                                     DLLayerClassIdConversion)
* Concatenate all box coordinates.
create_dl_layer_concat ([DLLayerInputRow1, DLLayerInputCol1, \
                        DLLayerInputRow2, DLLayerInputCol2, \
                        DLLayerClassIdConversion], \
                        'gt_boxes', 'height', [], [], DLLayerGTBoxes)
*
* Perform some operations on the input image to extract features.
* -> this serves as our backbone CNN here.
create_dl_layer_convolution (DLLayerInputImage, 'conv1', 3, 1, 2, 8, 1, \
                             'half_kernel_size', 'relu', [], [], \
                             DLLayerConvolution)
create_dl_layer_convolution (DLLayerConvolution, 'conv2', 3, 1, 2, 8, 1, \
                             'half_kernel_size', 'relu', [], [], \
                             DLLayerConvolution)
create_dl_layer_pooling (DLLayerConvolution, 'pool', 2, 2, 'none', \
                         'maximum', [], [], DLLayerPooling)
*
* Create the anchor boxes -> adapt the scale to fit the object size.
create_dl_layer_anchors (DLLayerPooling, DLLayerInputImage, 'anchor', \
                         AnchorAspectRatios, AnchorNumSubscales, [], \
                         ['scale'], [8], DLLayerAnchors)
*
* Create predictions for the classification and regression of anchors.
* We set the bias such that background is a lot more likely than foreground.
PriorProb := 0.05
BiasInit := -log((1.0 - PriorProb) / PriorProb)
create_dl_layer_convolution (DLLayerPooling, 'cls_logits', 3, 1, 1, \
                             NumClasses, 1, 'half_kernel_size', 'none', \
                             ['bias_filler_const_val'], \
                             [BiasInit], DLLayerClsLogits)
create_dl_layer_convolution (DLLayerPooling, 'box_delta_predictions', 5, 1, \
                             1, 4*|AnchorAspectRatios|*|AnchorNumSubscales|, \
                             1, 'half_kernel_size', 'none', [], [], \
                             DLLayerBoxDeltaPredictions)
*
* Generate the class and box regression targets for the anchors
* according to the ground truth boxes.
* -> we use inside-weights here, they also need to be set in the
*    corresponding box proposals layer later.
Targets := ['cls_target', 'cls_weight', 'box_target', 'box_weight', \
            'num_fg_instances']
create_dl_layer_box_targets (DLLayerAnchors, DLLayerGTBoxes, [], Targets, \
                             'anchors', Targets, NumClasses, \
                             ['inside_center_weight', \
                             'inside_dimension_weight'], [10.0, 5.0], \
                             DLLayerClassTarget, DLLayerClassWeight, \
                             DLLayerBoxTarget, DLLayerBoxWeight, \
                             DLLayerNumFgInstances, _, _)
*
* We use a focal loss for the classification predictions.
create_dl_layer_loss_focal (DLLayerClsLogits, DLLayerClassTarget, \
                            DLLayerClassWeight, DLLayerNumFgInstances, \
                            'loss_cls', 1.0, 2.0, 0.25, \
                            'sigmoid_focal_binary', [], [], DLLayerLossCls)
* We use an L1-loss for the box deltas.
create_dl_layer_loss_huber (DLLayerBoxDeltaPredictions, DLLayerBoxTarget, \
  DLLayerBoxWeight, [], 'loss_box', 1.0, 0.0, [], [], DLLayerLossBox)
*
* Apply sigmoid to class-predictions and compute box outputs.
* --> alternatively, we could directly apply the prediction and set the
*     focal loss mode to 'focal_binary' instead of 'sigmoid_focal_binary'.
create_dl_layer_activation (DLLayerClsLogits, 'cls_probs', 'sigmoid', \
                            [], [], DLLayerClsProbs)
create_dl_layer_box_proposals (DLLayerClsProbs, DLLayerBoxDeltaPredictions, \
                               DLLayerAnchors, DLLayerInputImage, \
                               'anchors', ['inside_center_weight', \
                               'inside_dimension_weight'], [10.0, 5.0], \
                               DLLayerBoxProposals)
*
* Create the model.
OutputLayers := [DLLayerLossCls, DLLayerLossBox, DLLayerBoxProposals]
create_dl_model (OutputLayers, DLModelHandle)
*
* Prepare the model for using it as a detection model.
set_dl_model_param (DLModelHandle, 'type', 'detection')
ClassIDs := [2]
set_dl_model_param (DLModelHandle, 'class_ids', ClassIDs)
set_dl_model_param (DLModelHandle, 'max_overlap', 0.1)
*
* Create a sample.
create_dict (DLSample)
gen_image_const (Image, 'real', 224, 224)
gen_circle (Circle, [50., 100.], [50., 150.], [20., 20.])
overpaint_region (Image, Circle, [255], 'fill')
compose3 (Image, Image, Image, Image)
set_dict_object (Image, DLSample, 'image')
smallest_rectangle1 (Circle, Row1, Col1, Row2, Col2)
set_dict_tuple (DLSample, 'bbox_row1', Row1)
set_dict_tuple (DLSample, 'bbox_row2', Row2)
set_dict_tuple (DLSample, 'bbox_col1', Col1)
set_dict_tuple (DLSample, 'bbox_col2', Col2)
set_dict_tuple (DLSample, 'bbox_label_id', [2,2])
*
* Train the model for some iterations (heavy overfitting).
set_dl_model_param (DLModelHandle, 'learning_rate', 0.0001)
Iteration := 0
TotalLoss := 1e6
LossCls := 1e6
LossBox := 1e6
dev_inspect_ctrl ([Iteration, TotalLoss, LossCls, LossBox])
while (TotalLoss > 0.2 and Iteration < 3000)
  train_dl_model_batch (DLModelHandle, DLSample, DLResult)
  get_dict_tuple (DLResult, 'loss_cls', LossCls)
  get_dict_tuple (DLResult, 'loss_box', LossBox)
  get_dict_tuple (DLResult, 'total_loss', TotalLoss)
  Iteration := Iteration + 1
endwhile
dev_close_inspect_ctrl ([Iteration, TotalLoss, LossCls, LossBox])
*
* Apply the detection model.
apply_dl_model (DLModelHandle, DLSample, [], DLResult)
*
* Display ground truth and result.
create_dict (DLDatasetInfo)
set_dict_tuple (DLDatasetInfo, 'class_ids', ClassIDs)
set_dict_tuple (DLDatasetInfo, 'class_names', ['circle'])
create_dict (WindowHandleDict)
dev_display_dl_data (DLSample, DLResult, DLDatasetInfo, \
                    ['image', 'bbox_ground_truth', 'bbox_result'], [], \
                    WindowHandleDict)
stop ()
dev_close_window_dict (WindowHandleDict)
```

## See also

`create_dl_layer_box_targets`,
`create_dl_layer_roi_pooling`,
`create_dl_layer_anchors`

## References

Tsung-Yi Lin, Piotr Dollàr, Ross B. Girshick, Kaiming He,
Bharath Hariharan, and Serge J. Belongie,
"Feature Pyramid Networks for Object Detection,"
2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR),
Honolulu, HI, USA, 2017, pp. 936--944,
doi: 10.1109/CVPR.2017.106.,
  
Navaneeth Bodla, Bharat Singh, Rama Chellappa, and Larry S. Davis,
SSoft-NMS - Improving Object Detection with One Line of Code,"
2017 IEEE International Conference on Computer Vision (ICCV),
Venice, Italy, 2017, pp. 5562--5570,
doi: 10.1109/ICCV.2017.593.

## Module

Deep Learning Professional
