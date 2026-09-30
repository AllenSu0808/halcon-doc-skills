# create_dl_transform_resize (Operator)

## Name

`create_dl_transform_resize` — Create a resize transform using absolute dimensions.

## Signature

`create_dl_transform_resize( : : TransformName, ImageDimensions, GenParamName, GenParamValue : Resize)`

## Description

The operator `create_dl_transform_resize` creates a resize transform
with absolute output dimensions and returns the transform handle in
*`Resize`*. The transform resizes the input image to the specified
dimensions if required.

The parameter *`TransformName`* specifies a unique, non-empty
name for the transform.
Note that when creating a transform pipeline using
[`create_dl_transform_pipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameter *`ImageDimensions`* defines the absolute output
dimensions of the resize transform *`Resize`*. It contains the
output image dimensions `'width'`, `'height'`, and
`'num_channels'` as a tuple. Passing *-1* keeps the
corresponding dimension of the input image unchanged.
It is not permitted to set all image dimensions to *-1*
simultaneously.
The number of input channels is checked to be equal to the wanted
number of channels. The number of channels can only be adapted to
*3* (for input containing *1* channel) or
*1* (for input containing *3* channels).
In all other cases, an error is raised.

The following generic parameters *`GenParamName`* and their
corresponding values *`GenParamValue`* are supported:

- ***'alignment'*:** —

  Specifies the alignment mode
  when *'zoom_type'*=*'fit'* is used.
  Currently the alignments *'center'* and
  *'top_left'* are supported.

  Default:
   *'center'*.
- ***'interpolation'*:** —

  Specifies the interpolation mode.
  Currently the modes *'constant'* and
  *'nearest_neighbor'* are supported.

  Default:
   *'constant'*.
- ***'zoom_type'*:** —

  Specifies the zooming mode applied during resizing.
  Possible values are:

  - *'fill'*:
    Resizes the image to the specified `width` and
    `height`. The aspect ratio may change.
    Padding is not applied.
  - *'fit'*:
    Resizes the image to fit into the specified `width` or
    `height`. The aspect ratio is preserved.
    Padding is applied if required, the *'fill_value'*
    can be specified using [`set_dl_transform_pipeline_param`](set_dl_transform_pipeline_param.md).

  Default:
   *'fill'*.

The following parameters are specific to the transforms of type
*'resize'*. They can respectively be get
or set using the operators [`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md) and
[`set_dl_transform_pipeline_param`](set_dl_transform_pipeline_param.md):

| ParamName | `set` | `get` |
| --- | --- | --- |
| *'alignment'* | `x` | `x` |
| *'image_dimensions'* | `x` | `x` |
| *'interpolation'* | `x` | `x` |
| *'zoom_type'* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`TransformName`** (input_control)  string `→`  (string)

Name of the output transform.

Default:
'resize'

**`ImageDimensions`** (input_control)  integer-array `→`  (integer)

Image dimensions width, height and number of channels.

Default:
[512,512,3]

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'alignment', 'interpolation', 'zoom_type'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (string / real / integer)

Generic input parameter values.

Default:
[]

Suggested values:
'fill', 'fit', 1.0

**`Resize`** (output_control)  dl_transform `→`  (handle)

Resize transform.

## Possible Successors

`create_dl_transform_pipeline`

## See also

`create_dl_transform_random_hsv`,
`transform_dl_sample_batch`

## Module

Foundation
