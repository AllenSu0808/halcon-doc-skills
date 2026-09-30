# set_check (Operator)

## Name

`set_check` — Activating and deactivating of HALCON control modes.

## Signature

`set_check( : : Check : )`

## Description

With the help of the operator `set_check` different control modes
of the HALCON system can be activated or deactivated. If a certain control
mode is activated, parameters etc., will be checked at runtime. Whenever an
inconsistency is hereby detected, the program will be interrupted by an
exception.

It is recommendable to activate the control modes during the development of
a program and to deactivate them only after a successfully concluded test run.
For if the control mode is deactivated and an error occurs, the system may
react in an unpredictable way.

The HALCON system provides various possible control modes which can be
activated and deactivated independently. By calling the operator
`set_check` with the name (*`Check`*) of the desired control
mode, this control mode is activated; the control mode is deactivated by
passing its name prefixed with a tilde
(~, e.g., '~data').

Except for the control mode *'memory'* that is set exclusively for
the whole system, all control modes are set thread-specific by default. When
preceding the name of these control modes with a *'ref_'* prefix, only
the reference value of the particular mode is set. The reference value is
used to initialize the respective mode when starting a new user thread.

Available control modes:

- **'color':** —

  If this control mode is activated, only colors may be used which are
  supported by the display for the currently active window. Otherwise an
  error message is displayed.

  In case of deactivated control mode and non existent colors, the {em
  nearest color} is used (see also [`set_color`](set_color.md),
  [`set_gray`](set_gray.md), [`set_rgb`](set_rgb.md)).
- **'text':** —

  If this control mode is activated, it will check the coordinates
  during the setting of the text cursor as well as during the display
  of strings ([`write_string`](write_string.md)) to the effect whether
  a part of a sign would lie outside the window frame (a fact which
  is not forbidden in principle by the system).

  If the control mode is deactivated, the text will be clipped at
  the window frame.
- **'data':** —

  (For program development)

  Checks the consistency of image objects (regions and gray value
  components.
- **'interface':** —

  If this control mode is activated, the interface between the host
  language and the HALCON procedures will be checked in course
  (e.g., typifying and counting of the values).
- **'database':** —

  This is a consistency check of objects (e.g., checks whether
  an object which shall be canceled does indeed exist or not.)
- **'give_error':** —

  Determines whether errors shall trigger exceptions or not. If this
  control modes is deactivated, the application program must provide
  a suitable error treatment itself. Please note that errors which
  are not reported usually lead to undefined output parameters which
  may cause an unpredictable reaction of the program. Details about
  how to handle exceptions in the different HALCON language
  interfaces can be found in the HALCON `“Programmer's Guide”` and
  the `“HDevelop User's Guide”`.
- **'father':** —

  If this control mode is activated when calling the operators
  [`open_window`](open_window.md), HALCON allows only
  the usage of the number of another HALCON window as the father
  window of the new window; otherwise it allows also the usage of
  IDs of operating system windows as the father window. This control
  mode is only relevant for windows of type 'WIN32-Window' and 'X-Window'.
- **'region':** —

  (For program development)

  Checks the consistency of chords (this may lead to a notable
  speed reduction of routines).
- **'clear':** —

  Normally, if a list of objects shall be canceled by using
  [`clear_obj`](clear_obj.md), an exception will be raised, in case individual
  objects do not or no longer exist. If the *'clear'* mode is
  activated, such objects will be ignored.
- **'memory':** —

  (For program development)

  Checks the memory blocks freed by the HALCON
  memory management on consistency and overwriting of memory borders.
- **'all':** —

  Activates all control modes.
- **'none':** —

  Deactivates all control modes.
- **'default':** —

  Default settings: ['give_error','database']

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Check`** (input_control)  string(-array) `→`  (string)

Desired control mode.

Default:
'default'

List of values:
'all', 'clear', 'color', 'data', 'database', 'default', 'father', 'give_error', 'interface', 'memory', 'none', 'region', 'text'

## Result

The operator `set_check` returns the value 2 (
H_MSG_TRUE)
, if
the parameters are correct.
Otherwise an exception will be raised.

## See also

`get_check`,
`set_color`,
`set_rgb`,
`set_hsi`,
`write_string`

## Module

none
