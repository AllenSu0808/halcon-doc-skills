## Drawing

List of Operators ↓

This chapter describes operators that allow the user to manually draw
geometric shapes. They require mouse interaction and in general block the
application until the mouse interaction is finished. For non-blocking
interactive creation of geometric shapes, HALCON also provides drawing
objects with the operators listed in [Graphics / Object](toc_graphics_object.md).

### General Objectives

The draw operators [`DrawRegion`](draw_region.md), [`DrawXld`](draw_xld.md), [`DrawXldMod`](draw_xld_mod.md),
[`DrawNurbs`](draw_nurbs.md), [`DrawNurbsMod`](draw_nurbs_mod.md), [`DrawNurbsInterp`](draw_nurbs_interp.md),
[`DrawNurbsInterpMod`](draw_nurbs_interp_mod.md), as well as [`DragRegion1`](drag_region1.md),
[`DragRegion2`](drag_region2.md) and [`DragRegion3`](drag_region3.md) return iconic objects.
All other draw operators return the geometric parameters that are needed to
create regions or contours in the respective shape (see table).
Most draw operators have a modifying variant that allows the user to
specify the initial parameters of the shown shape.

### Drawing in Buffer Windows

Because the draw operators rely on mouse interaction, they generally do
not work when used with buffer windows (see [`OpenWindow`](open_window.md)), so you
should use drawing objects instead. Nevertheless some operators (see table)
can be used in buffer windows.
These operators are controlled through a mouse state.
In order to use these operators (and to not cause a deadlock) the
application has to provide the mouse state with the operators
[`SendMouseDoubleClickEvent`](send_mouse_double_click_event.md), [`SendMouseDownEvent`](send_mouse_down_event.md),
[`SendMouseDragEvent`](send_mouse_drag_event.md) and [`SendMouseUpEvent`](send_mouse_up_event.md) as well as the
state of the modifier keys (also by using [`SendMouseDragEvent`](send_mouse_drag_event.md)),
whereas the draw operators themselves must be run in another thread.
While using the draw operator, the image section must not be changed.

| Drawing Operators | Output | Generate Object | Works in Buffer Windows |
| --- | --- | --- | --- |
| [`DrawPoint`](draw_point.md) | `row`, `column` | [`GenCrossContourXld`](gen_cross_contour_xld.md) | yes |
| [`DrawLine`](draw_line.md) | `row1`, `column1`, `row2`, `column2` | [`GenContourPolygonXld`](gen_contour_polygon_xld.md) | yes |
| [`DrawRectangle1`](draw_rectangle1.md) | `row1`, `column1`, `row2`, `column2` | [`GenRectangle1`](gen_rectangle1.md) | yes |
| [`DrawRectangle2`](draw_rectangle2.md) | `row`, `column`, `phi`, `length1`, `length2` | [`GenRectangle2`](gen_rectangle2.md), [`GenRectangle2ContourXld`](gen_rectangle2_contour_xld.md) | yes |
| [`DrawCircle`](draw_circle.md) | `row`, `column`, `radius` | [`GenCircle`](gen_circle.md), [`GenCircleContourXld`](gen_circle_contour_xld.md) | yes |
| [`DrawEllipse`](draw_ellipse.md) | `row`, `column`, `phi`, `radius1`, `radius2` | [`GenEllipse`](gen_ellipse.md), [`GenEllipseContourXld`](gen_ellipse_contour_xld.md) | yes |
| [`DrawXld`](draw_xld.md) | `contour` | - | yes |
| [`DrawRegion`](draw_region.md) | `region` | - | yes |
| [`DrawPolygon`](draw_polygon.md) | `region` | - | yes |
| [`DrawNurbs`](draw_nurbs.md) | `contour`, `rows`, `columns`, `weights` | - | no |
| [`DrawNurbsInterp`](draw_nurbs_interp.md) | `contour`, `rows`, `columns`, `knots`, `tangents` | - | no |
| [`DragRegion1`](drag_region1.md) | `region` | - | no |
| [`DragRegion2`](drag_region2.md) | `region` | - | no |
| [`DragRegion3`](drag_region3.md) | `region` | - | no |
|  |

---

#### List of Operators

- [`DragRegion1`](drag_region1.md) — Interactive moving of a region.

- [`DragRegion2`](drag_region2.md) — Interactive movement of a region with fixpoint specification.

- [`DragRegion3`](drag_region3.md) — Interactive movement of a region with restriction of positions.

- [`DrawCircle`](draw_circle.md) — Interactive drawing of a circle.

- [`DrawCircleMod`](draw_circle_mod.md) — Interactive drawing of a circle.

- [`DrawEllipse`](draw_ellipse.md) — Interactive drawing of an ellipse.

- [`DrawEllipseMod`](draw_ellipse_mod.md) — Interactive drawing of an ellipse.

- [`DrawLine`](draw_line.md) — Draw a line.

- [`DrawLineMod`](draw_line_mod.md) — Draw a line.

- [`DrawNurbs`](draw_nurbs.md) — Interactive drawing of a NURBS curve.

- [`DrawNurbsInterp`](draw_nurbs_interp.md) — Interactive drawing of a NURBS curve using interpolation.

- [`DrawNurbsInterpMod`](draw_nurbs_interp_mod.md) — Interactive modification of a NURBS curve using interpolation.

- [`DrawNurbsMod`](draw_nurbs_mod.md) — Interactive modification of a NURBS curve.

- [`DrawPoint`](draw_point.md) — Draw a point.

- [`DrawPointMod`](draw_point_mod.md) — Draw a point.

- [`DrawPolygon`](draw_polygon.md) — Interactive drawing of a polygon row.

- [`DrawRectangle1`](draw_rectangle1.md) — Draw a rectangle parallel to the coordinate axis.

- [`DrawRectangle1Mod`](draw_rectangle1_mod.md) — Draw a rectangle parallel to the coordinate axis.

- [`DrawRectangle2`](draw_rectangle2.md) — Interactive drawing of any orientated rectangle.

- [`DrawRectangle2Mod`](draw_rectangle2_mod.md) — Interactive drawing of any orientated rectangle.

- [`DrawRegion`](draw_region.md) — Interactive drawing of a closed region.

- [`DrawXld`](draw_xld.md) — Interactive drawing of a contour.

- [`DrawXldMod`](draw_xld_mod.md) — Interactive modification of a contour.
