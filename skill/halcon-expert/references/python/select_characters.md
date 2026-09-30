# select_characters (Operator)

## Name

`select_characters` — Selects characters from a given region.

## Signature

`def select_characters(region: HObject, dot_print: str, stroke_width: str, char_width: Sequence[int], char_height: Sequence[int], punctuation: str, diacritic_marks: str, partition_method: str, partition_lines: str, fragment_distance: str, connect_fragments: str, clutter_size_max: int, stop_after: str) -> HObject`

## Description

`select_characters` selects from a given *`region`* the
areas which might be characters and returns them in
*`region_characters`*. This is done by using features like
*`stroke_width`*, *`dot_print`*, the size of the characters and
some more. The given *`region`* should be united, else every
*`region`* is processed separately. Thus do not call
[`connection`](connection.md) before calling `select_characters`, because
then fragments or dots would not be connected to a character.
If you have more than one region with text, you can of course handle
them without merging them.
The *`region`* for `select_characters` typically comes
from [`segment_characters`](segment_characters.md) but also any other segmentation operators
can be used.

The process of the selection can be partitioned into four parts.
All steps are influenced by the parameters *`stroke_width`*,
*`char_height`*, and *`char_width`*.
If you loose small objects like dots, adapt the minimum *`char_width`*
and the minimum *`char_height`*.
But some parameters affect the result of a certain step in particular.
A closer description follows below.
With the parameter *`stop_after`* you can terminate after a specified
step.

In the first step, *"step1_select_candidates"*,
*`char_width`* and the *`char_height`* are used to select the
candidates. The result of this step is also affected by
*`clutter_size_max`*.

In the next step, *"step2_partition_characters"*, the parameter
*`partition_method`* and the parameter *`partition_lines`* influence
the result.

Step three, *"step3_connect_fragments"*, uses the parameters
*`connect_fragments`* and *`dot_print`*. If dot-printed characters
have to be detected and some dots are not connected to the character, there
are two ways to overcome this problem:
You can increase the *`fragment_distance`* and/or decrease the
*`stroke_width`*.

In the last step, *"step4_select_characters"*, the result is affected
by the parameters *`diacritic_marks`* and *`punctuation`*.

*`dot_print`*:
Should be set to *"true"* if dot prints should be read, else to
*"false"*.

*`stroke_width`*:
Specifies the stroke width of the text. It is used to calculate internally
used mask sizes to determine the characters. This mask sizes are also
influenced through the parameters *`dot_print`*, the average
*`char_width`*, and the average *`char_height`*.

*`char_width`*:
This can be a tuple with up to three values. The first value is the
average width of a character. The second is the minimum width of a
character and the third is the maximum width of a character.
If the minimum is not set or equal -1, the operator automatically sets
these value depending on average *`char_width`*. The same is the
case if the maximum is not set. Some examples:

[10] sets the average character width to 10, the minimum and
maximum are calculated by the operator.

[10,-1,20] sets the average character width to 10, the minimum value is
calculated by the system, and the maximum is set to 20.

[10,5,20] sets the average character width to 10, the minimum to 5,
and the maximum to 20.

*`char_height`*:
This can be a tuple with up to three values. The first value is the
average height of a character. The second is the minimum height of a
character and the third is the maximum height of a character.
If the minimum is not set or equal -1, the operator automatically sets
these value depending on average *`char_height`*. The same is the
case if the maximum is not set. Some examples:

[10] sets the average character height to 10, the minimum and
maximum are calculated by the operator.

[10,-1,20] sets the average character height to 10 the minimum value is
calculated by the system and the maximum is set to 20.

[10,5,20] this sets the average character height to 10, the minimum to 5
and the maximum to 20.

