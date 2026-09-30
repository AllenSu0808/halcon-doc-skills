# get_shape_model_params (Operator)

## Name

`get_shape_model_params` — Return the parameters of a shape model.

## Signature

`def get_shape_model_params(model_id: HHandle) -> Tuple[Sequence[int], float, float, float, Sequence[float], Sequence[float], Sequence[float], str, int]`

`def get_shape_model_params_s(model_id: HHandle) -> Tuple[int, float, float, float, float, float, float, str, int]`

## Description

The operator `get_shape_model_params` returns the parameters
of the shape model *`model_id`* that were used to create it
using [`create_shape_model`](create_shape_model.md), [`create_scaled_shape_model`](create_scaled_shape_model.md),
or [`create_aniso_shape_model`](create_aniso_shape_model.md). In particular, this output can
be used to check the parameters *`num_levels`*,
*`angle_step`*, *`scale_step`*, and *`min_contrast`* if
they were determined automatically during the model creation with
[`create_shape_model`](create_shape_model.md), [`create_scaled_shape_model`](create_scaled_shape_model.md), or
[`create_aniso_shape_model`](create_aniso_shape_model.md).

If the *`model_id`* was adapted with
[`adapt_shape_model_high_noise`](adapt_shape_model_high_noise.md), NumLevels contains two values: the
highest pyramid level and the estimated lowest pyramid level.

If the shape model was created using [`create_shape_model`](create_shape_model.md) or
[`create_scaled_shape_model`](create_scaled_shape_model.md) a single value is returned in
*`scale_min`*, *`scale_max`*, and *`scale_step`*. This
parameters corresponds to the isotropic scaling parameters of the
shape model. If the shape model was created using
[`create_aniso_shape_model`](create_aniso_shape_model.md) two values each are returned in the
above three parameters. Here, the first value of the respective
parameter refers to the scaling in the row direction, while the
second value refers to the scaling in the column direction.

Note that the parameters `optimization` and
`contrast` that also can be determined automatically during
the model creation cannot be queried by using
`get_shape_model_params`. If their value is of interest
[`determine_shape_model_params`](determine_shape_model_params.md) should be used instead.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`model_id`** (input_control)  shape_model `→` HHandle

Handle of the model.

**`num_levels`** (output_control)  integer(-array) `→` Sequence[int]

Number of pyramid levels.

**`angle_start`** (output_control)  angle.rad `→` float

Smallest rotation of the pattern.

**`angle_extent`** (output_control)  angle.rad `→` float

Extent of the rotation angles.

Assertion:
`AngleExtent >= 0`

**`angle_step`** (output_control)  angle.rad `→` float

Step length of the angles (resolution).

Assertion:
`AngleStep >= 0 && AngleStep <= pi / 2`

**`scale_min`** (output_control)  number(-array) `→` Sequence[float]

Minimum scale of the pattern.

Assertion:
`ScaleMin > 0`

**`scale_max`** (output_control)  number(-array) `→` Sequence[float]

Maximum scale of the pattern.

Assertion:
`ScaleMax >= ScaleMin`

**`scale_step`** (output_control)  number(-array) `→` Sequence[float]

Scale step length (resolution).

Assertion:
`ScaleStep >= 0`

**`metric`** (output_control)  string `→` str

Match metric.

**`min_contrast`** (output_control)  number `→` int

Minimum contrast of the objects in the search images.

## Result

If the handle of the model is valid, the operator
`get_shape_model_params` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`create_shape_model`,
`create_scaled_shape_model`,
`create_aniso_shape_model`,
`read_shape_model`

## Alternatives

`get_generic_shape_model_param`

## See also

`find_shape_model`,
`find_scaled_shape_model`,
`find_aniso_shape_model`,
`find_shape_models`,
`find_scaled_shape_models`,
`find_aniso_shape_models`

## Module

Matching
