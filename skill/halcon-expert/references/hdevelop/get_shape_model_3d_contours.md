# get_shape_model_3d_contours (Operator)

## Name

`get_shape_model_3d_contours` — Return the contour representation of a 3D shape model view.

## Signature

`get_shape_model_3d_contours( : ModelContours : ShapeModel3DID, Level, View : ViewPose)`

## Description

The operator `get_shape_model_3d_contours` returns a
representation of a single model view of the 3D shape model
*`ShapeModel3DID`* as XLD contours in *`ModelContours`*.
The parameters *`Level`* and *`View`* determine for which
model view the contour representation should be returned, where
*`Level`* denotes the pyramid level and *`View`* denotes
the model view on this pyramid level.

The permitted range of values for *`Level`* and *`View`*
can previously be determined by using the operator
[`get_shape_model_3d_params`](get_shape_model_3d_params.md) and passing
*'num_views_per_level'* for `GenParamName`.

The contours can be used to visualize and rate the 3D shape model
that was created with [`create_shape_model_3d`](create_shape_model_3d.md). With this it is
possible, for example, to decide whether the number of pyramid
levels in the model is appropriate or not. If the contours on the
highest pyramid do not show enough details to be representative for
the model view, the number of pyramid levels that are used during
the search with [`find_shape_model_3d`](find_shape_model_3d.md) should be adjusted
downwards. In contrast, if the contours show too many details even
on the highest pyramid level, a higher number of pyramid levels
should be chosen already during the creation of the 3D shape model
by using [`create_shape_model_3d`](create_shape_model_3d.md).

Additionally, the pose of the selected view is returned in
*`ViewPose`*. It can be used, for example, to project the 3D
shape model according to the view pose by using
[`project_shape_model_3d`](project_shape_model_3d.md). The rating of the model contours
that was described above can then be performed by comparing the
*`ModelContours`* to the projected model. Note that the
position of the contours of the projection and the position of the
model contours may slightly differ because of radial distortions.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelContours`** (output_object)  xld_cont-array `→` object

Contour representation of the model view.

**`ShapeModel3DID`** (input_control)  shape_model_3d `→`  (handle)

Handle of the 3D shape model.

**`Level`** (input_control)  integer `→`  (integer)

Pyramid level for which the contour representation
should be returned.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`Level >= 1`

**`View`** (input_control)  integer `→`  (integer)

View for which the contour representation should be
returned.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`View >= 1`

**`ViewPose`** (output_control)  pose `→`  (real / integer)

3D pose of the 3D shape model at the current view.

## Result

If the parameters are valid, the operator
`get_shape_model_3d_contours` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`create_shape_model_3d`,
`read_shape_model_3d`,
`get_shape_model_3d_params`

## Possible Successors

`create_shape_model_3d`

## Module

3D Metrology
