# reduce_object_model_3d_by_view (Operator)

## Name

`reduce_object_model_3d_by_view` — Remove points from a 3D object model by projecting it to a virtual view
and removing all points outside of a given region.

## Signature

`reduce_object_model_3d_by_view(Region : : ObjectModel3D, CamParam, Pose : ObjectModel3DReduced)`

## Description

`reduce_object_model_3d_by_view` projects the points of
*`ObjectModel3D`* into the image plane given by *`Pose`* and
*`CamParam`* and reduces the 3D object model to the points lying inside
the region given in *`Region`*.
In particular, the points are first transformed with the pose and then
projected using the camera parameters.
Only those points that are located inside the specified region
are copied to the new 3D object model.

Faces of a mesh are only contained in the output 3D object model if all
corner points are within the region.

As alternative to camera parameters and a pose, an XYZ-mapping contained
in *`ObjectModel3D`* can be used for the reduction.
For this, *`CamParam`* must be set to *'xyz_mapping'*
or an empty tuple and
an empty tuple must be passed to *`Pose`*.
In this case, the original image coordinates of the 3D points
are used to check if a point is inside *`Region`*.

## Attention

Cameras with hypercentric lenses are not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Region in the image plane.

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handle of the 3D object model.

**`CamParam`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters.

Suggested values:
'xyz_mapping', []

**`Pose`** (input_control)  pose(-array) `→`  (real / integer)

3D pose of the world coordinate system in camera
coordinates.

Number of elements:
Pose == 7

**`ObjectModel3DReduced`** (output_control)  object_model_3d(-array) `→`  (handle)

Handle of the reduced 3D object model.

## Example (HDevelop)

```
gen_object_model_3d_from_points (200*(rand(100)-0.5), \
                                 200*(rand(100)-0.5), \
                                 200*(rand(100)-0.5), ObjectModel3D)
gen_circle (Circle, 240, 320, 60)
CamParam := ['area_scan_telecentric_division',1,0,1,1,320,240,640,480]
Pose := [0,0,1,0,0,0,0]
reduce_object_model_3d_by_view (Circle, ObjectModel3D, CamParam, \
                                Pose, ObjectModel3DReduced)
dev_get_window (WindowHandle)
visualize_object_model_3d (WindowHandle, [ObjectModel3D, \
                           ObjectModel3DReduced], CamParam, Pose, \
                           ['color_0', 'point_size_1'], ['blue',6], \
                           [], [], [], PoseOut)
```

## Result

`reduce_object_model_3d_by_view` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`

## Possible Successors

`project_object_model_3d`,
`object_model_3d_to_xyz`

## See also

`select_points_object_model_3d`

## Module

3D Metrology
