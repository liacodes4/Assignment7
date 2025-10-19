class Patient:
     def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency



class MinHeap:
     def __init__(self):
        self.data = []

     def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break

     def heapify_down(self, index):
        n = len(self.data)
        while index < n:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < n and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < n and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

     def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

     def print_heap(self):
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")

     def peek(self):
        if self.data:
            return self.data[0]
        return None

     def remove_min(self):
        if not self.data:
            return None
        min_patient = self.data[0]
        last_patient = self.data.pop()
        if self.data:
            self.data[0] = last_patient
            self.heapify_down(0)
        return min_patient




# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))

    heap.print_heap()
    # Peek at next patient
    next_up = heap.peek()
    print(next_up.name, next_up.urgency)  # Taylor 1

    # Serve patient
    served = heap.remove_min()
    print(served.name)  # Taylor
    heap.print_heap()