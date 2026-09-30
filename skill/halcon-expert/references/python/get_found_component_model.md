# get_found_component_model (Operator)

## Name

`get_found_component_model` — Return the components of a found instance of a component model.

## Warning

**`get_found_component_model` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def get_found_component_model(component_model_id: HHandle, model_start: MaybeSequence[int], model_end: MaybeSequence[int], row_comp: MaybeSequence[float], column_comp: MaybeSequence[float], angle_comp: MaybeSequence[float], score_comp: MaybeSequence[float], model_comp: MaybeSequence[int], model_match: int, mark_orientation: str) -> Tuple[HObject, Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def get_found_component_model_s(component_model_id: HHandle, model_start: MaybeSequence[int], model_end: MaybeSequence[int], row_comp: MaybeSequence[float], column_comp: MaybeSequence[float], angle_comp: MaybeSequence[float], score_comp: MaybeSequence[float], model_comp: MaybeSequence[int], model_match: int, mark_orientation: str) -> Tuple[HObject, float, float, float, float]`

## Description

`get_found_component_model` returns the components of a found
instance of the component model *`component_model_id`* in form of
contour regions in *`found_components`* as well as in numerical
form.

The operator `get_found_component_model` is particularly
useful in order to visualize the matches that have been obtained by
[`find_component_model`](find_component_model.md).

The pose of the returned components corresponds to their pose in the
search image as returned by [`find_component_model`](find_component_model.md). Hence, the
parameters *`model_start`*, *`model_end`*, *`row_comp`*,
*`column_comp`*, *`angle_comp`*, *`score_comp`*, and
*`model_comp`* must be passed to
`get_found_component_model` as they have been returned by
[`find_component_model`](find_component_model.md). In *`model_match`* the index of
the found instance of the component model must be passed.
Consequently, *`model_match`* must lie within the range between
0 and *m*-1, where *m* is the number of elements in
*`model_start`* and *`model_end`*, and hence corresponds to
the number of found model instances. For example, if the best match
should be returned, *`model_match`* should be set to *0*.

When dealing with rotationally symmetric components, one may wish to
mark the current orientation of the found component. This can be
achieved by setting *`mark_orientation`* to *"true"*. In
this case, the contour region of each component is complemented by
an arrow at its reference point that points in the reference
direction. The reference direction of a component is based on the
orientation of the component in the model image (see
[`train_model_components`](train_model_components.md) or [`create_component_model`](create_component_model.md))
and is represented by an arrow that starts at the reference point
and points to the right in the horizontal direction.

For convenience, the pose parameters as well as the score of each
component of the found model instance are additionally returned in
numerical form in *`row_comp_inst`*, *`column_comp_inst`*,
*`angle_comp_inst`*, and *`score_comp_inst`*. The four tuples
are always of length *n*, where *n* is the number of
components in the component model *`component_model_id`*. If a
component could not be found during the search, an empty region is
passed in the corresponding element of *`found_components`* and
the value of the corresponding element in *`row_comp_inst`*,
*`column_comp_inst`*, *`angle_comp_inst`*, and
*`score_comp_inst`* is set to *0*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`found_components`** (output_object)  region-array `→` HObject

Found components of the selected component model
instance.

**`component_model_id`** (input_control)  component_model `→` HHandle

Handle of the component model.

**`model_start`** (input_control)  integer(-array) `→` MaybeSequence[int]

Start index of each found instance of the component
model in the tuples describing the component matches.

**`model_end`** (input_control)  integer(-array) `→` MaybeSequence[int]

End index of each found instance of the component
model to the tuples describing the component matches.

**`row_comp`** (input_control)  point.y(-array) `→` MaybeSequence[float]

Row coordinate of the found component matches.

**`column_comp`** (input_control)  point.x(-array) `→` MaybeSequence[float]

Column coordinate of the found component matches.

**`angle_comp`** (input_control)  angle.rad(-array) `→` MaybeSequence[float]

Rotation angle of the found component matches.

**`score_comp`** (input_control)  real(-array) `→` MaybeSequence[float]

Score of the found component matches.

**`model_comp`** (input_control)  integer(-array) `→` MaybeSequence[int]

Index of the found components.

**`model_match`** (input_control)  integer `→` int

Index of the found instance of the component model
to be returned.

**`mark_orientation`** (input_control)  string `→` str

Mark the orientation of the components.

Default:
"false"

List of values:
"false", "true"

**`row_comp_inst`** (output_control)  point.y(-array) `→` Sequence[float]

Row coordinate of all components of the selected
model instance.

**`column_comp_inst`** (output_control)  point.x(-array) `→` Sequence[float]

Column coordinate of all components of the selected
model instance.

**`angle_comp_inst`** (output_control)  angle.rad(-array) `→` Sequence[float]

Rotation angle of all components of the selected model
instance.

**`score_comp_inst`** (output_control)  real(-array) `→` Sequence[float]

Score of all components of the selected model
instance.

## Result

If the parameters are valid, the operator
`get_found_component_model` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
