# DequeueMessage (Operator)

## Name

`DequeueMessage` — Receive one or more messages from the message queue.

## Signature

`static void HOperatorSet.DequeueMessage(HTuple queueHandle, HTuple genParamName, HTuple genParamValue, out HTuple messageHandle)`

`HMessage[] HMessageQueue.DequeueMessage(HTuple genParamName, HTuple genParamValue)`

`HMessage HMessageQueue.DequeueMessage(string genParamName, HTuple genParamValue)`

## Description

`DequeueMessage` dequeues a message from the message queue
denoted by the *`queueHandle`* parameter.
The message must have been enqueued by any thread using
[`EnqueueMessage`](enqueue_message.md).

The messages are delivered in FIFO (first-in first-out) order, every message
is delivered only once. If the queue is not empty, `DequeueMessage`
immediately delivers the oldest message from the queue. This message
is removed from the queue and a handle to the message is returned
in the *`messageHandle`* output parameter. The message data ownership
is transferred (no copy) from the message queue to the newly created
message handle.

If the queue is empty, `DequeueMessage` blocks until a message
becomes available for delivery (being queued from another thread
using [`EnqueueMessage`](enqueue_message.md)).

The data stored in the message can be queried using
[`GetMessageTuple`](get_message_tuple.md), [`GetMessageObj`](get_message_obj.md), or
[`GetMessageParam`](get_message_param.md).

The message handles obtained through `DequeueMessage` can be
further reused (modified and/or enqueued to another message queue).

If multiple messages were enqueued using a single [`EnqueueMessage`](enqueue_message.md)
call, all those messages will be also retrieved together through a single
`DequeueMessage` call, delivering multiple message handles via
the *`messageHandle`* tuple.

The queue access is internally fully synchronized, no external locking
is required.

During application reconfiguration or cleanup, it might be necessary
to wake threads waiting for messages in `DequeueMessage`.
This can be achieved using the operator [`SetMessageQueueParam`](set_message_queue_param.md)
with the parameter *"abort_dequeuing"*. In such case the currently
blocked `DequeueMessage` calls return immediately with H_ERR_MQCNCL.

Finally, it is possible to adjust `DequeueMessage` behavior
through generic parameters within *`genParamName`* and
*`genParamValue`*. Currently, just a single generic parameter
is supported:

- ***"timeout"*:** —

  Timeout controlling how long the operator will block while waiting for
  a message if the queue is empty. When expired, the operator returns
  with H_ERR_TIMEOUT.
  The timeout can be specified as an integer or double value in seconds
  or as the string *"infinite"*. When no timeout is specified,
  infinite timeout is used as default, meaning that the operator would
  block until a new message is enqueued or until the operation is aborted.

  Suggested values:
   *-1*, *"infinite"*,
  *1*, *10*

  Default:
   *-1*

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`queueHandle`** (input_control)  message_queue `→` [HMessageQueue](HMessageQueue.md), [HTuple](HTuple.md) (*IntPtr*)

Message queue handle.

Number of elements:
QueueHandle == 1

Restriction:
`QueueHandle != 0`

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of optional generic parameters

Number of elements:
GenParamName == GenParamValue

Default:
"timeout"

List of values:
"timeout"

**`genParamValue`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of optional generic parameters

Number of elements:
GenParamName == GenParamValue

Default:
"infinite"

List of values:
"infinite"

**`messageHandle`** (output_control)  message(-array) `→` [HMessage](HMessage.md), [HTuple](HTuple.md) (*IntPtr*)

Handle(s) of the dequeued message(s).

Number of elements:
MessageHandle > 0

Assertion:
`MessageHandle != 0`

## Example (HDevelop)

```
create_message_queue (Queue)
* ...
dequeue_message (Queue, [], [], Message)
get_message_obj (Image, Message, 'my_image')
```

## Result

If the operation succeeds, `DequeueMessage` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters, message dequeue wait timeout (H_ERR_TIMEOUT)
or message dequeue wait abortion (H_ERR_MQCNCL).
Note that in some rare cases, when an error occurs when finishing the
operator call (after the message has already been removed from the queue),
the operator will attempt to put the message back at the head of the queue
to not lose it.
This might lead to a different message delivery order
if another thread removed another message from the queue in the meanwhile.

## Possible Successors

`GetMessageTuple`,
`GetMessageObj`,
`GetMessageParam`

## See also

`CreateMessageQueue`,
`ClearMessageQueue`,
`EnqueueMessage`,
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
