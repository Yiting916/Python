itemA = {'蘋果', '香蕉', '鳳梨', '芭樂'}
itemB = {'鳳梨', '蘋果', '水梨', '蓮霧'}

print('itemA 新增兩樣水果:')
itemA.add(input())
itemA.add(input())
print('itemA 刪除了:',itemA.pop(), ', 蘋果')
itemA.discard('蘋果')

print('itemB 新增兩樣水果:')
itemB.add(input())
itemB.add(input())
print('itemB 刪除了:',itemB.pop(), ', 蓮霧')
itemB.discard('蓮霧')

print('所有的水果且不重覆: ', sorted(itemA | itemB))
print('兩者皆有的水果: ', sorted(itemA & itemB))
print('itmesA獨有的水果: ', sorted(itemA - itemB))
print('itmesB獨有的水果: ', sorted(itemB - itemA))
print('兩者不重覆的水果: ', sorted(itemA ^ itemB))



