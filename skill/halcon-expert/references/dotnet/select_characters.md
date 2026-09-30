# SelectCharacters (Operator)

## Name

`SelectCharacters` — Selects characters from a given region.

## Signature

`static void HOperatorSet.SelectCharacters(HObject region, out HObject regionCharacters, HTuple dotPrint, HTuple strokeWidth, HTuple charWidth, HTuple charHeight, HTuple punctuation, HTuple diacriticMarks, HTuple partitionMethod, HTuple partitionLines, HTuple fragmentDistance, HTuple connectFragments, HTuple clutterSizeMax, HTuple stopAfter)`

`HRegion HRegion.SelectCharacters(string dotPrint, string strokeWidth, HTuple charWidth, HTuple charHeight, string punctuation, string diacriticMarks, string partitionMethod, string partitionLines, string fragmentDistance, string connectFragments, int clutterSizeMax, string stopAfter)`

## Description

`SelectCharacters` selects from a given *`region`* the
areas which might be characters and returns them in
*`regionCharacters`*. This is done by using features like
*`strokeWidth`*, *`dotPrint`*, the size of the characters and
some more. The given *`region`* should be united, else every
*`region`* is processed separately. Thus do not call
[`Connection`](connection.md) before calling `SelectCharacters`, because
then fragments or dots would not be connected to a character.
If you have more than one region with text, you can of course handle
them without merging them.
The *`region`* for `SelectCharacters` typically comes
from [`SegmentCharacters`](segment_characters.md) but also any other segmentation operators
can be used.

The process of the selection can be partitioned into four parts.
All steps are influenced by the parameters *`strokeWidth`*,
*`charHeight`*, and *`charWidth`*.
If you loose small objects like dots, adapt the minimum *`charWidth`*
and the minimum *`charHeight`*.
But some parameters affect the result of a certain step in particular.
A closer description follows below.
With the parameter *`stopAfter`* you can terminate after a specified
step.

In the first step, *"step1_select_candidates"*,
*`charWidth`* and the *`charHeight`* are used to select the
candidates. The result of this step is also affected by
*`clutterSizeMax`*.

In the next step, *"step2_partition_characters"*, the parameter
*`partitionMethod`* and the parameter *`partitionLines`* influence
the result.

Step three, *"step3_connect_fragments"*, uses the parameters
*`connectFragments`* and *`dotPrint`*. If dot-printed characters
have to be detected and some dots are not connected to the character, there
are two ways to overcome this problem:
You can increase the *`fragmentDistance`* and/or decrease the
*`strokeWidth`*.

In the last step, *"step4_select_characters"*, the result is affected
by the parameters *`diacriticMarks`* and *`punctuation`*.

*`dotPrint`*:
Should be set to *"true"* if dot prints should be read, else to
*"false"*.

*`strokeWidth`*:
Specifies the stroke width of the text. It is used to calculate internally
used mask sizes to determine the characters. This mask sizes are also
influenced through the parameters *`dotPrint`*, the average
*`charWidth`*, and the average *`charHeight`*.

*`charWidth`*:
This can be a tuple with up to three values. The first value is the
average width of a character. The second is the minimum width of a
character and the third is the maximum width of a character.
If the minimum is not set or equal -1, the operator automatically sets
these value depending on average *`charWidth`*. The same is the
case if the maximum is not set. Some examples:

[10] sets the average character width to 10, the minimum and
maximum are calculated by the operator.

[10,-1,20] sets the average character width to 10, the minimum value is
calculated by the system, and the maximum is set to 20.

[10,5,20] sets the average character width to 10, the minimum to 5,
and the maximum to 20.

*`charHeight`*:
This can be a tuple with up to three values. The first value is the
average height of a character. The second is the minimum height of a
character and the third is the maximum height of a character.
If the minimum is not set or equal -1, the operator automatically sets
these value depending on average *`charHeight`*. The same is the
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

*`diacriticMarks`*:
Set this parameter to *"true"* if the text in your application
contains diacritic marks (e.g., â,é,ö), or to *"false"* to suppress
them.

*`partitionMethod`*:
If neighboring characters are printed close to each other, they may be
partly merged. With this parameter you can specify the method to partition
such characters. The possible values are *"none"*, which means no
partitioning is performed. *"fixed_width"* means that the partitioning
assumes a constant character width. If the width of the extracted region is
well above the average *`charWidth`*, the region is split into parts
that have the given average *`charWidth`*. The partitioning starts at
the left border of the region.
*"variable_width"* means that the characters are partitioned at the
position where they have the thinnest connection. This method can be selected
for characters that are printed with a variable-width font or if many
consecutive characters are extracted as one symbol.
It could be helpful to call [`TextLineSlant`](text_line_slant.md) and/or use
[`TextLineOrientation`](text_line_orientation.md) before calling `SelectCharacters`.

*`partitionLines`*:
If some text lines or some characters of different text lines are connected,
set this parameter to *"true"*.

*`fragmentDistance`*:
This parameter influences the connection of character fragments. If too
much is connected, set the parameter to *"narrow"* or
*"medium"*. In the case that more fragments should be connected,
set the parameter to *"medium"* or *"wide"*.
The connection is also influenced by the maximum of *`charWidth`* and
*`charHeight`*. See also *`connectFragments`*.

*`connectFragments`*:
Set this parameter to *"true"* if the extracted symbols are
fragmented, i.e., if a symbol is not extracted as one region but broken
up into several parts. See also *`fragmentDistance`* and
*`stopAfter`* in the step *"step3_connect_fragments"*.

*`clutterSizeMax`*:
If the extracted characters contain clutter, i.e., small regions near the
actual symbols, increase this value. If parts of the symbols are missing,
decrease this value.

*`stopAfter`*:
Use this parameter in the case the operator does not produce the
desired results. By modifying this value the operator stops after the
execution of the selected step and provides the corresponding results.
To end on completion, set *`stopAfter`* to *"completion"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region of text lines in which to select the characters.

**`regionCharacters`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Selected characters.

**`dotPrint`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Should dot print characters be detected?

Default:
"false"

List of values:
"false", "true"

**`strokeWidth`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Stroke width of a character.

Default:
"medium"

List of values:
"bold", "light", "medium", "ultra_light"

**`charWidth`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Width of a character.

Default:
25

Value range:
`1
≤
charWidth`

**`charHeight`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Height of a character.

Default:
25

Value range:
`1
≤
charHeight`

**`punctuation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Add punctuation?

Default:
"false"

List of values:
"false", "true"

**`diacriticMarks`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Exist diacritic marks?

Default:
"false"

List of values:
"false", "true"

**`partitionMethod`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method to partition neighbored characters.

Default:
"none"

List of values:
"fixed_width", "none", "variable_width"

**`partitionLines`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Should lines be partitioned?

Default:
"false"

List of values:
"false", "true"

**`fragmentDistance`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Distance of fragments.

Default:
"medium"

List of values:
"medium", "narrow", "wide"

**`connectFragments`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Connect fragments?

Default:
"false"

List of values:
"false", "true"

**`clutterSizeMax`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum size of clutter.

Default:
0

Value range:
`0
≤
clutterSizeMax`

**`stopAfter`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

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
`SelectCharacters` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`SegmentCharacters`,
`TextLineSlant`

## Possible Successors

`DoOcrSingleClassMlp`,
`DoOcrMultiClassMlp`

## Alternatives

`Connection`

## Module

Foundation
