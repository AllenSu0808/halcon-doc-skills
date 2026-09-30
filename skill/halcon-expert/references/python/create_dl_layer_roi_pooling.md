# create_dl_layer_roi_pooling (Operator)

## Name

`create_dl_layer_roi_pooling` — Create an ROI pooling layer.

## Signature

`def create_dl_layer_roi_pooling(dllayer_input_image: HHandle, dllayer_ro_i: HHandle, dllayer_feature: MaybeSequence[HHandle], dllayer_instance_index: HHandle, layer_name: str, type: str, grid_size: Sequence[int], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_roi_pooling` creates a region of interest
(ROI) pooling layer whose handle is returned in *`dllayer_ro_ipooling`*.
Features within the given ROIs are pooled to a fixed output spatial dimension
for further processing. The output spatial dimension is given by
*`grid_size`*.

This layer expects several feeding input layers:

- *`dllayer_input_image`*: Determines the feeding input layer
  which should contain the network input image.
  It is used to infer the scales (in terms of width and height) of the feature
  maps with respect to the input image dimension.
- *`dllayer_ro_i`*: Determines the feeding input layer
  containing the coordinates of the ROIs. The ROI-coordinates should be given
  with respect to the input image and are taken as pixel centered coordinates
  (see [Transformations / 2D Transformations](toc_transformations_2dtransformations.md)).
  The shape of a layer is of form
  [`width`, `height`, `depth`, `batch_size`],
  where the fourth value for the batch size is alterable.
  For this layer this leads to [1, *NBP* + 2, *MNR*,
  *"batch_size"*] where *MNR* is the maximum number of ROIs
  for one image and *NBP* is the number of box parameters.
  *NBP* depends on the *"instance_type"*: there are
  4 parameters for *"rectangle1"* (`row1`, `column1`,
  `row2`, `column2`), and
  5 parameters for *"rectangle2"* (`row`, `column`,
  `phi`, `length1`, `length2`) respectively.
  The second dimension contains next to the *NBP* rectangle
  parameters two further values: One for the class and one for the
  score of each ROI. An ROI is ignored if its class value is negative.
  If fewer than *MNR* ROIs are available, the coordinates should all
  be set to zero.
  This feeding layer typically is the output of a box proposal layer, see
  [`create_dl_layer_box_proposals`](create_dl_layer_box_proposals.md).
- *`dllayer_feature`*: Determines the feeding input layer
  containing one or more feature maps to be pooled from.
  If more than one feature map is given they have to be ordered by
  decreasing spatial dimensions. For example, if a Feature Pyramid Network
  (FPN) is used, that means the layers are ordered by increasing FPN-level.
  Refer to chapter [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md) or the reference
  given below for more detailed information on the FPN and its levels.
- *`dllayer_instance_index`*: Determines the feeding input
  layer containing for each ROI the index of the ground truth instance
  with highest IoU. See [`create_dl_layer_box_targets`](create_dl_layer_box_targets.md) for further
  information. This input layer is only used if the generic parameter
  *"mode"* is set to *"mask_target"*.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The ROI pooling operation works as follows.
A grid is laid over each ROI and the features within each
bin of the grid are pooled. How this is done in detail depends on the
*`type`*:

- ***"roi_pool"*:** —

  Performs a max-pooling, thus the calculated
  grid coordinates are rounded to pixel-precise coordinates.
- ***"roi_align"*:** —

  For each sampling point the value is
  determined by bilinear interpolation of the four neighboring
  pixel-values. The output value for each grid bin is the average of the
  sampling point values.
  The number of uniformly distributed sampling points in each
  output grid bin is determined by *"sampling_ratio"*.

The pooled features can for example be used to predict object
masks within the given ROIs. In this case it may be useful to pool from
a slightly larger ROI to increase the probability that the object is
completely contained in the ROI. With the generic parameters
*"enlarge_box_factor_long"* and *"enlarge_box_factor_short"*
the scaling of the longer and shorter box lengths before pooling can be
controlled.

For multiple feature maps, the ROIs will be distributed over the feature maps
according to their size by the following formula:

$$level = level_0 + \left[ \log\left(\text{scale}/\text{scale}_0 + \varepsilon \right) \right]$$ ![figure](../assets/0dd239128fa1ada7.svg)

where $scale$ is the ROI scale, calculated as square root
of the ROI area.
$level_{0}$ is the canonical FPN level and
$scale_{0}$ is the canonical FPN scale. The canonical
FPN level and scale can be set via the generic parameters
*"fpn_roi_canonical_level"* and
*"fpn_roi_canonical_scale"* respectively.
$\epsilon$ is added for robustness and set to *1e-6*.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"enlarge_box_factor_long"*:** —

  Factor with which the longer
  side of the box is multiplied before pooling.

  Default:
   *1.0*.
- ***"enlarge_box_factor_short"*:** —

  Factor with which the shorter
  side of the box is multiplied before pooling.

  Default:
   *1.0*.
