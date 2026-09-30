# set_shape_model_param (Operator)

## Name

`set_shape_model_param` — Set selected parameters of the shape model.

## Signature

`set_shape_model_param( : : ModelID, GenParamName, GenParamValue : )`

## Description

The operator `set_shape_model_param` sets the selected parameters
*`GenParamName`* in the shape model *`ModelID`*. The following
parameters can be modified:

*'min_contrast'*

Sets the minimum contrast of the object in the search images for the shape
model *`ModelID`*.
Thereby, the value of *'min_contrast'* that was originally set,
e.g., with [`create_shape_model`](create_shape_model.md), is overwritten for the shape model
*`ModelID`*. Note that if the shape model *`ModelID`* was read from
file and if this file should be changed as well, the shape model
*`ModelID`* must again be written to file after the execution of the
operator `set_shape_model_param`.

*'timeout'*

Sets the maximum runtime of the operators used to find the shape model
*`ModelID`* (e.g., [`find_shape_model`](find_shape_model.md)). This is especially useful
in cases where a maximum cycle time has to be ensured. The *'timeout'*
must be given in milliseconds. The temporal accuracy depends on several
factors including the size of the model, the speed of your computer, and
the *'timer_mode'* set via [`set_system`](set_system.md). Be aware that the
runtime of the search increases by up to 10 percent with activated timeout.
To disable the timeout you can either use a negative value or
*'false'*.

*'border_shape_models'*

This parameter determines whether the shape model *`ModelID`* to be
found with, e.g., [`find_shape_model`](find_shape_model.md), may lie partially outside the
image (i.e., whether they may cross the image border). Partially means that
the model's origin still must be located within the image. A different origin
set with [`set_shape_model_origin`](set_shape_model_origin.md) is not taken into account.

The value of *'border_shape_models'* can be *'true'*,
*'false'*, or *'system'*. The value *'system'*
is the default behavior and uses the system-wide used value that was set by
[`set_system`](set_system.md) for the parameter *'border_shape_models'*.

*'use_clutter'*

Disables or enables the use of clutter parameters for the shape model
*`ModelID`*, which have been set previously using
[`set_shape_model_clutter`](set_shape_model_clutter.md). The value of *'use_clutter'* can be
*'true'* or *'false'*. Note that the value of
*'use_clutter'* affects the expected number of entries in the input
parameter `MinScore` of the find operators. Please refer to the
documentation of the different find operators, e.g., [`find_shape_model`](find_shape_model.md).

For newly created shape models, the use of clutter parameters is disabled.
After calling [`set_shape_model_clutter`](set_shape_model_clutter.md), the use of clutter parameters is
enabled. Clutter parameters and the value of *'use_clutter'* can be
queried using [`get_shape_model_clutter`](get_shape_model_clutter.md).

*'model_cache'*

Disables or enables the use of an internal cache based on temporary memory
that is used by a shape model when it executes, e.g., [`find_shape_model`](find_shape_model.md).
The size of the cache depends on whether the find operation needs a big
parameter space with many discretization steps.
This means that a small `AngleStep` and
`ScaleStep` and a big `AngleExtent` and a big range given by
`ScaleMin` and `ScaleMax` result in a
big memory consumption.
Switching the *'model_cache'* off (by setting *'false'*) sometimes
results in slightly longer execution times but constantly small memory
footprint, particularly important in embedded applications.
By default, this cache is switched on (*'true'*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ModelID`** (input_control, state is modified)  shape_model `→`  (handle)

Handle of the model.

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Parameter names.

List of values:
'border_shape_models', 'min_contrast', 'model_cache', 'timeout', 'use_clutter'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (real / integer / string)

Parameter values.

List of values:
'false', 'system', 'true'

## Result

If the parameters are valid, the operator `set_shape_model_param`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`create_shape_model_xld`,
`create_scaled_shape_model_xld`,
`create_aniso_shape_model_xld`

## Possible Successors

`find_shape_model`,
`find_scaled_shape_model`,
`find_aniso_shape_model`

## Alternatives

`set_generic_shape_model_param`

## See also

`create_shape_model_xld`,
`create_scaled_shape_model_xld`,
`create_aniso_shape_model_xld`,
`set_shape_model_clutter`,
`get_shape_model_clutter`

## Module

Matching
