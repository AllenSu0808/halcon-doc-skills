# clear_message_queue (Operator)

## Name

`clear_message_queue` — Close a message queue handle and release all associated resources.

## Signature

`def clear_message_queue(queue_handle: MaybeSequence[HHandle]) -> None`

## Description

`clear_message_queue` closes a message queue handle
*`queue_handle`* that was previously opened with
[`create_message_queue`](create_message_queue.md).
Any resources owned by the message queue, in particular
message data queued in the message queue will be released.

Multiple message queue handles can be closed in a single
`clear_message_queue` call, passing them as a tuple to the
*`queue_handle`* parameter.

## Attention

The handle(s) must not be used again after being invalidated using
`clear_message_queue`. Using an invalid handle results in
undefined behavior.
Operator `clear_message_queue` must not be called while the
handle is used concurrently from other threads, because this would result
in undefined behavior.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- queue_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`queue_handle`** (input_control, state is modified)  message_queue(-array) `→` MaybeSequence[HHandle]

Message queue handle(s) to be closed.

Number of elements:
QueueHandle >= 1

Restriction:
`QueueHandle != 0`

## Example (HDevelop)

```
create_message_queue (ProducerQueue)
create_message_queue (ResultQueue)
* ...
```

## Result

If the message queue handle(s) passed to the operator are valid,
`clear_message_queue` returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.
If a tuple of handles is passed and some of them are invalid,
`clear_message_queue` attempts to clear as many handles
from the tuple as possible before reporting the error.

## Possible Predecessors

`create_message_queue`,
`set_message_queue_param`

## See also

`create_message_queue`,
`enqueue_message`,
`dequeue_message`,
`set_message_queue_param`,
`get_message_queue_param`,
`create_message`,
`clear_message`,
`set_message_tuple`,
`get_message_tuple`,
`set_message_obj`,
`get_message_obj`

## Module

Foundation
