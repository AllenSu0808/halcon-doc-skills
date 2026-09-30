# query_window_type (Operator)

## Name

`query_window_type` — Query all available window types.

## Signature

`def query_window_type() -> Sequence[str]`

## Description

`query_window_type` returns a tuple which contains all devices or
software systems, respectively, which are used to display image objects.
You may use `query_window_type` usefully while developing machine
independent programs.
Possible values are:

- ***"X-Window"*** —

  X-Window Version 11.
- ***"WIN32-Window"*** —

  Microsoft Windows.
- ***"pixmap"*** —

  Windows are not displayed, but managed in memory.
  In this manner it is possible to port HALCON programs to computers without
  graphical display.
- ***"PostScript"*** —

  Objects are output to a PostScript File.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_types`** (output_control)  string-array `→` Sequence[str]

Names of available window types.

## Result

`query_window_type` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`reset_obj_db`

## Module

Foundation
