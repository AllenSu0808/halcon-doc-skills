# serialize_data_code_2d_model (Operator)

## Name

`serialize_data_code_2d_model` — Serialize a 2D code model.

## Signature

`serialize_data_code_2d_model( : : DataCodeHandle : SerializedItemHandle)`

## Description

`serialize_data_code_2d_model` serializes a 2D code model (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_data_code_2d_model`](write_data_code_2d_model.md) is converted to a serialized item.
The 2D code model is defined by the handle *`DataCodeHandle`*.
The serialized 2D code model is returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_data_code_2d_model`](deserialize_data_code_2d_model.md).

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DataCodeHandle`** (input_control)  datacode_2d `→`  (handle)

Handle of the 2D code model.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_data_code_2d_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`set_data_code_2d_param`,
`find_data_code_2d`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_data_code_2d_model`

## Alternatives

`get_data_code_2d_param`

## See also

`create_data_code_2d_model`,
`set_data_code_2d_param`,
`find_data_code_2d`

## Module

Data Code
