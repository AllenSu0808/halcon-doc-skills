# max_diameter_object_model_3d (Operator)

## Name

`max_diameter_object_model_3d` — Calculate the maximal diameter of a 3D object model.

## Signature

`def max_diameter_object_model_3d(object_model_3d: MaybeSequence[HHandle]) -> Sequence[float]`

`def max_diameter_object_model_3d_s(object_model_3d: MaybeSequence[HHandle]) -> float`

## Description

`max_diameter_object_model_3d` calculates the maximal diameter of
the 3D object model by calculating the
convex hull of the object and searching for the pair of points on the convex
hull with the largest distance.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object_model_3d`** (input_control)  object_model_3d(-array) `→` MaybeSequence[HHandle]

Handle of the 3D object model.

**`diameter`** (output_control)  number(-array) `→` Sequence[float]

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

`max_diameter_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`connection_object_model_3d`

## Possible Successors

`select_object_model_3d`

## See also

`volume_object_model_3d_relative_to_plane`,
`area_object_model_3d`,
`moments_object_model_3d`

## Module

3D Metrology
