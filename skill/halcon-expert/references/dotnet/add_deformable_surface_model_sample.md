# AddDeformableSurfaceModelSample (Operator)

## Name

`AddDeformableSurfaceModelSample` — Add a sample deformation to a deformable surface model

## Signature

`static void HOperatorSet.AddDeformableSurfaceModelSample(HTuple deformableSurfaceModel, HTuple objectModel3D)`

`static void HObjectModel3D.AddDeformableSurfaceModelSample(HDeformableSurfaceModel deformableSurfaceModel, HObjectModel3D[] objectModel3D)`

`void HObjectModel3D.AddDeformableSurfaceModelSample(HDeformableSurfaceModel deformableSurfaceModel)`

`void HDeformableSurfaceModel.AddDeformableSurfaceModelSample(HObjectModel3D[] objectModel3D)`

`void HDeformableSurfaceModel.AddDeformableSurfaceModelSample(HObjectModel3D objectModel3D)`

## Description

The operator `AddDeformableSurfaceModelSample` adds the example
deformation passed in *`objectModel3D`* to the deformable surface model
*`deformableSurfaceModel`*.
The point cloud given in *`objectModel3D`* must have exactly as many
points as the sampled deformation model, and is usually the result of the
operator [`FindDeformableSurfaceModel`](find_deformable_surface_model.md) or
[`RefineDeformableSurfaceModel`](refine_deformable_surface_model.md).
The deformable surface model must have been created beforehand using, for
example, [`CreateDeformableSurfaceModel`](create_deformable_surface_model.md).
The operator re-trains the deformable surface model including the
passed deformation. This allows [`FindDeformableSurfaceModel`](find_deformable_surface_model.md) to
find deformations that are similar to the one given in
*`objectModel3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator supports canceling timeouts and interrupts.

This operator modifies the state of the following input parameter:

- deformableSurfaceModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`deformableSurfaceModel`** (input_control, state is modified)  deformable_surface_model `→` [HDeformableSurfaceModel](HDeformableSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deformable surface model.

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deformed 3D object model.

## Result

`AddDeformableSurfaceModelSample` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`CreateDeformableSurfaceModel`,
`FindDeformableSurfaceModel`,
`RefineDeformableSurfaceModel`

## Possible Successors

`FindDeformableSurfaceModel`,
`RefineDeformableSurfaceModel`,
`GetDeformableSurfaceModelParam`,
`WriteDeformableSurfaceModel`,
`ClearDeformableSurfaceModel`

## Alternatives

`ReadDeformableSurfaceModel`

## See also

`FindDeformableSurfaceModel`,
`RefineDeformableSurfaceModel`,
`ReadDeformableSurfaceModel`,
`CreateDeformableSurfaceModel`,
`WriteDeformableSurfaceModel`,
`ClearDeformableSurfaceModel`

## Module

3D Metrology
