# disp_distribution (Operator)

## Name

`disp_distribution` — Displays a noise distribution.

## Warning

**`disp_distribution` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def disp_distribution(window_handle: HHandle, distribution: Sequence[float], row: int, column: int, scale: int) -> None`

## Description

`disp_distribution` displays a distribution in the window.
*`row`* and *`column`* define the position of the center of
the graphic.
*`scale`* allows scaling of the graphic, whereby *1* means
displaying all 256 values, *2* means displaying 128 values, *3*
means displaying only 64 values, etc.
Noise distributions can be generated with
operations like [`gauss_distribution`](gauss_distribution.md) or
[`noise_distribution_mean`](noise_distribution_mean.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`distribution`** (input_control)  real-array `→` Sequence[float]

Gray value distribution (513 values).

**`row`** (input_control)  point.y `→` int

Row index of center.

Default:
256

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
row
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`column`** (input_control)  point.x `→` int

Column index of center.

Default:
256

Suggested values:
0, 64, 128, 256

Value range:
`0
≤
column
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`scale`** (input_control)  integer `→` int

Size of display.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6

## Example (HDevelop)

```
open_window(0,0,-1,-1,'root','visible','',WindowHandle)
set_draw(WindowHandle,'fill')
set_color(WindowHandle,'white')
read_image(Image,'monkey')
draw_region(Region,WindowHandle)
noise_distribution_mean(Region,Image,21,Distribution)
disp_distribution (WindowHandle,Distribution,100,100,3)
```

## Possible Predecessors

`open_window`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`,
`set_rgb`,
`set_hsi`,
`noise_distribution_mean`,
`gauss_distribution`

## See also

`gen_region_histo`,
`gauss_distribution`,
`noise_distribution_mean`

## Module

Foundation
