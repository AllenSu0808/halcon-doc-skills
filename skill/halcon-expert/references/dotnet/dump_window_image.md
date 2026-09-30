# DumpWindowImage (Operator)

## Name

`DumpWindowImage` — Write the window content in an image object.

## Signature

`static void HOperatorSet.DumpWindowImage(out HObject image, HTuple windowHandle)`

`void HImage.DumpWindowImage(HWindow windowHandle)`

`HImage HWindow.DumpWindowImage()`

## Description

`DumpWindowImage` writes the content of the graphics window
(*`windowHandle`*) in an image (*`image`*).
To transform gray values the current color table of the window is
used.

## Attention

Under Unix-like systems, the graphics window must be completely visible on the
root window, because otherwise the contents of the window cannot be
read due to limitations in X Windows.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image `→` [HImage](HImage.md) (byte)

Saved image.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Result

If the window is valid `DumpWindowImage` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetDraw`,
`SetColor`,
`SetColored`,
`SetLineWidth`,
`DispRegion`

## See also

`OpenWindow`,
`SetSystem`,
`DumpWindow`

## Module

Foundation
