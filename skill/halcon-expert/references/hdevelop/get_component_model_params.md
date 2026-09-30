# get_component_model_params (Operator)

## Name

`get_component_model_params` — Return the parameters of a component model.

## Warning

**`get_component_model_params` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`get_component_model_params( : : ComponentModelID : MinScoreComp, RootRanking, ShapeModelIDs)`

## Description

The operator `get_component_model_params` returns the
parameters of the component model *`ComponentModelID`*. In
particular, this output can be used to check the parameters
*`RootRanking`* and *`MinScoreComp`* after reading the
component model with [`read_component_model`](read_component_model.md). Additionally, the
operator returns the shape model IDs *`ShapeModelIDs`* of the
model components. The order of the returned shape model IDs
corresponds to the indices of the components within the component
model *`ComponentModelID`*. The IDs can be used to query their
shape model parameters with [`get_shape_model_params`](get_shape_model_params.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`ComponentModelID`** (input_control)  component_model `→`  (handle)

Handle of the component model.

**`MinScoreComp`** (output_control)  real(-array) `→`  (real)

Minimum score of the instances of the components to
be found.

**`RootRanking`** (output_control)  integer(-array) `→`  (integer)

Ranking of the model components expressing their
suitability to act as root component.

**`ShapeModelIDs`** (output_control)  shape_model(-array) `→`  (handle)

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
