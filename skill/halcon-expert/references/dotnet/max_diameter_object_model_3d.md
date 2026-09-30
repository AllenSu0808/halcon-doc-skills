# MaxDiameterObjectModel3d (Operator)

## Name

`MaxDiameterObjectModel3d` — Calculate the maximal diameter of a 3D object model.

## Signature

`static void HOperatorSet.MaxDiameterObjectModel3d(HTuple objectModel3D, out HTuple diameter)`

`static HTuple HObjectModel3D.MaxDiameterObjectModel3d(HObjectModel3D[] objectModel3D)`

`double HObjectModel3D.MaxDiameterObjectModel3d()`

## Description

`MaxDiameterObjectModel3d` calculates the maximal diameter of
the 3D object model by calculating the
convex hull of the object and searching for the pair of points on the convex
hull with the largest distance.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`diameter`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Calculated diameter.

Number of elements:
Diameter == ObjectModel3D

## Example (HDevelop)

```
gen_object_model_3d_from_points (rand(200), rand(200),\
                                    rand(200), ObjectModel3D)
max_diameter_object_model_3d (ObjectModel3D, Diameter)
```

## Result

`MaxDiameterObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`ConnectionObjectModel3d`

## Possible Successors

`SelectObjectModel3d`

## See also

`VolumeObjectModel3dRelativeToPlane`,
`AreaObjectModel3d`,
`MomentsObjectModel3d`

## Module

3D Metrology
