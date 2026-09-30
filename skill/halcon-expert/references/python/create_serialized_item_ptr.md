# create_serialized_item_ptr (Operator)

## Name

`create_serialized_item_ptr` — Create a serialized item.

## Warning

**It is not recommended to use the operator
`create_serialized_item_ptr` in HDevelop.**

## Signature

`def create_serialized_item_ptr(pointer: int, size: int, copy: str) -> HHandle`

## Description

`create_serialized_item_ptr` creates a serialized item
and returns the handle *`serialized_item_handle`* (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basics of
serialization). The data pointer, i.e., the beginning of the
serialized item, is passed by the parameter *`pointer`*.
The size of the serialized item in bytes is passed by parameter
*`size`*. The behavior of the operator is controlled by the
parameter *`copy`*. If *`copy`* is set to *"true"*,
a new serialized item is created and the values of the existing
serialized item are copied. If *`copy`* is set to
*"false"*, only the data pointer of the input serialized item
is stored, i.e., the actual data are not copied, which leads to shorter
execution times.

## Attention

If the parameter *`copy`* is set to *"false"*, the data
pointer of the serialized item must not be deleted during using the
new serialized item.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`pointer`** (input_control)  pointer `→` int

Data pointer of the serialized item.

**`size`** (input_control)  integer `→` int

Size of the serialized item.

**`copy`** (input_control)  string `→` str

Copy mode of the serialized item.

Default:
"true"

List of values:
"false", "true"

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`create_serialized_item_ptr` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`get_serialized_item_ptr`

## Module

Foundation
