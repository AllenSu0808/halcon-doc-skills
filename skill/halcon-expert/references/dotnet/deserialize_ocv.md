# DeserializeOcv (Operator)

## Name

`DeserializeOcv` — Deserialize a serialized OCV tool.

## Signature

`static void HOperatorSet.DeserializeOcv(HTuple serializedItemHandle, out HTuple OCVHandle)`

`void HOCV.DeserializeOcv(HSerializedItem serializedItemHandle)`

## Description

`DeserializeOcv` deserializes an OCV tool, that was serialized
by [`SerializeOcv`](serialize_ocv.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized OCV tool is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
OCV tool with the handle *`OCVHandle`*. After deserializing the
tool the training can be completed for those patterns which have not been
trained so far. Otherwise, a pattern comparison can be
applied directly by calling [`DoOcvSimple`](do_ocv_simple.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`OCVHandle`** (output_control)  ocv `→` [HOCV](HOCV.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCV tool.

## Result

If the parameters are valid, the operator
`DeserializeOcv` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeOcv`

## Possible Successors

`DoOcvSimple`,
`CloseOcv`

## Module

OCR/OCV
