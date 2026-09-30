# SetMessageQueueParam (Operator)

## Name

`SetMessageQueueParam` — Set message queue parameters or invoke commands on the queue.

## Signature

`static void HOperatorSet.SetMessageQueueParam(HTuple queueHandle, HTuple genParamName, HTuple genParamValue)`

`void HMessageQueue.SetMessageQueueParam(HTuple genParamName, HTuple genParamValue)`

`void HMessageQueue.SetMessageQueueParam(string genParamName, HTuple genParamValue)`

## Description

`SetMessageQueueParam` sets message
queue parameters or invokes action commands on the queue.

Multiple parameters and action commands can be passed through a single
`SetMessageQueueParam` call, passing multiple parameter names
in a tuple *`genParamName`* and corresponding values
in *`genParamValue`*. There must be always the same number
of names and values and the values must be in the same order
as the names. The parameters and action commands are applied
in the same order passed in *`genParamName`*. It is important to
understand that in particular in case of the action commands, it might not
be possible to revert the effect of previous action commands if a later
command fails, the caller therefore might need to be careful when
setting multiple commands in a single call.

Currently supported parameter names are:

- ***"abort_dequeuing"*:** —
- ***"abort_enqueuing"*:** —

  Aborts any [`DequeueMessage`](dequeue_message.md) or [`EnqueueMessage`](enqueue_message.md) operator
  waiting in any thread for data to be delivered.
  Any currently waiting call will unblock
  and return H_ERR_MQCNCL. Any [`DequeueMessage`](dequeue_message.md) or
  [`EnqueueMessage`](enqueue_message.md) call invoked
  in the future will return H_ERR_MQCNCL immediately regardless of the
  queue status.

  This command is typically needed for cleanup when any threads
  using the message queue and possibly blocked in [`DequeueMessage`](dequeue_message.md)
  or [`EnqueueMessage`](enqueue_message.md)
  must be released, because it is not allowed to destroy the queue
  ([`ClearMessageQueue`](clear_message_queue.md)) while any operators might still use it.
  It might be necessary to wait for the completion of those threads
  after invoking the *"abort_dequeuing"* and *"abort_enqueuing"*
  command to be sure
  any operators using the queue are completed.

  The message data currently stored in the message queue is not affected
  by the command. The effect of canceling any further
  [`DequeueMessage`](dequeue_message.md) or [`EnqueueMessage`](enqueue_message.md) calls can be reset
  again using the
  *"restore_queue"* command.

  The parameter value must be integer *1*.
- ***"restore_queue"*:** —

  Clears the effect of a previous *"abort_dequeuing"* and
  *"abort_enqueuing"* command.
  This means the next call to [`DequeueMessage`](dequeue_message.md) will again
  attempt to deliver message data, and the next call to
  [`EnqueueMessage`](enqueue_message.md) will be able to enqueue new messages.

  The parameter value must be integer *1*.
- ***"flush_queue"*:** —

  Flushes the queue. All currently enqueued messages are removed from
  the queue and all associated resources, in particular the tuple
  or object data stored in the messages, are released.

  The parameter value must be integer *1*.
- ***"max_message_num"*:** —

  Sets the maximum number of messages that can be stored in the queue.
  The setting *"wait_on_full"* can be used to change the
  behavior of an [`EnqueueMessage`](enqueue_message.md) operator call that would result
  in the queue containing more messages after the operation than the defined
  maximum.
  In such a case, if *"wait_on_full"* is set to *"false"*,
  [`EnqueueMessage`](enqueue_message.md) would fail with code H_ERR_MQOVL.
  If *"wait_on_full"* is set to *"true"*,
  [`EnqueueMessage`](enqueue_message.md) would wait until enough space becomes
  available in the queue.

  Setting the *"max_message_num"* parameter has no effect on
  the messages already present in the queue. No messages that are already
  in the queue can be removed by this operation.

  The parameter value can be a positive integer or *-1* if
  the queue size should be unlimited. The string value *"infinite"*
  is accepted as well. The queue size is unlimited by default.

  Suggested values:
   *-1*, *"infinite"*,
  *10*, *20*

  Default:
   *-1*
- ***"wait_on_full"*:** —

  If *"max_message_num"* is set for the queue, this parameter can be
  used to configure the behavior of [`EnqueueMessage`](enqueue_message.md) when the queue
  is full.

  If this parameter is set to *"false"* (default), then
  [`EnqueueMessage`](enqueue_message.md) returns the value H_ERR_MQOVL when the queue is
  full.

  If this parameter is set to *"true"*, then [`EnqueueMessage`](enqueue_message.md)
  waits when the queue is full until space becomes available again. This
  can happen through a call to [`DequeueMessage`](dequeue_message.md), by increasing the
  value of *"max_message_num"*, or by manually clearing the queue
  using *"flush_queue"*.

  If a call to [`EnqueueMessage`](enqueue_message.md) attempts to place more messages in
  the queue than allowed by *"max_message_num"*, then
  [`EnqueueMessage`](enqueue_message.md) returns an error regardless of the setting of
  *"wait_on_full"*.

  Pending calls to [`EnqueueMessage`](enqueue_message.md) can also be aborted using
  *"abort_enqueuing"*.

  List of values:
   *"false"*, *"true"*

  Default:
   *"false"*

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

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the queue parameters or action commands.

Number of elements:
GenParamName == GenParamValue

Default:
"max_message_num"

List of values:
"abort_dequeuing", "abort_enqueuing", "flush_queue", "max_message_num", "restore_queue", "wait_on_full"

**`genParamValue`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of the queue parameters or action commands.

Number of elements:
GenParamName == GenParamValue

Default:
1

Suggested values:
1, -1, "true", "false"

## Example (HDevelop)

```
* abort waiting dequeue_message operators
set_message_queue_param (Queue, 'abort_dequeuing', 1)
* abort waiting enqueue_message operators (if 'wait_on_full' is set)
set_message_queue_param (Queue, 'abort_enqueuing', 1)
*
* ... wait for the operators to abort
*
* Restore normal queue operations
set_message_queue_param (Queue, 'restore_queue', 1)
```

## Result

If all the operator parameters and their values are valid,
`SetMessageQueueParam` returns 2 (
H_MSG_TRUE)
. Otherwise an exception is
raised.

## Possible Predecessors

`CreateMessageQueue`

## Possible Successors

`ClearMessageQueue`

## See also

`CreateMessageQueue`,
`ClearMessageQueue`,
`EnqueueMessage`,
`DequeueMessage`,
`GetMessageQueueParam`,
`CreateMessage`,
`ClearMessage`,
`SetMessageTuple`,
`GetMessageTuple`,
`SetMessageObj`,
`GetMessageObj`

## Module

Foundation
