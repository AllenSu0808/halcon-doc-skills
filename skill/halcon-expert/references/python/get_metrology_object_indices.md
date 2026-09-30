# get_metrology_object_indices (Operator)

## Name

`get_metrology_object_indices` — Get the indices of the metrology objects of a metrology model.

## Signature

`def get_metrology_object_indices(metrology_handle: HHandle) -> Sequence[int]`

`def get_metrology_object_indices_s(metrology_handle: HHandle) -> int`

## Description

`get_metrology_object_indices` allows to access the indices of
the metrology objects.

For an explanation of the concept of 2D metrology see the introduction of
chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`metrology_handle`*. The
operator `get_metrology_object_indices` returns the indices of the
metrology object in the parameter *`indices`*. Access to the parameters
of the metrology object is possible, e.g., with the operator
[`get_metrology_object_param`](get_metrology_object_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrology_handle`** (input_control)  metrology_model `→` HHandle

Handle of the metrology model.

**`indices`** (output_control)  integer(-array) `→` Sequence[int]

Indices of the metrology objects.

## Result

If the parameters are valid, the operator
`get_metrology_object_indices` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_metrology_model`

## Possible Successors

`get_metrology_object_param`,
`get_metrology_object_fuzzy_param`

## See also

`get_metrology_object_num_instances`

## Module

2D Metrology
