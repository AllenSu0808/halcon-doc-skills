# SerializeOcv (Operator)

## Name

`SerializeOcv` — Serialize an OCV tool.

## Signature

`static void HOperatorSet.SerializeOcv(HTuple OCVHandle, out HTuple serializedItemHandle)`

`HSerializedItem HOCV.SerializeOcv()`

## Description

`SerializeOcv` serializes the data of an OCV tool (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`WriteOcv`](write_ocv.md) is converted to a serialized item.
The OCV tool is defined by the handle *`OCVHandle`*. The
serialized OCV tool is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeOcv`](deserialize_ocv.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCVHandle`** (input_control)  ocv `→` [HOCV](HOCV.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCV tool.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeOcv` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TraindOcvProj`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeOcv`

## Module

OCR/OCV
