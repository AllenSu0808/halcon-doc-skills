# get_generic_shape_model_object (Operator)

## Name

`get_generic_shape_model_object` — Get iconic objects of the shape model.

## Signature

`def get_generic_shape_model_object(model_id: HHandle, gen_param_name: Sequence[str]) -> HObject`

## Description

The operator `get_generic_shape_model_object` reads out objects
of the shape model *`model_id`* and returns them in *`object`*.

*`gen_param_name`* specifies which iconic object will be returned.
The following values are possible:

- ***"clutter_region"*:** —

  The clutter region of the shape model.
- ***"contours"*:** —

  Representation of the shape model *`model_id`* for the bottom-most
  pyramid level as XLD contours. Thereby the contour is translated so that
  the origin of the model with the coordinates *"origin_row"* and
  *"origin_column"* (see [`set_generic_shape_model_param`](set_generic_shape_model_param.md)) is
  located at the origin of the pixel centered HALCON standard coordinate system
  (see [Transformations / 2D Transformations](toc_transformations_2dtransformations.md)). The contours can be used,
  for example, to visualize the found instances of the model in an image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object`** (output_object)  (multichannel-)object(-array) `→` HObject

Iconic object to be returned.

**`model_id`** (input_control)  shape_model `→` HHandle

Handle of the shape model.

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

Parameter names.

Default:
"clutter_region"

List of values:
"clutter_region", "contours"

## Result

If the parameters are valid, the operator
`get_generic_shape_model_object` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`create_generic_shape_model`,
`set_generic_shape_model_object`,
`train_generic_shape_model`

## Module

Matching
