# copy_metrology_model (Operator)

## Name

`copy_metrology_model` — Copy a metrology model.

## Signature

`copy_metrology_model( : : MetrologyHandle, Index : CopiedMetrologyHandle)`

## Description

`copy_metrology_model` creates a new metrology model and
copies the selected metrology objects of the input metrology model
to this new output metrology model.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The input metrology model is defined by a handle *`MetrologyHandle`*.
The parameter *`Index`* determines the metrology objects that are
copied. With *`Index`* set to *'all'*, all metrology objects are
copied. The operator returns the handle *`CopiedMetrologyHandle`* of
the new metrology model. It can be used to save memory space. Access to the
parameters of the metrology objects is possible, e.g., with the operator
[`get_metrology_object_param`](get_metrology_object_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MetrologyHandle`** (input_control)  metrology_model `→`  (handle)

Handle of the metrology model.

**`Index`** (input_control)  integer(-array) `→`  (string / integer)

Index of the metrology objects.

Default:
'all'

Suggested values:
'all', 0, 1, 2

**`CopiedMetrologyHandle`** (output_control)  integer `→`  (integer)

Handle of the copied metrology model.

## Result

If the parameters are valid, the operator
`copy_metrology_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Module

2D Metrology
