# CreateDlLayerBoxTargets (Operator)

## Name

`CreateDlLayerBoxTargets` — Create a layer for generating box targets.

## Signature

`static void HOperatorSet.CreateDlLayerBoxTargets(HTuple DLLayerBoxProposal, HTuple DLLayerGTBox, HTuple DLLayerGTMask, HTuple layerNames, HTuple inputMode, HTuple outputModes, HTuple numClasses, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerBoxTargetsClsTarget, out HTuple DLLayerBoxTargetsClsWeight, out HTuple DLLayerBoxTargetsBoxTarget, out HTuple DLLayerBoxTargetsBoxWeight, out HTuple DLLayerBoxTargetsNumFgInstances, out HTuple DLLayerBoxTargetsAssignedIdxs, out HTuple DLLayerBoxTargetsMaskWeight)`

`static HDlLayer[] HDlLayer.CreateDlLayerBoxTargets(HDlLayer[] DLLayerBoxProposal, HDlLayer DLLayerGTBox, HDlLayer DLLayerGTMask, HTuple layerNames, string inputMode, HTuple outputModes, int numClasses, HTuple genParamName, HTuple genParamValue, out HDlLayer[] DLLayerBoxTargetsClsWeight, out HDlLayer[] DLLayerBoxTargetsBoxTarget, out HDlLayer[] DLLayerBoxTargetsBoxWeight, out HDlLayer DLLayerBoxTargetsNumFgInstances, out HDlLayer DLLayerBoxTargetsAssignedIdxs, out HDlLayer DLLayerBoxTargetsMaskWeight)`

`HDlLayer HDlLayer.CreateDlLayerBoxTargets(HDlLayer DLLayerGTBox, HDlLayer DLLayerGTMask, string layerNames, string inputMode, HTuple outputModes, int numClasses, string genParamName, string genParamValue, out HDlLayer DLLayerBoxTargetsClsWeight, out HDlLayer DLLayerBoxTargetsBoxTarget, out HDlLayer DLLayerBoxTargetsBoxWeight, out HDlLayer DLLayerBoxTargetsNumFgInstances, out HDlLayer DLLayerBoxTargetsAssignedIdxs, out HDlLayer DLLayerBoxTargetsMaskWeight)`

## Description

The operator `CreateDlLayerBoxTargets` creates layers for generating
box targets to be used in a box classification or box regression loss
and returns the corresponding layer handles, see below.

This layer expects several feeding input layers:

- *`DLLayerBoxProposal`*: Containing the boxes for which the
  targets should be computed.
- *`DLLayerGTBox`*: Containing the ground truth boxes for all
  images within this batch.
- *`DLLayerGTMask`* (optional): Containing the ground truth
  masks for all images within this batch.

  This input is necessary if the model also predicts instance masks (cf.
  *`outputModes`* *"mask_weight"*). Otherwise, if instance
  masks are not of interest, it can be set to an empty tuple.

Depending on the *`outputModes`*, different output layers are derived
from *`DLLayerBoxProposal`* and for
each of them a name shall be given in *`layerNames`*. Note that if
creating a model using [`CreateDlModel`](create_dl_model.md) each layer of the created
network must have a unique name.

The length of *`layerNames`* has to be the length of
*`outputModes`* times the length of *`DLLayerBoxProposal`*.
Layers that apply to all levels and are therefore not given for every level
in particular (see the respective entry in the description of
*`outputModes`*) are excepted from the multiplication and added on
individually.
*`layerNames`* should be given in the order corresponding to the
output layers, thus *`DLLayerBoxTargetsClsTarget`*,
*`DLLayerBoxTargetsClsWeight`*,
*`DLLayerBoxTargetsBoxTarget`*,
*`DLLayerBoxTargetsBoxWeight`*,
*`DLLayerBoxTargetsNumFgInstances`*,
*`DLLayerBoxTargetsAssignedIdxs`*,
*`DLLayerBoxTargetsMaskWeight`*.

*Example:* for two levels (2,3) and *`outputModes`* =
*["cls_target", "cls_weight", "num_fg_instances"]*:
*["cls_t_l2", "cls_t_l3", "cls_w_l2", "cls_w_l3", "num_fg_instances"]*.

### Determining the expected input

The parameter *`inputMode`* determines the type of inputs expected in
*`DLLayerBoxProposal`*.
The following values are possible:

