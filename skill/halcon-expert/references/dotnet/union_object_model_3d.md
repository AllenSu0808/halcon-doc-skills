# UnionObjectModel3d (Operator)

## Name

`UnionObjectModel3d` — Combine several 3D object models to a new 3D object model.

## Signature

`static void HOperatorSet.UnionObjectModel3d(HTuple objectModels3D, HTuple method, out HTuple unionObjectModel3D)`

`static HObjectModel3D HObjectModel3D.UnionObjectModel3d(HObjectModel3D[] objectModels3D, string method)`

`HObjectModel3D HObjectModel3D.UnionObjectModel3d(string method)`

## Description

`UnionObjectModel3d` combines the data of all input models
in *`objectModels3D`* to a new 3D object model that is returned in
*`unionObjectModel3D`*.

Overlapping areas in the 3D object models
might cause the potential 2D mapping, polygons, or triangles in the output
to be less useful, since they might overlap, too.

The only supported *`method`* is so far *"points_surface"*,
which combines all points, surfaces and lines into the output
*`unionObjectModel3D`*.
Extended Attributes are copied if no holes appear, i.e., if they are
present in all input object models where the standard attribute they are
attached to exists.

## Attention

`UnionObjectModel3d` ignores 3D object models of type 3D primitive
and 3D shape model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`objectModels3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of input 3D object models.

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method used for the union.

Default:
"points_surface"

List of values:
"points_surface"

**`unionObjectModel3D`** (output_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the resulting 3D object model.

## Example (HDevelop)

```
gen_object_model_3d_from_points ([0,0,0,0],[1,1,0,0], [0,1,1,0],\
                                    ObjectModel3D1)
gen_object_model_3d_from_points ([1,1,1,1],[1,1,0,0], [0,1,1,0],\
                                    ObjectModel3D2)
get_object_model_3d_params (ObjectModel3D1, 'diameter', DiameterOld)
union_object_model_3d ([ObjectModel3D1,ObjectModel3D2], 'points_surface',\
                       UnionObjectModel3D)
get_object_model_3d_params (UnionObjectModel3D, 'diameter', DiameterNew)
```

## Result

`UnionObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If there is no attribute common in all input
objects, an exception is raised.

## Possible Predecessors

`GetObjectModel3dParams`

## Possible Successors

`ConnectionObjectModel3d`,
`ConvexHullObjectModel3d`

## See also

`GenBoxObjectModel3d`,
`GenSphereObjectModel3d`,
`GenCylinderObjectModel3d`

## Module

3D Metrology
