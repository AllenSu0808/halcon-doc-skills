# AreaObjectModel3d (Operator)

## Name

`AreaObjectModel3d` — Calculate the area of all faces of a 3D object model.

## Signature

`static void HOperatorSet.AreaObjectModel3d(HTuple objectModel3D, out HTuple area)`

`static HTuple HObjectModel3D.AreaObjectModel3d(HObjectModel3D[] objectModel3D)`

`double HObjectModel3D.AreaObjectModel3d()`

## Description

`AreaObjectModel3d` calculates the area of all faces in a
3D object model. The 3D object model requires faces or triangles.
The resulting area is returned in *`area`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`area`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Calculated area.

Number of elements:
Area == ObjectModel3D

## Example (HDevelop)

```
gen_box_object_model_3d ([0,0,0,0,0,0,0],3,2,1, ObjectModel3D)
convex_hull_object_model_3d (ObjectModel3D, ObjectModel3DConvexHull)
area_object_model_3d (ObjectModel3DConvexHull, Area)
```

## Result

`AreaObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`ConnectionObjectModel3d`,
`SelectPointsObjectModel3d`,
`PrepareObjectModel3d`,
`ConvexHullObjectModel3d`

## Possible Successors

`SelectObjectModel3d`

## See also

`VolumeObjectModel3dRelativeToPlane`,
`MaxDiameterObjectModel3d`,
`MomentsObjectModel3d`

## Module

3D Metrology
