# add_deformable_surface_model_sample (Operator)

## Name

`add_deformable_surface_model_sample` — Add a sample deformation to a deformable surface model

## Signature

`def add_deformable_surface_model_sample(deformable_surface_model: HHandle, object_model_3d: MaybeSequence[HHandle]) -> None`

## Description

The operator `add_deformable_surface_model_sample` adds the example
deformation passed in *`object_model_3d`* to the deformable surface model
*`deformable_surface_model`*.
The point cloud given in *`object_model_3d`* must have exactly as many
points as the sampled deformation model, and is usually the result of the
operator [`find_deformable_surface_model`](find_deformable_surface_model.md) or
[`refine_deformable_surface_model`](refine_deformable_surface_model.md).
The deformable surface model must have been created beforehand using, for
example, [`create_deformable_surface_model`](create_deformable_surface_model.md).
The operator re-trains the deformable surface model including the
passed deformation. This allows [`find_deformable_surface_model`](find_deformable_surface_model.md) to
find deformations that are similar to the one given in
*`object_model_3d`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator supports canceling timeouts and interrupts.

This operator modifies the state of the following input parameter:

- deformable_surface_model

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`deformable_surface_model`** (input_control, state is modified)  deformable_surface_model `→` HHandle

Handle of the deformable surface model.

**`object_model_3d`** (input_control)  object_model_3d(-array) `→` MaybeSequence[HHandle]

Handle of the deformed 3D object model.

## Result

`add_deformable_surface_model_sample` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`create_deformable_surface_model`,
`find_deformable_surface_model`,
`refine_deformable_surface_model`

## Possible Successors

`find_deformable_surface_model`,
`refine_deformable_surface_model`,
`get_deformable_surface_model_param`,
`write_deformable_surface_model`,
`clear_deformable_surface_model`

## Alternatives

`read_deformable_surface_model`

## See also

`find_deformable_surface_model`,
`refine_deformable_surface_model`,
`read_deformable_surface_model`,
`create_deformable_surface_model`,
`write_deformable_surface_model`,
`clear_deformable_surface_model`

## Module

3D Metrology
