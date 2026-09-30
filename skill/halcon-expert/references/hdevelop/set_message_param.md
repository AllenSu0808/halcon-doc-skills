# set_message_param (Operator)

## Name

`set_message_param` — Set message parameter or invoke commands on the message.

## Signature

`set_message_param( : : MessageHandle, GenParamName, Key, GenParamValue : )`

## Description

`set_message_param` sets message
parameters or invokes action commands on the message.

For each call of `set_message_param`, only a single parameter can be
set. However, there are two types of parameters/commands:

- Parameters/commands applicable to the entire message. In this case
  no keys must be specified, i.e., the parameter *`Key`* must be an empty
  tuple.
- Parameters/commands applicable to the individual keys. In this case a
  non-empty list of keys must be specified in parameter *`Key`*. The
  keys are processed in the same order as specified in the *`Key`*
  parameter.

Key-independent parameter names:

- ***'remove_all_keys'*:** —

  Removes all the keys currently stored in the message and releases
  all the (control or iconic) data associated with those keys.
  The operation results in an empty message.
  Note that contents of *`GenParamValue`* is ignored for this
  parameter, while *`Key`* must be an empty tuple.

Key-specific parameter names:

- ***'remove_key'*:** —

  Removes the keys specified in the *`Key`* parameter and releases
  all the (tuple or object) data associated with those keys.
  If an error occurs while processing one or more keys (in particular
  if the key is invalid), the operator attempts to continue removing
  as many keys as possible before reporting the failure.
  Note that the contents of *`GenParamValue`* is ignored for this
  parameter.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MessageHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MessageHandle`** (input_control, state is modified)  message `→`  (handle)

Message handle.

Number of elements:
MessageHandle == 1

Restriction:
`MessageHandle != 0`

**`GenParamName`** (input_control)  string `→`  (string)

Names of the message parameters or action commands.

Number of elements:
GenParamName == 1

Default:
'remove_key'

List of values:
'remove_all_keys', 'remove_key'

**`Key`** (input_control)  string(-array) `→`  (string / integer)

Message keys the parameter/command should be applied to.

**`GenParamValue`** (input_control)  tuple(-array) `→`  (string / integer / real)

Values of the message parameters or action commands.

## Example (HDevelop)

```
* Remove some keys
set_message_param (Message, 'remove_key', ['my_image', 'simple_string'], [])
```

## Result

If all the operator parameters, and their values, as well as specified
keys are valid, `set_message_param` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`dequeue_message`,
`create_message`

## Possible Successors

`enqueue_message`,
`clear_message`

## See also

`create_message`,
`clear_message`,
`set_message_tuple`,
`get_message_tuple`,
`set_message_obj`,
`get_message_obj`,
`get_message_param`,
`enqueue_message`,
`dequeue_message`

## Module

Foundation
