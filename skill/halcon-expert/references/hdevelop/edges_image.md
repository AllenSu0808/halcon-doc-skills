# edges_image (Operator)

## Name

`edges_image` — Extract edges using Deriche, Lanser, Shen, or Canny filters.

## Signature

`edges_image(Image : ImaAmp, ImaDir : Filter, Alpha, NMS, Low, High : )`

## Description

`edges_image` detects step edges using recursively implemented
filters (according to Deriche, Lanser and Shen) or the
conventionally implemented “derivative of Gaussian” filter (using
filter masks) proposed by Canny. Furthermore, a very fast variant
of the Sobel filter can be used. Thus, the following edge operators
are available:

*'deriche1'*, *'lanser1'*, *'deriche1_int4'*,
*'deriche2'*, *'lanser2'*, *'deriche2_int4'*,
*'shen'*, *'mshen'*, *'canny'*,
and *'sobel_fast'*

(parameter *`Filter`*).

The edge amplitudes (gradient magnitude) are returned in
*`ImaAmp`*.

For all filters except *'sobel_fast'*, the edge directions
are returned in *`ImaDir`*. For *'sobel_fast'*, the
edge direction is not computed to speed up the filter.
Consequently, *`ImaDir`* is an empty image object.
The edge operators *'deriche1'* respectively *'deriche2'* are
also available for int4-images, and return the signed filter response instead
of its absolute value. This behavior can be obtained for byte-images as
well by selecting *'deriche1_int4'* respectively
*'deriche2_int4'* as filter.
This can be used to calculate the second derivative of an image by
applying `edges_image` (with parameter value *'lanser2'*) to the
signed first derivative. Edge directions are stored in 2-degree
steps, i.e., an edge direction of $x$ degrees in mathematically
positive sense and with respect to
the horizontal axis is stored as $x/2$ in the edge
direction image. Furthermore, the direction of the change of
intensity is taken into account. Let $[E_{x},E_{y}]$
denote the image gradient. Then the following edge directions are
returned as $r/2$:
$$\mathrm{E}_{x}/\mathrm{E}_{y}$$ ![figure](../assets/b6369c3c39fd2405.svg)
Points with edge amplitude 0 are assigned the edge direction 255
(undefined direction).

The “filter width” (i.e., the amount of smoothing) can be chosen
arbitrarily for all filters except *'sobel_fast'* (where the
filter width is 3x3 and *`Alpha`* is
ignored), and can be estimated by calling [`info_edges`](info_edges.md) for
concrete values of the parameter *`Alpha`*. It decreases for
increasing *`Alpha`* for the Deriche, Lanser and Shen filters
and increases for the Canny filter, where it is the standard
deviation of the Gaussian on which the Canny operator is based.
“Wide” filters exhibit a larger invariance to noise, but also a
decreased ability to detect small details. Non-recursive filters,
such as the Canny filter, are realized using filter masks, and thus
the execution time increases for increasing filter width. In
contrast, the execution time for recursive filters does not depend
on the filter width. Thus, arbitrary filter widths are possible
using the Deriche, Lanser and Shen filters without increasing the
run time of the operator. The resulting advantage in speed compared
to the Canny operator naturally increases for larger filter widths.
As border treatment, the recursive operators assume that the images
to be zero outside of the image, while the Canny operator repeats
the gray value at the image's border. The signal-noise-ratio of the
filters is comparable for the following choices of *`Alpha`*:
Alpha('lanser1') = Alpha('deriche1'),
Alpha('deriche2') = Alpha('deriche1') / 2,
Alpha('lanser2') = Alpha('deriche2'),
Alpha('shen') = Alpha('deriche1') / 2,
Alpha('mshen') = Alpha('shen'),
Alpha('canny') = 1.77 / Alpha('deriche1').
The originally proposed recursive filters
(*'deriche1'*, *'deriche2'*, *'shen'*) return a biased
estimate of the amplitude of diagonal edges.
This bias is removed in the corresponding modified version
of the operators
(*'lanser1'*, *'lanser2'* and *'mshen'*),
while maintaining the same execution speed.

For relatively small filter widths (11 x 11),
i.e., for
*`Alpha`*('lanser2') = *0.5*,
all filters yield similar results.
Only for “wider” filters differences begin to appear:
the Shen filters begin to yield qualitatively inferior results.
However, they are the fastest of the implemented operators ---
closely followed by the Deriche operators.

`edges_image` optionally offers to apply a
non-maximum-suppression
(*`NMS`* = *'nms'*/*'inms'*/*'hvnms'*;
*'none'*
if not desired) and hysteresis threshold operation
(*`Low`*,*`High`*; at least one negative if not
desired) to the resulting edge image.
Conceptually, this corresponds to the following calls:

|  |
| --- |
| `nonmax_suppression_dir(...,NMS,...)` |
| `hysteresis_threshold(...,Low,High,999,...)`. |

