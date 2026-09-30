# gen_sphere_object_model_3d (Operator)

## Name

`gen_sphere_object_model_3d` — Create a 3D object model that represents a sphere.

## Signature

`def gen_sphere_object_model_3d(pose: Sequence[Union[int, float]], radius: MaybeSequence[float]) -> Sequence[HHandle]`

`def gen_sphere_object_model_3d_s(pose: Sequence[Union[int, float]], radius: MaybeSequence[float]) -> HHandle`

## Description

`gen_sphere_object_model_3d` creates a sphere-shaped 3D
primitive, i.e., a 3D object model that represents a sphere.
A sphere is defined by its center given in *`pose`* and its radius
given in *`radius`*.
The handle of the
3D object model is returned by the parameter *`object_model_3d`*.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of created items is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`pose`** (input_control)  pose(-array) `→` Sequence[Union[int, float]]

The pose that describes the position of
the sphere.

**`radius`** (input_control)  number(-array) `→` MaybeSequence[float]

The radius of the sphere.

**`object_model_3d`** (output_control)  object_model_3d(-array) `→` Sequence[HHandle]

Handle of the resulting 3D object model.

## Result

`gen_sphere_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`smallest_sphere_object_model_3d`

## Possible Successors

`get_object_model_3d_params`,
`sample_object_model_3d`,
`clear_object_model_3d`

## Alternatives

`gen_sphere_object_model_3d_center`

## See also

`gen_cylinder_object_model_3d`,
`gen_plane_object_model_3d`,
`gen_box_object_model_3d`

## Module

3D Metrology
