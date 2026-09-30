# WriteLut (Operator)

## Name

`WriteLut` — Write look-up-table (lut) as file.

## Warning

**`WriteLut` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.WriteLut(HTuple windowHandle, HTuple fileName)`

`void HWindow.WriteLut(string fileName)`

## Description

`WriteLut` saves the look-up-table (resp. the part of it that
is relevant for displaying image gray values) of the valid output
window into a file named '*`fileName`*.lut'. It can be read again
later with [`SetLut`](set_lut.md).

## Attention

`WriteLut` is only suitable for systems using 256 colors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name (of file containing the look-up-table).

Default:
"/tmp/lut"

File extension:
.`lut`

## Result

`WriteLut` returns 2 (
H_MSG_TRUE)
if the window with the required
properties (256 colors) is valid and the parameter (file name) is
correct. Otherwise an exception is raised.

## Possible Predecessors

`SetLut`

## See also

`SetLut`,
`SetPixel`,
`GetPixel`

## Module

Foundation
