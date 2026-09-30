# CreateMessageQueue (Operator)

## Name

`CreateMessageQueue` — Create a new empty message queue.

## Signature

`static void HOperatorSet.CreateMessageQueue(out HTuple queueHandle)`

`public HMessageQueue()`

`void HMessageQueue.CreateMessageQueue()`

## Description

`CreateMessageQueue` creates a new empty message queue.
The output parameter *`queueHandle`* is a handle to the newly created
message queue and is used to identify the queue in any subsequent operator
calls using the queue.

The message queues are designed as FIFO pipes delivering arbitrary sets of
data safely among different threads. The queue access is internally fully
synchronized, no explicit locking is required from the application.
The data is traveling through the queue in so called messages
(see [`CreateMessage`](create_message.md)).

Multiple producer threads can append data simultaneously
([`EnqueueMessage`](enqueue_message.md)) while multiple consumer threads are simultaneously
retrieving the data again ([`DequeueMessage`](dequeue_message.md)). Multiple messages
can be enqueued together using a single [`EnqueueMessage`](enqueue_message.md) operation.
In such case, those messages will travel together through the queue
and will be delivered through a single [`DequeueMessage`](dequeue_message.md) call.

All the enqueued messages are copied by the
[`EnqueueMessage`](enqueue_message.md) operation. The original message(s) can thus be
immediately reused after the [`EnqueueMessage`](enqueue_message.md) call without affecting
the enqueued copy.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`queueHandle`** (output_control)  message_queue `→` [HMessageQueue](HMessageQueue.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the newly created message queue.

Number of elements:
QueueHandle == 1

Assertion:
`QueueHandle != 0`

## Example (HDevelop)

```
create_message_queue (ProducerQueue)
create_message_queue (ResultQueue)
* ...
```

## Result

Returns 2 (
H_MSG_TRUE)
unless a resource allocation error occurs. Otherwise
an exception is raised.

## Possible Successors

`EnqueueMessage`,
`DequeueMessage`

## See also

`ClearMessageQueue`,
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
