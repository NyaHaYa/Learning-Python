# 딕셔너리

{Key1 : Value1, Key2: Value2, Key3: Value3 ...}

dic = {'name': 'abc', 'phone': '01012341234', 'brith': 0123}

a = {1: 'hi'}

a = {'a': [1,2,3]}

## 딕셔너리 쌍 추가, 삭제하기

### 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)                    # {1: 'a', 2: 'b'}

a['name'] = 'abc'
print(a)                    # {1: 'a', 2: 'b', 'name': 'abc'}

a[3] = [1,2,3]
print(a)                    # {1: 'a', 2: 'b', 'name': 'abc', 3: [1,2,3]}

### 딕셔너리 요소 삭제하기
del a[1]                    # {2: 'b', 'name': 'abc', 3: [1,2,3]}


## 딕셔너리 사용하기