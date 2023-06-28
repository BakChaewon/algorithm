1. str
   - .upper(), .lower() 함수를 통해 문자의 대소문자 변경 가능
   - f-string - format과 유사하게 print(f'hello {name}')과 같이 변수를 대괄호 안에 써서 바로 print 가능. 이 함수를 통해 int를 str으로 변환할 수도 있음
   - max() - str에서도 max 함수 사용이 가능. 유니코드 값이 큰 인자 반환. 숫자로 이루어진 문자열이 들어온다면 가장 앞의 숫자로 비교. 2000 vs 899면 899반환

2. list
   - prod(list)는 각 원소의 곱을 반환. 리스트가 행렬일 경우 각 열의 곱을 반환한다.
   - join() - "".join(list) 와 같이 리스트 내 요소를 한 문장으로 결합할 수 있음
  
3. int
   - not() 함수를 통해 0을 True로 0이 아닌 값을 False로 만들 수 있음. not(0)==True / not(22)==False
