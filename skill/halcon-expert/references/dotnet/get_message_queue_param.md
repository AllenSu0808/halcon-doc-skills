# GetMessageQueueParam (Operator)

## Name

`GetMessageQueueParam` — Query message queue parameters or information about the queue.

## Signature

`static void HOperatorSet.GetMessageQueueParam(HTuple queueHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HMessageQueue.GetMessageQueueParam(HTuple genParamName)`

`HTuple HMessageQueue.GetMessageQueueParam(string genParamName)`

## Description

`GetMessageQueueParam` queries current values of message
queue parameters or other information about the queue status.

Multiple queries can be carried out with a single
`GetMessageQueueParam` call, passing multiple parameter names
to parameter *`genParamName`*. The parameter values are returned
in *`genParamValue`* in the same order as the parameter names
requested by the caller.

Currently, following parameter names are supported:

- ***"is_empty"*:** —

  Returns *1* if the queue is empty, *0* otherwise.
- ***"message_num"*:** —

  Returns the number of messages currently stored in the queue.
- ***"max_message_num"*:** —

  Returns the current value of the *"max_message_num"* parameter
  of the message queue, as it was set using
  [`SetMessageQueueParam`](set_message_queue_param.md).
  The default value *-1* stands for no limit.
- ***"wait_on_full"*:** —

  Returns if [`EnqueueMessage`](enqueue_message.md) would return an error code
  if the message queue is full, or would wait until space becomes
  available.

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

Names of the queue parameters or info queries.

Number of elements:
GenParamName == GenParamValue

Default:
"max_message_num"

List of values:
"is_empty", "max_message_num", "message_num", "wait_on_full"

**`genParamValue`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of the queue parameters or info queries.

Number of elements:
GenParamName == GenParamValue

## Example (HDevelop)

```
create_message_queue (QueueHandle)
set_message_queue_param ( QueueHandle, 'max_message_num', 10)
* ...
get_message_queue_param( QueueHandle, 'message_num', Num)
```

## Result

If all the operator parameters are valid, `GetMessageQueueParam`
returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`CreateMessageQueue`,
`EnqueueMessage`,
`DequeueMessage`

## See also

`CreateMessageQueue`,
`ClearMessageQueue`,
`EnqueueMessage`,
`DequeueMessage`,
`SetMessageQueueParam`,
`CreateMessage`,
`ClearMessage`,
`SetMessageTuple`,
`GetMessageTuple`,
`SetMessageObj`,
`GetMessageObj`

## Module

Foundation
