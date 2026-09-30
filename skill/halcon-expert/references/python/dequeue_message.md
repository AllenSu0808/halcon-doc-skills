# dequeue_message (Operator)

## Name

`dequeue_message` — Receive one or more messages from the message queue.

## Signature

`def dequeue_message(queue_handle: HHandle, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> Sequence[HHandle]`

`def dequeue_message_s(queue_handle: HHandle, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

`dequeue_message` dequeues a message from the message queue
denoted by the *`queue_handle`* parameter.
The message must have been enqueued by any thread using
[`enqueue_message`](enqueue_message.md).

The messages are delivered in FIFO (first-in first-out) order, every message
is delivered only once. If the queue is not empty, `dequeue_message`
immediately delivers the oldest message from the queue. This message
is removed from the queue and a handle to the message is returned
in the *`message_handle`* output parameter. The message data ownership
is transferred (no copy) from the message queue to the newly created
message handle.

If the queue is empty, `dequeue_message` blocks until a message
becomes available for delivery (being queued from another thread
using [`enqueue_message`](enqueue_message.md)).

The data stored in the message can be queried using
[`get_message_tuple`](get_message_tuple.md), [`get_message_obj`](get_message_obj.md), or
[`get_message_param`](get_message_param.md).

The message handles obtained through `dequeue_message` can be
further reused (modified and/or enqueued to another message queue).

If multiple messages were enqueued using a single [`enqueue_message`](enqueue_message.md)
call, all those messages will be also retrieved together through a single
`dequeue_message` call, delivering multiple message handles via
the *`message_handle`* tuple.

The queue access is internally fully synchronized, no external locking
is required.

During application reconfiguration or cleanup, it might be necessary
to wake threads waiting for messages in `dequeue_message`.
This can be achieved using the operator [`set_message_queue_param`](set_message_queue_param.md)
with the parameter *"abort_dequeuing"*. In such case the currently
blocked `dequeue_message` calls return immediately with H_ERR_MQCNCL.

Finally, it is possible to adjust `dequeue_message` behavior
through generic parameters within *`gen_param_name`* and
*`gen_param_value`*. Currently, just a single generic parameter
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

**`queue_handle`** (input_control)  message_queue `→` HHandle

Message queue handle.

Number of elements:
QueueHandle == 1

Restriction:
`QueueHandle != 0`

**`gen_param_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Names of optional generic parameters

Number of elements:
GenParamName == GenParamValue

Default:
"timeout"

List of values:
"timeout"

**`gen_param_value`** (input_control)  tuple(-array) `→` MaybeSequence[Union[int, float, str]]

Values of optional generic parameters

Number of elements:
GenParamName == GenParamValue

Default:
"infinite"

List of values:
"infinite"

**`message_handle`** (output_control)  message(-array) `→` Sequence[HHandle]

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

If the operation succeeds, `dequeue_message` returns 2 (
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

`get_message_tuple`,
`get_message_obj`,
`get_message_param`

## See also

`create_message_queue`,
`clear_message_queue`,
`enqueue_message`,
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
