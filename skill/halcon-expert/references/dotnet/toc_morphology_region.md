## Region

List of Operators ↓

This chapter describes operators of region morphology.

### Concept of Region Morphology

Region morphology provides a set of morphological operators that allow to
modify or describe the shape of a region.
The morphological operators can be used, for example, to connect or
disconnect adjacent regions or to smooth the boundary of a region.
In the following, we will take a closer look at the morphological
operators.

### Dilation and Erosion

To dilate or erode an input region, a structuring element is applied
to the input region. This structuring element is scanned over the
image line-by-line. During dilation the reference point of the
structuring element is added to the resulting region whenever the
structuring element and the input region have at least one pixel in
common. This results in an enlarged region, as shown in the image
below. Erosion reduces the area of the input region because the
reference point is only added to the resulting region if the structuring
element lies completely within the input region. As a result, erosion can
alternatively be used to find objects.

|  |  |  |  |
| --- | --- | --- | --- |
| ![figure](../assets/10c8338307dbcf2b.svg) | ![figure](../assets/83f72dee859e40bc.svg) | ![figure](../assets/b0046540114d6af0.svg) | ![figure](../assets/3cb6b55241ce8c9b.svg) |
| ( 1) | ( 2) | ( 3) | ( 4) |

(1) Image with input region,
(2) structuring element with reference point in the origin,
(3) result of dilating the input region,
(4) result of eroding the input region.

These operators can be used to dilate or erode a region:

| Morphological Operators |  | Structuring Element | Reference Point |
| --- | --- | --- | --- |
| [`Dilation1`](dilation1.md) | [`Erosion1`](erosion1.md) | arbitrary | origin |
| [`MinkowskiAdd1`](minkowski_add1.md) | [`MinkowskiSub1`](minkowski_sub1.md) | arbitrary, transposed | origin |
| [`Dilation2`](dilation2.md) | [`Erosion2`](erosion2.md) | arbitrary | arbitrary |
| [`MinkowskiAdd2`](minkowski_add2.md) | [`MinkowskiSub2`](minkowski_sub2.md) | arbitrary, transposed | arbitrary |
| [`DilationCircle`](dilation_circle.md) | [`ErosionCircle`](erosion_circle.md) | circular | origin |
| [`DilationRectangle1`](dilation_rectangle1.md) | [`ErosionRectangle1`](erosion_rectangle1.md) | rectangular | origin |

Note that Minkowski addition and dilation are identical if
the structuring element is symmetric. The same applies to Minkowski
subtraction and erosion. Erosion can be used to separate objects
that are attached to each other. In the following, the steps that are
required to separate objects are described briefly.

First, the objects of the image must be segmented, for example by
using the operator [`Threshold`](threshold.md). Next, the operator
[`Connection`](connection.md) is used to get multiple regions instead of a
single region. As you can see in the image (3) below, the result of
the connection is unsatisfactory because several objects are merged.

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/825a780a01007ca9.svg) | ![figure](../assets/cd5b04d0eb4796a7.svg) | ![figure](../assets/04a8fb45487af325.svg) |
| ( 1) | ( 2) | ( 3) |

(1) Image with globular objects,
(2) segmented regions,
(3) connected components.

This problem can be solved using erosion. As mentioned above,
erosion reduces the area of the input region. Thus, if erosion
is applied prior to the operator [`Connection`](connection.md), the regions
are separated as desired. Lastly, dilation is applied on the
separated regions to approximately get the original shape back.

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/ea1f400629d795a0.svg) | ![figure](../assets/21ac7684f2bafa55.svg) | ![figure](../assets/10be2a311d47437c.svg) |
| ( 1) | ( 2) | ( 3) |

(1) Segmented regions after erosion,
(2) connected components,
(3) connected components after dilation.

### Opening and Closing

Both operations generate the resulting region by combining dilation
and erosion operations. Opening is an erosion followed by a dilation.
It is useful to eliminate small unwanted structures.
Closing is the opposite of opening, i.e., a dilation followed by
an erosion. The closing operator is able to close small
gaps, as shown below.

