# set_spy (Operator)

## Name

`set_spy` — Control of the HALCON Debugging Tools.

## Signature

`def set_spy(class_val: str, value: Union[str, int, float]) -> None`

## Description

The operator `set_spy` is the HALCON debugging tool.
This tool allows the flexible control of the input and output data
of HALCON-operators - in graphical as well as in textual form.
The data control is activated by using

`set_spy(::'mode','on':)`,

and deactivated by using

`set_spy(::'mode','off':)`.

The debugging tool can further be activated with the help of the
environment variable HALCONSPY. The definition of this variable
corresponds to calling up *"mode"* and *"on"*.

The following control modes (*`class`*) can be tuned using
*`value`*:

- ***`class`* = *"operator"*** —

  When a routine is called, its name and the
  names of its parameters will be given
  (in TRIAS notation).

  List of values:
   *"on"*, *"off"*

  Default:
   *"off"*.
- ***`class`* = *"input_control"*** —

  When a routine is called, the names and values of the
  input control parameters will be given.

  List of values:
   *"on"*, *"off"*

  Default:
   *"off"*.
- ***`class`* = *"output_control"*** —

  When a routine is called, the names and values of the
  output control parameters are given.

  List of values:
   *"on"*, *"off"*

  Default:
   *"off"*.
- ***`class`* = *"parameter_values"*** —

  Additional information on *"input_control"* and
  *"output_control"*:
  indicates how many values per parameter shall be
  displayed at most (maximum tuple length of the output).

  Default:
   *4*
- ***`class`* = *"db"*** —

  Information concerning the 4 relations in the
  HALCON-database. This is especially valuable
  in looking for forgotten [`clear_obj`](clear_obj.md).

  List of values:
   *"on"*, *"off"*

  Default:
   *"off"*.
- ***`class`* = *"time"*** —

  Processing time of the operator

  List of values:
   *"on"*, *"off"*

  Default:
   *"off"*.
- ***`class`* = *"log_file"*** —

  Spy can hereby divert the text output into a file having
  been opened with [`open_file`](open_file.md).

  List of values:
   a file handle (see [`open_file`](open_file.md))
- ***`class`* = *"internal"*** —

  If *"internal"* is activated, spy will display the
  internal procedures and their parameters (file/line)
  while an HALCON-operator
  is processed.

  List of values:
   *"on"*, *"off"*

  Default:
   *"off"*.

Each output starts with the thread handle, followed by a global counter
that marks the order of the outputs. In multi-threaded applications, this
information can be used to assign the output to individual user threads
and to reconstruct the chronological sequence.

## Attention

Note that under Windows the output on stdout works only in combination with a
console application.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`class`** (input_control)  string `→` str

Control mode

Default:
"mode"

List of values:
"db", "input_control", "internal", "log_file", "mode", "operator", "output_control", "parameter_values", "time"

**`value`** (input_control)  string `→` Union[str, int, float]

State of the control mode to be set.

Default:
"on"

Suggested values:
"on", "off", 1, 2, 3, 4, 5, 10, 50, 0.0, 1.0, 2.0, 5.0, 10.0

## Example (C)

```
/* init spy: Setting of the wished control modi */
set_spy("mode","on");
set_spy("operator","on");
set_spy("input_control","on");
set_spy("output_control","on");
/* calling of program section, that will be examined */
set_spy("mode","off");
```

## Result

The operator `set_spy` returns the value 2 (
H_MSG_TRUE)
if the parameters
are correct.
Otherwise an exception is raised.

## Possible Predecessors

`reset_obj_db`

## See also

`get_spy`,
`query_spy`

## Module

Foundation
