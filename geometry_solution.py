"""
Bài tập: Giải sử về điểm và hình chữ nhật trong mặt phẳng 2D

Câu a) (2 điểm): Mô tả cấu trúc dữ liệu cho điểm và hình chữ nhật
Câu b) (1.5 điểm): Viết hàm kiểm tra điểm có nằm trong hình chữ nhật hay không
Câu c) (1.5 điểm): Viết hàm kiểm tra 2 hình chữ nhật có rời nhau hay không
"""

# ============================================================================
# Câu a) (2 điểm): Cấu trúc dữ liệu
# ============================================================================

class Point:
    """
    Cấu trúc dữ liệu biểu diễn một điểm trong mặt phẳng 2D
    
    Thuộc tính:
        x (float): Tọa độ x của điểm
        y (float): Tọa độ y của điểm
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Rectangle:
    """
    Cấu trúc dữ liệu biểu diễn một hình chữ nhật trong mặt phẳng 2D
    
    Hình chữ nhật được biểu diễn bởi 2 điểm:
    - (x_min, y_min): Góc dưới bên trái (bottom-left)
    - (x_max, y_max): Góc trên bên phải (top-right)
    
    Thuộc tính:
        x_min (float): Tọa độ x nhỏ nhất (cạnh trái)
        y_min (float): Tọa độ y nhỏ nhất (cạnh dưới)
        x_max (float): Tọa độ x lớn nhất (cạnh phải)
        y_max (float): Tọa độ y lớn nhất (cạnh trên)
    """
    def __init__(self, x_min, y_min, x_max, y_max):
        # Đảm bảo x_min < x_max và y_min < y_max
        if x_min >= x_max or y_min >= y_max:
            raise ValueError("Invalid rectangle coordinates: x_min < x_max and y_min < y_max required")
        
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
    
    def __repr__(self):
        return f"Rectangle(x_min={self.x_min}, y_min={self.y_min}, x_max={self.x_max}, y_max={self.y_max})"


# ============================================================================
# Câu b) (1.5 điểm): Kiểm tra điểm có nằm trong hình chữ nhật hay không
# ============================================================================

def is_point_inside_rectangle(point, rectangle):
    """
    Kiểm tra một điểm có nằm trong một hình chữ nhật hay không.
    
    Theo đề bài: Một điểm nằm trong hình chữ nhật nếu điểm đó thuộc hình chữ nhật
    (bao gồm cả các điểm trên biên).
    
    Điều kiện:
        x_min <= point.x <= x_max
        y_min <= point.y <= y_max
    
    Args:
        point (Point): Điểm cần kiểm tra
        rectangle (Rectangle): Hình chữ nhật
    
    Returns:
        bool: True nếu điểm nằm trong hình chữ nhật, False nếu không
    """
    return (rectangle.x_min <= point.x <= rectangle.x_max and
            rectangle.y_min <= point.y <= rectangle.y_max)


# ============================================================================
# Câu c) (1.5 điểm): Kiểm tra 2 hình chữ nhật có rời nhau hay không
# ============================================================================

def are_rectangles_disjoint(rect1, rect2):
    """
    Kiểm tra 2 hình chữ nhật có rời nhau hay không.
    
    Theo đề bài: Hai hình chữ nhật rời nhau nếu phần giao của chúng là rỗng.
    
    Hai hình chữ nhật KHÔNG rời nhau (có giao nhau) nếu:
        - Không có khoảng cách theo trục x: rect1.x_max >= rect2.x_min AND rect2.x_max >= rect1.x_min
        - Không có khoảng cách theo trục y: rect1.y_max >= rect2.y_min AND rect2.y_max >= rect1.y_min
    
    Hai hình chữ nhật rời nhau nếu:
        - Có khoảng cách theo trục x: rect1.x_max < rect2.x_min OR rect2.x_max < rect1.x_min
        - Hoặc có khoảng cách theo trục y: rect1.y_max < rect2.y_min OR rect2.y_max < rect1.y_min
    
    Args:
        rect1 (Rectangle): Hình chữ nhật thứ nhất
        rect2 (Rectangle): Hình chữ nhật thứ hai
    
    Returns:
        bool: True nếu 2 hình chữ nhật rời nhau, False nếu có giao nhau
    """
    # Kiểm tra xem có rời nhau theo trục x không
    if rect1.x_max < rect2.x_min or rect2.x_max < rect1.x_min:
        return True
    
    # Kiểm tra xem có rời nhau theo trục y không
    if rect1.y_max < rect2.y_min or rect2.y_max < rect1.y_min:
        return True
    
    # Nếu không rời nhau theo cả 2 trục thì chúng có giao nhau
    return False


# ============================================================================
# Test cases để kiểm tra các hàm
# ============================================================================

def test_solution():
    """
    Kiểm tra các hàm với test cases dựa trên hình vẽ trong đề bài
    """
    print("="*70)
    print("KIỂM TRA CÁC HÀM VỚI TEST CASES")
    print("="*70)
    
    # Tạo các điểm P1, P2 (ước lượng từ hình vẽ)
    P1 = Point(3, 4)
    P2 = Point(8, 7)
    
    # Tạo các hình chữ nhật H1, H2, H3 (ước lượng từ hình vẽ)
    # Điều chỉnh để phù hợp với điều kiện:
    # - P1 nằm trong H1 và H2, nhưng không nằm trong H3
    # - P2 không nằm trong cả 3 hình chữ nhật
    # - H2 và H3 RỜI NHAU (disjoint)
    # - H1 và H2 GIAO NHAU, H1 và H3 cũng GIAO NHAU
    H1 = Rectangle(2, 3, 6.5, 7)      # Hình chữ nhật H1
    H2 = Rectangle(1, 2, 4, 5)        # Hình chữ nhật H2  
    H3 = Rectangle(6, 3, 10, 6)       # Hình chữ nhật H3
    
    print("\n--- Thông tin điểm và hình chữ nhật ---")
    print(f"P1 = {P1}")
    print(f"P2 = {P2}")
    print(f"H1 = {H1}")
    print(f"H2 = {H2}")
    print(f"H3 = {H3}")
    
    # Test câu b) - Kiểm tra điểm trong hình chữ nhật
    print("\n--- Câu b) Kiểm tra điểm có nằm trong hình chữ nhật ---")
    print(f"P1 nằm trong H1? {is_point_inside_rectangle(P1, H1)} (Kỳ vọng: True)")
    print(f"P1 nằm trong H2? {is_point_inside_rectangle(P1, H2)} (Kỳ vọng: True)")
    print(f"P1 nằm trong H3? {is_point_inside_rectangle(P1, H3)} (Kỳ vọng: False)")
    print(f"P2 nằm trong H1? {is_point_inside_rectangle(P2, H1)} (Kỳ vọng: False)")
    print(f"P2 nằm trong H2? {is_point_inside_rectangle(P2, H2)} (Kỳ vọng: False)")
    print(f"P2 nằm trong H3? {is_point_inside_rectangle(P2, H3)} (Kỳ vọng: False)")
    
    # Test câu c) - Kiểm tra 2 hình chữ nhật có rời nhau
    print("\n--- Câu c) Kiểm tra 2 hình chữ nhật có rời nhau ---")
    print(f"H1 và H2 rời nhau? {are_rectangles_disjoint(H1, H2)} (Kỳ vọng: False - có giao nhau)")
    print(f"H1 và H3 rời nhau? {are_rectangles_disjoint(H1, H3)} (Kỳ vọng: False - có giao nhau)")
    print(f"H2 và H3 rời nhau? {are_rectangles_disjoint(H2, H3)} (Kỳ vọng: True)")
    
    # Thêm các test cases khác
    print("\n--- Test cases bổ sung ---")
    
    # Test trường hợp điểm nằm trên biên
    P_edge = Point(2, 4)
    print(f"\nĐiểm trên biên {P_edge} nằm trong H1? {is_point_inside_rectangle(P_edge, H1)} (Kỳ vọng: True)")
    
    # Test trường hợp 2 hình chữ nhật chạm nhau tại biên
    H4 = Rectangle(0, 0, 2, 2)
    H5 = Rectangle(2, 0, 4, 2)
    print(f"H4={H4} và H5={H5} rời nhau? {are_rectangles_disjoint(H4, H5)} (Kỳ vọng: False - chạm nhau tại biên)")
    
    # Test trường hợp 2 hình chữ nhật hoàn toàn rời nhau
    H6 = Rectangle(0, 0, 1, 1)
    H7 = Rectangle(2, 2, 3, 3)
    print(f"H6={H6} và H7={H7} rời nhau? {are_rectangles_disjoint(H6, H7)} (Kỳ vọng: True)")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    test_solution()
