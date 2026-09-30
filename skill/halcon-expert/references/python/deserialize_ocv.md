# deserialize_ocv (Operator)

## Name

`deserialize_ocv` — Deserialize a serialized OCV tool.

## Signature

`def deserialize_ocv(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_ocv` deserializes an OCV tool, that was serialized
by [`serialize_ocv`](serialize_ocv.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized OCV tool is defined by the handle *`serialized_item_handle`*.
The deserialized values are stored in an automatically created
OCV tool with the handle *`ocvhandle`*. After deserializing the
tool the training can be completed for those patterns which have not been
trained so far. Otherwise, a pattern comparison can be
applied directly by calling [`do_ocv_simple`](do_ocv_simple.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`ocvhandle`** (output_control)  ocv `→` HHandle

Handle of the OCV tool.

## Result

If the parameters are valid, the operator
`deserialize_ocv` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_ocv`

## Possible Successors

`do_ocv_simple`,
`close_ocv`

## Module

OCR/OCV
