# DeserializeClassSvm (Operator)

## Name

`DeserializeClassSvm` — Deserialize a serialized support vector machine (SVM).

## Signature

`static void HOperatorSet.DeserializeClassSvm(HTuple serializedItemHandle, out HTuple SVMHandle)`

`void HClassSvm.DeserializeClassSvm(HSerializedItem serializedItemHandle)`

## Description

`DeserializeClassSvm` deserializes a support vector machine (SVM)
(including its training samples), that was serialized
by [`SerializeClassSvm`](serialize_class_svm.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized support vector machine is defined by the handle
*`serializedItemHandle`*. The deserialized values are stored in an
automatically created support vector machine with the handle
*`SVMHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`SVMHandle`** (output_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

## Result

If the parameters are valid, the operator
`DeserializeClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeClassSvm`

## Possible Successors

`ClassifyClassSvm`,
`CreateClassLutSvm`

## See also

`CreateClassSvm`,
`WriteClassSvm`,
`SerializeClassSvm`

## Module

Foundation