- ***"anchors"*:** —

  The input boxes in *`DLLayerBoxProposal`*
  shall be anchors, e.g., from an anchor layer as created by
  [`CreateDlLayerAnchors`](create_dl_layer_anchors.md). Anchors from multiple feature maps
  might be given in *`DLLayerBoxProposal`*.
- ***"box_proposals"*:** —

  The input boxes in
  *`DLLayerBoxProposal`* shall be box proposals, e.g., from a box
  proposals layer as created by [`CreateDlLayerBoxProposals`](create_dl_layer_box_proposals.md).

### Determining the output to be computed

Depending on *`outputModes`* the following loss targets are computed:

- ***"cls_target"*:** —

  The target class for each of the input boxes.
  A diagram that shows the rules for assigning the input boxes to the
  ground truth boxes or to the background is shown in the figure.

  ![figure](../assets/3e9101a72ba842c4.svg)

  Assignment rules for target calculations: Generally, the target is set
  to the class label of a ground truth box (foreground) if the IoU with
  the ground truth box is above *"fg_pos_thresh"* or if the IoU is
  above *"fg_neg_thresh"* and there is no other box with a higher
  IoU. It is set to *0* (background) if the IoU
  with all ground truth boxes is below *"fg_neg_thresh"* and to
  *-1* (ignore) if the IoU is above *"fg_neg_thresh"* and
  there is no other box with a higher IoU.
  However, if *"set_weak_boxes_to_bg"*
  is set to *"false"*, any box will also be assigned to the
  corresponding ground truth box as long as it achieves the highest IoU
  with the respective ground truth box and this IoU is larger than zero.

  The class targets depend on the *`inputMode`*:
  - *"anchors"*: The class targets are given one-hot encoded
    suitable for a focal loss-layer ([`CreateDlLayerLossFocal`](create_dl_layer_loss_focal.md)).
  - *"box_proposals"*: The class targets are given as class index
    suitable for a softmax- followed by a cross entropy layer
    ([`CreateDlLayerSoftmax`](create_dl_layer_softmax.md),
    [`CreateDlLayerLossCrossEntropy`](create_dl_layer_loss_cross_entropy.md)).
- ***"cls_weight"*:** —

  The class loss weight for each of the input
  boxes. Class weights have the same shape as class targets such that they
  can be used as feeding layers for the class loss together.
  The class weights are set depending on the class targets (see
  *"cls_target"* above). For foreground and background boxes, the
  weight is set to *1.0*, while for ignore boxes the weight is set to
  *0.0*, such that these boxes are not considered in the loss
  calculation.
  If *`inputMode`* is *"box_proposals"*, the weights for all
  boxes with zero area are set to *0*.
- ***"box_target"*:** —

  For all boxes that are assigned to the
  foreground (see *"cls_target"* above) the box delta targets are
  calculated as coordinate differences to the assigned ground truth boxes
  such that they can be used as feeding inputs to a following loss
  layer, e.g., a Huber loss layer ([`CreateDlLayerLossHuber`](create_dl_layer_loss_huber.md)).
  For background or ignore-boxes the targets are set to *0*.
  The box delta targets depend on the *"instance_type"*:

  - *"rectangle1"*:
    The box delta targets ($\text{r , c, w , h}$)
    are calculated as follows:
    $$t_r = \, i_x(p_r - g t_r)/g t_h t_c = \, i_x(p_c - g t_c)/g t_w t_w = \, i_d \, log(p_w / g t_w) t_h = \, i_d \, log(p_h / g t_h)$$ ![figure](../assets/539340f1e5ae249c.svg)
    where $\text{p}$ are the input box parameters and $\text{gt}$ are the
    ground truth box parameters.
  - *"rectangle2"*:
    The box delta targets ($r,c,p,l1,l2$)
    are calculated as follows:
    $$t_r = \,i_x^2(p_r - g t_r)/(g t_{l1} + g t_{l2}) t_c = \,i_x^2(p_c - g t_c)/(g t_{l1} + g t_{l2}) t_p = \,i_p((g t_p - p_p) + dt) t_{l1} = \,i_d \log(p_{l1}/g t_{l1}) t_{l2} = \,i_d \log(p_{l2}/g t_{l2})$$ ![figure](../assets/736118394eab356a.svg)
    where $p$ are the input box parameters and $gt$ are the
    ground truth box parameters, ($i_{x},i_{d},i_{p}$)
    are the inside weights given by *"inside_center_weight"*,
    *"inside_dimension_weight"*, and *"inside_angle_weight"*.
    $dt$ corrects the angle into the appropriate interval, which
    depends on whether the direction of the object within the box is
    considered. This behavior is determined by the parameter
    *"ignore_direction"*, see [`GetDlModelParam`](get_dl_model_param.md) and below.
    If *"ignore_direction"* is *"false"*, the boxes have
    orientations in the range $(-\pi,\pi]$, else in the range
    $(-\pi/2,\pi/2]$.
