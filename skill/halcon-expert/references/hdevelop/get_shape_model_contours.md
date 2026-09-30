# get_shape_model_contours (Operator)

## Name

`get_shape_model_contours` — Return the contour representation of a shape model.

## Signature

`get_shape_model_contours( : ModelContours : ModelID, Level : )`

## Description

The operator `get_shape_model_contours` returns a
representation of the shape model *`ModelID`* as XLD contours
in *`ModelContours`*. The parameter *`Level`* determines
for which pyramid level of the model the contour representation
should be returned. The contours can be used, for example, to
visualize the found instances of the model in an image. It should
be noted that the position of *`ModelContours`* is normalized
such that the reference point of the model (see
[`set_shape_model_origin`](set_shape_model_origin.md)) lies at the pixel position (0,0).
Hence, the contours simply need to be translated to the found
position in the image (and possibly rotated and scaled around this
point).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelContours`** (output_object)  xld_cont-array `→` object

Contour representation of the shape model.

**`ModelID`** (input_control)  shape_model `→`  (handle)

Handle of the model.

**`Level`** (input_control)  integer `→`  (integer)

Pyramid level for which the contour representation
should be returned.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`Level >= 1`

## Result

If the handle of the model is valid, the operator
`get_shape_model_contours` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`create_shape_model`,
`create_scaled_shape_model`,
`create_aniso_shape_model`,
`read_shape_model`

## Alternatives

`get_generic_shape_model_object`

## See also

`find_shape_model`,
`find_scaled_shape_model`,
`find_aniso_shape_model`,
`find_shape_models`,
`find_scaled_shape_models`,
`find_aniso_shape_models`

## Module

Matching
