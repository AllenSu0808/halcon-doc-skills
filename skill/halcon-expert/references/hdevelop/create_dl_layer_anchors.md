# create_dl_layer_anchors (Operator)

## Name

`create_dl_layer_anchors` — Create a layer for generating anchor boxes.

## Signature

`create_dl_layer_anchors( : : DLLayerInput, DLLayerInputImage, LayerName, AspectRatios, NumSubscales, Angles, GenParamName, GenParamValue : DLLayerAnchors)`

## Description

The operator `create_dl_layer_anchors` creates a layer for generating
anchor boxes whose handle is returned in *`DLLayerAnchors`*.
The parameter *`DLLayerInput`* determines the feeding input layer which
is used to determine the width and height of the spatial grid,
on which the anchors are generated. For example, this could be the last or
any intermediate feature layer of a CNN.
Usually, when using anchors, the same layer is feeding a classification
and box regression branch that are used to determine the class of each
anchor and to refine its shape
(see also [`create_dl_layer_box_proposals`](create_dl_layer_box_proposals.md) and
[`create_dl_layer_box_targets`](create_dl_layer_box_targets.md)).

The parameter *`DLLayerInputImage`* determines the feeding input layer
which is used to determine the scaling factor of the grid and the
size of the anchors. Usually, this is the network input image layer.
For instance, if the width and height of *`DLLayerInput`*
is half the width and height of the *`DLLayerInputImage`*, the anchor
grid and anchor size are scaled by a factor of two.
The ratio between the size (width and height) of *`DLLayerInputImage`*
and *`DLLayerInput`* must always be a power of two,
for example 1, 2, 4, 8, 16, and so on.

The parameter *`LayerName`* sets an individual layer name. Note that if
creating a model using [`create_dl_model`](create_dl_model.md) each layer of the created
network must have a unique name.

The parameter *`AspectRatios`* determines the aspect ratios of the
anchor boxes (height to width for instance type *'rectangle1'* and
`length1` to `length2` for instance type
*'rectangle2'* respectively).

The parameter *`NumSubscales`* determines the number of different scales
at which anchor boxes are generated for each aspect ratio. To determine the
anchor scales the base scale of the anchor boxes which is given via the
generic parameter *'scale'* is multiplied with each subscale.
The subscales are computed as follows
$$subscale_i = 2^i/NumSubscales$$ ![figure](../assets/87c449abe45e6ef3.svg)
where
$i\in[0,\texttt{NumSubscales}-1]$.

The parameter *`Angles`* determines the orientation of the anchor boxes
in case of instance type *'rectangle2'*. The values must be given in
radian. If *`Angles`* is an empty tuple,
the instance type is implicitly set to *'rectangle1'*, if not
specified otherwise via the generic parameter *'instance_type'*.
For each point in the anchor grid and each combination of aspect ratio,
subscale and angle an anchor box is generated to cover the
input image uniformly.
Typically, the output layer *`DLLayerAnchors`* is a feeding input layer
to a box target and a box proposal layer to build a detection model.
Refer to chapter [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md) for further
information on anchors and the *'instance_type'*.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'instance_type'*:** —

  Instance type of anchors. Possible values:

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
- ***'scale'*:** —

  Base scale of the anchor boxes. See the description above for more
  information.

  Default:
   *4.0*

Certain parameters of layers created using this operator
`create_dl_layer_anchors` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note, the
operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and [`get_dl_model_layer_param`](get_dl_model_layer_param.md)
require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Internal Parameters | `set` | `get` |
| --- | --- | --- |
| *'anchor_angles'* (*`Angles`*) |  | `x` |
| *'anchor_aspect_ratios'* (*`AspectRatios`*) |  | `x` |
| *'anchor_num_subscales'* (*`NumSubscales`*) |  | `x` |
| *'input_layer'* (*`DLLayerInput`*) |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerAnchors`*) |  | `x` |
| *'shape'* |  | `x` |
| *'type'* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'instance_type'* |  | `x` |
| *'is_inference_output'* | `x` | `x` |
| *'num_trainable_params'* |  | `x` |
| *'scale'* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerInput`** (input_control)  dl_layer `→`  (handle)

Feeding layer to determine anchor grid size.

**`DLLayerInputImage`** (input_control)  dl_layer `→`  (handle)

Feeding layer to determine the grid
scale and anchor sizes.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`AspectRatios`** (input_control)  number-array `→`  (real / integer)

Anchor aspect ratios.

