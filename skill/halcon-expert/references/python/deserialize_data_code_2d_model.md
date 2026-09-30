# deserialize_data_code_2d_model (Operator)

## Name

`deserialize_data_code_2d_model` — Deserialize a serialized 2D code model.

## Signature

`def deserialize_data_code_2d_model(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_data_code_2d_model` deserializes a 2D code model,
that was serialized by [`serialize_data_code_2d_model`](serialize_data_code_2d_model.md)
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized 2D code model is defined
by the handle *`serialized_item_handle`*. The deserialized values are
stored in a new 2D code model with the handle *`data_code_handle`*.

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`data_code_handle`** (output_control)  datacode_2d `→` HHandle

Handle of the 2D code model.

## Result

The operator `deserialize_data_code_2d_model` returns the value 2 (
H_MSG_TRUE)
if the 2D code can be correctly deserialized.
Otherwise, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_data_code_2d_model`

## Possible Successors

`find_data_code_2d`

## Alternatives

`create_data_code_2d_model`

## See also

`serialize_data_code_2d_model`,
`clear_data_code_2d_model`

## Module

Data Code
