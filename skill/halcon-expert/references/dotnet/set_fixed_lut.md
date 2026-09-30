# SetFixedLut (Operator)

## Name

`SetFixedLut` — Fix “look-up-table” (lut) for “real color images”.

## Warning

**`SetFixedLut` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.SetFixedLut(HTuple windowHandle, HTuple mode)`

`void HWindow.SetFixedLut(string mode)`

## Description

Fix “look-up-table” (lut) for “real color images”.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode of fixing.

Default:
"true"

List of values:
"false", "true"

## Possible Predecessors

`GetFixedLut`

## Module

Foundation
