# GIẢI BÀI TẬP DANH SÁCH LIÊN KẾT

## Đề bài
Cho cấu trúc nút danh sách liên kết:
```c
struct NODE {
    int data;
    NODE *next;
};
```

**a)** Viết hàm `void remove(NODE *&head, int x)` để xóa tất cả các nút mang giá trị x trong danh sách liên kết bằng **kỹ thuật lặp**.

**b)** Tương tự câu (a) nhưng viết bằng **kỹ thuật đệ quy**.

---

## Câu a) Giải pháp dùng KỸ THUẬT LẶP

### Thuật toán:

1. **Xử lý các nút đầu danh sách:**
   - Dùng vòng lặp `while` để xóa liên tiếp các nút ở đầu có giá trị x
   - Cập nhật `head` để trỏ đến nút tiếp theo
   - Giải phóng bộ nhớ của nút bị xóa

2. **Xử lý các nút ở giữa và cuối:**
   - Duyệt danh sách với con trỏ `current`
   - Kiểm tra nút tiếp theo (`current->next`)
   - Nếu nút tiếp theo có giá trị x:
     - Liên kết `current->next` với `current->next->next`
     - Giải phóng bộ nhớ
     - KHÔNG di chuyển `current` (vì cần kiểm tra nút tiếp theo mới)
   - Nếu không, di chuyển `current` sang nút tiếp theo

### Code:
```cpp
void remove(NODE *&head, int x) {
    // Xóa các nút ở đầu danh sách có giá trị x
    while (head != NULL && head->data == x) {
        NODE *temp = head;
        head = head->next;
        delete temp;
    }
    
    // Nếu danh sách rỗng sau khi xóa các nút đầu
    if (head == NULL) {
        return;
    }
    
    // Xóa các nút ở giữa và cuối danh sách
    NODE *current = head;
    while (current->next != NULL) {
        if (current->next->data == x) {
            NODE *temp = current->next;
            current->next = current->next->next;
            delete temp;
        } else {
            current = current->next;
        }
    }
}
```

### Ví dụ minh họa:
```
Danh sách ban đầu: 3 -> 2 -> 3 -> 7 -> 3 -> 5 -> NULL
Xóa giá trị 3:     2 -> 7 -> 5 -> NULL
```

### Phân tích độ phức tạp:
- **Thời gian:** O(n) - duyệt qua tất cả các nút một lần
- **Không gian:** O(1) - chỉ dùng biến tạm

---

## Câu b) Giải pháp dùng ĐỆ QUY

### Thuật toán:

1. **Trường hợp cơ sở (base case):**
   - Nếu `head == NULL`, kết thúc đệ quy

2. **Trường hợp đệ quy:**
   - Nếu `head->data == x`:
     - Lưu con trỏ tạm
     - Cập nhật `head` thành `head->next`
     - Giải phóng bộ nhớ
     - Gọi đệ quy tiếp với `head` mới (vì có thể nút mới cũng có giá trị x)
   - Nếu không:
     - Gọi đệ quy với `head->next` (xử lý phần còn lại của danh sách)

### Code:
```cpp
void removeRecursive(NODE *&head, int x) {
    // Trường hợp cơ sở: danh sách rỗng
    if (head == NULL) {
        return;
    }
    
    // Nếu nút hiện tại có giá trị x
    if (head->data == x) {
        NODE *temp = head;
        head = head->next;
        delete temp;
        // Đệ quy tiếp với nút tiếp theo
        removeRecursive(head, x);
    } else {
        // Đệ quy với phần còn lại của danh sách
        removeRecursive(head->next, x);
    }
}
```

### Ví dụ minh họa:
```
Danh sách ban đầu: 3 -> 9 -> 2 -> 9 -> 9 -> 6 -> NULL
Xóa giá trị 9:     3 -> 2 -> 6 -> NULL
```

### Phân tích độ phức tạp:
- **Thời gian:** O(n) - mỗi nút được xử lý một lần
- **Không gian:** O(n) - do stack đệ quy (worst case khi xóa tất cả)

---

## So sánh hai phương pháp

| Tiêu chí | Kỹ thuật lặp | Đệ quy |
|----------|--------------|--------|
| Độ phức tạp thời gian | O(n) | O(n) |
| Độ phức tạp không gian | O(1) | O(n) |
| Dễ hiểu | Trung bình | Dễ hơn (tư duy tự nhiên) |
| Hiệu năng | Tốt hơn | Kém hơn (overhead của stack) |
| Nguy cơ stack overflow | Không | Có (với danh sách rất dài) |

---

## Các trường hợp đặc biệt cần lưu ý

1. **Danh sách rỗng:** `head == NULL`
2. **Tất cả nút đều có giá trị x:** Danh sách trở thành rỗng
3. **Không có nút nào có giá trị x:** Danh sách không thay đổi
4. **Giá trị x chỉ ở đầu/giữa/cuối:** Cần xử lý đúng các trường hợp này

---

## Kết quả chạy test

### Test kỹ thuật lặp:
```
Danh sách ban đầu: 3 -> 2 -> 3 -> 7 -> 3 -> 5 -> NULL
Sau khi xóa giá trị 3: 2 -> 7 -> 5 -> NULL

Danh sách ban đầu: 5 -> 5 -> 5 -> NULL
Sau khi xóa giá trị 5: NULL

Danh sách ban đầu: 1 -> 1 -> 8 -> 4 -> NULL
Sau khi xóa giá trị 1: 8 -> 4 -> NULL
```

### Test đệ quy:
```
Danh sách ban đầu: 3 -> 9 -> 2 -> 9 -> 9 -> 6 -> NULL
Sau khi xóa giá trị 9 (đệ quy): 3 -> 2 -> 6 -> NULL

Danh sách ban đầu: 7 -> 7 -> 7 -> NULL
Sau khi xóa giá trị 7 (đệ quy): NULL

Danh sách ban đầu: 2 -> 8 -> 4 -> NULL
Sau khi xóa giá trị 10 (không tồn tại): 2 -> 8 -> 4 -> NULL
```

✅ **Cả hai phương pháp đều hoạt động chính xác!**
