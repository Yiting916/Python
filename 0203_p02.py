itemA = {'蘋果', '香蕉', '鳳梨', '芭樂'}
itemB = {'鳳梨', '蘋果', '水梨', '蓮霧'}

itemA.add('橘子')
itemA.add('番茄')
print('itemA 新增: 橘子, 番茄')
print('itemA 刪除:',itemA.pop(), ', 蘋果')
itemA.discard('蘋果')

itemB.add('番茄')
itemB.add('榴槤')
print('itemB 新增: 榴槤, 番茄')
print('itemB 刪除:',itemB.pop(), ', 蓮霧')
itemB.discard('蓮霧')

print('所有的水果且不重覆: ', sorted(itemA | itemB))
print('兩者皆有的水果: ', sorted(itemA & itemB))
print('itmesA獨有的水果: ', sorted(itemA - itemB))
print('itmesB獨有的水果: ', sorted(itemB - itemA))
print('兩者不重覆的水果: ', sorted(itemA ^ itemB))



