# SetMessageParam (Operator)

## Name

`SetMessageParam` — Set message parameter or invoke commands on the message.

## Signature

`static void HOperatorSet.SetMessageParam(HTuple messageHandle, HTuple genParamName, HTuple key, HTuple genParamValue)`

`void HMessage.SetMessageParam(string genParamName, HTuple key, HTuple genParamValue)`

`void HMessage.SetMessageParam(string genParamName, string key, HTuple genParamValue)`

## Description

`SetMessageParam` sets message
parameters or invokes action commands on the message.

For each call of `SetMessageParam`, only a single parameter can be
set. However, there are two types of parameters/commands:

- Parameters/commands applicable to the entire message. In this case
  no keys must be specified, i.e., the parameter *`key`* must be an empty
  tuple.
- Parameters/commands applicable to the individual keys. In this case a
  non-empty list of keys must be specified in parameter *`key`*. The
  keys are processed in the same order as specified in the *`key`*
  parameter.

Key-independent parameter names:

- ***"remove_all_keys"*:** —

  Removes all the keys currently stored in the message and releases
  all the (control or iconic) data associated with those keys.
  The operation results in an empty message.
  Note that contents of *`genParamValue`* is ignored for this
  parameter, while *`key`* must be an empty tuple.

Key-specific parameter names:

- ***"remove_key"*:** —

  Removes the keys specified in the *`key`* parameter and releases
  all the (tuple or object) data associated with those keys.
  If an error occurs while processing one or more keys (in particular
  if the key is invalid), the operator attempts to continue removing
  as many keys as possible before reporting the failure.
  Note that the contents of *`genParamValue`* is ignored for this
  parameter.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- messageHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`messageHandle`** (input_control, state is modified)  message `→` [HMessage](HMessage.md), [HTuple](HTuple.md) (*IntPtr*)

Message handle.

Number of elements:
MessageHandle == 1

Restriction:
`MessageHandle != 0`

**`genParamName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Names of the message parameters or action commands.

Number of elements:
GenParamName == 1

Default:
"remove_key"

List of values:
"remove_all_keys", "remove_key"

**`key`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Message keys the parameter/command should be applied to.

**`genParamValue`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of the message parameters or action commands.

## Example (HDevelop)

```
* Remove some keys
set_message_param (Message, 'remove_key', ['my_image', 'simple_string'], [])
```

## Result

If all the operator parameters, and their values, as well as specified
keys are valid, `SetMessageParam` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`DequeueMessage`,
`CreateMessage`

## Possible Successors

`EnqueueMessage`,
`ClearMessage`

## See also

`CreateMessage`,
`ClearMessage`,
`SetMessageTuple`,
`GetMessageTuple`,
`SetMessageObj`,
`GetMessageObj`,
`GetMessageParam`,
`EnqueueMessage`,
`DequeueMessage`

## Module

Foundation
