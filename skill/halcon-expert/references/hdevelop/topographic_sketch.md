# topographic_sketch (Operator)

## Name

`topographic_sketch` — Compute the topographic primal sketch of an image.

## Signature

`topographic_sketch(Image : Sketch : : )`

## Description

`topographic_sketch` computes the topographic primal
sketch of the input image *`Image`*. This is done by
approximating the image locally by a bicubic polynomial (“facet
model”). It serves to calculate the first and second partial
derivatives of the image, and thus to classify the image into 11
classes. These classes are coded in the output image
*`Sketch`* as numbers from 1 to 11. The classes are as
follows:

|  |  |
| --- | --- |
| Peak | 1 |
| Pit | 2 |
| Ridge | 3 |
| Ravine | 4 |
| Saddle | 5 |
| Flat | 6 |
| Hillside Slope | 7 |
| Hillside Convex | 8 |
| Hillside Concave | 9 |
| Hillside Saddle | 10 |
| Hillside Inflection | 11 |

In order to obtain the separate classes as regions, a threshold
operation has to be applied to the result image with the appropriate
thresholds.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte)

Image for which the topographic primal sketch
is to be computed.

**`Sketch`** (output_object)  (multichannel-)image(-array) `→` object (byte)

Label image containing the 11 classes.

## Example (HDevelop)

```
* To extract the Ridges from a Image
read_image(Image,'sinus')
topographic_sketch(Image,Sketch)
threshold(Sketch,Ridges,3,3)
```

## Complexity

Let n be the number of pixels in the image. Then O(n)
operations are performed.

## Result

`topographic_sketch` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Successors

`threshold`

## References

R. Haralick, L. Shapiro: “Computer and Robot Vision, Volume I”;
Reading, Massachusetts, Addison-Wesley; 1992; Kapitel 8.13.

## Module

Foundation
