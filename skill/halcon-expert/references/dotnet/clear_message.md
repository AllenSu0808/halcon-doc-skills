# ClearMessage (Operator)

## Name

`ClearMessage` — Close a message handle and release all associated resources.

## Signature

`static void HOperatorSet.ClearMessage(HTuple messageHandle)`

`static void HMessage.ClearMessage(HMessage[] messageHandle)`

`void HMessage.ClearMessage()`

## Description

`ClearMessage` closes a message handle *`messageHandle`* that
was previously opened with [`CreateMessage`](create_message.md) or
[`DequeueMessage`](dequeue_message.md). Any resources owned by the message, in particular
the tuple or object data stored in the message, will be released.

Multiple message handles can be closed in a single `ClearMessage`
call, passing them as a tuple to the *`messageHandle`* parameter.

## Attention

The handle(s) must not be used again after being invalidated using
`ClearMessage`. Using an invalid handle results in
undefined behavior.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- messageHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`messageHandle`** (input_control, state is modified)  message(-array) `→` [HMessage](HMessage.md), [HTuple](HTuple.md) (*IntPtr*)

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
`ClearMessage` returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.
If a tuple of handles is passed and some of them are invalid,
`ClearMessage` attempts to clear as many handles from the tuple as
possible before reporting the error.

## Possible Predecessors

`CreateMessage`,
`DequeueMessage`

## See also

`CreateMessage`,
`SetMessageTuple`,
`GetMessageTuple`,
`SetMessageObj`,
`GetMessageObj`,
`SetMessageParam`,
`GetMessageParam`,
`EnqueueMessage`,
`DequeueMessage`

## Module

Foundation
