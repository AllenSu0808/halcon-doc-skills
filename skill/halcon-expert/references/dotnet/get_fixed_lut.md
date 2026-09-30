# GetFixedLut (Operator)

## Name

`GetFixedLut` — Get fixing of “look-up-table” (lut) for “real color images”

## Warning

**`GetFixedLut` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.GetFixedLut(HTuple windowHandle, out HTuple mode)`

`string HWindow.GetFixedLut()`

## Description

Get fixing of “look-up-table” (lut) for “real color images”

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`mode`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode of fixing.

## Possible Successors

`SetFixedLut`

## Module

Foundation
