# union_object_model_3d (Operator)

## Name

`union_object_model_3d` — Combine several 3D object models to a new 3D object model.

## Signature

`union_object_model_3d( : : ObjectModels3D, Method : UnionObjectModel3D)`

## Description

`union_object_model_3d` combines the data of all input models
in *`ObjectModels3D`* to a new 3D object model that is returned in
*`UnionObjectModel3D`*.

Overlapping areas in the 3D object models
might cause the potential 2D mapping, polygons, or triangles in the output
to be less useful, since they might overlap, too.

The only supported *`Method`* is so far *'points_surface'*,
which combines all points, surfaces and lines into the output
*`UnionObjectModel3D`*.
Extended Attributes are copied if no holes appear, i.e., if they are
present in all input object models where the standard attribute they are
attached to exists.

## Attention

`union_object_model_3d` ignores 3D object models of type 3D primitive
and 3D shape model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`ObjectModels3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handle of input 3D object models.

**`Method`** (input_control)  string `→`  (string)

Method used for the union.

Default:
'points_surface'

List of values:
'points_surface'

**`UnionObjectModel3D`** (output_control)  object_model_3d `→`  (handle)

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

`union_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If there is no attribute common in all input
objects, an exception is raised.

## Possible Predecessors

`get_object_model_3d_params`

## Possible Successors

`connection_object_model_3d`,
`convex_hull_object_model_3d`

## See also

`gen_box_object_model_3d`,
`gen_sphere_object_model_3d`,
`gen_cylinder_object_model_3d`

## Module

3D Metrology
