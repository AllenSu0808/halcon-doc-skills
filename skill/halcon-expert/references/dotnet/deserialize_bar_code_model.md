# DeserializeBarCodeModel (Operator)

## Name

`DeserializeBarCodeModel` — Deserialize a bar code model.

## Signature

`static void HOperatorSet.DeserializeBarCodeModel(HTuple serializedItemHandle, out HTuple barCodeHandle)`

`void HBarCode.DeserializeBarCodeModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeBarCodeModel` deserializes a bar code model
that was serialized by [`SerializeBarCodeModel`](serialize_bar_code_model.md)
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized model is defined by the
handle *`serializedItemHandle`*. The deserialized values are stored
in a new bar code model with the handle *`barCodeHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`barCodeHandle`** (output_control)  barcode `→` [HBarCode](HBarCode.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bar code model.

## Result

The operator `DeserializeBarCodeModel` returns the value 2 (
H_MSG_TRUE)
if the bar code can be correctly deserialized.
Otherwise, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeBarCodeModel`

## Possible Successors

`FindBarCode`

## Alternatives

`CreateBarCodeModel`

## See also

`SerializeBarCodeModel`,
`ClearBarCodeModel`

## Module

Bar Code
