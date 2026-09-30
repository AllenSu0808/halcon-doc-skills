# SerializeBarCodeModel (Operator)

## Name

`SerializeBarCodeModel` — Serialize a bar code model.

## Signature

`static void HOperatorSet.SerializeBarCodeModel(HTuple barCodeHandle, out HTuple serializedItemHandle)`

`HSerializedItem HBarCode.SerializeBarCodeModel()`

## Description

`SerializeBarCodeModel` serializes a bar code model (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`WriteBarCodeModel`](write_bar_code_model.md) is converted to a serialized item.
The bar code model is defined by the handle *`barCodeHandle`*.
The serialized model is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeBarCodeModel`](deserialize_bar_code_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`barCodeHandle`** (input_control)  barcode `→` [HBarCode](HBarCode.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bar code model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

The operator `SerializeBarCodeModel` returns the value 2 (
H_MSG_TRUE)
if the passed handle of the bar code model is valid and if the model
can be serialized into the serialized item.
Otherwise, an exception is raised.

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeBarCodeModel`

## See also

`CreateBarCodeModel`,
`SetBarCodeParam`,
`FindBarCode`

## Module

Bar Code
