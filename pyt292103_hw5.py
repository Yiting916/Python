mathPass = {'柯南', '灰原', '步美', '美環', '光彦'}
englishPass = {'柯南', '灰原', '丸尾', '野口', '步美'}

#數學及格但英文不及格
print(sorted(mathPass-englishPass))

#英文及格但數學不及格
print(sorted(englishPass-mathPass))

#英文及格且數學及格
print(sorted(mathPass & englishPass))
