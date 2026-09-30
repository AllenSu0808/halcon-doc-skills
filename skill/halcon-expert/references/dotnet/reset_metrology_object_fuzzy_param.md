# ResetMetrologyObjectFuzzyParam (Operator)

## Name

`ResetMetrologyObjectFuzzyParam` — Reset all fuzzy parameters and fuzzy functions of a metrology
model.

## Signature

`static void HOperatorSet.ResetMetrologyObjectFuzzyParam(HTuple metrologyHandle, HTuple index)`

`void HMetrologyModel.ResetMetrologyObjectFuzzyParam(HTuple index)`

`void HMetrologyModel.ResetMetrologyObjectFuzzyParam(string index)`

## Description

`ResetMetrologyObjectFuzzyParam` discards all fuzzy
parameters and fuzzy functions of the metrology objects
that can be set by the operator [`SetMetrologyObjectFuzzyParam`](set_metrology_object_fuzzy_param.md)
and restores the default values.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`metrologyHandle`*. The
parameter *`index`* determines the metrology objects to reset. With
*`index`* set to *"all"*, all metrology objects are reset.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- metrologyHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`metrologyHandle`** (input_control, state is modified)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Index of the metrology objects.

Default:
"all"

Suggested values:
"all", 0, 1, 2

## Result

If the parameters are valid, the operator
`ResetMetrologyObjectFuzzyParam` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`SetMetrologyObjectFuzzyParam`

## See also

`ResetMetrologyObjectParam`

## Module

2D Metrology
