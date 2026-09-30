# reset_metrology_object_fuzzy_param (Operator)

## Name

`reset_metrology_object_fuzzy_param` — Reset all fuzzy parameters and fuzzy functions of a metrology
model.

## Signature

`reset_metrology_object_fuzzy_param( : : MetrologyHandle, Index : )`

## Description

`reset_metrology_object_fuzzy_param` discards all fuzzy
parameters and fuzzy functions of the metrology objects
that can be set by the operator [`set_metrology_object_fuzzy_param`](set_metrology_object_fuzzy_param.md)
and restores the default values.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`MetrologyHandle`*. The
parameter *`Index`* determines the metrology objects to reset. With
*`Index`* set to *'all'*, all metrology objects are reset.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MetrologyHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MetrologyHandle`** (input_control, state is modified)  metrology_model `→`  (handle)

Handle of the metrology model.

**`Index`** (input_control)  integer(-array) `→`  (string / integer)

Index of the metrology objects.

Default:
'all'

Suggested values:
'all', 0, 1, 2

## Result

If the parameters are valid, the operator
`reset_metrology_object_fuzzy_param` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`set_metrology_object_fuzzy_param`

## See also

`reset_metrology_object_param`

## Module

2D Metrology
