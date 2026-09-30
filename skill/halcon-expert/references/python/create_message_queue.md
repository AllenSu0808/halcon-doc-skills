# create_message_queue (Operator)

## Name

`create_message_queue` — Create a new empty message queue.

## Signature

`def create_message_queue() -> HHandle`

## Description

`create_message_queue` creates a new empty message queue.
The output parameter *`queue_handle`* is a handle to the newly created
message queue and is used to identify the queue in any subsequent operator
calls using the queue.

The message queues are designed as FIFO pipes delivering arbitrary sets of
data safely among different threads. The queue access is internally fully
synchronized, no explicit locking is required from the application.
The data is traveling through the queue in so called messages
(see [`create_message`](create_message.md)).

Multiple producer threads can append data simultaneously
([`enqueue_message`](enqueue_message.md)) while multiple consumer threads are simultaneously
retrieving the data again ([`dequeue_message`](dequeue_message.md)). Multiple messages
can be enqueued together using a single [`enqueue_message`](enqueue_message.md) operation.
In such case, those messages will travel together through the queue
and will be delivered through a single [`dequeue_message`](dequeue_message.md) call.

All the enqueued messages are copied by the
[`enqueue_message`](enqueue_message.md) operation. The original message(s) can thus be
immediately reused after the [`enqueue_message`](enqueue_message.md) call without affecting
the enqueued copy.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`queue_handle`** (output_control)  message_queue `→` HHandle

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

`enqueue_message`,
`dequeue_message`

## See also

`clear_message_queue`,
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
