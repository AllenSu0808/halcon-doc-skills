# serialize_measure (Operator)

## Name

`serialize_measure` — Serialize a measure object.

## Signature

`def serialize_measure(measure_handle: HHandle) -> HHandle`

## Description

`serialize_measure` serializes the data of a measure object
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`write_measure`](write_measure.md) is converted to a serialized
item. The measure object is defined by the handle
*`measure_handle`*. The serialized measure object is returned
by the handle *`serialized_item_handle`* and can be
deserialized by [`deserialize_measure`](deserialize_measure.md).

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- measure_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`measure_handle`** (input_control, state is modified)  measure `→` HHandle

Measure object handle.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_measure` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`gen_measure_rectangle2`,
`gen_measure_arc`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_measure`

## See also

`read_measure`,
`write_measure`

## Module

1D Metrology
