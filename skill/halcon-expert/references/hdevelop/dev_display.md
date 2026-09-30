# dev_display (Operator)

## Name

`dev_display` — Displays image objects in the current graphics window.

## Signature

`dev_display(Object : : : )`

## Description

`dev_display` displays an iconic object (image, region, or XLD)
in the active graphics window. This is equivalent to a double click
on an icon variable inside the variable window.

## Attention

Using the code export feature of HDevelop, the code that is generated
for this operator may have a different behavior than the related
HALCON operator.
For a detailed description of the code export of HDevelop graphics
operators into the different programming languages see in the
`“HDevelop User's Guide”` the chapter `Code Export`
-> `General Aspects of Code Generation`
-> `Graphics Windows`.

## Parameters

**`Object`** (input_object)  object(-array) `→` object

Image objects to be displayed.

## Example (HDevelop)

```
read_image (Image, 'fabrik')
regiongrowing (Image, Regions, 3, 3, 6, 100)
dev_clear_window ()
dev_display (Image)
dev_set_colored (12)
dev_set_draw ('margin')
dev_display (Regions)
```

## Result

If the values of the specified parameters are correct,
`dev_display` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Alternatives

`disp_obj`,
`disp_image`,
`disp_region`,
`disp_xld`

## See also

`dev_set_color`,
`dev_set_colored`,
`dev_set_draw`,
`dev_set_line_width`

## Module

Foundation
