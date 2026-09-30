# read_gray_se (Operator)

## Name

`read_gray_se` — Load a structuring element for gray morphology.

## Signature

`read_gray_se( : SE : FileName : )`

## Description

`read_gray_se` loads a structuring element for gray morphology
from a file. The file names of these structuring elements must end
in '.gse' (for gray-scale structuring element). This suffix is
automatically appended by `read_gray_se` to the passed file
name, and thus must not be passed. The structuring element's data
must be contained in the file in the following format: The first
line specifies the data type of the structuring element as `byte`,
`uint2` or `real` (without enclosing quotes). It must match the
image type of the image to be processed in subsequent operator calls
using this structuring element. The following two numbers in the
file determine the width and height of the structuring element and
determine a rectangle enclosing the structuring element. Both
values must be greater than 0. Then the number of chords of the
region to be defined follows. Then the chords themselves follow:
Each chord is defined by the row of the chord (L), the column begin
(CB) and the column end (CE), separated by a space between
them. Then values follow that are regarded as the corresponding
values for gray morphology (their number depends on the defined
width and height of the structuring element). Values that will not
be part of the region of the structuring element (because no chord
is defined for this points) must not be omitted. Nevertheless they
will be ignored in the resulting structuring element. Structuring
elements are stored internally as images with the data type
specified above. Normal images can also be used as structuring
elements, where the region of the image defines the shape of the
structuring element. However, take care not to use too large images,
since the runtime is proportional to the area of the image
multiplied by the area of the structuring element. Flat structuring
elements (i.e. elements with constant gray values) will be executed
particularly fast though. The origin of the structuring element lies
at half of the defined width and height. For even dimensions the
origin will be rounded towards the upper left corner. The
structuring element can be saved as image with the help of the
operator [`write_image`](write_image.md). However, take care to use an image
format that supports alpha channels to save the shape of the
structuring element such as 'tiff', 'jp2' or 'png'. These files can
then be loaded again with the operator [`read_image`](read_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SE`** (output_object)  image `→` object (byte / uint2 / real)

Generated structuring element.

**`FileName`** (input_control)  filename.read `→`  (string)

Name of the file containing the structuring element.

File extension:
.`gse`

## Example (HDevelop)

```
* Load a byte structuring element of width 3 and height 3 that
* consists of 3 chords at lines 0 (from x=1 to x=1), 1 (from x=0
* to x=2) and 2 (from x=1 to x=1). The (used) grayvalues are
* 0, 0, 1, 0, 0 .
* contents of file 'isod4.gse':
* byte
*  3 3
*
* 3
* 0 1 1
* 1 0 2
* 2 1 1
*
*  -1  0 -1
*   0  1  0
*  -1  0 -1
read_gray_se (SE, environment('HALCONROOT')+'/filter/isod4')
```

## Result

`read_gray_se` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
Otherwise, an exception is raised.

## Possible Successors

`gray_erosion`,
`gray_dilation`,
`gray_opening`,
`gray_closing`,
`gray_tophat`,
`gray_bothat`,
`write_image`

## Alternatives

`gen_disc_se`,
`read_image`,
`change_domain`

## See also

`paint_region`,
`paint_gray`,
`crop_part`

## Module

Foundation