- ***"box_weight"*:** —

  For all boxes that are assigned to the
  foreground (see *"cls_target"* above) the weights are set to
  *"center_weight"* for $(r,c)$,
  *"dimension_weight"* for $(w,h)$ or
  $(l1,l2)$ depending on *"instance_type"*, and
  *"angle_weight"* for $p$, else to 0.0.
- ***"num_fg_instances"*:** —

  This output contains a scalar with
  the number of foreground boxes (see *"cls_target"* above)
  of the whole input batch. It can be used, e.g., as a normalization value
  within a consecutive focal loss layer
  ([`CreateDlLayerLossFocal`](create_dl_layer_loss_focal.md)).
  Note, that the same output value is given for all items within
  the batch. Note also, that also for multiple anchor levels there will
  be only one output layer *`DLLayerBoxTargetsNumFgInstances`*.
- ***"assigned_idxs"*:** —

  This output contains the index of the
  assigned ground truth box for all foreground boxes (see
  *"cls_target"* above). For all other boxes the output value is set
  to -1. This mode is only available for *`inputMode`*
  *"box_proposals"*. The output can be used to calculate mask
  targets using a ROI pooling layer ([`CreateDlLayerRoiPooling`](create_dl_layer_roi_pooling.md))
  on the ground truth masks.
- ***"mask_weight"*:** —

  This output contains the weights for
  a consecutive mask prediction loss (see e.g.,
  [`CreateDlLayerLossDistance`](create_dl_layer_loss_distance.md)). Each channel is of dimensions
  *"mask_width"* times *"mask_height"*. In each channel
  where the corresponding assigned index (see *"assigned_idxs"*
  above) is larger or equal to *0.0* all values are set to
  *1.0*, else to *0.0*. The mask weight is also set to
  *0.0* if a ground truth box instance does
  not contain a ground truth mask. This enables to train with datasets
  where not all boxes are also annotated with instance masks.

Duplicate entries in *`outputModes`* are ignored. If an empty list
is given, all available options are switched on.

### Further specifications

*`numClasses`* shall be set to the number of classes contained in the
dataset (excluding background), or to *1*, if the class targets for
output mode *"cls_target"* should be computed class-agnostically.
For example, this is the case in a region proposal network, that builds the
first stage of the Faster R-CNN architecture (see references below). In the
latter case, all ground truth boxes are interpreted as belonging to a single
category 'object'.

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"angle_weight"*:** —

  Outside weight multiplier for box-angles
  (phi) used in output *"box_weight"*.

  Restriction:
   Only applicable for *"instance_type"*
  *"rectangle2"*.

  Default:
   *1.0*.
- ***"box_cls_specific"*:** —

  Determines whether the *"box_target"* and *"box_weight"*
  outputs are class specific (*"true"*) or not (*"false"*).
  If so, the targets and weights are only set within the `depth` index
  that corresponds to the target class.

  Restriction:
   Only applicable to *`inputMode`*
  *"box_proposals"* and if *`outputModes`*
  *"box_target"* is used.

  Default:
   *"false"*.
- ***"center_weight"*:** —

  Outside weight multiplier for box-center
  coordinates $(r,c)$ used in output *"box_weight"*.

  Default:
   *1.0*.
- ***"dimension_weight"*:** —

  Outside weight multiplier for
  box dimensions $(w,h)$ for *"instance_type"*
  *"rectangle1"* and $(l1,l2)$ for
  *"instance_type"* *"rectangle2"* used in output
  *"box_weight"*.

  Default:
   *1.0*.
- ***"fg_neg_thresh"*:** —

  Foreground negative threshold. Anchors
  with IoU smaller than this threshold to any ground truth box are assigned
  to the background. If you still want an anchor to be assigned to a
  foreground class, you can use *"set_weak_boxes_to_bg"* (see below).
  See detailed explanations in the scheme above.

  Default:
   *0.4*.
