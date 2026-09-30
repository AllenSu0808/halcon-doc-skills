# SerializeClassSvm (Operator)

## Name

`SerializeClassSvm` — Serialize a support vector machine (SVM).

## Signature

`static void HOperatorSet.SerializeClassSvm(HTuple SVMHandle, out HTuple serializedItemHandle)`

`HSerializedItem HClassSvm.SerializeClassSvm()`

## Description

`SerializeClassSvm` serializes a support vector machine (SVM) and
its stored training samples (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The same data that
is written in a file by [`WriteClassSvm`](write_class_svm.md) and
[`WriteSamplesClassSvm`](write_samples_class_svm.md) is converted to a serialized item.
The support vector machine is defined by the handle *`SVMHandle`*.
The serialized support vector machine is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeClassSvm`](deserialize_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainClassSvm`

## Possible Successors

`ClearClassSvm`,
`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeClassSvm`

## See also

`CreateClassSvm`,
`ReadClassSvm`,
`WriteSamplesClassSvm`,
`DeserializeClassSvm`

## Module

Foundation
