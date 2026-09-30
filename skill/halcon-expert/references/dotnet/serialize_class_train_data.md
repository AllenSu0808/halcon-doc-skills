# SerializeClassTrainData (Operator)

## Name

`SerializeClassTrainData` — Serialize training data for classifiers.

## Signature

`static void HOperatorSet.SerializeClassTrainData(HTuple classTrainDataHandle, out HTuple serializedItemHandle)`

`HSerializedItem HClassTrainData.SerializeClassTrainData()`

## Description

`SerializeClassTrainData` serializes training data for classifiers
and its stored training samples (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The same data that
is written in a file by [`WriteClassTrainData`](write_class_train_data.md) is converted to a
serialized item. The training data is defined by the handle
*`classTrainDataHandle`*. The serialized training data is returned by
the handle *`serializedItemHandle`* and can be deserialized by
[`DeserializeClassTrainData`](deserialize_class_train_data.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`classTrainDataHandle`** (input_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training data.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeClassTrainData` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`DeserializeClassTrainData`

## See also

`CreateClassTrainData`,
`ReadClassTrainData`

## Module

Foundation
