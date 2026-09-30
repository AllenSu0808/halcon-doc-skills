# clear_message (Operator)

## Name

`clear_message` — Close a message handle and release all associated resources.

## Signature

`def clear_message(message_handle: MaybeSequence[HHandle]) -> None`

## Description

`clear_message` closes a message handle *`message_handle`* that
was previously opened with [`create_message`](create_message.md) or
[`dequeue_message`](dequeue_message.md). Any resources owned by the message, in particular
the tuple or object data stored in the message, will be released.

Multiple message handles can be closed in a single `clear_message`
call, passing them as a tuple to the *`message_handle`* parameter.

## Attention

The handle(s) must not be used again after being invalidated using
`clear_message`. Using an invalid handle results in
undefined behavior.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- message_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`message_handle`** (input_control, state is modified)  message(-array) `→` MaybeSequence[HHandle]

Message handle(s) to be closed.

Number of elements:
MessageHandle >= 1

Restriction:
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

If the message handle(s) passed to the operator are valid,
`clear_message` returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.
If a tuple of handles is passed and some of them are invalid,
`clear_message` attempts to clear as many handles from the tuple as
possible before reporting the error.

## Possible Predecessors

`create_message`,
`dequeue_message`

## See also

`create_message`,
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
