# deserialize_class_train_data (Operator)

## Name

`deserialize_class_train_data` — Deserialize serialized training data for classifiers.

## Signature

`def deserialize_class_train_data(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_class_train_data` deserializes training data for
classifiers, that were serialized
by [`serialize_class_train_data`](serialize_class_train_data.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization). The
serialized training data is defined by the handle
*`serialized_item_handle`*. The deserialized values are stored in an
automatically created training data block with the handle
*`class_train_data_handle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`class_train_data_handle`** (output_control)  class_train_data `→` HHandle

Handle of the training data.

## Result

If the parameters are valid, the operator
`deserialize_class_train_data` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`serialize_class_train_data`

## Possible Successors

`fwrite_serialized_item`

## See also

`create_class_train_data`

## Module

Foundation
