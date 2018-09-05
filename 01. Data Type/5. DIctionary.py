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
example = {"김연아":"피겨스케이팅","류현진":"야구","박지성":"축구","저녁":"밥"}

### 딕셔너리에서 Key 사용해서 Value 얻기
grade = {'pey':10, 'julliet':99}
grade['pey']                # 10
grade['julliet']            # 99

# 어떤 Key의 Value를 얻기 위해서는 "딕셔너리 변수[Key]"를 사용한다.

a = {1: 'a', 2: 'b'}
a[1]                        # 'a'
a[2]                        # 'b'

## 딕셔너리 관련 함수들

### Key 리스트 만들기 (keys)
a = {'name': 'pey', 'phone':'01012341234', 'brith':'1118'}
a,keys()                    # dict_keys(['name','phone','brith'])

### Value 리스트 만들기 (values)
a.values()                  # dict_values(['pey','01012341234','1118'])

### Key, Value 쌍 얻기 (items)
a.items()                   # dict_items([('name', 'pey'), ('phone', '01012341234'), ('brith', '1118')])

### Key, Value 쌍 모두 지우기 (clear)
a.clear()                   # {}

### Key로 Value 얻기 (get)
a.get('name')               # 'pey'
a.get('phone')              # '01012341234'