|  |  |  |  |
| --- | --- | --- | --- |
| ![figure](../assets/10c8338307dbcf2b.svg) | ![figure](../assets/83f72dee859e40bc.svg) | ![figure](../assets/0f33b08820fbb448.svg) | ![figure](../assets/968235193f8febdb.svg) |
| ( 1) | ( 2) | ( 3) | ( 4) |

(1) Image with input region,
(2) structuring element with reference point,
(3) result of applying an opening to the input region,
(4) result of applying a closing.

These operators can be used to open or close a region:

| Morphological Operators |  | Structuring Element | Reference Point |
| --- | --- | --- | --- |
| [`Opening`](opening.md) | [`Closing`](closing.md) | arbitrary | origin |
| [`OpeningCircle`](opening_circle.md) | [`ClosingCircle`](closing_circle.md) | circular | origin |
| [`OpeningRectangle1`](opening_rectangle1.md) | [`ClosingRectangle1`](closing_rectangle1.md) | rectangular | origin |

### Further Operators

In addition to the operators mentioned above, you can use
[`TopHat`](top_hat.md) to get the difference between the input region and
the result of the opening, or [`BottomHat`](bottom_hat.md) to get the
difference between the result of the closing and the input region.
Furthermore, you can calculate the boundary of a region
with the operator [`Boundary`](boundary.md).

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/dfe78b35564df33f.svg) | ![figure](../assets/2349fb2405d0e296.svg) | ![figure](../assets/a21814294faf631a.svg) |
| ( 1) | ( 2) | ( 3) |

(1) Top hat,
(2) bottom hat,
(3) boundary.

The operator [`HitOrMiss`](hit_or_miss.md) can be used to find objects, taking
the foreground and the background of the image into account.
To remove unwanted branches from a skeleton, [`Pruning`](pruning.md)
is a suitable operator.

### Glossary

In the following list, the most important terms that are used in the
context of Morphology are described.

- **input region** —

  Region which is modified by morphological
  operators.
- **structuring element** —

  Region which is used to scan the input
  region.

---

#### List of Operators

- [`BottomHat`](bottom_hat.md) — Compute the bottom hat of regions.

- [`Boundary`](boundary.md) — Reduce a region to its boundary.

- [`Closing`](closing.md) — Close a region.

- [`ClosingCircle`](closing_circle.md) — Close a region with a circular structuring element.

- [`ClosingRectangle1`](closing_rectangle1.md) — Close a region with a rectangular structuring element.

- [`Dilation1`](dilation1.md) — Dilate a region.

- [`Dilation2`](dilation2.md) — Dilate a region (using a reference point).

- [`DilationCircle`](dilation_circle.md) — Dilate a region with a circular structuring element.

- [`DilationRectangle1`](dilation_rectangle1.md) — Dilate a region with a rectangular structuring element.

- [`Erosion1`](erosion1.md) — Erode a region.

- [`Erosion2`](erosion2.md) — Erode a region (using a reference point).

- [`ErosionCircle`](erosion_circle.md) — Erode a region with a circular structuring element.

- [`ErosionRectangle1`](erosion_rectangle1.md) — Erode a region with a rectangular structuring element.

- [`HitOrMiss`](hit_or_miss.md) — Hit-or-miss operation for regions.

- [`MinkowskiAdd1`](minkowski_add1.md) — Perform a Minkowski addition on a region.

- [`MinkowskiAdd2`](minkowski_add2.md) — Dilate a region (using a reference point).

- [`MinkowskiSub1`](minkowski_sub1.md) — Erode a region.

- [`MinkowskiSub2`](minkowski_sub2.md) — Erode a region (using a reference point).

- [`Opening`](opening.md) — Open a region.

- [`OpeningCircle`](opening_circle.md) — Open a region with a circular structuring element.

- [`OpeningRectangle1`](opening_rectangle1.md) — Open a region with a rectangular structuring element.

- [`Pruning`](pruning.md) — Prune the branches of a region.

- [`TopHat`](top_hat.md) — Compute the top hat of regions.
