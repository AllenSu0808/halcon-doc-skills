# DeserializeObjectModel3d (Operator)

## Name

`DeserializeObjectModel3d` — Deserialize a serialized 3D object model.

## Signature

`static void HOperatorSet.DeserializeObjectModel3d(HTuple serializedItemHandle, out HTuple objectModel3D)`

`void HObjectModel3D.DeserializeObjectModel3d(HSerializedItem serializedItemHandle)`

## Description

`DeserializeObjectModel3d` deserializes a 3D object model
that was serialized by [`SerializeObjectModel3d`](serialize_object_model_3d.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized 3D object model is
defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
3D object model with the handle *`objectModel3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`objectModel3D`** (output_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

## Result

If the parameters are valid, the operator
`DeserializeObjectModel3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`WriteObjectModel3d`,
`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeObjectModel3d`

## Possible Successors

`AffineTransObjectModel3d`,
`ObjectModel3dToXyz`,
`PrepareObjectModel3d`

## Alternatives

`XyzToObjectModel3d`

## See also

`WriteObjectModel3d`,
`ClearObjectModel3d`

## Module

3D Metrology
