# set_fixed_lut (Operator)

## Name

`set_fixed_lut` — Fix “look-up-table” (lut) for “real color images”.

## Warning

**`set_fixed_lut` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`set_fixed_lut( : : WindowHandle, Mode : )`

## Description

Fix “look-up-table” (lut) for “real color images”.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Mode`** (input_control)  string `→`  (string)

Mode of fixing.

Default:
'true'

List of values:
'false', 'true'

## Possible Predecessors

`get_fixed_lut`

## Module

Foundation
