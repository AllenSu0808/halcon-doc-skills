# Python（halcon 套件）常見陷阱

來源標示：「文件」表示可在 `references/` 查證；「經驗」表示本文件未收錄的一般使用經驗，
使用前請以專案實際的 `halcon` 套件版本確認。

## 環境與匯入

1. 慣用匯入方式為 `import halcon as ha`；`check` 只認得 `import halcon` 與
   `import halcon as <別名>`，不支援 `from halcon import ...`。（經驗）
2. PyPI 套件版本必須對應已安裝的 HALCON 版本（26.05），並需要 HALCON 原生函式庫
   在執行環境中可被找到。（經驗）
3. 運算子是模組層級函式，名稱為 snake_case：`ha.read_image(...)`、`ha.find_shape_model(...)`。（文件）
4. Python 版本不含 `dev_*` 運算子（那些只存在於 HDevelop）；顯示用 `open_window`、
   `disp_obj` 等一般運算子。（文件：python/ 下無 dev_*.md）

## 呼叫與回傳

5. 函式參數只有輸入參數（輸入物件與輸入控制）；輸出參數全部由回傳值取得。（文件：Signature）
6. 只有一個輸出時直接回傳；多個輸出時回傳 tuple，順序與 `sig` 的回傳型別相同，
   解構時數量要一致。（文件）
7. 所有參數都沒有預設值，必須全部傳入；預設值請以 `params` 查 `Default`。（文件：Signature）
8. 可以用關鍵字參數（名稱為文件中的 snake_case 參數名，例如 `num_levels=0`）提高可讀性。（文件）
9. 控制輸出通常是 `Sequence[...]`（list）；部分運算子另有 `_s` 版本回傳單一值，
   以 `sig` 查看是否存在，不要自行在名稱後加 `_s`。（文件）
10. `MaybeSequence[T]` 參數可傳單一值或 list。（文件）
11. 物件輸出（`HObject`）可能包含多個物件，用 `ha.count_obj` 取得數量，
    `ha.select_obj` 取出單一物件，索引從 1 開始。（文件：select_obj）
12. 找不到結果時回傳空 list（例如 `find_shape_model` 沒有匹配），取 `[0]` 前先檢查長度。（經驗）
13. 多值輸出（Row / Column / Angle / Score）同索引對應同一個結果，可用 `zip` 一起走訪。（文件）

## 型別與資料

14. `HObject` 不是 numpy 陣列；需要像素資料時以套件提供的轉換函式
    （例如 `ha.himage_as_numpy_array` / `ha.himage_from_numpy_array`，不在本文件中，
    使用前確認套件版本）轉換。（經驗）
15. 不要用 `get_grayval` 逐點迴圈讀取像素，速度很慢；改用整張影像的運算子或 numpy 轉換。（經驗）
16. Handle 參數型別為 `HHandle`；不要把 handle 轉成 int 保存。（文件：Signature）
17. Handle 在所有參考消失後自動清除；需要立即釋放時呼叫 `ha.clear_handle` 或專用的
    `ha.clear_shape_model` 等運算子，之後該 handle 失效。（文件：clear_handle、clear_shape_model）
18. tuple 運算（`tuple_*` 運算子）在 Python 中通常直接用原生 list 與 `math` 即可，
    不必逐一呼叫 `ha.tuple_*`。（經驗）
19. 字串參數直接傳 Python 字串，不需要額外加引號（寫 `'use_polarity'`，不是 `"'use_polarity'"`）。（經驗）

## 座標、角度與單位

20. 座標順序是 (row, column) = (y, x)；與 numpy 陣列索引 `arr[row, col]` 一致，
    但與 OpenCV / PIL 的 (x, y) 相反。（文件）
21. 大多數角度是弧度（參數標頭 `angle.rad`），少數是度數（`angle.deg`，例如 `rotate_image`
    的 `phi`）；以 `params` 查看標頭。弧度轉換用 `math.radians`。（文件：rotate_image）
22. 像素座標以像素中心為整數座標。（經驗）

## 字串參數

23. 字串值必須完全一致，先以 `params` 查 `List of values`；`check` 會標出不合法的字串常值。（文件）
24. `Suggested values` 不是完整清單，其他值可能也合法；有疑慮時讀 Description。（文件）
25. 泛用參數（`gen_param_name` / `gen_param_value`）以兩個等長 list 成對傳入。（文件）

## 錯誤處理與效能

26. 運算子錯誤以例外拋出（`ha.HOperatorError`，名稱以套件版本為準）；
    捕捉特定例外，不要用裸 `except Exception:` 吞掉。（經驗）
27. 模型建立（例如 `create_shape_model`）很耗時，應只建立一次並重複使用，或以
    `write_shape_model` / `read_shape_model` 保存。（文件）
28. 平行執行前以 `section <名稱> "Execution Information"` 確認執行緒安全等級。（文件）
29. `read_image` 會搜尋 `image_dir` 系統參數並自動嘗試補副檔名。（文件：read_image）
30. HDevelop 範例（`section <名稱> Example`）的參數順序是「輸入…輸出」混在一起，
    轉成 Python 時要把輸出參數移到回傳值。（文件）
