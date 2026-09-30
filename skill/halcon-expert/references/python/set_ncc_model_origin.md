# set_ncc_model_origin (Operator)

## Name

`set_ncc_model_origin` — Set the origin (reference point) of an NCC model.

## Signature

`def set_ncc_model_origin(model_id: HHandle, row: float, column: float) -> None`

## Description

The operator `set_ncc_model_origin` sets the origin (reference
point) of the NCC model *`model_id`* to a new value. The origin
is specified relative to the center of gravity of the domain
(region) of the image that was used to create the NCC model with
[`create_ncc_model`](create_ncc_model.md). Hence, an origin of (0,0) means that the
center of gravity of the domain of the model image is used as the
origin. An origin of (-20,-40) means that the origin lies to the
upper left of the center of gravity.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- model_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`model_id`** (input_control, state is modified)  ncc_model `→` HHandle

Handle of the model.

**`row`** (input_control)  point.y `→` float

Row coordinate of the origin of the NCC model.

**`column`** (input_control)  point.x `→` float

Column coordinate of the origin of the NCC model.

## Result

If the handle of the model is valid, the operator
`set_ncc_model_origin` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`create_ncc_model`,
`read_ncc_model`

## Possible Successors

`find_ncc_model`,
`get_ncc_model_origin`,
`find_ncc_models`

## See also

`area_center`

## Module

Matching
