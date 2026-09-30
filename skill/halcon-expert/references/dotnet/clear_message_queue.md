# ClearMessageQueue (Operator)

## Name

`ClearMessageQueue` — Close a message queue handle and release all associated resources.

## Signature

`static void HOperatorSet.ClearMessageQueue(HTuple queueHandle)`

`static void HMessageQueue.ClearMessageQueue(HMessageQueue[] queueHandle)`

`void HMessageQueue.ClearMessageQueue()`

## Description

`ClearMessageQueue` closes a message queue handle
*`queueHandle`* that was previously opened with
[`CreateMessageQueue`](create_message_queue.md).
Any resources owned by the message queue, in particular
message data queued in the message queue will be released.

Multiple message queue handles can be closed in a single
`ClearMessageQueue` call, passing them as a tuple to the
*`queueHandle`* parameter.

## Attention

The handle(s) must not be used again after being invalidated using
`ClearMessageQueue`. Using an invalid handle results in
undefined behavior.
Operator `ClearMessageQueue` must not be called while the
handle is used concurrently from other threads, because this would result
in undefined behavior.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- queueHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`queueHandle`** (input_control, state is modified)  message_queue(-array) `→` [HMessageQueue](HMessageQueue.md), [HTuple](HTuple.md) (*IntPtr*)

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
`ClearMessageQueue` returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.
If a tuple of handles is passed and some of them are invalid,
`ClearMessageQueue` attempts to clear as many handles
from the tuple as possible before reporting the error.

## Possible Predecessors

`CreateMessageQueue`,
`SetMessageQueueParam`

## See also

`CreateMessageQueue`,
`EnqueueMessage`,
`DequeueMessage`,
`SetMessageQueueParam`,
`GetMessageQueueParam`,
`CreateMessage`,
`ClearMessage`,
`SetMessageTuple`,
`GetMessageTuple`,
`SetMessageObj`,
`GetMessageObj`

## Module

Foundation
