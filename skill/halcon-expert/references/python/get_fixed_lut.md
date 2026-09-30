# get_fixed_lut (Operator)

## Name

`get_fixed_lut` — Get fixing of “look-up-table” (lut) for “real color images”

## Warning

**`get_fixed_lut` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def get_fixed_lut(window_handle: HHandle) -> str`

## Description

Get fixing of “look-up-table” (lut) for “real color images”

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`mode`** (output_control)  string `→` str

Mode of fixing.

## Possible Successors

`set_fixed_lut`

## Module

Foundation
