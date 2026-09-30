# get_metrology_object_indices (Operator)

## Name

`get_metrology_object_indices` — Get the indices of the metrology objects of a metrology model.

## Signature

`get_metrology_object_indices( : : MetrologyHandle : Indices)`

## Description

`get_metrology_object_indices` allows to access the indices of
the metrology objects.

For an explanation of the concept of 2D metrology see the introduction of
chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`MetrologyHandle`*. The
operator `get_metrology_object_indices` returns the indices of the
metrology object in the parameter *`Indices`*. Access to the parameters
of the metrology object is possible, e.g., with the operator
[`get_metrology_object_param`](get_metrology_object_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MetrologyHandle`** (input_control)  metrology_model `→`  (handle)

Handle of the metrology model.

**`Indices`** (output_control)  integer(-array) `→`  (integer)

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
