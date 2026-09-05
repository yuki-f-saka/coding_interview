from typing import List

# インデックスがiのノードの左の子のインデックスを返す
def leftChild(i: int) -> int:
    return (i + 1) * 2 - 1

# 右
def rightChild(i: int) -> int:
    return (i + 1) * 2

# 親
def parent(i: int) -> int:
    return (i - 1) // 2

# heappush
# 親ノード>=子ノードの条件を保ちながら新しく要素を追加する
def heappush(heap: List[int], x: int) -> None:
    # xを配列の末尾に追加
    heap.append(x)
    # 新しく追加したxのインデックス
    i = len(heap) - 1

    # 根はi = -1なので
    while i > 0:
        # 親のインデックス
        parent_index = parent(i)
        # 親より大きい場合、交換する
        if heap[parent_index] < heap[i]:
            heap[parent_index], heap[i] = heap[i], heap[parent_index]
            # iを更新し、上に交換していく
            i = parent_index
        else:
            break

# インデックスがiのノードの子のうち、最も値が大きいものと交換するのを上から下へと行う
def topDown(ary: List[int], i: int) -> None:
    N = len(ary)

    while i < N:
        left = leftChild(i)
        right = rightChild(i)

        target = i

        # 左の子の方がiより大きい場合
        if left < N and ary[left] > ary[i]:
            target = left
        # この時点でtargetはiか左のこの大きい方となる

        # iと左の子のどちらよりも右の子が大きい場合
        if right < N and ary[right] > ary[target]:
            target = right

        # targetがiでなければ、iとtargetを交換
        if target != i:
            ary[i], ary[target] = ary[target], ary[i]
            # iをtargetに更新して、下の階層へ交換していく
            i = target
        else:
            break

def heapify(ary: List[int]) -> None:
    N = len(ary)

    # 最後のノードの親ノードから上に向かってheapifyを行う
    for i in range((N - 1) // 2, -1, -1):
        topDown(ary, i)

if __name__ == '__main__':
    test_array = [4,10,3,5,1]
    print(f'ヒープ化前: {test_array}')

    heapify(test_array)
    print(f'ヒープ化後: {test_array}')

    heappush(test_array, 8)
    print(f'heappush後: {test_array}')