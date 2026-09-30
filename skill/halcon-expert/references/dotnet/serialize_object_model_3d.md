# SerializeObjectModel3d (Operator)

## Name

`SerializeObjectModel3d` — Serialize a 3D object model.

## Signature

`static void HOperatorSet.SerializeObjectModel3d(HTuple objectModel3D, out HTuple serializedItemHandle)`

`HSerializedItem HObjectModel3D.SerializeObjectModel3d()`

## Description

`SerializeObjectModel3d` serializes the data of a 3D object
model (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file using the file format 'om3' of [`WriteObjectModel3d`](write_object_model_3d.md)
is converted to a serialized item. The 3D object model is defined by
the handle *`objectModel3D`*. The serialized 3D object model is
returned by the handle *`serializedItemHandle`* and can be
deserialized by [`DeserializeObjectModel3d`](deserialize_object_model_3d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeObjectModel3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`

## Possible Successors

`ReadObjectModel3d`,
`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeObjectModel3d`

## See also

`ReadObjectModel3d`

## Module

3D Metrology
