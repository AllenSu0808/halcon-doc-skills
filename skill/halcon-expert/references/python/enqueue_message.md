# enqueue_message (Operator)

## Name

`enqueue_message` — Enqueue one or more messages to the message queue.

## Signature

`def enqueue_message(queue_handle: HHandle, message_handle: MaybeSequence[HHandle], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> None`

## Description

`enqueue_message` enqueues one or more messages to the message queue
denoted by the *`queue_handle`* parameter.
The enqueued messages can be retrieved from the queue by any thread using
[`dequeue_message`](dequeue_message.md).

The messages (see [`create_message`](create_message.md)) to be enqueued are specified
in the *`message_handle`* parameter which accepts a single handle
as well as tuple of handles. When enqueuing multiple handles together
in a single `enqueue_message` call, they are delivered again
together through a single [`dequeue_message`](dequeue_message.md) call.

Multiple producer (enqueuing) threads and multiple consumer (dequeuing)
threads can share the same queue at a time. The messages are delivered
in FIFO (first-in first-out) order. Every message is delivered only once,
even if multiple consumer threads are using the queue.

The queue access is internally fully synchronized, no external locking
is required. If the queue is empty and there is at least one consumer
thread waiting for the message data in [`dequeue_message`](dequeue_message.md),
one of those threads is woken up by a successful `enqueue_message`
call and the enqueued message data are immediately delivered.
Otherwise the message data is appended to the queue asynchronously,
to be delivered as soon as a consumer thread is ready to dequeue
the message data again.

All the enqueued messages (*`message_handle`*) are copied by the
`enqueue_message` operation. The original message(s) can thus be
immediately reused after the `enqueue_message` call without affecting
the enqueued copy.

If, after the operation, the queue would hold a larger number of messages
than the specified maximum number, either the error H_ERR_MQOVL is returned,
or the operator waits until space becomes available in the queue.
The behavior can be configured for the queue using the parameter
*"wait_on_full"* in the operator [`set_message_queue_param`](set_message_queue_param.md).
The maximum number of messages that may be held is defined by the
parameter value *"max_message_num"* in the operator
[`set_message_queue_param`](set_message_queue_param.md).
If more messages shall be enqueued than the queue has capacity,
i.e. if the tuple *`message_handle`* has more elements than
what is set in ValRe('max_message_num'), the operator
`enqueue_message` will always return the error code
H_ERR_MQOVL, independent of the setting of *"wait_on_full"*.

Finally, it is possible to adjust `enqueue_message` behavior
through generic parameters within *`gen_param_name`* and
*`gen_param_value`*. Currently, just a single generic parameter
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

**`queue_handle`** (input_control)  message_queue `→` HHandle

Message queue handle.

Number of elements:
QueueHandle == 1

Restriction:
`QueueHandle != 0`

**`message_handle`** (input_control)  message(-array) `→` MaybeSequence[HHandle]

Handle(s) of message(s) to be enqueued.

Number of elements:
MessageHandle > 0

Restriction:
`MessageHandle != 0`

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

Names of optional generic parameters.

Number of elements:
GenParamName == GenParamValue

**`gen_param_value`** (input_control)  tuple-array `→` Sequence[Union[int, float, str]]

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

If the operation succeeds, `enqueue_message` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters or resource allocation error.

## Possible Predecessors

`set_message_tuple`,
`set_message_obj`

## See also

`create_message_queue`,
`clear_message_queue`,
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
