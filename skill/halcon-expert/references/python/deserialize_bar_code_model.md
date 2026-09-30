# deserialize_bar_code_model (Operator)

## Name

`deserialize_bar_code_model` — Deserialize a bar code model.

## Signature

`def deserialize_bar_code_model(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_bar_code_model` deserializes a bar code model
that was serialized by [`serialize_bar_code_model`](serialize_bar_code_model.md)
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized model is defined by the
handle *`serialized_item_handle`*. The deserialized values are stored
in a new bar code model with the handle *`bar_code_handle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`bar_code_handle`** (output_control)  barcode `→` HHandle

Handle of the bar code model.

## Result

The operator `deserialize_bar_code_model` returns the value 2 (
H_MSG_TRUE)
if the bar code can be correctly deserialized.
Otherwise, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_bar_code_model`

## Possible Successors

`find_bar_code`

## Alternatives

`create_bar_code_model`

## See also

`serialize_bar_code_model`,
`clear_bar_code_model`

## Module

Bar Code
