# EnqueueMessage (Operator)

## Name

`EnqueueMessage` — Enqueue one or more messages to the message queue.

## Signature

`static void HOperatorSet.EnqueueMessage(HTuple queueHandle, HTuple messageHandle, HTuple genParamName, HTuple genParamValue)`

`void HMessageQueue.EnqueueMessage(HMessage[] messageHandle, HTuple genParamName, HTuple genParamValue)`

`void HMessageQueue.EnqueueMessage(HMessage messageHandle, HTuple genParamName, HTuple genParamValue)`

## Description

`EnqueueMessage` enqueues one or more messages to the message queue
denoted by the *`queueHandle`* parameter.
The enqueued messages can be retrieved from the queue by any thread using
[`DequeueMessage`](dequeue_message.md).

The messages (see [`CreateMessage`](create_message.md)) to be enqueued are specified
in the *`messageHandle`* parameter which accepts a single handle
as well as tuple of handles. When enqueuing multiple handles together
in a single `EnqueueMessage` call, they are delivered again
together through a single [`DequeueMessage`](dequeue_message.md) call.

Multiple producer (enqueuing) threads and multiple consumer (dequeuing)
threads can share the same queue at a time. The messages are delivered
in FIFO (first-in first-out) order. Every message is delivered only once,
even if multiple consumer threads are using the queue.

The queue access is internally fully synchronized, no external locking
is required. If the queue is empty and there is at least one consumer
thread waiting for the message data in [`DequeueMessage`](dequeue_message.md),
one of those threads is woken up by a successful `EnqueueMessage`
call and the enqueued message data are immediately delivered.
Otherwise the message data is appended to the queue asynchronously,
to be delivered as soon as a consumer thread is ready to dequeue
the message data again.

All the enqueued messages (*`messageHandle`*) are copied by the
`EnqueueMessage` operation. The original message(s) can thus be
immediately reused after the `EnqueueMessage` call without affecting
the enqueued copy.

If, after the operation, the queue would hold a larger number of messages
than the specified maximum number, either the error H_ERR_MQOVL is returned,
or the operator waits until space becomes available in the queue.
The behavior can be configured for the queue using the parameter
*"wait_on_full"* in the operator [`SetMessageQueueParam`](set_message_queue_param.md).
The maximum number of messages that may be held is defined by the
parameter value *"max_message_num"* in the operator
[`SetMessageQueueParam`](set_message_queue_param.md).
If more messages shall be enqueued than the queue has capacity,
i.e. if the tuple *`messageHandle`* has more elements than
what is set in ValRe('max_message_num'), the operator
`EnqueueMessage` will always return the error code
H_ERR_MQOVL, independent of the setting of *"wait_on_full"*.

Finally, it is possible to adjust `EnqueueMessage` behavior
through generic parameters within *`genParamName`* and
*`genParamValue`*. Currently, just a single generic parameter
is supported:

- ***"timeout"*:** —

  Timeout controlling how long the operator will block while waiting
  for space in the message queue to become available if the queue
  is full and *"wait_on_full"* is set to *"true"*.
  In case of a timeout, the operator returns with H_ERR_TIMEOUT.

  The timeout can be specified as an integer or double value in seconds
  or as the string *"infinite"*. When no timeout is specified,
  infinite timeout is used as default, meaning that the operator would
  block until space becomes available or until the operation is aborted.

  Suggested values:
   *-1*, *"infinite"*,
  *1*, *10*

  Default:
   *-1*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`queueHandle`** (input_control)  message_queue `→` [HMessageQueue](HMessageQueue.md), [HTuple](HTuple.md) (*IntPtr*)

Message queue handle.

Number of elements:
QueueHandle == 1

Restriction:
`QueueHandle != 0`

**`messageHandle`** (input_control)  message(-array) `→` [HMessage](HMessage.md), [HTuple](HTuple.md) (*IntPtr*)

Handle(s) of message(s) to be enqueued.

Number of elements:
MessageHandle > 0

Restriction:
`MessageHandle != 0`

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of optional generic parameters.

Number of elements:
GenParamName == GenParamValue

**`genParamValue`** (input_control)  tuple-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of optional generic parameters.

Number of elements:
GenParamName == GenParamValue

## Example (HDevelop)

```
create_message_queue (Queue)
* ...
create_message (Message)
set_message_tuple (Message, 'mixed_tuple', ['The answer', 42])
enqueue_message (Queue, Message, [], [])
```

## Result

If the operation succeeds, `EnqueueMessage` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters or resource allocation error.

## Possible Predecessors

`SetMessageTuple`,
`SetMessageObj`

## See also

`CreateMessageQueue`,
`ClearMessageQueue`,
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
