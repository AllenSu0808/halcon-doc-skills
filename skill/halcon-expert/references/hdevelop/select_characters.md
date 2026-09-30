# select_characters (Operator)

## Name

`select_characters` — Selects characters from a given region.

## Signature

`select_characters(Region : RegionCharacters : DotPrint, StrokeWidth, CharWidth, CharHeight, Punctuation, DiacriticMarks, PartitionMethod, PartitionLines, FragmentDistance, ConnectFragments, ClutterSizeMax, StopAfter : )`

## Description

`select_characters` selects from a given *`Region`* the
areas which might be characters and returns them in
*`RegionCharacters`*. This is done by using features like
*`StrokeWidth`*, *`DotPrint`*, the size of the characters and
some more. The given *`Region`* should be united, else every
*`Region`* is processed separately. Thus do not call
[`connection`](connection.md) before calling `select_characters`, because
then fragments or dots would not be connected to a character.
If you have more than one region with text, you can of course handle
them without merging them.
The *`Region`* for `select_characters` typically comes
from [`segment_characters`](segment_characters.md) but also any other segmentation operators
can be used.

The process of the selection can be partitioned into four parts.
All steps are influenced by the parameters *`StrokeWidth`*,
*`CharHeight`*, and *`CharWidth`*.
If you loose small objects like dots, adapt the minimum *`CharWidth`*
and the minimum *`CharHeight`*.
But some parameters affect the result of a certain step in particular.
A closer description follows below.
With the parameter *`StopAfter`* you can terminate after a specified
step.

In the first step, *'step1_select_candidates'*,
*`CharWidth`* and the *`CharHeight`* are used to select the
candidates. The result of this step is also affected by
*`ClutterSizeMax`*.

In the next step, *'step2_partition_characters'*, the parameter
*`PartitionMethod`* and the parameter *`PartitionLines`* influence
the result.

Step three, *'step3_connect_fragments'*, uses the parameters
*`ConnectFragments`* and *`DotPrint`*. If dot-printed characters
have to be detected and some dots are not connected to the character, there
are two ways to overcome this problem:
You can increase the *`FragmentDistance`* and/or decrease the
*`StrokeWidth`*.

In the last step, *'step4_select_characters'*, the result is affected
by the parameters *`DiacriticMarks`* and *`Punctuation`*.

*`DotPrint`*:
Should be set to *'true'* if dot prints should be read, else to
*'false'*.

*`StrokeWidth`*:
Specifies the stroke width of the text. It is used to calculate internally
used mask sizes to determine the characters. This mask sizes are also
influenced through the parameters *`DotPrint`*, the average
*`CharWidth`*, and the average *`CharHeight`*.

*`CharWidth`*:
This can be a tuple with up to three values. The first value is the
average width of a character. The second is the minimum width of a
character and the third is the maximum width of a character.
If the minimum is not set or equal -1, the operator automatically sets
these value depending on average *`CharWidth`*. The same is the
case if the maximum is not set. Some examples:

[10] sets the average character width to 10, the minimum and
maximum are calculated by the operator.

[10,-1,20] sets the average character width to 10, the minimum value is
calculated by the system, and the maximum is set to 20.

[10,5,20] sets the average character width to 10, the minimum to 5,
and the maximum to 20.

*`CharHeight`*:
This can be a tuple with up to three values. The first value is the
average height of a character. The second is the minimum height of a
character and the third is the maximum height of a character.
If the minimum is not set or equal -1, the operator automatically sets
these value depending on average *`CharHeight`*. The same is the
case if the maximum is not set. Some examples:

[10] sets the average character height to 10, the minimum and
maximum are calculated by the operator.

[10,-1,20] sets the average character height to 10 the minimum value is
calculated by the system and the maximum is set to 20.

[10,5,20] this sets the average character height to 10, the minimum to 5
and the maximum to 20.

