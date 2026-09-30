# GetMessageObj (Operator)

## Name

`GetMessageObj` — Retrieve an object associated with the key from the message.

## Signature

`static void HOperatorSet.GetMessageObj(out HObject objectData, HTuple messageHandle, HTuple key)`

`HObject HMessage.GetMessageObj(HTuple key)`

`HObject HMessage.GetMessageObj(string key)`

## Description

`GetMessageObj` retrieves an object associated with the *`key`*
from the message denoted by the *`messageHandle`*.
The object has to be previously stored to the message using
[`SetMessageObj`](set_message_obj.md).

The operator returns the data in the parameter *`objectData`*. The
iconic object is copied by the operation. Therefore, clearing or reusing
the message object afterwards will not have any side-effect on the returned
iconic object, afterwards.

If the given *`key`* is not present in the message or if the data
associated with the key is not an object, `GetMessageObj` fails.
Presence of keys and information about the data associated with the key can
be verified using [`GetMessageParam`](get_message_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectData`** (output_object)  object(-array) `→` [HObject](HObject.md)

Tuple value retrieved from the message.

**`messageHandle`** (input_control)  message `→` [HMessage](HMessage.md), [HTuple](HTuple.md) (*IntPtr*)

Message handle.

Number of elements:
MessageHandle == 1

Restriction:
`MessageHandle != 0`

**`key`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Key string or integer.

Number of elements:
Key == 1

## Example (HDevelop)

```
* ...
get_message_param (Message,'key_exists',['simple_string','foo','my_image'],\
                   KeysPresence)
get_message_param (Message,'key_data_type',['simple_string','my_image'],\
                   KeysType)
get_message_obj (Image, Message, 'my_image')
```

## Result

If the operation succeeds, `GetMessageObj` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key), the required key not found in the
message or other than object data associated with given key.

## Possible Predecessors

`DequeueMessage`

## Alternatives

`GetMessageTuple`

## See also

`CreateMessage`,
`ClearMessage`,
`SetMessageTuple`,
`GetMessageTuple`,
`SetMessageObj`,
`SetMessageParam`,
`GetMessageParam`,
`EnqueueMessage`,
`DequeueMessage`

## Module

Foundation
