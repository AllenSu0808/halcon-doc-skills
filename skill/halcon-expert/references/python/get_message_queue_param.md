# get_message_queue_param (Operator)

## Name

`get_message_queue_param` — Query message queue parameters or information about the queue.

## Signature

`def get_message_queue_param(queue_handle: HHandle, gen_param_name: MaybeSequence[str]) -> Sequence[Union[int, float, str]]`

`def get_message_queue_param_s(queue_handle: HHandle, gen_param_name: MaybeSequence[str]) -> Union[int, float, str]`

## Description

`get_message_queue_param` queries current values of message
queue parameters or other information about the queue status.

Multiple queries can be carried out with a single
`get_message_queue_param` call, passing multiple parameter names
to parameter *`gen_param_name`*. The parameter values are returned
in *`gen_param_value`* in the same order as the parameter names
requested by the caller.

Currently, following parameter names are supported:

- ***"is_empty"*:** —

  Returns *1* if the queue is empty, *0* otherwise.
- ***"message_num"*:** —

  Returns the number of messages currently stored in the queue.
- ***"max_message_num"*:** —

  Returns the current value of the *"max_message_num"* parameter
  of the message queue, as it was set using
  [`set_message_queue_param`](set_message_queue_param.md).
  The default value *-1* stands for no limit.
- ***"wait_on_full"*:** —

  Returns if [`enqueue_message`](enqueue_message.md) would return an error code
  if the message queue is full, or would wait until space becomes
  available.

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

**`gen_param_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Names of the queue parameters or info queries.

Number of elements:
GenParamName == GenParamValue

Default:
"max_message_num"

List of values:
"is_empty", "max_message_num", "message_num", "wait_on_full"

**`gen_param_value`** (output_control)  tuple(-array) `→` Sequence[Union[int, float, str]]

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
