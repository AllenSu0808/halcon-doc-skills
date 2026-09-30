# determine_ncc_model_params (Operator)

## Name

`determine_ncc_model_params` — Determine the parameters of an NCC model.

## Signature

`def determine_ncc_model_params(template: HObject, num_levels: Union[int, str], angle_start: float, angle_extent: float, metric: str, parameters: MaybeSequence[str]) -> Tuple[Sequence[str], Sequence[Union[int, float]]]`

## Description

`determine_ncc_model_params` determines certain parameters
of an NCC model automatically from the model image
*`template`*. The parameters to be determined can be specified
with *`parameters`*. `determine_ncc_model_params` can
be used to determine the same parameters that are determined
automatically when the respective parameter in
[`create_ncc_model`](create_ncc_model.md) is set to *"auto"*: the
number of pyramid levels (*`parameters`* =
*"num_levels"*) and/or the angle step length
(*`parameters`* = *"angle_step"*). By passing a tuple
of the above values in *`parameters`*, an arbitrary combination
of these parameters can be determined. If all of the above
parameters should be determined, the value *"all"* can be
passed.

`determine_ncc_model_params` is mainly useful to determine
the above parameters before creating the model, e.g., in an
interactive system, which makes suggestions for these parameters to
the user, but enables the user to modify the suggested values.

The automatically determined parameters are returned as a name-value
pair in *`parameter_name`* and *`parameter_value`*. The
parameter names in *`parameter_name`* are identical to the names
in *`parameters`*, where, of course, the value *"all"*
is replaced by the actual parameter names.

The input parameters (*`num_levels`*, *`angle_start`*,
*`angle_extent`*, and *`metric`*) have the same meaning as
in [`create_ncc_model`](create_ncc_model.md). The description of these parameters
can be looked up with this operator. These parameters are used
by `determine_ncc_model_params` to calculate the parameters
to be determined in the same manner as in [`create_ncc_model`](create_ncc_model.md).

Note that in `determine_ncc_model_params` the input
parameter *`num_levels`* can also be determined automatically.
If this parameter should not be determined automatically, i.e.,
the name is not passed in *`parameters`*, the parameter must
contain a valid value and must not be set to *"auto"*. In
contrast, if the maximum number of pyramid levels is to be
determined automatically, i.e., *`parameters`* contains the
value *"num_levels"*, you can let HALCON determine a
suitable value and at the same time specify an upper boundary:

If the maximum number of pyramid levels should be specified in
advance, the input parameter *`num_levels`* can be set to the
particular value. If in this case *`parameters`* contains
the value *"num_levels"*, the computed number of pyramid
levels is at most *`num_levels`*. If *`num_levels`* is
set to *"auto"* or *0*, the number of pyramid levels
is determined without restrictions as large as possible.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`template`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image whose domain will be used to create
the model.

**`num_levels`** (input_control)  integer `→` Union[int, str]

Maximum number of pyramid levels.

Default:
"auto"

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "auto"

**`angle_start`** (input_control)  angle.rad `→` float

Smallest rotation of the model.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`angle_extent`** (input_control)  angle.rad `→` float

Extent of the rotation angles.

Default:
0.79

Suggested values:
6.29, 3.14, 1.57, 0.79, 0.39

Restriction:
`AngleExtent >= 0`

**`metric`** (input_control)  string `→` str

Match metric.

Default:
"use_polarity"

List of values:
"ignore_global_polarity", "use_polarity"

**`parameters`** (input_control)  string(-array) `→` MaybeSequence[str]

Parameters to be determined automatically.

Default:
"all"

List of values:
"all", "angle_step", "num_levels"

**`parameter_name`** (output_control)  string-array `→` Sequence[str]

Name of the automatically determined parameter.

**`parameter_value`** (output_control)  number-array `→` Sequence[Union[int, float]]

Value of the automatically determined parameter.

## Result

If the parameters are valid, the operator
`determine_ncc_model_params` returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`create_ncc_model`

## See also

`find_ncc_model`

## Module

Matching
