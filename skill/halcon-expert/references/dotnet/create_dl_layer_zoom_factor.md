# CreateDlLayerZoomFactor (Operator)

## Name

`CreateDlLayerZoomFactor` — Create a zoom layer using size factors.

## Signature

`static void HOperatorSet.CreateDlLayerZoomFactor(HTuple DLLayerInput, HTuple layerName, HTuple scaleWidth, HTuple scaleHeight, HTuple interpolation, HTuple alignCorners, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerZoom)`

`HDlLayer HDlLayer.CreateDlLayerZoomFactor(string layerName, HTuple scaleWidth, HTuple scaleHeight, string interpolation, string alignCorners, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerZoomFactor(string layerName, double scaleWidth, double scaleHeight, string interpolation, string alignCorners, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerZoomFactor` creates a zoom layer using
size factors and returns the layer handle in *`DLLayerZoom`*.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameters *`scaleWidth`* and *`scaleHeight`* specify the ratio
between the output and the corresponding input dimension. Together they
define the output size of the zoom layer *`DLLayerZoom`*.

The parameter *`interpolation`* defines the interpolation mode.
Currently the modes *"bilinear"* and *"nearest_neighbor"* are
supported.

The parameter *`alignCorners`* defines how coordinates are transformed
from the output to the input image. Alternatively, the generic parameter
*"coordinate_transformation_mode"* can be specified. Note, that the
specification of both parameters may not contradict each other:

- ***`alignCorners`* = *"true"* or
  *"coordinate_transformation_mode"* = *"align_corners"*:** —

  The transformation is applied in the HALCON Non-Standard Cartesian
  coordinate system (edge-centered, with the origin in the upper left corner,
  see chapter [Transformations / 2D Transformations](toc_transformations_2dtransformations.md)).
  Using the $x$ axis as an example, this leads to:
  $$x_{input}=x_{output}\ast(length_{input}-1)/(length_{output}-1)$$
- ***`alignCorners`* = *"false"*:** —
  - ***"coordinate_transformation_mode"* =
    *"half_pixel"* *(default)*:** —

    The transformation is applied in the HALCON standard
    coordinate system (pixel centered, with the origin in the center
    of the upper left pixel, see chapter
    [Transformations / 2D Transformations](toc_transformations_2dtransformations.md)).
    Using the $x$ axis as an example, this leads to:
    $$x_{input}=(x_{output}+0.5)\ast length_{input}/length_{output}-0.5$$
  - ***"coordinate_transformation_mode"* = *"pytorch_half_pixel"*:** —

    $$x_{input}=length_{output}>1?(x_{output}+0.5)\ast length_{input}/length_{output}-0.5:0.0$$
  - ***"coordinate_transformation_mode"* = *"asymmetric"*:** —

    The transformation is applied asymmetrically.
    Using the $x$ axis as an example, this leads to:
    $$x_{input}=x_{output}\ast length_{input}/length_{output}$$

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"coordinate_transformation_mode"*:** —

  Defines how coordinates are transformed from the output to the input
  image. If not specified, the parameter *`alignCorners`* determines
  the transformation.

  Default:
   *"half_pixel"*
- ***"nearest_mode"*:** —

  Defines how to get the "nearest" pixel in the input image. This parameter
  only applies if *`interpolation`* is set to
  *"nearest_neighbor"*.

  Suggested values:
   *"round_prefer_floor"*,
  *"round_prefer_ceil"*, *"floor"*, *"ceil"*

  Default:
   *"round_prefer_floor"*
- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerZoomFactor` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md).
Note, the operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and
[`GetDlModelLayerParam`](get_dl_model_layer_param.md) require a model created by
[`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"align_corners"* (*`alignCorners`*) | `x` | `x` |
| *"coordinate_transformation_mode"* | `x` | `x` |
| *"input_layer"* (*`DLLayerInput`*) |  | `x` |
| *"interpolation_mode"* (*`interpolation`*) |  | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"nearest_mode"* | `x` | `x` |
| *"output_layer"* (*`DLLayerZoom`*) |  | `x` |
| *"scale_params"* (*`scaleWidth`* and *`scaleHeight`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"is_inference_output"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerInput`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Feeding layer.

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`scaleWidth`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Ratio output/input width of the layer.

Default:
2.0

**`scaleHeight`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Ratio output/input height of the layer.

Default:
2.0

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode of interpolation.

Default:
"bilinear"

List of values:
"bilinear", "nearest_neighbor"

**`alignCorners`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of coordinate transformation between output/input
images.

Default:
"false"

List of values:
"false", "true"

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

List of values:
"coordinate_transformation_mode", "is_inference_output", "nearest_mode"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Generic input parameter values.

Default:
[]

Suggested values:
"align_corners", "asymmetric", "pytorch_half_pixel", "half_pixel", "true", "false", "ceil", "floor", "round_prefer_ceil", "round_prefer_floor"

**`DLLayerZoom`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Zoom layer.

## Alternatives

`CreateDlLayerZoomSize`,
`CreateDlLayerZoomToLayerSize`

## Module

Deep Learning Professional
