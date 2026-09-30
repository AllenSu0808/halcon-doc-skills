# serialize_ocv (Operator)

## Name

`serialize_ocv` — Serialize an OCV tool.

## Signature

`def serialize_ocv(ocvhandle: HHandle) -> HHandle`

## Description

`serialize_ocv` serializes the data of an OCV tool (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_ocv`](write_ocv.md) is converted to a serialized item.
The OCV tool is defined by the handle *`ocvhandle`*. The
serialized OCV tool is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_ocv`](deserialize_ocv.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocvhandle`** (input_control)  ocv `→` HHandle

Handle of the OCV tool.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

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
