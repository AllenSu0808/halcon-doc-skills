# GetFontExtents (Operator)

## Name

`GetFontExtents` — Get the maximum size of all characters of a font.

## Signature

`static void HOperatorSet.GetFontExtents(HTuple windowHandle, out HTuple maxAscent, out HTuple maxDescent, out HTuple maxWidth, out HTuple maxHeight)`

`HTuple HWindow.GetFontExtents(out HTuple maxDescent, out HTuple maxWidth, out HTuple maxHeight)`

`int HWindow.GetFontExtents(out int maxDescent, out int maxWidth, out int maxHeight)`

## Description

`GetFontExtents` queries the maximum width
(*`maxWidth`*), height (*`maxHeight`*), and extension
above and below the baseline (*`maxAscent`* and
*`maxDescent`*, respectively) of the font that is currently set
for the window *`windowHandle`*. The sizes are measured in
pixels.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`maxAscent`** (output_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long / double)

Maximum height above baseline.

**`maxDescent`** (output_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long / double)

Maximum extension below baseline.

**`maxWidth`** (output_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long / double)

Maximum character width.

**`maxHeight`** (output_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long / double)

Maximum character height.

## Result

`GetFontExtents` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetFont`

## Possible Successors

`SetTposition`,
`WriteString`,
`ReadString`,
`ReadChar`

## See also

`GetStringExtents`,
`SetTposition`,
`SetFont`

## Module

Foundation
