# GIẢI BÀI TẬP: ĐIỂM VÀ HÌNH CHỮ NHẬT TRONG MẶT PHẲNG 2D

## Tổng quan

Bài tập này yêu cầu thiết kế cấu trúc dữ liệu và thuật toán để làm việc với các điểm và hình chữ nhật trong mặt phẳng 2 chiều.

## Câu a) (2 điểm) - Cấu trúc dữ liệu

### 1. Class `Point` - Biểu diễn điểm

```python
class Point:
    def __init__(self, x, y):
        self.x = x  # Tọa độ x
        self.y = y  # Tọa độ y
```

**Giải thích:**
- Một điểm trong mặt phẳng 2D được xác định bởi 2 tọa độ: `x` và `y`
- Cấu trúc đơn giản, dễ sử dụng
- Ví dụ: `P1 = Point(3, 4)` tạo điểm có tọa độ (3, 4)

### 2. Class `Rectangle` - Biểu diễn hình chữ nhật

```python
class Rectangle:
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min  # Tọa độ x bên trái
        self.y_min = y_min  # Tọa độ y bên dưới
        self.x_max = x_max  # Tọa độ x bên phải
        self.y_max = y_max  # Tọa độ y bên trên
```

**Giải thích:**
- Hình chữ nhật được biểu diễn bằng 2 điểm góc:
  - Góc dưới bên trái (bottom-left): `(x_min, y_min)`
  - Góc trên bên phải (top-right): `(x_max, y_max)`
- Cách biểu diễn này có nhiều ưu điểm:
  - Đơn giản, chỉ cần 4 giá trị
  - Dễ dàng tính toán các phép kiểm tra (điểm trong hình, giao 2 hình)
  - Tiết kiệm bộ nhớ
- Ví dụ: `H1 = Rectangle(2, 3, 6, 7)` tạo hình chữ nhật có:
  - Góc dưới trái: (2, 3)
  - Góc trên phải: (6, 7)

## Câu b) (1.5 điểm) - Kiểm tra điểm trong hình chữ nhật

### Thuật toán

```python
def is_point_inside_rectangle(point, rectangle):
    return (rectangle.x_min <= point.x <= rectangle.x_max and
            rectangle.y_min <= point.y <= rectangle.y_max)
```

### Giải thích thuật toán

Một điểm `P(x, y)` nằm trong hình chữ nhật nếu và chỉ nếu:
1. Tọa độ x của điểm nằm trong khoảng [x_min, x_max]
2. Tọa độ y của điểm nằm trong khoảng [y_min, y_max]

**Minh họa:**

```
        y_max  ┌─────────────┐
               │             │
               │      • P    │  ← P nằm trong hình chữ nhật
               │             │
        y_min  └─────────────┘
             x_min         x_max

Điều kiện: x_min ≤ P.x ≤ x_max  VÀ  y_min ≤ P.y ≤ y_max
```

### Độ phức tạp
- **Thời gian:** O(1) - Chỉ cần 4 phép so sánh
- **Không gian:** O(1) - Không cần bộ nhớ phụ

## Câu c) (1.5 điểm) - Kiểm tra 2 hình chữ nhật rời nhau

### Thuật toán

```python
def are_rectangles_disjoint(rect1, rect2):
    # Rời nhau theo trục x
    if rect1.x_max < rect2.x_min or rect2.x_max < rect1.x_min:
        return True
    
    # Rời nhau theo trục y
    if rect1.y_max < rect2.y_min or rect2.y_max < rect1.y_min:
        return True
    
    # Không rời nhau (có giao nhau)
    return False
```

### Giải thích thuật toán

Hai hình chữ nhật **rời nhau** (disjoint) nếu phần giao của chúng là rỗng.

**Điều kiện để 2 hình chữ nhật rời nhau:**

Chúng rời nhau nếu một trong các điều kiện sau đúng:

1. **Rời nhau theo trục X:**
   - Hình 1 nằm hoàn toàn bên trái hình 2: `rect1.x_max < rect2.x_min`
   - Hình 2 nằm hoàn toàn bên trái hình 1: `rect2.x_max < rect1.x_min`

2. **Rời nhau theo trục Y:**
   - Hình 1 nằm hoàn toàn bên dưới hình 2: `rect1.y_max < rect2.y_min`
   - Hình 2 nằm hoàn toàn bên dưới hình 1: `rect2.y_max < rect1.y_min`

### Minh họa các trường hợp

#### 1. Rời nhau theo trục X

```
┌──────┐              ┌──────┐
│  R1  │              │  R2  │
└──────┘              └──────┘

R1.x_max < R2.x_min  →  RỜI NHAU
```

#### 2. Rời nhau theo trục Y

```
┌──────┐
│  R2  │
└──────┘

┌──────┐
│  R1  │
└──────┘

R1.y_max < R2.y_min  →  RỜI NHAU
```

#### 3. Giao nhau (không rời nhau)

```
┌──────────┐
│   R1     │
│    ┌─────┼───┐
│    │  X  │   │
└────┼─────┘   │
     │   R2    │
     └─────────┘

Có vùng giao X  →  KHÔNG rời nhau
```

#### 4. Chạm nhau tại biên (không rời nhau)

```
┌──────┬──────┐
│  R1  │  R2  │
└──────┴──────┘

R1.x_max = R2.x_min  →  KHÔNG rời nhau (chạm tại biên)
```

### Độ phức tạp
- **Thời gian:** O(1) - Chỉ cần 4 phép so sánh
- **Không gian:** O(1) - Không cần bộ nhớ phụ

## Cách chạy chương trình

```bash
python3 geometry_solution.py
```

Chương trình sẽ tự động chạy các test cases và hiển thị kết quả.

## Các test cases

Chương trình bao gồm các test cases sau:

1. **Test theo đề bài:**
   - P1 nằm trong H1 và H2 nhưng không trong H3
   - P2 không nằm trong bất kỳ hình chữ nhật nào
   - H1 và H2 giao nhau
   - H1 và H3 giao nhau
   - H2 và H3 rời nhau

2. **Test cases bổ sung:**
   - Điểm nằm trên biên hình chữ nhật
   - 2 hình chữ nhật chạm nhau tại biên
   - 2 hình chữ nhật hoàn toàn rời nhau

## Kết quả mong đợi

Tất cả các test cases đều PASS, cho thấy cấu trúc dữ liệu và thuật toán hoạt động chính xác.

## Tổng kết

**Ưu điểm của giải pháp:**
1. Cấu trúc dữ liệu đơn giản, dễ hiểu
2. Thuật toán hiệu quả với độ phức tạp O(1)
3. Code rõ ràng, có comment đầy đủ
4. Xử lý đúng các trường hợp biên (edge cases)
5. Có test cases đầy đủ để kiểm tra

**Các trường hợp đặc biệt được xử lý:**
- Điểm nằm trên biên hình chữ nhật → vẫn được coi là nằm trong
- 2 hình chữ nhật chạm nhau tại biên → không rời nhau
- Kiểm tra tính hợp lệ của hình chữ nhật khi khởi tạo
