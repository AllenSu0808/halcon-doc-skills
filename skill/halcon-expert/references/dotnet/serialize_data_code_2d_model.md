# SerializeDataCode2dModel (Operator)

## Name

`SerializeDataCode2dModel` — Serialize a 2D code model.

## Signature

`static void HOperatorSet.SerializeDataCode2dModel(HTuple dataCodeHandle, out HTuple serializedItemHandle)`

`HSerializedItem HDataCode2D.SerializeDataCode2dModel()`

## Description

`SerializeDataCode2dModel` serializes a 2D code model (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`WriteDataCode2dModel`](write_data_code_2d_model.md) is converted to a serialized item.
The 2D code model is defined by the handle *`dataCodeHandle`*.
The serialized 2D code model is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeDataCode2dModel`](deserialize_data_code_2d_model.md).

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dataCodeHandle`** (input_control)  datacode_2d `→` [HDataCode2D](HDataCode2D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 2D code model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeDataCode2dModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`SetDataCode2dParam`,
`FindDataCode2d`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeDataCode2dModel`

## Alternatives

`GetDataCode2dParam`

## See also

`CreateDataCode2dModel`,
`SetDataCode2dParam`,
`FindDataCode2d`

## Module

Data Code
