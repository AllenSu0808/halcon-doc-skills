# QueryWindowType (Operator)

## Name

`QueryWindowType` — Query all available window types.

## Signature

`static void HOperatorSet.QueryWindowType(out HTuple windowTypes)`

`static HTuple HSystem.QueryWindowType()`

`static HTuple HInfo.QueryWindowType()`

## Description

`QueryWindowType` returns a tuple which contains all devices or
software systems, respectively, which are used to display image objects.
You may use `QueryWindowType` usefully while developing machine
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

**`windowTypes`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of available window types.

## Result

`QueryWindowType` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`ResetObjDb`

## Module

Foundation
