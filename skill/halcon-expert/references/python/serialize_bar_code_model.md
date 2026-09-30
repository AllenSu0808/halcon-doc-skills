# serialize_bar_code_model (Operator)

## Name

`serialize_bar_code_model` — Serialize a bar code model.

## Signature

`def serialize_bar_code_model(bar_code_handle: HHandle) -> HHandle`

## Description

`serialize_bar_code_model` serializes a bar code model (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_bar_code_model`](write_bar_code_model.md) is converted to a serialized item.
The bar code model is defined by the handle *`bar_code_handle`*.
The serialized model is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_bar_code_model`](deserialize_bar_code_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`bar_code_handle`** (input_control)  barcode `→` HHandle

Handle of the bar code model.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

The operator `serialize_bar_code_model` returns the value 2 (
H_MSG_TRUE)
if the passed handle of the bar code model is valid and if the model
can be serialized into the serialized item.
Otherwise, an exception is raised.

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_bar_code_model`

## See also

`create_bar_code_model`,
`set_bar_code_param`,
`find_bar_code`

## Module

Bar Code