Default:
[0.5,1.0,2.0]

**`NumSubscales`** (input_control)  number `→`  (integer)

Number of anchor subscales.

Default:
3

Restriction:
`NumSubscales > 0`

**`Angles`** (input_control)  number-array `→`  (real / integer)

Anchor orientations.

Default:
[]

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'instance_type', 'is_inference_output', 'scale'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Generic input parameter values.

Default:
[]

Suggested values:
'rectangle1', 'rectangle2', 'true', 'false'

**`DLLayerAnchors`** (output_control)  dl_layer `→`  (handle)

Anchors layer.

## Example (HDevelop)

```
* Minimal example for the usage of layers
*  - create_dl_layer_anchors
*  - create_dl_layer_box_proposals
*  - create_dl_layer_box_targets
* for creating a model to perform object detection.
*
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
* Concatenate all box coordinates.
create_dl_layer_concat ([DLLayerInputRow1, DLLayerInputCol1, \
                        DLLayerInputRow2, DLLayerInputCol2, \
                        DLLayerInputLabelID], 'gt_boxes', \
                        'height', [], [], DLLayerGTBoxes)
*
* Perform some operations on the input image to extract features.
create_dl_layer_convolution (DLLayerInputImage, 'conv', 3, 1, 1, 32, 1, \
                             'half_kernel_size', 'relu', [], [], \
                             DLLayerConvolution)
create_dl_layer_pooling (DLLayerConvolution, 'pool', 2, 2, 'none', \
                         'maximum', [], [], DLLayerPooling)
*
* Create the anchor boxes.
create_dl_layer_anchors (DLLayerPooling, DLLayerInputImage, 'anchor', \
                         [0.5,1.0,2.0], 3, [], [], [], DLLayerAnchors)
*
* Generate the class and box regression targets for the anchors
* according to the ground truth boxes.
Targets := ['cls_target', 'box_target']
NumClasses := 3
create_dl_layer_box_targets (DLLayerAnchors, DLLayerGTBoxes, [], \
                             Targets, 'anchors', Targets, NumClasses, \
                             [], [], DLLayerClassTarget, _, \
                             DLLayerBoxTarget, _, _, _, _)
*
* For this example, we treat the targets as predictions and
* apply them directly to the anchors to get the ground truth
* boxes as output.
create_dl_layer_box_proposals (DLLayerClassTarget, DLLayerBoxTarget, \
                               DLLayerAnchors, DLLayerInputImage, \
                               'box_proposals', [], [], \
                               DLLayerBoxProposals)
*
* Create the model.
OutputLayers := DLLayerBoxProposals
create_dl_model (OutputLayers, DLModelHandle)
*
* Prepare the model for using it as a detection model.
set_dl_model_param (DLModelHandle, 'type', 'detection')
ClassIDs := [0,1,2]
set_dl_model_param (DLModelHandle, 'class_ids', ClassIDs)
*
* Create a sample.
create_dict (DLSample)
gen_image_const (Image, 'real', 224, 224)
gen_circle (Circle, [50., 100.], [50., 120.], [20., 30.])
overpaint_region (Image, Circle, 255, 'fill')
compose3 (Image, Image, Image, Image)
set_dict_object (Image, DLSample, 'image')
smallest_rectangle1 (Circle, Row1, Col1, Row2, Col2)
set_dict_tuple (DLSample, 'bbox_row1', Row1)
set_dict_tuple (DLSample, 'bbox_row2', Row2)
set_dict_tuple (DLSample, 'bbox_col1', Col1)
set_dict_tuple (DLSample, 'bbox_col2', Col2)
set_dict_tuple (DLSample, 'bbox_label_id', [1,2])
*
* Apply the detection model.
apply_dl_model (DLModelHandle, DLSample, [], DLResult)
*
* Display ground truth and result.
create_dict (DLDatasetInfo)
set_dict_tuple (DLDatasetInfo, 'class_ids', ClassIDs)
set_dict_tuple (DLDatasetInfo, 'class_names', \
                ['class_0', 'class_1', 'class_2'])
create_dict (WindowHandleDict)
dev_display_dl_data (DLSample, DLResult, DLDatasetInfo, \
                     ['image', 'bbox_ground_truth', 'bbox_result'], \
                     [], WindowHandleDict)
stop ()
dev_close_window_dict (WindowHandleDict)
```

## Possible Successors

`create_dl_layer_box_targets`,
`create_dl_layer_box_proposals`

## Module

Deep Learning Professional
