# GetComponentModelParams (Operator)

## Name

`GetComponentModelParams` — Return the parameters of a component model.

## Warning

**`GetComponentModelParams` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.GetComponentModelParams(HTuple componentModelID, out HTuple minScoreComp, out HTuple rootRanking, out HTuple shapeModelIDs)`

`HTuple HComponentModel.GetComponentModelParams(out HTuple rootRanking, out HShapeModel[] shapeModelIDs)`

`double HComponentModel.GetComponentModelParams(out int rootRanking, out HShapeModel shapeModelIDs)`

## Description

The operator `GetComponentModelParams` returns the
parameters of the component model *`componentModelID`*. In
particular, this output can be used to check the parameters
*`rootRanking`* and *`minScoreComp`* after reading the
component model with [`ReadComponentModel`](read_component_model.md). Additionally, the
operator returns the shape model IDs *`shapeModelIDs`* of the
model components. The order of the returned shape model IDs
corresponds to the indices of the components within the component
model *`componentModelID`*. The IDs can be used to query their
shape model parameters with [`GetShapeModelParams`](get_shape_model_params.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`componentModelID`** (input_control)  component_model `→` [HComponentModel](HComponentModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the component model.

**`minScoreComp`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum score of the instances of the components to
be found.

**`rootRanking`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Ranking of the model components expressing their
suitability to act as root component.

**`shapeModelIDs`** (output_control)  shape_model(-array) `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handles of the shape models of the individual model
components.

## Result

If the handle of the component model is valid, the operator
`GetComponentModelParams` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
