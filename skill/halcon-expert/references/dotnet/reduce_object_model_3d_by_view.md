# ReduceObjectModel3dByView (Operator)

## Name

`ReduceObjectModel3dByView` — Remove points from a 3D object model by projecting it to a virtual view
and removing all points outside of a given region.

## Signature

`static void HOperatorSet.ReduceObjectModel3dByView(HObject region, HTuple objectModel3D, HTuple camParam, HTuple pose, out HTuple objectModel3DReduced)`

`static HObjectModel3D[] HObjectModel3D.ReduceObjectModel3dByView(HRegion region, HObjectModel3D[] objectModel3D, HCamPar camParam, HPose[] pose)`

`HObjectModel3D HObjectModel3D.ReduceObjectModel3dByView(HRegion region, HCamPar camParam, HPose pose)`

`HObjectModel3D[] HCamPar.ReduceObjectModel3dByView(HRegion region, HObjectModel3D[] objectModel3D, HPose[] pose)`

`HObjectModel3D HCamPar.ReduceObjectModel3dByView(HRegion region, HObjectModel3D objectModel3D, HPose pose)`

`static HObjectModel3D[] HPose.ReduceObjectModel3dByView(HRegion region, HObjectModel3D[] objectModel3D, HCamPar camParam, HPose[] pose)`

`HObjectModel3D HPose.ReduceObjectModel3dByView(HRegion region, HObjectModel3D objectModel3D, HCamPar camParam)`

## Description

`ReduceObjectModel3dByView` projects the points of
*`objectModel3D`* into the image plane given by *`pose`* and
*`camParam`* and reduces the 3D object model to the points lying inside
the region given in *`region`*.
In particular, the points are first transformed with the pose and then
projected using the camera parameters.
Only those points that are located inside the specified region
are copied to the new 3D object model.

Faces of a mesh are only contained in the output 3D object model if all
corner points are within the region.

As alternative to camera parameters and a pose, an XYZ-mapping contained
in *`objectModel3D`* can be used for the reduction.
For this, *`camParam`* must be set to *"xyz_mapping"*
or an empty tuple and
an empty tuple must be passed to *`pose`*.
In this case, the original image coordinates of the 3D points
are used to check if a point is inside *`region`*.

## Attention

Cameras with hypercentric lenses are not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region in the image plane.

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`camParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

Suggested values:
"xyz_mapping", []

**`pose`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose of the world coordinate system in camera
coordinates.

Number of elements:
Pose == 7

**`objectModel3DReduced`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

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

`ReduceObjectModel3dByView` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`

## Possible Successors

`ProjectObjectModel3d`,
`ObjectModel3dToXyz`

## See also

`SelectPointsObjectModel3d`

## Module

3D Metrology
