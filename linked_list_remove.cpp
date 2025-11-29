#include <iostream>
using namespace std;

struct NODE
{
    int data;
    NODE *next;
};

// Hàm thêm nút vào đầu danh sách (để test)
void insertAtHead(NODE *&head, int value) {
    NODE *newNode = new NODE;
    newNode->data = value;
    newNode->next = head;
    head = newNode;
}

// Hàm in danh sách (để test)
void printList(NODE *head) {
    NODE *temp = head;
    while (temp != NULL) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

// ============================================
// Câu a) Xóa tất cả các nút có giá trị x bằng KỸ THUẬT LẶP
// ============================================
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

// ============================================
// Câu b) Xóa tất cả các nút có giá trị x bằng ĐỆ QUY
// ============================================
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

// Hàm giải phóng bộ nhớ
void deleteList(NODE *&head) {
    while (head != NULL) {
        NODE *temp = head;
        head = head->next;
        delete temp;
    }
}

// ============================================
// HÀM TEST
// ============================================
int main() {
    cout << "=== TEST CÂU A - KỸ THUẬT LẶP ===" << endl;
    
    // Test case 1: Xóa nút ở giữa
    NODE *list1 = NULL;
    insertAtHead(list1, 5);
    insertAtHead(list1, 3);
    insertAtHead(list1, 7);
    insertAtHead(list1, 3);
    insertAtHead(list1, 2);
    insertAtHead(list1, 3);
    
    cout << "Danh sách ban đầu: ";
    printList(list1);
    
    remove(list1, 3);
    cout << "Sau khi xóa giá trị 3: ";
    printList(list1);
    
    deleteList(list1);
    
    // Test case 2: Xóa tất cả nút
    NODE *list2 = NULL;
    insertAtHead(list2, 5);
    insertAtHead(list2, 5);
    insertAtHead(list2, 5);
    
    cout << "\nDanh sách ban đầu: ";
    printList(list2);
    
    remove(list2, 5);
    cout << "Sau khi xóa giá trị 5: ";
    printList(list2);
    
    // Test case 3: Xóa nút đầu
    NODE *list3 = NULL;
    insertAtHead(list3, 4);
    insertAtHead(list3, 8);
    insertAtHead(list3, 1);
    insertAtHead(list3, 1);
    
    cout << "\nDanh sách ban đầu: ";
    printList(list3);
    
    remove(list3, 1);
    cout << "Sau khi xóa giá trị 1: ";
    printList(list3);
    
    deleteList(list3);
    
    cout << "\n=== TEST CÂU B - ĐỆ QUY ===" << endl;
    
    // Test case 1: Xóa nút ở giữa
    NODE *list4 = NULL;
    insertAtHead(list4, 6);
    insertAtHead(list4, 9);
    insertAtHead(list4, 9);
    insertAtHead(list4, 2);
    insertAtHead(list4, 9);
    insertAtHead(list4, 3);
    
    cout << "Danh sách ban đầu: ";
    printList(list4);
    
    removeRecursive(list4, 9);
    cout << "Sau khi xóa giá trị 9 (đệ quy): ";
    printList(list4);
    
    deleteList(list4);
    
    // Test case 2: Xóa tất cả nút
    NODE *list5 = NULL;
    insertAtHead(list5, 7);
    insertAtHead(list5, 7);
    insertAtHead(list5, 7);
    
    cout << "\nDanh sách ban đầu: ";
    printList(list5);
    
    removeRecursive(list5, 7);
    cout << "Sau khi xóa giá trị 7 (đệ quy): ";
    printList(list5);
    
    // Test case 3: Không có giá trị cần xóa
    NODE *list6 = NULL;
    insertAtHead(list6, 4);
    insertAtHead(list6, 8);
    insertAtHead(list6, 2);
    
    cout << "\nDanh sách ban đầu: ";
    printList(list6);
    
    removeRecursive(list6, 10);
    cout << "Sau khi xóa giá trị 10 (không tồn tại): ";
    printList(list6);
    
    deleteList(list6);
    
    return 0;
}
