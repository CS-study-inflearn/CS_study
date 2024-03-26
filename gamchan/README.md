# 환경설정
## 가상환경 생성(optional)
```
python -m venv myenv # 가상 환경을 myenv로 설정
```
**macOS**
```
source myenv/bin/activate
```

**window**
```
.\venv\Scripts\activate
```

**공통: 가상 환경 비활성화**
```
deactivate
```

## 의존성 설치

```
pip install -r requirements.txt
```

## 실행 시 주의사항
- 아래 명령어로 환경 변수가 가리키는 인터프리터 확인

**macOS**
```
which pip
which python
```

**window**
```
where pip
where python
```