Note that the hysteresis threshold operation is not applied
if *`NMS`* is set to *'none'*.

For *'sobel_fast'*, the same non-maximum-suppression is
performed for all values of *`NMS`* except *'none'*.
Additionally, for *'sobel_fast'* the resulting edges are
thinned to a width of one pixel.

`edges_image` can be executed on OpenCL devices for the filter
types *'canny'* and *'sobel_fast'*.

## Attention

The OpenCL implementation of `edges_image` will generally compute
results that differ somewhat from the CPU implementation.

Since `edges_image` uses Gauss convolution internally for the
*'canny'* filter, the same limitations for OpenCL apply as for
[`derivate_gauss`](derivate_gauss.md): *`Alpha`* must be chosen small enough that
the required filter mask is less than 129 pixels in size.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2 / int4 / real)

Input image.

**`ImaAmp`** (output_object)  (multichannel-)image(-array) `→` object (byte / uint2 / int4 / real)

Edge amplitude (gradient magnitude) image.

**`ImaDir`** (output_object)  image(-array) `→` object (direction)

Edge direction image.

**`Filter`** (input_control)  string `→`  (string)

Edge operator to be applied.

Default:
'canny'

List of values:
'canny', 'deriche1', 'deriche1_int4', 'deriche2', 'deriche2_int4', 'lanser1', 'lanser2', 'mshen', 'shen', 'sobel_fast'

List of values (for compute devices):
'canny', 'sobel_fast'

**`Alpha`** (input_control)  real `→`  (real)

Filter parameter: small values result in strong
smoothing, and thus less detail (opposite for
'canny').

Default:
1.0

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.1

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Alpha > 0.0`

**`NMS`** (input_control)  string `→`  (string)

Non-maximum suppression ('none', if not desired).

Default:
'nms'

List of values:
'hvnms', 'inms', 'nms', 'none'

**`Low`** (input_control)  integer `→`  (integer / real)

Lower threshold for the hysteresis threshold operation
(negative, if no thresholding is desired).

Default:
20

Suggested values:
5, 10, 15, 20, 25, 30, 40

Minimum increment:
1

Recommended increment:
5

Restriction:
`Low != 0`

**`High`** (input_control)  integer `→`  (integer / real)

Upper threshold for the hysteresis threshold operation
(negative, if no thresholding is desired).

Default:
40

Suggested values:
10, 15, 20, 25, 30, 40, 50, 60, 70

Minimum increment:
1

Recommended increment:
5

Restriction:
`High >= Low`

## Example (HDevelop)

```
read_image(Image,'fabrik')
edges_image(Image,Amp,Dir,'lanser2',0.5,'none',-1,-1)
hysteresis_threshold(Amp,Margin,20,30,30)
```

## Result

`edges_image` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during execution. If the input is empty the
behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Predecessors

`info_edges`

## Possible Successors

`threshold`,
`hysteresis_threshold`,
`close_edges_length`

## Alternatives

`sobel_dir`,
`frei_dir`,
`kirsch_dir`,
`prewitt_dir`,
`robinson_dir`

## See also

`info_edges`,
`nonmax_suppression_amp`,
`hysteresis_threshold`,
`bandpass_image`

## References

S.Lanser, W.Eckstein: “Eine Modifikation des Deriche-Verfahrens zur
Kantendetektion”; 13. DAGM-Symposium, München; Informatik
Fachberichte 290; Seite 151 - 158; Springer-Verlag; 1991.
  
S.Lanser: “Detektion von Stufenkanten mittels rekursiver Filter
nach Deriche”; Diplomarbeit; Technische Universität München,
Institut für Informatik, Lehrstuhl Prof. Radig; 1991.
  
J.Canny: “Finding Edges and Lines in Images”; Report, AI-TR-720;
M.I.T. Artificial Intelligence Lab., Cambridge; 1983.
  
J.Canny: “A Computational Approach to Edge Detection”; IEEE
Transactions on Pattern Analysis and Machine Intelligence; PAMI-8,
vol. 6; S. 679-698; 1986.
  
R.Deriche: “Using Canny's Criteria to Derive a Recursively
Implemented Optimal Edge Detector”; International Journal of
Computer Vision; vol. 1, no. 2; S. 167-187; 1987.
  
R.Deriche: “Optimal Edge Detection Using Recursive Filtering”;
Proc. of the First International Conference on Computer Vision,
London; S. 501-505; 1987.
  
R.Deriche: “Fast Algorithms for Low-Level Vision”; IEEE
Transactions on Pattern Analysis and Machine Intelligence; PAMI-12,
no. 1; S. 78-87; 1990.
  
S.Castan, J.Zhao und J.Shen: “Optimal Filter for Edge Detection
Methods and Results”; Proc. of the First European Conference on
Computer Vision, Antibes; Lecture Notes on computer Science;
no. 427; S. 12-17; Springer-Verlag; 1990.

## Module

Foundation