- ***"fg_pos_thresh"*:** —

  Foreground positive threshold. Anchors
  with IoU larger than or equal to this threshold to any ground truth box are
  assigned to the foreground. See detailed explanations in the scheme above.

  Default:
   *0.5*.
- ***"ignore_direction"*:** —

  Determines whether the boxes of type
  *"rectangle2"* respect the direction of the object within the box:

  - *"true"*: Orientation of *"rectangle2"* boxes is in the
    range $(-\pi/2,\pi/2]$.
  - *"false"*: Orientation of *"rectangle2"* boxes is in the
    range $(-\pi,\pi]$

  Restriction:
   Only applicable for *"instance_type"*
  *"rectangle2"*.

  Default:
   *"false"*.
- ***"inside_angle_weight"*:** —

  Inside weight multiplier for
  box angles (phi) used in output *"box_target"*.

  Restriction:
   Only applicable for *"instance_type"*
  *"rectangle2"*.

  Default:
   *1.0*.
- ***"inside_center_weight"*:** —

  Inside weight multiplier for
  box-center coordinates $(r,c)$ used in output *"box_target"*.

  Default:
   *1.0*.
- ***"inside_dimension_weight"*:** —

  Inside weight multiplier for
  box dimensions $(w,h)$ for *"instance_type"*
  *"rectangle1"* and (l1, l2) for *"instance_type"*
  *"rectangle2"* used in output *"box_target"*.

  Default:
   *1.0*.
- ***"instance_type"*:** —

  Instance type of the boxes. Possible values:

  - *"rectangle1"*: axis-aligned rectangles.
  - *"rectangle2"*: oriented rectangles.

  Default:
   *"rectangle1"*.
- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*
- ***"mask_cls_specific"*:** —

  Determines whether *"mask_weight"* output is given class
  specifically. Thus, if set to *"true"*, the
  *"mask_weight"* output is given such that only
  the weight in the target class `depth` index is set to *1*.

  Restriction:
   Only applicable if the *`outputModes`*
  *"mask_weight"* is used.

  Default:
   *"false"*.
- ***"mask_height"*:** —

  Output height of the mask weight layer for
  output mode *"mask_weight"*.

  Default:
   *1*.
- ***"mask_width"*:** —

  Output width of the mask weight layer for
  output mode *"mask_weight"*.

  Default:
   *1*.
- ***"max_num_samples"*:** —

  Maximum number of randomly selected targets
  with weights set to a value larger than *0* per batch item.

  Restriction:
   Only for *`inputMode`*
  *"box_proposals"*.

  Default:
   *256*.
- ***"ratio_num_fg"*:** —

  Target ratio of foreground versus background
  boxes for random box sampling. The maximum number of foreground
  proposals with *"cls_weight"* set to *1* is
  *"max_num_samples"* times *"ratio_num_fg"*. The remaining
  up to *"max_num_samples"* are background proposals if so many are
  available.

  Restriction:
   Only for *`inputMode`*
  *"box_proposals"*.

  Default:
   *0.25*.
- ***"set_weak_boxes_to_bg"*:** —

  Determines whether predicted boxes
  need to achieve an IoU larger than *"fg_neg_thresh"* in order to
  be potentially assigned to a ground truth box, or if they are automatically
  assigned to the background (see scheme above):

  - *"true"*: Anchors with an IoU below
    *"fg_neg_thresh"* are assigned to the background automatically.
  - *"false"*: At least the predicted box with the highest IoU
    is set to foreground and thus as a positive example, independent of the
    IoU value.

  Default:
   *"false"*.

Certain parameters of layers created using this operator
`CreateDlLayerBoxTargets` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md).
Note, the operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and
[`GetDlModelLayerParam`](get_dl_model_layer_param.md) require a model created by
[`CreateDlModel`](create_dl_model.md).

