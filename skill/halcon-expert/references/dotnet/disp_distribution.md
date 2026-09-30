# DispDistribution (Operator)

## Name

`DispDistribution` — Displays a noise distribution.

## Warning

**`DispDistribution` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.DispDistribution(HTuple windowHandle, HTuple distribution, HTuple row, HTuple column, HTuple scale)`

`void HWindow.DispDistribution(HTuple distribution, int row, int column, int scale)`

## Description

`DispDistribution` displays a distribution in the window.
*`row`* and *`column`* define the position of the center of
the graphic.
*`scale`* allows scaling of the graphic, whereby *1* means
displaying all 256 values, *2* means displaying 128 values, *3*
means displaying only 64 values, etc.
Noise distributions can be generated with
operations like [`GaussDistribution`](gauss_distribution.md) or
[`NoiseDistributionMean`](noise_distribution_mean.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`distribution`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Gray value distribution (513 values).

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

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

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

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

**`scale`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

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

`OpenWindow`,
`SetDraw`,
`SetColor`,
`SetColored`,
`SetLineWidth`,
`SetRgb`,
`SetHsi`,
`NoiseDistributionMean`,
`GaussDistribution`

## See also

`GenRegionHisto`,
`GaussDistribution`,
`NoiseDistributionMean`

## Module

Foundation
