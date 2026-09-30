# CreateSerializedItemPtr (Operator)

## Name

`CreateSerializedItemPtr` — Create a serialized item.

## Warning

**It is not recommended to use the operator
`CreateSerializedItemPtr` in HDevelop.**

## Signature

`static void HOperatorSet.CreateSerializedItemPtr(HTuple pointer, HTuple size, HTuple copy, out HTuple serializedItemHandle)`

`public HSerializedItem(IntPtr pointer, int size, string copy)`

`void HSerializedItem.CreateSerializedItemPtr(IntPtr pointer, int size, string copy)`

## Description

`CreateSerializedItemPtr` creates a serialized item
and returns the handle *`serializedItemHandle`* (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basics of
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

**`pointer`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Data pointer of the serialized item.

**`size`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Size of the serialized item.

**`copy`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Copy mode of the serialized item.

Default:
"true"

List of values:
"false", "true"

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`CreateSerializedItemPtr` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`GetSerializedItemPtr`

## Module

Foundation
