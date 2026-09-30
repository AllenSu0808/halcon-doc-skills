# while (Operator)

## Name

`while` — Starts a loop block that is executed as long as the condition is true.

## Signature

`while( : : Condition : )`

## Description

`while` executes the loop body up to the corresponding
[`endwhile`](endwhile.md) statement as long as the *`Condition`* parameter
evaluates to *'true'* (or a number not equal *0*).

If the condition evaluates to *'false'* (*0*) the program is
continued after the corresponding [`endwhile`](endwhile.md) statement.

## Parameters

**`Condition`** (input_control)  integer `→`  (integer)

Condition for loop.

## Example (HDevelop)

```
dev_update_window ('off')
dev_close_window ()
dev_open_window (0, 0, 512, 512, 'black', WindowID)
read_image (Image, 'particle')
dev_display (Image)
stop ()
threshold (Image, Large, 110, 255)
dilation_circle (Large, LargeDilation, 7.5)
dev_display (Image)
dev_set_draw ('margin')
dev_set_line_width (3)
dev_set_color ('green')
dev_display (LargeDilation)
dev_set_draw ('fill')
stop ()
complement (LargeDilation, NotLarge)
reduce_domain (Image, NotLarge, ParticlesRed)
mean_image (ParticlesRed, Mean, 31, 31)
dyn_threshold (ParticlesRed, Mean, SmallRaw, 3, 'light')
opening_circle (SmallRaw, Small, 2.5)
connection (Small, SmallConnection)
dev_display (Image)
dev_set_colored (12)
dev_display (SmallConnection)
stop ()
dev_set_color ('green')
dev_display (Image)
dev_display (SmallConnection)
Button := 1
while (Button == 1)
  dev_set_color ('green')
  get_mbutton (WindowID, Row, Column, Button)
  dev_display (Image)
  dev_display (SmallConnection)
  dev_set_color ('red')
  select_region_point (SmallConnection, SmallSingle, Row, Column)
  dev_display (SmallSingle)
  NumSingle := |SmallSingle|
  if (NumSingle == 1)
    intensity (SmallSingle, Image, MeanGray, DeviationGray)
    area_center (SmallSingle, Area, Row, Column)
    dev_set_color ('yellow')
    set_tposition (WindowID, Row, Column)
    write_string (WindowID, 'Area='+Area+', Int='+MeanGray)
  endif
endwhile
dev_set_line_width (1)
dev_update_window ('on')
```

## Result

If the values of the specified parameters are correct,
`while` (as operator) returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Alternatives

`for`,
`until`

## See also

`repeat`,
`break`,
`continue`,
`if`,
`elseif`,
`else`

## Module

Foundation
