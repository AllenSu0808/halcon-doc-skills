# GetSerializedItemPtr (Operator)

## Name

`GetSerializedItemPtr` — Access the data pointer of a serialized item.

## Warning

**It is not recommended to use the operator
`GetSerializedItemPtr` in HDevelop.**

## Signature

`static void HOperatorSet.GetSerializedItemPtr(HTuple serializedItemHandle, out HTuple pointer, out HTuple size)`

`IntPtr HSerializedItem.GetSerializedItemPtr(out int size)`

## Description

`GetSerializedItemPtr` returns the data pointer to the
serialized item which is passed by the handle
*`serializedItemHandle`* (see [`FwriteSerializedItem`](fwrite_serialized_item.md)
for an introduction of the basics of serialization). The
data pointer, i.e., the beginning of the serialized item is returned
by the parameter *`pointer`*. The size of the serialized item
in bytes is passed by the parameter *`size`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`pointer`** (output_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Data pointer of the serialized item.

**`size`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Size of the serialized item.

## Result

If the parameters are valid, the operator
`GetSerializedItemPtr` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateSerializedItemPtr`

## Module

Foundation
