/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number[][]}
 */
var kSmallestPairs = function (list1, list2, k) {
    // storing the length of lists to use it in a loop later
    let listLength = list1.length;
    // declaring a min-heap to keep track of the smallest sums
    let minHeapForPairs = new MinHeap();
    // to store the pairs with smallest sums
    let pairs = [];

    // iterate over the length of list 1
    for (let i = 0; i < Math.min(k, listLength); i++) {
        // computing sum of pairs all elements of list1 with first index
        // of list2 and placing it in the min-heap
        minHeapForPairs.offer([list1[i] + list2[0], i, 0]);
    }

    let counter = 1;

    // iterate over elements of min-heap and only go upto k
    while (minHeapForPairs.size() > 0 && counter <= k) {
        // placing sum of the top element of min-heap
        // and its corresponding pairs in i and j
        let [sumOfPairs, i, j] = minHeapForPairs.poll();

        // add pairs with the smallest sum in the new list
        pairs.push([list1[i], list2[j]]);

        // increment the index for 2nd list, as we've
        // compared all possible pairs with the 1st index of list2
        let nextElement = j + 1;

        // if next element is available for list2 then add it to the heap
        if (list2.length > nextElement) {
            minHeapForPairs.offer([list1[i] + list2[nextElement], i, nextElement]);
        }
        counter++;
    }
    // return the pairs with the smallest sums
    return pairs;
};

class MinHeap {
    constructor(data = new Array()) {
        this.data = data;
        this.compareVal = (a, b) => a - b;
        this.heapify();
    }

    heapify() {
        if (this.size() < 2) {
            return;
        }
        for (let i = 1; i < this.size(); i++) {
            this.percolateUp(i);
        }
    }

    peek() {
        if (this.size() === 0) {
            return null;
        }
        return this.data[0];
    }

    offer(value) {
        this.data.push(value);
        this.percolateUp(this.size() - 1);
    }

    poll() {
        if (this.size() === 0) {
            return null;
        }
        const result = this.data[0];
        const last = this.data.pop();
        if (this.size() !== 0) {
            this.data[0] = last;
            this.percolateDown(0);
        }
        return result;
    }

    percolateUp(index) {
        while (index > 0) {
            const parentIndex = (index - 1) >> 1;
            if (
                this.compareVal(
                    this.data[index][0],
                    this.data[parentIndex][0]
                ) < 0
            ) {
                this.swap(index, parentIndex);
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    percolateDown(index) {
        const lastIndex = this.size() - 1;
        while (true) {
            const leftIndex = index * 2 + 1;
            const rightIndex = index * 2 + 2;
            let findIndex = index;

            if (
                leftIndex <= lastIndex &&
                this.compareVal(
                    this.data[leftIndex][0],
                    this.data[findIndex][0]
                ) < 0
            ) {
                findIndex = leftIndex;
            }

            if (
                rightIndex <= lastIndex &&
                this.compareVal(
                    this.data[rightIndex][0],
                    this.data[findIndex][0]
                ) < 0
            ) {
                findIndex = rightIndex;
            }

            if (index !== findIndex) {
                this.swap(index, findIndex);
                index = findIndex;
            } else {
                break;
            }
        }
    }

    swap(index1, index2) {
        [this.data[index1], this.data[index2]] = [
            this.data[index2],
            this.data[index1],
        ];
    }

    size() {
        return this.data.length;
    }
}