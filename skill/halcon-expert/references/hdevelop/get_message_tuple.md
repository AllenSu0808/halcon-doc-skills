# get_message_tuple (Operator)

## Name

`get_message_tuple` — Retrieve a tuple associated with the key from the message.

## Signature

`get_message_tuple( : : MessageHandle, Key : TupleData)`

## Description

`get_message_tuple` retrieves a tuple associated with the *`Key`*
from the message denoted by the *`MessageHandle`*.
The tuple has to be previously stored to the message using
[`set_message_tuple`](set_message_tuple.md).

The operator returns the data in the parameter *`TupleData`*.
The data including strings is copied by the operation, the message can thus
be immediately reused.

If the given *`Key`* is not present in the message or if the data
associated with the key is not a tuple, `get_message_tuple` fails.
Presence of keys and information about the data associated with the key
can be verified using [`get_message_param`](get_message_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MessageHandle`** (input_control)  message `→`  (handle)

Message handle.

Number of elements:
MessageHandle == 1

Restriction:
`MessageHandle != 0`

**`Key`** (input_control)  string `→`  (string / integer)

Key string or integer.

Number of elements:
Key == 1

**`TupleData`** (output_control)  tuple(-array) `→`  (string / integer / real / handle)

Tuple value retrieved from the message.

## Example (HDevelop)

```
* ...
get_message_param (Message,'key_exists',['simple_string','foo','my_image'],\
                   KeysPresence)
get_message_param (Message,'key_data_type',['simple_string','my_image'],\
                   KeysType)
get_message_tuple (Message,'simple_string',TupleString)
```

## Result

If the operation succeeds, `get_message_tuple` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key), the required key not found in the
message, or other than tuple data associated with given key.

## Possible Predecessors

`dequeue_message`

## Alternatives

`get_message_obj`

## See also

`create_message`,
`clear_message`,
`set_message_tuple`,
`set_message_obj`,
`get_message_obj`,
`set_message_param`,
`get_message_param`,
`enqueue_message`,
`dequeue_message`

## Module

Foundation
