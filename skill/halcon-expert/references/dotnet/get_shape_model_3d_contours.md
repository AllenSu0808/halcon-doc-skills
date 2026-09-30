# GetShapeModel3dContours (Operator)

## Name

`GetShapeModel3dContours` — Return the contour representation of a 3D shape model view.

## Signature

`static void HOperatorSet.GetShapeModel3dContours(out HObject modelContours, HTuple shapeModel3DID, HTuple level, HTuple view, out HTuple viewPose)`

`HXLDCont HShapeModel3D.GetShapeModel3dContours(int level, int view, out HPose viewPose)`

## Description

The operator `GetShapeModel3dContours` returns a
representation of a single model view of the 3D shape model
*`shapeModel3DID`* as XLD contours in *`modelContours`*.
The parameters *`level`* and *`view`* determine for which
model view the contour representation should be returned, where
*`level`* denotes the pyramid level and *`view`* denotes
the model view on this pyramid level.

The permitted range of values for *`level`* and *`view`*
can previously be determined by using the operator
[`GetShapeModel3dParams`](get_shape_model_3d_params.md) and passing
*"num_views_per_level"* for `genParamName`.

The contours can be used to visualize and rate the 3D shape model
that was created with [`CreateShapeModel3d`](create_shape_model_3d.md). With this it is
possible, for example, to decide whether the number of pyramid
levels in the model is appropriate or not. If the contours on the
highest pyramid do not show enough details to be representative for
the model view, the number of pyramid levels that are used during
the search with [`FindShapeModel3d`](find_shape_model_3d.md) should be adjusted
downwards. In contrast, if the contours show too many details even
on the highest pyramid level, a higher number of pyramid levels
should be chosen already during the creation of the 3D shape model
by using [`CreateShapeModel3d`](create_shape_model_3d.md).

Additionally, the pose of the selected view is returned in
*`viewPose`*. It can be used, for example, to project the 3D
shape model according to the view pose by using
[`ProjectShapeModel3d`](project_shape_model_3d.md). The rating of the model contours
that was described above can then be performed by comparing the
*`modelContours`* to the projected model. Note that the
position of the contours of the projection and the position of the
model contours may slightly differ because of radial distortions.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Contour representation of the model view.

**`shapeModel3DID`** (input_control)  shape_model_3d `→` [HShapeModel3D](HShapeModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D shape model.

**`level`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Pyramid level for which the contour representation
should be returned.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`Level >= 1`

**`view`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

View for which the contour representation should be
returned.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`View >= 1`

**`viewPose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose of the 3D shape model at the current view.

## Result

If the parameters are valid, the operator
`GetShapeModel3dContours` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CreateShapeModel3d`,
`ReadShapeModel3d`,
`GetShapeModel3dParams`

## Possible Successors

`CreateShapeModel3d`

## Module

3D Metrology
