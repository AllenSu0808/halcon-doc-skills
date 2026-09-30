# moments_object_model_3d (Operator)

## Name

`moments_object_model_3d` — Calculates the mean or the central moment of second order for a 3D object
model.

## Signature

`moments_object_model_3d( : : ObjectModel3D, MomentsToCalculate : Moments)`

## Description

`moments_object_model_3d` calculates the mean or
the central moment of second order for a 3D object model.
To calculate the mean of the points of the 3D object model,
select *'mean_points'*
in *`MomentsToCalculate`*. If instead the central moment
of second order should be calculated, select
*'central_moment_2_points'*. The results are the variances
of the x, y, z, x-y, x-z, and y-z axes.
To compute the three principal axes of the 3D object model
select *'principal_axes'* in *`MomentsToCalculate`*.
The result is a pose with the mean of the points as center. The
coordinate system that corresponds to the pose has the
x-axis along the first principal axis, the y-axis along the second
principal axis and the z-axis along the third principal axis.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handle of the 3D object model.

**`MomentsToCalculate`** (input_control)  number(-array) `→`  (string)

Moment to calculate.

Default:
'mean_points'

List of values:
'central_moment_2_points', 'mean_points', 'principal_axes'

**`Moments`** (output_control)  number(-array) `→`  (real)

Calculated moment.

Number of elements:
Moments == ObjectModel3D

## Example (HDevelop)

```
gen_object_model_3d_from_points (rand(200), rand(200),\
                                  rand(200), ObjectModel3D)
moments_object_model_3d (ObjectModel3D, ['mean_points',\
                         'central_moment_2_points','principal_axes'], \
                         Moments)
```

## Result

`moments_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`connection_object_model_3d`

## Possible Successors

`project_object_model_3d`,
`object_model_3d_to_xyz`,
`select_object_model_3d`

## See also

`volume_object_model_3d_relative_to_plane`

## Module

3D Metrology