| Layer Internal Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`DLLayerBoxProposal`*, *`DLLayerGTBox`*, *`DLLayerGTMask`*) |  | `x` |
| *"name"* (*`layerNames`*) | `x` | `x` |
| *"output_layer"* (*`DLLayerBoxTargetsClsTarget`*, *`DLLayerBoxTargetsClsWeight`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"angle_weight"* | `x` | `x` |
| *"box_cls_specific"* |  | `x` |
| *"center_weight"* | `x` | `x` |
| *"dimension_weight"* |  | `x` |
| *"fg_neg_thresh"* | `x` | `x` |
| *"fg_pos_thresh"* | `x` | `x` |
| *"ignore_direction"* |  | `x` |
| *"input_mode"* (*`inputMode`*) |  | `x` |
| *"inside_angle_weight"* |  | `x` |
| *"inside_center_weight"* |  | `x` |
| *"inside_dimension_weight"* |  | `x` |
| *"is_inference_output"* | `x` | `x` |
| *"instance_type"* |  | `x` |
| *"mask_cls_specific"* | `x` | `x` |
| *"mask_height"* | `x` | `x` |
| *"mask_width"* | `x` | `x` |
| *"max_num_samples"* | `x` | `x` |
| *"num_classes"* (*`numClasses`*) | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"ratio_num_fg"* | `x` | `x` |
| *"set_weak_boxes_to_bg"* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerBoxProposal`** (input_control)  dl_layer(-array) `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Feeding layers with box proposals or
anchors for which targets should be
computed.

**`DLLayerGTBox`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Feeding layer with ground truth boxes.

**`DLLayerGTMask`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Feeding layer with ground truth masks
(optional).

**`layerNames`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the output layers.

**`inputMode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode of the input boxes.

Default:
"box_proposals"

List of values:
"anchors", "box_proposals"

**`outputModes`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Modes that should be computed as outputs.

List of values:
"assigned_idxs", "box_target", "box_weight", "cls_target", "cls_weight", "mask_weight", "num_fg_instances"

**`numClasses`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Number of classes.

Restriction:
`NumClasses > 0`

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

List of values:
"angle_weight", "box_cls_specific", "center_weight", "dimension_weight", "fg_neg_thresh", "fg_pos_thresh", "ignore_direction", "inside_angle_weight", "inside_center_weight", "inside_dimension_weight", "instance_type", "is_inference_output", "mask_cls_specific", "mask_height", "mask_width", "max_num_samples", "ratio_num_fg", "set_weak_boxes_to_bg"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Generic input parameter values.

Default:
[]

Suggested values:
"rectangle1", "rectangle2", "true", "false", 0.4, 0.5, 256, 0.25, 1.0, 7, 14

**`DLLayerBoxTargetsClsTarget`** (output_control)  dl_layer(-array) `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Class target layer.

**`DLLayerBoxTargetsClsWeight`** (output_control)  dl_layer(-array) `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Class weight layer.

**`DLLayerBoxTargetsBoxTarget`** (output_control)  dl_layer(-array) `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Box target layer.

**`DLLayerBoxTargetsBoxWeight`** (output_control)  dl_layer(-array) `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Box weight layer.

**`DLLayerBoxTargetsNumFgInstances`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

NumFgInstances layer.

**`DLLayerBoxTargetsAssignedIdxs`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Assigned indices layer.

**`DLLayerBoxTargetsMaskWeight`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Mask weight layer.

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
                                     'from_class_id', \
                                     [], [], DLLayerClassIdConversion)
* Concatenate all box coordinates.
create_dl_layer_concat ([DLLayerInputRow1, DLLayerInputCol1, \
                        DLLayerInputRow2, DLLayerInputCol2, \
                        DLLayerClassIdConversion], 'gt_boxes', 'height', \
                        [], [], DLLayerGTBoxes)
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
                            DLLayerBoxWeight, [], 'loss_box', 1.0, 0.0, \
                            [], [], DLLayerLossBox)
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
                    ['image', 'bbox_ground_truth', 'bbox_result'], \
                    [], WindowHandleDict)
stop ()
dev_close_window_dict (WindowHandleDict)
```

## Possible Predecessors

`CreateDlLayerConvolution`,
`CreateDlLayerAnchors`,
`CreateDlLayerBoxProposals`

## Possible Successors

`CreateDlLayerBoxProposals`,
`CreateDlLayerLossFocal`,
`CreateDlLayerLossHuber`

## See also

`CreateDlLayerBoxProposals`,
`CreateDlLayerLossFocal`,
`CreateDlLayerLossHuber`

## References

Shaoqing Ren, Kaiming He, Ross B. Girshick, and Jian Sun,
"Faster R-CNN: Towards Real-Time Object Detection with Region Proposal
Networks,"
IEEE Transactions on Pattern Analysis and Machine Intelligence,
Volume 39, Number 6, pp. 1137--1149, 2017,
doi: 10.1109/TPAMI.2016.2577031.

## Module

Deep Learning Professional