*`Punctuation`*:
Set this parameter to *'true'* if the operator also has to detect
punctuation marks (e.g., .,:'`"), otherwise they will be suppressed.

*`DiacriticMarks`*:
Set this parameter to *'true'* if the text in your application
contains diacritic marks (e.g., â,é,ö), or to *'false'* to suppress
them.

*`PartitionMethod`*:
If neighboring characters are printed close to each other, they may be
partly merged. With this parameter you can specify the method to partition
such characters. The possible values are *'none'*, which means no
partitioning is performed. *'fixed_width'* means that the partitioning
assumes a constant character width. If the width of the extracted region is
well above the average *`CharWidth`*, the region is split into parts
that have the given average *`CharWidth`*. The partitioning starts at
the left border of the region.
*'variable_width'* means that the characters are partitioned at the
position where they have the thinnest connection. This method can be selected
for characters that are printed with a variable-width font or if many
consecutive characters are extracted as one symbol.
It could be helpful to call [`text_line_slant`](text_line_slant.md) and/or use
[`text_line_orientation`](text_line_orientation.md) before calling `select_characters`.

*`PartitionLines`*:
If some text lines or some characters of different text lines are connected,
set this parameter to *'true'*.

*`FragmentDistance`*:
This parameter influences the connection of character fragments. If too
much is connected, set the parameter to *'narrow'* or
*'medium'*. In the case that more fragments should be connected,
set the parameter to *'medium'* or *'wide'*.
The connection is also influenced by the maximum of *`CharWidth`* and
*`CharHeight`*. See also *`ConnectFragments`*.

*`ConnectFragments`*:
Set this parameter to *'true'* if the extracted symbols are
fragmented, i.e., if a symbol is not extracted as one region but broken
up into several parts. See also *`FragmentDistance`* and
*`StopAfter`* in the step *'step3_connect_fragments'*.

*`ClutterSizeMax`*:
If the extracted characters contain clutter, i.e., small regions near the
actual symbols, increase this value. If parts of the symbols are missing,
decrease this value.

*`StopAfter`*:
Use this parameter in the case the operator does not produce the
desired results. By modifying this value the operator stops after the
execution of the selected step and provides the corresponding results.
To end on completion, set *`StopAfter`* to *'completion'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Region of text lines in which to select the characters.

**`RegionCharacters`** (output_object)  region(-array) `→` object

Selected characters.

**`DotPrint`** (input_control)  string `→`  (string)

Should dot print characters be detected?

Default:
'false'

List of values:
'false', 'true'

**`StrokeWidth`** (input_control)  string `→`  (string)

Stroke width of a character.

Default:
'medium'

List of values:
'bold', 'light', 'medium', 'ultra_light'

**`CharWidth`** (input_control)  integer-array `→`  (integer)

Width of a character.

Default:
25

Value range:
`1
≤
CharWidth`

**`CharHeight`** (input_control)  integer-array `→`  (integer)

Height of a character.

Default:
25

Value range:
`1
≤
CharHeight`

**`Punctuation`** (input_control)  string `→`  (string)

Add punctuation?

Default:
'false'

List of values:
'false', 'true'

**`DiacriticMarks`** (input_control)  string `→`  (string)

Exist diacritic marks?

Default:
'false'

List of values:
'false', 'true'

**`PartitionMethod`** (input_control)  string `→`  (string)

Method to partition neighbored characters.

Default:
'none'

List of values:
'fixed_width', 'none', 'variable_width'

**`PartitionLines`** (input_control)  string `→`  (string)

Should lines be partitioned?

Default:
'false'

List of values:
'false', 'true'

**`FragmentDistance`** (input_control)  string `→`  (string)

Distance of fragments.

Default:
'medium'

List of values:
'medium', 'narrow', 'wide'

**`ConnectFragments`** (input_control)  string `→`  (string)

Connect fragments?

Default:
'false'

List of values:
'false', 'true'

**`ClutterSizeMax`** (input_control)  integer `→`  (integer)

Maximum size of clutter.

Default:
0

Value range:
`0
≤
ClutterSizeMax`

**`StopAfter`** (input_control)  string `→`  (string)

Stop execution after this step.

Default:
'completion'

List of values:
'completion', 'step1_select_candidates', 'step2_partition_characters', 'step3_connect_fragments', 'step4_select_characters'

## Example (HDevelop)

```
for Index := 1 to 5 by 1
  read_image (Image, 'dot_print_rotated/dot_print_rotated_'+Index$'02d')
  text_line_orientation (Image, Image, 50, rad(-30), rad(30), \
                         OrientationAngle)
  rotate_image (Image, ImageRotate, deg(-OrientationAngle), 'constant')
  segment_characters (ImageRotate, ImageRotate, ImageForeground, \
                      RegionForeground, 'local_auto_shape', 'false', \
                      'false', 'medium', 25, 25, 0, 10, UsedThreshold)
  select_characters (RegionForeground, RegionCharacters, 'true', \
                     'ultra_light', [60,1,100], [60,1,100], 'false', \
                     'false', 'none', 'true', 'wide', 'true', 0, 'completion')
endfor
```

## Result

If the input parameters are set correctly, the operator
`select_characters` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`segment_characters`,
`text_line_slant`

## Possible Successors

`do_ocr_single_class_mlp`,
`do_ocr_multi_class_mlp`

## Alternatives

`connection`

## Module

Foundation