- ***"fpn_roi_canonical_level"*:** —

  FPN-level, the ROIs
  with the canonical scale are assigned to.

  Default:
   *4*.
- ***"fpn_roi_canonical_scale"*:** —

  ROIs with this scale will be
  assigned to the canonical level.

  Default:
   *224*.
- ***"instance_type"*:** —

  Type of RoIs. Possible values:

  - *"rectangle1"*: axis-aligned rectangles.
  - *"rectangle2"*: oriented rectangles.

  Default:
   *"rectangle1"*.
- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*
- ***"mode"*:** —

  Mode of the layer. Possible values:

  - *"feature"*: Feature pooling.
    *`dllayer_input_image`* has to be given and
    *`dllayer_instance_index`* must be empty.
  - *"mask_target"*: Mask target generation.
    *`dllayer_input_image`* must be empty and
    *`dllayer_instance_index`* has to be given.

    With this mode *`dllayer_feature`* can only be a single layer.
    In this case it is no layer containing feature maps but an input
    layer containing the ground truth instance masks with shape
    (*"batch_size"*, *MNI*, *IH*, *IW*), where
    *MNI* is the maximum number of instances in an image, and
    *IH* and *IW* are the network input
    image height and width, respectively.
    Each channel corresponds to one ground truth instance where the mask
    is encoded in binary format. The output of the layer then contains
    the cropped and resized mask targets which can for example be fed to a
    focal loss layer (see [`create_dl_layer_loss_focal`](create_dl_layer_loss_focal.md)) together with
    mask predictions.

  Default:
   *"feature"*.
- ***"num_classes"*:** —

  The number of classes to be predicted
  by the model. This parameter is only available for *"mode"*
  *"mask_target"*.

  Restriction:
   If set to a value greater than 1, the mask
  targets are generated class specifically. This also affects the
  output shape of the layer, i.e., the depth of the mask targets will
  be equal to *"num_classes"*.

  Default:
   *1*.
- ***"sampling_ratio"*:** —

  Number of sampling points distributed
  over the bin height and width in one grid bin. E.g., for
  *"sampling_ratio"* set to two, there are four sampling points in
  each grid bin. If set to *0*, this number is computed
  automatically.

  Default:
   *0*.
- ***"threshold_value"*:** —

  This value sets a threshold between
  zero and one for the outputs.
  Set to *-1* in order to switch
  thresholding off.

  Restriction:
   Only available for *"mode"*
  *"mask_target"* and *`type`* *"roi_align"*.

  Default:
   *0.5*.

Some parameters are not supported by `create_dl_layer_roi_pooling`,
since they are computed internally using the input *`dllayer_feature`*.
These are the following:

- ***"fpn_roi_min_level"*:** —

  Minimum FPN-level used for pooling.

  Restriction:
   Applies only to *"mode"* *"feature"*.

  Default:
   *0*.
- ***"fpn_roi_max_level"*:** —

  Maximum FPN-level used for pooling.

  Restriction:
   Applies only to *"mode"* *"feature"*.

  Default:
   *0*.

