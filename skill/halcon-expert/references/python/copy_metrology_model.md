# copy_metrology_model (Operator)

## Name

`copy_metrology_model` — Copy a metrology model.

## Signature

`def copy_metrology_model(metrology_handle: HHandle, index: MaybeSequence[Union[str, int]]) -> int`

## Description

`copy_metrology_model` creates a new metrology model and
copies the selected metrology objects of the input metrology model
to this new output metrology model.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The input metrology model is defined by a handle *`metrology_handle`*.
The parameter *`index`* determines the metrology objects that are
copied. With *`index`* set to *"all"*, all metrology objects are
copied. The operator returns the handle *`copied_metrology_handle`* of
the new metrology model. It can be used to save memory space. Access to the
parameters of the metrology objects is possible, e.g., with the operator
[`get_metrology_object_param`](get_metrology_object_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrology_handle`** (input_control)  metrology_model `→` HHandle

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` MaybeSequence[Union[str, int]]

Index of the metrology objects.

Default:
"all"

Suggested values:
"all", 0, 1, 2

**`copied_metrology_handle`** (output_control)  integer `→` int

Handle of the copied metrology model.

## Result

If the parameters are valid, the operator
`copy_metrology_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Module

2D Metrology
