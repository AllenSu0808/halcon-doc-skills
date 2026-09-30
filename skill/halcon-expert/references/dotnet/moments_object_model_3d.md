# MomentsObjectModel3d (Operator)

## Name

`MomentsObjectModel3d` — Calculates the mean or the central moment of second order for a 3D object
model.

## Signature

`static void HOperatorSet.MomentsObjectModel3d(HTuple objectModel3D, HTuple momentsToCalculate, out HTuple moments)`

`static HTuple HObjectModel3D.MomentsObjectModel3d(HObjectModel3D[] objectModel3D, HTuple momentsToCalculate)`

`double HObjectModel3D.MomentsObjectModel3d(string momentsToCalculate)`

## Description

`MomentsObjectModel3d` calculates the mean or
the central moment of second order for a 3D object model.
To calculate the mean of the points of the 3D object model,
select *"mean_points"*
in *`momentsToCalculate`*. If instead the central moment
of second order should be calculated, select
*"central_moment_2_points"*. The results are the variances
of the x, y, z, x-y, x-z, and y-z axes.
To compute the three principal axes of the 3D object model
select *"principal_axes"* in *`momentsToCalculate`*.
The result is a pose with the mean of the points as center. The
coordinate system that corresponds to the pose has the
x-axis along the first principal axis, the y-axis along the second
principal axis and the z-axis along the third principal axis.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`momentsToCalculate`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*string*)

Moment to calculate.

Default:
"mean_points"

List of values:
"central_moment_2_points", "mean_points", "principal_axes"

**`moments`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

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

`MomentsObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`ConnectionObjectModel3d`

## Possible Successors

`ProjectObjectModel3d`,
`ObjectModel3dToXyz`,
`SelectObjectModel3d`

## See also

`VolumeObjectModel3dRelativeToPlane`

## Module

3D Metrology
