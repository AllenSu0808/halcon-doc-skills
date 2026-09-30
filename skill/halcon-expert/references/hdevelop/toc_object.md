## Object

List of Sections ↓

This chapter contains operators that can be used to either query
information related to iconic objects or to manipulate iconic objects.

### Available Iconic Objects

HALCON provides different kinds of iconic objects that are suitable for
different needs:

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/87e71164f02ec257.svg) | ![figure](../assets/31f93b102e536dd0.svg) | ![figure](../assets/28b2353fb4bd532c.svg) |
| ( 1) | ( 2) | ( 3) |
| ![figure](../assets/6fe5d3581de986ca.svg) | ![figure](../assets/d50f764af2c10b2a.svg) | ![figure](../assets/945b1c2485acdee5.svg) |
| ( 4) | ( 5) | ( 6) |

Within the image of a metal part (1) a region (2), an ROI
that is created using the dilated boundary of the region (3),
contours (4), polygons (5), and parallels (6) are extracted.

- **Images:** —

  An image consists of one to multiple channels, i.e., matrices
  of similar size that contain gray values of various pixel types. Images are
  the major source for most machine vision tasks.
- **Regions:** —

  A region is defined as a set of pixels. The pixels of a region
  do not need to be connected. This means that even an arbitrary collection of
  pixels can be handled as a single region. Region processing is suitable, e.g.,
  to apply a blob analysis within images or to define a region of interest (ROI)
  for following subpixel-precise operations.
- **XLDs:** —

  XLD is the abbreviation for eXtended Line Description and
  comprises all contour and polygon based data. Note that XLD contours are
  returned or used by many HALCON operators whereas XLD polygons and XLD
  parallels are needed only in special cases. A contour is a sequence of
  subpixel-accurate 2D control points that are connected by lines. Typically,
  the distance between control points is about one pixel. XLD objects contain,
  besides the control points, so-called local and global attributes. Typical
  examples for these are, e.g., the edge amplitude of a control point or the
  regression parameters of a contour segment. Contour processing is suitable,
  e.g., for subpixel-precise measurements. Subpixel-precise operations can be
  faster if they are applied within an ROI.

### Further Information

See the `“Quick Guide”` for further details about the
available data structures.

---

#### List of Sections

- [Information](toc_object_information.md)
- [Manipulation](toc_object_manipulation.md)
