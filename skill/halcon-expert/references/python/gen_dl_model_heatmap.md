# gen_dl_model_heatmap (Operator)

## Name

`gen_dl_model_heatmap` — Infer the sample and generate a heatmap.

## Signature

`def gen_dl_model_heatmap(dlmodel_handle: HHandle, dlsample: MaybeSequence[HHandle], heatmap_method: str, target_classes: int, gen_param: HHandle) -> Sequence[HHandle]`

`def gen_dl_model_heatmap_s(dlmodel_handle: HHandle, dlsample: MaybeSequence[HHandle], heatmap_method: str, target_classes: int, gen_param: HHandle) -> HHandle`

## Description

The operator `gen_dl_model_heatmap` infers the sample given
by *`dlsample`* and generates a heatmap for the class specified by
*`target_classes`*.
*`dlsample`* can be a single dictionary or a tuple of dictionaries for
different samples.
To do so, the operator uses the deep learning model given by
*`dlmodel_handle`*.
The parameter *`heatmap_method`* determines, which method is used
to calculate the heatmap.
The operator returns *`dlresult`* with a result dictionary for every
given sample.
Note, *`dlresult`* will be newly created
and already existing parameters with this name will be overwritten.

A heatmap can be useful to analyze which parts of an image have a strong
influence for the inference into a certain class.
Shape and area of these parts and therewith the heatmaps may vary widely
for differing networks especially if their architectures differ.
There are different methods how a heatmap is calculated.
The following ones can be selected using *`heatmap_method`*:

- ***"grad_cam"*:** —

  Provides region-based heatmap information based on
  Gradient-weighted Class Activation Mapping (Grad-CAM).
  For a more detailed description refer to the referenced paper below.
- ***"guided_grad_cam"*:** —

  Provides pixel-based heatmap information
  based on Guided gradient-weighted Class Activation
  Mapping (Guided Grad-CAM).
  For a more detailed description refer to the referenced paper below.

The input parameter *`target_classes`* determines the target class, the
class for which the heatmap is generated.
As value the class ID has to be set.
Alternatively, an empty tuple can be handed over. In this case, the heatmap
is calculated for the class with the highest confidence value, thus the
top inferred class.
Currently, *`target_classes`* only supports a single value or an
empty tuple.

The following entries can be set in the dictionary *`gen_param`*:

- **`target_conv_layer`:** —

  Specifies the convolution layer whose activation and gradient are
  used for the heatmap.
  The convolution layer can be specified using its `NAME`,
  as returned using *"summary"* in [`get_dl_model_param`](get_dl_model_param.md),
  e.g., *"conv10"*.
  As default, the last (deepest) convolution layer of the network with a
  non-trivial activation (width and height not equal to 1) is used.
  As a general rule, the activation of the deepest convolution layer
  is most suitable for calculating the heatmap, therefore it is
  recommended to keep the default layer.
- **`use_conv_only`:** —

  In case the convolution layer (selected with `target_conv_layer`)
  is fused with a directly following ReLU activation layer, this parameter can
  be used to determine, from which of these layers the activation and gradient
  will be used for the heatmap. The following values are supported:

  - —

    *"true"*: convolution layer
  - —

    *"false"*: ReLU layer

  Restriction:
   Only applicable if *`heatmap_method`* is set to
  *"grad_cam"*.

  Default:
   `use_conv_only` = *"true"*.
- **`scaling`:** —

  Sets the scaling method for the heatmap. The following values are supported:

  - —

    *"scale_after_relu"*: Negative
    values of the heatmap are set to 0 and then all values are
    scaled within the range [0,1].
    As a consequence, areas within the heatmap can attain very high
    values close to 1 although their contribution to the classification
    result might be small.
  - —

    *"scale_before_relu"*: All values of the heatmap
    are divided by the maximum absolute value and then negative values
    are set to 0. This leads to values for the heatmap in
    [0,1]. However, areas of less activation (and hence with a small
    contribution to the classification result) may not tend to attain
    values near 1.
  - —

    *"scale_without_relu"*: All values are
    scaled within the range [0,1]. No ReLU is applied to the heatmap.
    As a consequence, areas within the heatmap can attain very high
    values close to 1 although their contribution to the classification
    result might be small.
  - —

    *"none"*: The heatmap values are not scaled.

  Default:
   `scaling` = *"scale_without_relu"*.

Every output dictionary in *`dlresult`* contains the inference results
as obtained using [`apply_dl_model`](apply_dl_model.md).
Additionally it includes a nested dictionary under the key
`heatmap_method`, where `method` is the name of the
specified method as given in *`heatmap_method`*.
In this nested dictionary the heatmap is saved under the key
`heatmap_image_class_classID`, in case of *"guided_grad_cam"*
the key is `guided_grad_cam_image_class_classID`,
where `classID` is the ID of the target class.

## Attention

System requirements:
This operator performs a backward pass. As a consequence the same system
requirements apply as for the training of deep-learning-based models.
For further details, please refer to the `“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”.

The heatmap should be used as a tool for visualizing and better
understanding classification results. It is not intended as a
segmentation tool.
Moreover, `gen_dl_model_heatmap` currently only supports models with
*"type"*=*"classification"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dlmodel_handle`** (input_control)  dl_model `→` HHandle

Handle of a Deep learning model.

**`dlsample`** (input_control)  dict(-array) `→` MaybeSequence[HHandle]

Dictionaries with the sample input data.

**`heatmap_method`** (input_control)  string `→` str

Method to be used for the heatmap calculation.

Default:
"grad_cam"

List of values:
"grad_cam", "guided_grad_cam"

**`target_classes`** (input_control)  tuple `→` int

ID of the target class.

Default:
[]

**`gen_param`** (input_control)  dict `→` HHandle

Dictionary for generic parameters.

Default:
[]

**`dlresult`** (output_control)  dict(-array) `→` Sequence[HHandle]

Dictionaries with the result data.

## Possible Predecessors

`apply_dl_model`

## References

R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, D. Batra:
"Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based
Localization," 2017 IEEE International Conference on Computer Vision (ICCV),
Venice, 2017, pp. 618-626. doi: 10.1109/ICCV.2017.74

## Module

Deep Learning Enhanced
