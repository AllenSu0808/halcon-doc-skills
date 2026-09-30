# create_deformable_surface_model (Operator)

## Name

`create_deformable_surface_model` — Create the data structure needed to perform deformable
surface-based matching.

## Signature

`create_deformable_surface_model( : : ObjectModel3D, RelSamplingDistance, GenParamName, GenParamValue : DeformableSurfaceModel)`

## Description

The operator `create_deformable_surface_model` creates a model for
deformable surface-based matching for the 3D object stored in the
3D object model *`ObjectModel3D`*.
The 3D object model can, for example, have been read previously from a file
by using [`read_object_model_3d`](read_object_model_3d.md) or it can have been created by using
[`xyz_to_object_model_3d`](xyz_to_object_model_3d.md).
The created surface model is returned in *`DeformableSurfaceModel`*.

The creation of the deformable surface model requires that the 3D object model
contains points and normals. The following combinations are possible:

- points and point normals, e.g., from a call to
  [`surface_normals_object_model_3d`](surface_normals_object_model_3d.md)
- points and a triangular or polygon mesh, e.g., from a CAD file
- points and a 2D-Mapping, e.g., from an XYZ image triple converted with
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md)

Note that the direction and orientation (inward or outward) of the normals
of the model are important for matching.

The deformable surface model is created by sampling the 3D object model with
a certain distance.
The sampling distance must be specified in the parameter
*`RelSamplingDistance`* and is parametrized relative to the diameter
of the axis-parallel bounding box of the 3D object model.
For example, if *`RelSamplingDistance`* is set to 0.05 and
the diameter of *`ObjectModel3D`* is 10 cm, the points
sampled from the object's surface will be approximately 5 mm
apart.
The sampled points can be obtained with the operator
[`get_deformable_surface_model_param`](get_deformable_surface_model_param.md) using the value
*'sampled_model'*.
Note that outlier points in the object model should be avoided, as they would
corrupt the diameter.
Reducing *`RelSamplingDistance`* leads to more points, and in turn
to a more stable but slower matching. Increasing
*`RelSamplingDistance`* leads to less points, and in turn to a less
stable but faster matching.

|  |  |  |  |
| --- | --- | --- | --- |
| ![figure](../assets/030e47a431e61de4.svg) | ![figure](../assets/5d7237c57f6ab936.svg) | ![figure](../assets/828c81224b55bc7d.svg) | ![figure](../assets/fd3aa3ea4b54bbeb.svg) |
| ( 1) | ( 2) | ( 3) | ( 4) |

(1) Original 3D model. (2) 3D model sampled with
*`RelSamplingDistance`* = *0.02*.
(3) *`RelSamplingDistance`* = *0.03*.
(4) *`RelSamplingDistance`* = *0.05*.

By default, deformable surface models created with
`create_deformable_surface_model` can handle a moderate amount of
deformation. The operator [`add_deformable_surface_model_sample`](add_deformable_surface_model_sample.md)
can be used to add additional training samples, thus expanding the
range of possible deformations.
The amount of deformation that can be found can also be controlled with the
generic parameters *'scale_min'*, *'scale_max'* and
*'bending_max'* (see below).

The generic parameter pair *`GenParamName`* and *`GenParamValue`*
is used to set additional parameters for the model generation.
*`GenParamName`* contains the tuple of parameter names that shall be
set and *`GenParamValue`* contains the corresponding values.
The following values are possible for *`GenParamName`*:

- ***'model_invert_normals'*:** —

  Invert the orientation of the surface normals of the model.
  The normal orientation needs to be known for the model generation.
  If both the model and the scene are acquired with the same setup,
  the normals will already point in the same direction.
  If the model was loaded from a CAD file, the normals might point
  into the opposite direction. If you experience the effect that the
  model is found on the 'outside' of the scene surface and the
  model was created from a CAD file, try to set this parameter to
  *'true'*.
  Also, make sure that the normals in the CAD file all point either
  outward or inward, i.e., are oriented consistently.

  List of values:
   *'false'*, *'true'*

  Default:
   *'false'*
- ***'scale_min'* and *'scale_max'*:** —

  The minimum and maximum allowed scaling of the model.
  Note that if you set one of the two parameters, the other one must
  be set too.

  Suggested values:
  *0.8*, *1*, *1.2*

  Default:
   No scaling

  Restriction:
   *0* < *'scale_min'* < *'scale_max'*
- ***'bending_max'*:** —

  Controls the maximum automatic deformation of the model.
  The model is deformed automatically by bending it with an angle up
  to the value of *'bending_max'*. This allows for deformations to be found
  that are within this bending range.
  The angle is passed in degrees.

  Suggested values:
  *5*, *10*, *30*

  Default:
   *20*

  Restriction:
   *0* <= *'bending_max'* < *90*
- ***'stiffness'*:** —

  Control the stiffness of the model when performing the
  refinement.
  Larger values of this parameter lead to a more stiff model that can
  be less deformed. Smaller values lead to a less stiff model that
  allows more deformation.

  Suggested values:
  *0.2*, *0.5*, *0.8*

  Default:
   *0.5*

  Restriction:
   *0* < *'stiffness'* <= *1*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d `→`  (handle)

Handle of the 3D object model.

**`RelSamplingDistance`** (input_control)  real `→`  (real)

Sampling distance relative to the object's diameter

Default:
0.05

Suggested values:
0.1, 0.05, 0.03, 0.02, 0.01

Restriction:
`0 < RelSamplingDistance < 1`

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Names of the generic parameters.

Default:
[]

Suggested values:
'model_invert_normals', 'scale_min', 'scale_max', 'bending_max', 'stiffness'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / real / integer)

Values of the generic parameters.

Default:
[]

Suggested values:
'true', 'false', 1, 0.9, 1.1, 5, 10, 20, 30, 0.05, 0.1, 0.2

**`DeformableSurfaceModel`** (output_control)  deformable_surface_model `→`  (handle)

Handle of the deformable surface model.

## Result

`create_deformable_surface_model` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`,
`get_object_model_3d_params`

## Possible Successors

`add_deformable_surface_model_sample`,
`add_deformable_surface_model_reference_point`,
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
`add_deformable_surface_model_sample`,
`add_deformable_surface_model_reference_point`,
`write_deformable_surface_model`,
`clear_deformable_surface_model`

## References

Bertram Drost, Slobodan Ilic: “Graph-Based Deformable
3D Object Matching.” Proceedings of the 37th German Conference
on Pattern Recognition, pp. 222-233, 2015.

## Module

3D Metrology
