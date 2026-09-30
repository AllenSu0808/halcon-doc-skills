# get_message_queue_param (Operator)

## Name

`get_message_queue_param` — Query message queue parameters or information about the queue.

## Signature

`get_message_queue_param( : : QueueHandle, GenParamName : GenParamValue)`

## Description

`get_message_queue_param` queries current values of message
queue parameters or other information about the queue status.

Multiple queries can be carried out with a single
`get_message_queue_param` call, passing multiple parameter names
to parameter *`GenParamName`*. The parameter values are returned
in *`GenParamValue`* in the same order as the parameter names
requested by the caller.

Currently, following parameter names are supported:

- ***'is_empty'*:** —

  Returns *1* if the queue is empty, *0* otherwise.
- ***'message_num'*:** —

  Returns the number of messages currently stored in the queue.
- ***'max_message_num'*:** —

  Returns the current value of the *'max_message_num'* parameter
  of the message queue, as it was set using
  [`set_message_queue_param`](set_message_queue_param.md).
  The default value *-1* stands for no limit.
- ***'wait_on_full'*:** —

  Returns if [`enqueue_message`](enqueue_message.md) would return an error code
  if the message queue is full, or would wait until space becomes
  available.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`QueueHandle`** (input_control)  message_queue `→`  (handle)

Message queue handle.

Number of elements:
QueueHandle == 1

Restriction:
`QueueHandle != 0`

**`GenParamName`** (input_control)  string(-array) `→`  (string)

Names of the queue parameters or info queries.

Number of elements:
GenParamName == GenParamValue

Default:
'max_message_num'

List of values:
'is_empty', 'max_message_num', 'message_num', 'wait_on_full'

**`GenParamValue`** (output_control)  tuple(-array) `→`  (string / integer / real)

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

If all the operator parameters are valid, `get_message_queue_param`
returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`create_message_queue`,
`enqueue_message`,
`dequeue_message`

## See also

`create_message_queue`,
`clear_message_queue`,
`enqueue_message`,
`dequeue_message`,
`set_message_queue_param`,
`create_message`,
`clear_message`,
`set_message_tuple`,
`get_message_tuple`,
`set_message_obj`,
`get_message_obj`

## Module

Foundation
