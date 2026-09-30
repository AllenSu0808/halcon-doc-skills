# GetMetrologyObjectIndices (Operator)

## Name

`GetMetrologyObjectIndices` — Get the indices of the metrology objects of a metrology model.

## Signature

`static void HOperatorSet.GetMetrologyObjectIndices(HTuple metrologyHandle, out HTuple indices)`

`HTuple HMetrologyModel.GetMetrologyObjectIndices()`

## Description

`GetMetrologyObjectIndices` allows to access the indices of
the metrology objects.

For an explanation of the concept of 2D metrology see the introduction of
chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`metrologyHandle`*. The
operator `GetMetrologyObjectIndices` returns the indices of the
metrology object in the parameter *`indices`*. Access to the parameters
of the metrology object is possible, e.g., with the operator
[`GetMetrologyObjectParam`](get_metrology_object_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrologyHandle`** (input_control)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`indices`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Indices of the metrology objects.

## Result

If the parameters are valid, the operator
`GetMetrologyObjectIndices` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadMetrologyModel`

## Possible Successors

`GetMetrologyObjectParam`,
`GetMetrologyObjectFuzzyParam`

## See also

`GetMetrologyObjectNumInstances`

## Module

2D Metrology
