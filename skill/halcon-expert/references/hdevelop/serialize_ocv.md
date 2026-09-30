# serialize_ocv (Operator)

## Name

`serialize_ocv` — Serialize an OCV tool.

## Signature

`serialize_ocv( : : OCVHandle : SerializedItemHandle)`

## Description

`serialize_ocv` serializes the data of an OCV tool (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_ocv`](write_ocv.md) is converted to a serialized item.
The OCV tool is defined by the handle *`OCVHandle`*. The
serialized OCV tool is returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_ocv`](deserialize_ocv.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCVHandle`** (input_control)  ocv `→`  (handle)

Handle of the OCV tool.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_ocv` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`traind_ocv_proj`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_ocv`

## Module

OCR/OCV
