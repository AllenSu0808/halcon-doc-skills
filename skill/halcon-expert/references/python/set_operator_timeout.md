# set_operator_timeout (Operator)

## Name

`set_operator_timeout` — Set a timeout for an operator.

## Signature

`def set_operator_timeout(operator_name: MaybeSequence[str], timeout: MaybeSequence[Union[int, float, str]], mode: str) -> None`

## Description

`set_operator_timeout` sets a timeout for the
operator *`operator_name`*.
*`timeout`* is given in seconds.
Setting *`timeout`* to *0* or *"off"* clears the timeout.
The timeout is set for the current thread only and is not inherited by
child threads.

Multiple operator names can be passed to *`operator_name`*.
In this case, one can either pass a single timeout in *`timeout`*,
which is then set for all operators, or one timeout per operator.

Two timeout modes are supported and selected with *`mode`*:

- **'cancel'** —

  Cancels the execution of the operator after the timeout expires,
  raises the exception H_ERR_TIMEOUT (9400).
  All results computed by the operator are discarded.
- **'break'** —

  Break the execution of the operator after the timeout expires.
  The operator returns normally. If possible, results computed by the
  operator up to the point of the timeout are returned.

## Attention

Note that not all operators support timeouts.
If a given operator supports timeouts and which modes are supported is
described in the execution information section of the reference documentation
of the corresponding operator.

Also note that there is no hard guarantee about the granularity of the
timeout.
The granularity can depend on the operator, its input data and the speed of
the device.
It is typically finer than 10 ms.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`operator_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Operator for which the timeout shall be set.

**`timeout`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float, str]]

Timeout in seconds.

Default:
1

Suggested values:
1, 0.1, 0.5, "off", 0

**`mode`** (input_control)  string `→` str

Timeout mode to be set.

Default:
"cancel"

Suggested values:
"cancel", "break"

## Result

The operator `set_operator_timeout` returns the
value 2 (
H_MSG_TRUE)
if the parameters are correct. Otherwise
an exception will be raised.

## Alternatives

`interrupt_operator`

## See also

`interrupt_operator`,
`get_current_hthread_id`

## Module

Foundation
