# xyz_to_object_model_3d (Operator)

## Name

`xyz_to_object_model_3d` — Transform 3D points from images to a 3D object model.

## Signature

`xyz_to_object_model_3d(X, Y, Z : : : ObjectModel3D)`

## Description

The operator `xyz_to_object_model_3d` transforms an image triple
that contains the X, Y, and Z-coordinates of 3D points to a 3D object model.
Thereby, only points in the intersecting domains of all three images are
used and the images need to be of same size.
The size of these images can be queried from the model by
[`get_object_model_3d_params`](get_object_model_3d_params.md) with *'mapping_size'*.
The handle of the created 3D object model is returned in
*`ObjectModel3D`*.
The created 3D object model contains the coordinates of the points, as well
as a mapping attribute that contains the original row and column of each
3D point.
Points where one of the coordinates is infinity or "Not a Number" (NaN)
are ignored and not added to the 3D object model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`X`** (input_object)  singlechannelimage `→` object (real)

Image with the X-Coordinates and the ROI of the 3D points.

**`Y`** (input_object)  singlechannelimage `→` object (real)

Image with the Y-Coordinates of the 3D points.

**`Z`** (input_object)  singlechannelimage `→` object (real)

Image with the Z-Coordinates of the 3D points.

**`ObjectModel3D`** (output_control)  object_model_3d `→`  (handle)

Handle of the 3D object model.

## Result

The operator `xyz_to_object_model_3d` returns the value
2 (
H_MSG_TRUE)
if the given parameters are correct. Otherwise, an exception
will be raised.

## Possible Predecessors

`disparity_image_to_xyz`,
`get_sheet_of_light_result`

## Alternatives

`gen_object_model_3d_from_points`,
`get_sheet_of_light_result_object_model_3d`

## See also

`read_object_model_3d`

## Module

3D Metrology
