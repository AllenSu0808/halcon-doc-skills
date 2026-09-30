# create_message (Operator)

## Name

`create_message` — Create a new empty message.

## Signature

`create_message( : : : MessageHandle)`

## Description

`create_message` creates a new empty message. The output parameter
*`MessageHandle`* is a handle to the newly created message
and is used to identify the message in any subsequent operator
call using the message.

The message serves as a dictionary-like container that can be passed
between the threads of an application using asynchronous message queues.
Alternatively, HALCON also provides dictionaries ([`create_dict`](create_dict.md)) to
group parameters in programs and procedures.

Messages can store an arbitrary number of entries, each having its unique
key (string or integer) and associated value. Each key can refer either to
a control parameter tuple or to an iconic object. These data are stored to
the message using [`set_message_tuple`](set_message_tuple.md) or [`set_message_obj`](set_message_obj.md),
respectively, from where they can be retrieved again using
[`get_message_tuple`](get_message_tuple.md) or [`get_message_obj`](get_message_obj.md).

The control parameter tuples stored in the message are always deep copies
of the original data. The original data can thus be reused immediately
after the [`set_message_tuple`](set_message_tuple.md) call without affecting the message.
Notable exceptions are handles: Storing any handle in the message
will copy the handle value, but not the resource behind the handle.

As mentioned above, the messages can be passed between the threads of an
application using asynchronous message queues.
The data can be appended to the queue by multiple producer threads
using [`enqueue_message`](enqueue_message.md) and retrieved from the queue
by multiple receiver threads using [`dequeue_message`](dequeue_message.md).
All these operations are internally properly synchronized.
Therefore, the queue can be safely accessed by all producers
and consumers without any explicit locking.
All the enqueued messages are copied by the
[`enqueue_message`](enqueue_message.md) operation. The original message(s) can thus be
immediately reused after the [`enqueue_message`](enqueue_message.md) call without affecting
the enqueued copy.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MessageHandle`** (output_control)  message `→`  (handle)

Handle of the newly created message.

Number of elements:
MessageHandle == 1

Assertion:
`MessageHandle != 0`

## Example (HDevelop)

```
MessageHandles := []
for idx := 0 to 4 by 1
  create_message (MessageHandle)
  MessageHandles[idx]:= MessageHandle
endfor
* ...
```

## Result

Returns 2 (
H_MSG_TRUE)
unless a resource allocation error occurs.

## Possible Successors

`set_message_tuple`,
`set_message_obj`

## Alternatives

`create_dict`

## See also

`clear_message`,
`set_message_tuple`,
`get_message_tuple`,
`set_message_obj`,
`get_message_obj`,
`set_message_param`,
`get_message_param`,
`enqueue_message`,
`dequeue_message`

## Module

Foundation
