# DeserializeDataCode2dModel (Operator)

## Name

`DeserializeDataCode2dModel` — Deserialize a serialized 2D code model.

## Signature

`static void HOperatorSet.DeserializeDataCode2dModel(HTuple serializedItemHandle, out HTuple dataCodeHandle)`

`void HDataCode2D.DeserializeDataCode2dModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeDataCode2dModel` deserializes a 2D code model,
that was serialized by [`SerializeDataCode2dModel`](serialize_data_code_2d_model.md)
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized 2D code model is defined
by the handle *`serializedItemHandle`*. The deserialized values are
stored in a new 2D code model with the handle *`dataCodeHandle`*.

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`dataCodeHandle`** (output_control)  datacode_2d `→` [HDataCode2D](HDataCode2D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 2D code model.

## Result

The operator `DeserializeDataCode2dModel` returns the value 2 (
H_MSG_TRUE)
if the 2D code can be correctly deserialized.
Otherwise, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeDataCode2dModel`

## Possible Successors

`FindDataCode2d`

## Alternatives

`CreateDataCode2dModel`

## See also

`SerializeDataCode2dModel`,
`ClearDataCode2dModel`

## Module

Data Code
