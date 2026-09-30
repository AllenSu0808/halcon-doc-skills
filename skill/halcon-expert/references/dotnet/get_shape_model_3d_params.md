# GetShapeModel3dParams (Operator)

## Name

`GetShapeModel3dParams` — Return the parameters of a 3D shape model.

## Signature

`static void HOperatorSet.GetShapeModel3dParams(HTuple shapeModel3DID, HTuple genParamName, out HTuple genParamValue)`

`HTuple HShapeModel3D.GetShapeModel3dParams(HTuple genParamName)`

`HTuple HShapeModel3D.GetShapeModel3dParams(string genParamName)`

## Description

The operator `GetShapeModel3dParams` allows to query
parameters of the 3D shape model. The names of the desired
parameters are passed in the generic parameter
*`genParamName`*, the corresponding values are returned in
*`genParamValue`*.

The following parameters can be queried:

- ***"cam_param"*:** —

  Internal parameters of the camera that is used for the matching.
- ***"ref_rot_x"*:** —

  Reference orientation: Rotation around x-axis or x component of
  the Rodriguez vector (in radians or without unit).
- ***"ref_rot_y"*:** —

  Reference orientation: Rotation around y-axis or y component of
  the Rodriguez vector (in radians or without unit).
- ***"ref_rot_z"*:** —

  Reference orientation: Rotation around z-axis or z component of
  the Rodriguez vector (in radians or without unit).
- ***"order_of_rotation"*:** —

  Meaning of the rotation values of the reference orientation.
- ***"longitude_min"*:** —

  Minimum longitude of the model views.
- ***"longitude_max"*:** —

  Maximum longitude of the model views.
- ***"latitude_min"*:** —

  Minimum latitude of the model views.
- ***"latitude_max"*:** —

  Maximum latitude of the model views.
- ***"cam_roll_min"*:** —

  Minimum camera roll angle of the model views.
- ***"cam_roll_max"*:** —

  Maximum camera roll angle of the model views.
- ***"dist_min"*:** —

  Minimum camera-object-distance of the model views.
- ***"dist_max"*:** —

  Maximum camera-object-distance of the model views.
- ***"min_contrast"*:** —

  Minimum contrast of the objects in the search images.
- ***"num_levels"*:** —

  User-specified number of pyramid levels.
- ***"num_levels_max"*:** —

  Maximum number of used pyramid levels over all model views.
- ***"optimization"*:** —

  Kind of optimization by reducing the number of model points.
- ***"metric"*:** —

  Match metric.
- ***"part_size"*:** —

  Size of the model parts that is used when *"metric"*
  is set to *"ignore_part_polarity"*.
- ***"min_face_angle"*:** —

  Minimum 3D face angle for which 3D object model edges are included
  in the 3D shape model.
- ***"min_size"*:** —

  Minimum size of the projected 3D object model edge (in number of
  pixels) to include the projected edge in the 3D shape model.
- ***"model_tolerance"*:** —

  Maximum acceptable tolerance of the projected 3D object model
  edges (in pixels).
- ***"num_views_per_level"*:** —

  Number of model views per pyramid level. For each pyramid level
  the number of views that are stored in the 3D shape model are
  returned. Thus, the number of returned elements corresponds to the
  number of used pyramid levels, which can be queried with
  *"num_levels_max"*. Note that for pyramid levels below
  *"lowest_model_level"* (see documentation of
  [`CreateShapeModel3d`](create_shape_model_3d.md)), the value *0* is returned.
- ***"reference_pose"*:** —

  Reference position and orientation of the 3d shape model.
  The returned pose is in the form $r c s \; P \; m c s$ ![figure](../assets/f56ec9dca1d0a24f.svg),
  where *rcs* denotes the reference coordinates system and
  *mcs* the model coordinate system (which is a 3D world coordinate
  system), see [Transformations / Poses](toc_transformations_poses.md) and
  `“Solution Guide III-C - 3D Vision”`.
  Hence, it describes the pose of the
  coordinate system that is used in the underlying 3D object model
  relative to the internally used reference
  coordinate system of the 3D shape model.
  With this pose, points given in the object coordinate system can be
  transformed into the reference coordinate system.
- ***"reference_point"*:** —

  3D coordinates of the reference point of the underlying 3D object
  model.
- ***"bounding_box1"*:** —

  Smallest enclosing axis-parallel cuboid of the underlying 3D
  object model in the following order: [min_x, min_y, min_z, max_x,
  max_y, max_z].
- ***"fast_pose_refinement"*:** —

  Describes whether the pose refinement during the search is
  performed in a sped up mode (*"true"*) or in the
  conventional mode (*"false"*).
- ***"lowest_model_level"*:** —

  Lowest pyramid level down to which views are stored in the model.
- ***"union_adjacent_contours"*:** —

  Describes whether in [`ProjectShapeModel3d`](project_shape_model_3d.md) adjacent contours
  should be joined or not.

A detailed description of the parameters can be looked up with the
operator [`CreateShapeModel3d`](create_shape_model_3d.md).

It is possible to query the values of several parameters with a
single operator call by passing a tuple containing the names of all
desired parameters to *`genParamName`*. As a result a tuple of
the same length with the corresponding values is returned in
*`genParamValue`*. Note that this is solely possible for
parameters that return only a single value.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`shapeModel3DID`** (input_control)  shape_model_3d `→` [HShapeModel3D](HShapeModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D shape model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that
are to be queried for the 3D shape model.

Default:
"num_levels_max"

List of values:
"bounding_box1", "cam_param", "cam_roll_max", "cam_roll_min", "dist_max", "dist_min", "fast_pose_refinement", "latitude_max", "latitude_min", "longitude_max", "longitude_min", "lowest_model_level", "metric", "min_contrast", "min_face_angle", "min_size", "model_tolerance", "num_levels", "num_levels_max", "num_views_per_level", "optimization", "order_of_rotation", "part_size", "ref_rot_x", "ref_rot_y", "ref_rot_z", "reference_point", "reference_pose", "union_adjacent_contours"

**`genParamValue`** (output_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of the generic parameters.

## Result

If the parameters are valid, the operator
`GetShapeModel3dParams` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CreateShapeModel3d`,
`ReadShapeModel3d`

## Possible Successors

`FindShapeModel3d`

## See also

`ConvertPoint3dCartToSpher`,
`ConvertPoint3dSpherToCart`,
`CreateCamPoseLookAtPoint`,
`TransPoseShapeModel3d`

## Module

3D Metrology
