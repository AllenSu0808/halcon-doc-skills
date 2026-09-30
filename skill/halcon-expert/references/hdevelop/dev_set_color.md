# dev_set_color (Operator)

## Name

`dev_set_color` — Set one or more output colors.

## Signature

`dev_set_color( : : ColorName : )`

## Description

`dev_set_color` defines the color(s) that are used to display regions,
XLDs, and other geometrical objects in the graphics windows. The available
colors can be queried with the operator [`query_color`](query_color.md). In
addition, the *`ColorName`* may be specified as hexadecimal RGB triplet
or RGBA quadruplet in the form *'#rrggbb'* and *'#rrggbbaa'*.
'rr', 'gg', 'bb', and 'aa' are hexadecimal numbers
between '00' and 'ff', respectively. 'aa' denotes the alpha value of a
color and can be used to display transparent regions.

For more information see the description of the operator [`set_color`](set_color.md).
However, in contrast to that operator the color setting is also used for
all new graphics windows that are opened afterwards.

These color settings remain valid until `dev_set_color` or
[`dev_set_colored`](dev_set_colored.md) is called or until the color settings are modified
interactively.

![figure](../assets/48cd03cb301baa25.svg)

Examples of possible color strings

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

**`ColorName`** (input_control)  string(-array) `→`  (string)

Output color names.

Default:
'white'

Suggested values:
'white', 'black', 'gray', 'red', 'green', 'blue', '#003075', '#e53019', '#ffb529'

## Example (HDevelop)

```
read_image(Image,'mreut')
dev_set_draw('fill')
dev_set_color('red')
threshold(Image,Region,180,255)
dev_set_color('green')
threshold(Image,Region,0,179)
```

## Result

If the values of the specified parameters are correct,
`dev_set_color` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Predecessors

`dev_open_window`,
`query_color`,
`query_all_colors`

## Possible Successors

`dev_display`

## Alternatives

`dev_set_colored`

## See also

`dev_set_draw`,
`dev_set_line_width`,
`set_color`

## Module

Foundation
