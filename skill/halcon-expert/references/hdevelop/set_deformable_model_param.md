# set_deformable_model_param (Operator)

## Name

`set_deformable_model_param` — Set selected parameters of the deformable model.

## Signature

`set_deformable_model_param( : : ModelID, GenParamName, GenParamValue : )`

## Description

The operator `set_deformable_model_param` sets the selected parameters
*`GenParamName`* in the deformable model *`ModelID`*. The
following parameters can be modified:

*'min_contrast'*

Sets the minimum contrast of the object in the search images for the
deformable model *`ModelID`*.
Thereby, the value of *'min_contrast'* that was originally set, e.g.,
with [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md), is overwritten
for the deformable model *`ModelID`*. Note that if the
deformable model *`ModelID`* was read from
file and if this file should be changed as well, the deformable model
*`ModelID`* must again be written to file after the execution of the
operator `set_deformable_model_param`.

*'get_deformable_model_contours_coord_system'*

Sets the coordinate system in which the contours are returned when
calling the operator [`get_deformable_model_contours`](get_deformable_model_contours.md).
If *'world'* is passed, the contours
are returned in the world coordinate system in metric units. Note that
this is only possible for the calibrated case. If *'image'*
is passed, the contours are returned in the image coordinate system
in pixel units. In the calibrated case this system corresponds to the
rectified image coordinate system. The
rectified image coordinate system is the coordinate system of an image
one would obtain by [`change_radial_distortion_image`](change_radial_distortion_image.md) when
using the rectified camera parameters. The rectified camera parameters
can be queried by [`get_deformable_model_params`](get_deformable_model_params.md). If the model
was created by [`create_planar_calib_deformable_model_xld`](create_planar_calib_deformable_model_xld.md)
the value of *'get_deformable_model_contours_coord_system'*
is *'world'* by default. In all other cases it is
*'image'* by default.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ModelID`** (input_control, state is modified)  deformable_model `→`  (handle)

Handle of the model.

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Parameter names.

List of values:
'get_deformable_model_contours_coord_system', 'min_contrast'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (real / integer / string)

Parameter values.

Suggested values:
5, 6, 7, 8, 9, 10, 'image', 'world'

## Result

If the parameters are valid, the operator `set_deformable_model_param`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`create_planar_uncalib_deformable_model`,
`create_planar_calib_deformable_model`,
`create_local_deformable_model`,
`read_deformable_model`

## Possible Successors

`find_planar_uncalib_deformable_model`,
`find_planar_calib_deformable_model`

## See also

`get_deformable_model_contours`,
`get_deformable_model_params`

## Module

Matching