*`punctuation`*:
Set this parameter to *"true"* if the operator also has to detect
punctuation marks (e.g., .,:'`"), otherwise they will be suppressed.

*`diacritic_marks`*:
Set this parameter to *"true"* if the text in your application
contains diacritic marks (e.g., â,é,ö), or to *"false"* to suppress
them.

*`partition_method`*:
If neighboring characters are printed close to each other, they may be
partly merged. With this parameter you can specify the method to partition
such characters. The possible values are *"none"*, which means no
partitioning is performed. *"fixed_width"* means that the partitioning
assumes a constant character width. If the width of the extracted region is
well above the average *`char_width`*, the region is split into parts
that have the given average *`char_width`*. The partitioning starts at
the left border of the region.
*"variable_width"* means that the characters are partitioned at the
position where they have the thinnest connection. This method can be selected
for characters that are printed with a variable-width font or if many
consecutive characters are extracted as one symbol.
It could be helpful to call [`text_line_slant`](text_line_slant.md) and/or use
[`text_line_orientation`](text_line_orientation.md) before calling `select_characters`.

*`partition_lines`*:
If some text lines or some characters of different text lines are connected,
set this parameter to *"true"*.

*`fragment_distance`*:
This parameter influences the connection of character fragments. If too
much is connected, set the parameter to *"narrow"* or
*"medium"*. In the case that more fragments should be connected,
set the parameter to *"medium"* or *"wide"*.
The connection is also influenced by the maximum of *`char_width`* and
*`char_height`*. See also *`connect_fragments`*.

*`connect_fragments`*:
Set this parameter to *"true"* if the extracted symbols are
fragmented, i.e., if a symbol is not extracted as one region but broken
up into several parts. See also *`fragment_distance`* and
*`stop_after`* in the step *"step3_connect_fragments"*.

*`clutter_size_max`*:
If the extracted characters contain clutter, i.e., small regions near the
actual symbols, increase this value. If parts of the symbols are missing,
decrease this value.

*`stop_after`*:
Use this parameter in the case the operator does not produce the
desired results. By modifying this value the operator stops after the
execution of the selected step and provides the corresponding results.
To end on completion, set *`stop_after`* to *"completion"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Region of text lines in which to select the characters.

**`region_characters`** (output_object)  region(-array) `→` HObject

Selected characters.

**`dot_print`** (input_control)  string `→` str

Should dot print characters be detected?

Default:
"false"

List of values:
"false", "true"

**`stroke_width`** (input_control)  string `→` str

Stroke width of a character.

Default:
"medium"

List of values:
"bold", "light", "medium", "ultra_light"

**`char_width`** (input_control)  integer-array `→` Sequence[int]

Width of a character.

Default:
25

Value range:
`1
≤
char_width`

**`char_height`** (input_control)  integer-array `→` Sequence[int]

Height of a character.

Default:
25

Value range:
`1
≤
char_height`

**`punctuation`** (input_control)  string `→` str

Add punctuation?

Default:
"false"

List of values:
"false", "true"

**`diacritic_marks`** (input_control)  string `→` str

Exist diacritic marks?

Default:
"false"

List of values:
"false", "true"

**`partition_method`** (input_control)  string `→` str

Method to partition neighbored characters.

Default:
"none"

List of values:
"fixed_width", "none", "variable_width"

**`partition_lines`** (input_control)  string `→` str

Should lines be partitioned?

Default:
"false"

List of values:
"false", "true"

**`fragment_distance`** (input_control)  string `→` str

Distance of fragments.

Default:
"medium"

List of values:
"medium", "narrow", "wide"

**`connect_fragments`** (input_control)  string `→` str

Connect fragments?

Default:
"false"

List of values:
"false", "true"

**`clutter_size_max`** (input_control)  integer `→` int

Maximum size of clutter.

Default:
0

Value range:
`0
≤
clutter_size_max`

**`stop_after`** (input_control)  string `→` str

Stop execution after this step.

Default:
"completion"

List of values:
"completion", "step1_select_candidates", "step2_partition_characters", "step3_connect_fragments", "step4_select_characters"

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
