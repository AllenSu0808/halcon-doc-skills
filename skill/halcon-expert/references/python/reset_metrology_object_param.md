# reset_metrology_object_param (Operator)

## Name

`reset_metrology_object_param` — Reset all parameters of a metrology model.

## Signature

`def reset_metrology_object_param(metrology_handle: HHandle, index: MaybeSequence[Union[str, int]]) -> None`

## Description

`reset_metrology_object_param` discards all settings of the
parameters for the metrology objects that can be
set by the operator [`set_metrology_object_param`](set_metrology_object_param.md) and restores
the default values.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by
the handle *`metrology_handle`*. The parameter *`index`*
determines the metrology objects to reset. With *`index`* set
to *"all"*, all metrology objects are reset.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- metrology_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`metrology_handle`** (input_control, state is modified)  metrology_model `→` HHandle

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` MaybeSequence[Union[str, int]]

Index of the metrology objects.

Default:
"all"

Suggested values:
"all", 0, 1, 2

## Result

If the parameters are valid, the operator
`reset_metrology_object_param` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`set_metrology_object_param`

## See also

`reset_metrology_object_fuzzy_param`

## Module

2D Metrology
