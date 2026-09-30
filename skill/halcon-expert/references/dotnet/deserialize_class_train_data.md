# DeserializeClassTrainData (Operator)

## Name

`DeserializeClassTrainData` — Deserialize serialized training data for classifiers.

## Signature

`static void HOperatorSet.DeserializeClassTrainData(HTuple serializedItemHandle, out HTuple classTrainDataHandle)`

`void HClassTrainData.DeserializeClassTrainData(HSerializedItem serializedItemHandle)`

## Description

`DeserializeClassTrainData` deserializes training data for
classifiers, that were serialized
by [`SerializeClassTrainData`](serialize_class_train_data.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization). The
serialized training data is defined by the handle
*`serializedItemHandle`*. The deserialized values are stored in an
automatically created training data block with the handle
*`classTrainDataHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`classTrainDataHandle`** (output_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training data.

## Result

If the parameters are valid, the operator
`DeserializeClassTrainData` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`SerializeClassTrainData`

## Possible Successors

`FwriteSerializedItem`

## See also

`CreateClassTrainData`

## Module

Foundation
