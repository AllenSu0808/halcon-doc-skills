# remove_object_model_3d_attrib_mod (Operator)

## Name

`remove_object_model_3d_attrib_mod` — Remove attributes of a 3D object model.

## Signature

`remove_object_model_3d_attrib_mod( : : ObjectModel3D, Attributes : )`

## Description

`remove_object_model_3d_attrib_mod` removes the standard and/or extended
attributes given in *`Attributes`* of a 3D object model
*`ObjectModel3D`*.
Doing so changes the 3D object model. This is in contrast to the
operator [`remove_object_model_3d_attrib`](remove_object_model_3d_attrib.md), which creates a new model
but functions identically otherwise.

If the *`Attributes`* do not exist in *`ObjectModel3D`*, no
exception is raised.

For a detailed description of *`Attributes`* see operator
[`remove_object_model_3d_attrib`](remove_object_model_3d_attrib.md).

## Attention

`remove_object_model_3d_attrib_mod` removes *`Attributes`*
unchecked from the 3D object model. Special attention must be paid
to retain a consistent 3D object model, as most of the operators expect
consistent 3D object models. Furthermore, the mapping of the 3D points to
image coordinates should not be removed because it speeds up the
computation of many operators.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d `→`  (handle)

Handle of the input 3D object model.

**`Attributes`** (input_control)  string(-array) `→`  (string)

Name of the attributes to be removed.

Default:
'extended_attribute'

List of values:
'all', 'blue', 'distance_computation_data', 'extended_attribute', 'green', 'lines', 'original_point_indices', 'point_normal', 'polygons', 'primitive_box', 'primitive_cylinder', 'primitive_plane', 'primitive_sphere', 'primitives_all', 'red', 'score', 'shape_based_matching_3d_data', 'triangles', 'xyz_mapping'

## Result

If the parameters are valid, the operator
`remove_object_model_3d_attrib_mod` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`set_object_model_3d_attrib_mod`

## Possible Successors

`get_object_model_3d_params`

## Alternatives

`remove_object_model_3d_attrib`

## See also

`copy_object_model_3d`,
`set_object_model_3d_attrib_mod`

## Module

3D Metrology
