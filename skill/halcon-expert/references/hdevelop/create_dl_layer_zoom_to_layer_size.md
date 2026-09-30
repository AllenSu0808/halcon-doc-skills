# create_dl_layer_zoom_to_layer_size (Operator)

## Name

`create_dl_layer_zoom_to_layer_size` — Create a zoom layer using the output size of a reference layer.

## Signature

`create_dl_layer_zoom_to_layer_size( : : DLLayerInput, DLLayerReference, LayerName, Interpolation, AlignCorners, GenParamName, GenParamValue : DLLayerZoom)`

## Description

The operator `create_dl_layer_zoom_to_layer_size` creates a zoom layer
using the output size of a reference layer and returns the layer handle in
*`DLLayerZoom`*.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`DLLayerReference`* is used to define the output size of
the zoom layer *`DLLayerZoom`*: the size is adapted to the output size of
*`DLLayerReference`*.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`Interpolation`* defines the interpolation mode.
Currently the modes *'bilinear'* and *'nearest_neighbor'* are
supported.

The parameter *`AlignCorners`* defines how coordinates are transformed
from the output to the input image. Alternatively, the generic parameter
*'coordinate_transformation_mode'* can be specified. Note, that the
specification of both parameters may not contradict each other:

- ***`AlignCorners`* = *'true'* or
  *'coordinate_transformation_mode'* = *'align_corners'*:** —

  The transformation is applied in the HALCON Non-Standard Cartesian
  coordinate system (edge-centered, with the origin in the upper left corner,
  see chapter [Transformations / 2D Transformations](toc_transformations_2dtransformations.md)).
  Using the $x$ axis as an example, this leads to:
  $$x_{input}=x_{output}\ast(length_{input}-1)/(length_{output}-1)$$
- ***`AlignCorners`* = *'false'*:** —
  - ***'coordinate_transformation_mode'* =
    *'half_pixel'* *(default)*:** —

    The transformation is applied in the HALCON standard
    coordinate system (pixel centered, with the origin in the center
    of the upper left pixel, see chapter
    [Transformations / 2D Transformations](toc_transformations_2dtransformations.md)).
    Using the $x$ axis as an example, this leads to:
    $$x_{input}=(x_{output}+0.5)\ast length_{input}/length_{output}-0.5$$
  - ***'coordinate_transformation_mode'* = *'pytorch_half_pixel'*:** —

    $$x_{input}=length_{output}>1?(x_{output}+0.5)\ast length_{input}/length_{output}-0.5:0.0$$
  - ***'coordinate_transformation_mode'* = *'asymmetric'*:** —

    The transformation is applied asymmetrically.
    Using the $x$ axis as an example, this leads to:
    $$x_{input}=x_{output}\ast length_{input}/length_{output}$$

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'coordinate_transformation_mode'*:** —

  Defines how coordinates are transformed from the output to the input
  image. If not specified, the parameter *`AlignCorners`* determines
  the transformation.

  Default:
   *'half_pixel'*
- ***'nearest_mode'*:** —

  Defines how to get the "nearest" pixel in the input image. This parameter
  only applies if *`Interpolation`* is set to
  *'nearest_neighbor'*.

  Suggested values:
   *'round_prefer_floor'*,
  *'round_prefer_ceil'*, *'floor'*, *'ceil'*

  Default:
   *'round_prefer_floor'*
- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*

Certain parameters of layers created using this operator
`create_dl_layer_zoom_to_layer_size` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'align_corners'* (*`AlignCorners`*) | `x` | `x` |
| *'coordinate_transformation_mode'* | `x` | `x` |
| *'input_layer'* (*`DLLayerInput`*) |  | `x` |
| *'interpolation_mode'* (*`Interpolation`*) |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'nearest_mode'* | `x` | `x` |
| *'output_layer'* (*`DLLayerZoom`*) |  | `x` |
| *'scale_params'* (*`DLLayerReference`*) |  | `x` |
| *'shape'* |  | `x` |
| *'type'* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'is_inference_output'* | `x` | `x` |
| *'num_trainable_params'* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerInput`** (input_control)  dl_layer `→`  (handle)

Feeding layer.

**`DLLayerReference`** (input_control)  dl_layer `→`  (handle)

Reference layer to define the output size.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`Interpolation`** (input_control)  string `→`  (string)

Mode of interpolation.

Default:
'bilinear'

List of values:
'bilinear', 'nearest_neighbor'

**`AlignCorners`** (input_control)  string `→`  (string)

Type of coordinate transformation between output/input
images.

Default:
'false'

List of values:
'false', 'true'

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'coordinate_transformation_mode', 'is_inference_output', 'nearest_mode'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Generic input parameter values.

Default:
[]

Suggested values:
'align_corners', 'asymmetric', 'pytorch_half_pixel', 'half_pixel', 'true', 'false', 'ceil', 'floor', 'round_prefer_ceil', 'round_prefer_floor'

**`DLLayerZoom`** (output_control)  dl_layer `→`  (handle)

Zoom layer.

## Alternatives

`create_dl_layer_zoom_size`,
`create_dl_layer_zoom_factor`

## Module

Deep Learning Professional