Certain parameters of layers created using this operator
`create_dl_layer_roi_pooling` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note, the
operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and [`get_dl_model_layer_param`](get_dl_model_layer_param.md)
require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"grid_size"* (*`grid_size`*) |  | `x` |
| *"input_layer"* (*`dllayer_input_image`*, *`dllayer_ro_i`*, *`dllayer_feature`*, and/or *`dllayer_instance_index`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"output_layer"* (*`dllayer_ro_ipooling`*) |  | `x` |
| *"shape"* |  | `x` |
| *"roi_pooling_type"* (*`type`*) | `x` | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"enlarge_box_factor_long"* | `x` | `x` |
| *"enlarge_box_factor_short"* | `x` | `x` |
| *"fpn_roi_canonical_level"* | `x` | `x` |
| *"fpn_roi_canonical_scale"* | `x` | `x` |
| *"fpn_roi_max_level"* |  | `x` |
| *"fpn_roi_min_level"* |  | `x` |
| *"is_inference_output"* | `x` | `x` |
| *"instance_type"* |  | `x` |
| *"mode"* |  | `x` |
| *"num_classes"* |  | `x` |
| *"num_trainable_params"* |  | `x` |
| *"sampling_ratio"* | `x` | `x` |
| *"threshold_value"* | `x` | `x` |
|  |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dllayer_input_image`** (input_control)  dl_layer `→` HHandle

Feeding layer containing network input image.

Default:
"InputImageLayer"

**`dllayer_ro_i`** (input_control)  dl_layer `→` HHandle

Feeding layer containing ROI coordinates.

Default:
"RoILayer"

**`dllayer_feature`** (input_control)  dl_layer(-array) `→` MaybeSequence[HHandle]

Feeding layers containing the features/ground
truth instance masks to be pooled from.

Default:
"FeatureLayers"

**`dllayer_instance_index`** (input_control)  dl_layer `→` HHandle

Feeding layer containing matched instance indices for
each ROI.

Default:
"InstanceIndexLayer"

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`type`** (input_control)  string `→` str

Type of ROI pooling.

Default:
"roi_pool"

List of values:
"roi_align", "roi_pool"

**`grid_size`** (input_control)  number-array `→` Sequence[int]

Spatial dimensions of the pooling grid, output spatial dimensions.

Default:
[7,7]

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"enlarge_box_factor_long", "enlarge_box_factor_short", "fpn_roi_canonical_level", "fpn_roi_canonical_scale", "instance_type", "is_inference_output", "mode", "num_classes", "sampling_ratio", "threshold_value"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"feature", "mask_target", "rectangle1", "rectangle2", "true", "false", 0.5

**`dllayer_ro_ipooling`** (output_control)  dl_layer `→` HHandle

ROI pooling layer.

## Example (HDevelop)

```
* Example for create_dl_layer_roi_pooling.
* This model can be trained to classify multiple
* predefined RoIs in an image.
*
* Create simple model.
create_dl_layer_input ('image', [224,224,3], [], [], DLGraphNodeInput)
create_dl_layer_input ('gt_boxes', [1, 5, 5], [], [], DLGraphNodeGTBoxes)
create_dl_layer_input ('rois', [1, 6, 5], [], [], DLGraphNodeRoIs)
*
* Apply two convolution layer to extract features of the image.
create_dl_layer_convolution (DLGraphNodeInput, 'conv1', 3, 1, 2, 32, 1, \
                             'half_kernel_size', 'relu', [], [], \
                             DLGraphNodeConvolution)
create_dl_layer_convolution (DLGraphNodeConvolution, 'conv2', 3, 1, 2, 32, \
                             1, 'half_kernel_size', 'relu', [], [], \
                             DLGraphNodeConvolution2)
*
* Apply RoI pooling to pool the features for each RoI.
GridSize := [7,7]
create_dl_layer_roi_pooling (DLGraphNodeInput, DLGraphNodeRoIs, \
                             DLGraphNodeConvolution2, [], 'roi_pool', \
                             'roi_pool', GridSize, [], [], \
                             DLGraphNodeRoIPooling)
*
* Classify the RoIs according to the pooled features.
NumClasses := 3
create_dl_layer_dense (DLGraphNodeRoIPooling, 'fc1', 64, [], [], \
                       DLGraphNodeDense)
create_dl_layer_activation (DLGraphNodeDense, 'relu1', 'relu', [], \
                            [], Relu1)
create_dl_layer_dense (Relu1, 'cls_score', NumClasses + 1, [], [], \
                       DLGraphNodeScore)
create_dl_layer_softmax (DLGraphNodeScore, 'cls_prob', [], [], \
                          DLGraphNodeSoftMax)
*
* Append a cross entropy loss to train the classifier.
TargetOutputModes := ['cls_target', 'cls_weight']
TargetOutputNames := TargetOutputModes
create_dl_layer_box_targets (DLGraphNodeRoIs, DLGraphNodeGTBoxes, [], \
                             TargetOutputNames, 'box_proposals', \
                             TargetOutputModes, NumClasses, [], [], \
                             DLGraphNodeClsTarget, DLGraphNodeClsWeight, \
                             _, _, _, _, _)
create_dl_layer_loss_cross_entropy (DLGraphNodeSoftMax, \
                                    DLGraphNodeClsTarget, \
                                    DLGraphNodeClsWeight, 'cls_loss', \
                                    1.0, [], [], \
                                    DLGraphNodeLossCrossEntropy)
*
* Append a box proposal layer to get a detection-like output.
GenParamNameBoxProposal := ['input_mode', 'apply_box_regression', \
                        'max_overlap', 'max_overlap_class_agnostic']
GenParamValueBoxProposal := ['dense', 'false', 1.0, 1.0]
create_dl_layer_box_proposals (DLGraphNodeSoftMax, [], DLGraphNodeRoIs, \
                               DLGraphNodeInput, 'box_output', \
                               GenParamNameBoxProposal, \
                               GenParamValueBoxProposal, \
                               DLGraphNodeGenerateBoxProposals)
*
* Create the model.
create_dl_model ([DLGraphNodeLossCrossEntropy, \
                 DLGraphNodeGenerateBoxProposals], \
                 DLModelHandle)
set_dl_model_param (DLModelHandle, 'type', 'detection')
ClassIDs := [1:NumClasses]
set_dl_model_param (DLModelHandle, 'class_ids', ClassIDs)
```

## References

Tsung-Yi Lin, Piotr Dollàr, Ross B. Girshick, Kaiming He,
Bharath Hariharan, and Serge J. Belongie,
"Feature Pyramid Networks for Object Detection,"
2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR),
Honolulu, HI, USA, 2017, pp. 936--944,
doi: 10.1109/CVPR.2017.106.

## Module

Deep Learning Professional
