# area_object_model_3d (Operator)

## Name

`area_object_model_3d` — Calculate the area of all faces of a 3D object model.

## Signature

`def area_object_model_3d(object_model_3d: MaybeSequence[HHandle]) -> Sequence[float]`

`def area_object_model_3d_s(object_model_3d: MaybeSequence[HHandle]) -> float`

## Description

`area_object_model_3d` calculates the area of all faces in a
3D object model. The 3D object model requires faces or triangles.
The resulting area is returned in *`area`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object_model_3d`** (input_control)  object_model_3d(-array) `→` MaybeSequence[HHandle]

Handle of the 3D object model.

**`area`** (output_control)  number(-array) `→` Sequence[float]

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

`area_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`connection_object_model_3d`,
`select_points_object_model_3d`,
`prepare_object_model_3d`,
`convex_hull_object_model_3d`

## Possible Successors

`select_object_model_3d`

## See also

`volume_object_model_3d_relative_to_plane`,
`max_diameter_object_model_3d`,
`moments_object_model_3d`

## Module

3D Metrology
