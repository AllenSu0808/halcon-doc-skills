# copy_metrology_object (Operator)

## Name

`copy_metrology_object` — Copy metrology metrology objects of a metrology model.

## Warning

**`copy_metrology_object` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def copy_metrology_object(metrology_handle: HHandle, index: MaybeSequence[Union[str, int]]) -> Sequence[int]`

`def copy_metrology_object_s(metrology_handle: HHandle, index: MaybeSequence[Union[str, int]]) -> int`

## Description

`copy_metrology_object` copies metrology metrology objects
within this metrology model.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`metrology_handle`*. The
parameter *`index`* determines the metrology objects that are copied.
With *`index`* set to *"all"*, all metrology objects are copied.
The operator `copy_metrology_object` returns the index of the new
created metrology objects in the parameter *`copied_indices`*. The order
of the new metrology objects corresponds to the order of the original
metrology objects. Access to the parameters of the metrology objects of the
metrology model is possible, e.g., with the operator
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

**`copied_indices`** (output_control)  integer(-array) `→` Sequence[int]

Indices of the copied metrology objects.

## Result

If the parameters are valid, the operator
`copy_metrology_object` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Module

2D Metrology
