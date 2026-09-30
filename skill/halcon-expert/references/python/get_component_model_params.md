# get_component_model_params (Operator)

## Name

`get_component_model_params` — Return the parameters of a component model.

## Warning

**`get_component_model_params` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def get_component_model_params(component_model_id: HHandle) -> Tuple[Sequence[float], Sequence[int], Sequence[HHandle]]`

`def get_component_model_params_s(component_model_id: HHandle) -> Tuple[float, int, HHandle]`

## Description

The operator `get_component_model_params` returns the
parameters of the component model *`component_model_id`*. In
particular, this output can be used to check the parameters
*`root_ranking`* and *`min_score_comp`* after reading the
component model with [`read_component_model`](read_component_model.md). Additionally, the
operator returns the shape model IDs *`shape_model_ids`* of the
model components. The order of the returned shape model IDs
corresponds to the indices of the components within the component
model *`component_model_id`*. The IDs can be used to query their
shape model parameters with [`get_shape_model_params`](get_shape_model_params.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`component_model_id`** (input_control)  component_model `→` HHandle

Handle of the component model.

**`min_score_comp`** (output_control)  real(-array) `→` Sequence[float]

Minimum score of the instances of the components to
be found.

**`root_ranking`** (output_control)  integer(-array) `→` Sequence[int]

Ranking of the model components expressing their
suitability to act as root component.

**`shape_model_ids`** (output_control)  shape_model(-array) `→` Sequence[HHandle]

Handles of the shape models of the individual model
components.

## Result

If the handle of the component model is valid, the operator
`get_component_model_params` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
