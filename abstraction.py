# ### 5단계: 추상화 (Abstraction)

# 내부의 복잡한 조립 과정(`<ul>`, `<li>` 문자열 결합 등)을 더 작은 단위로 쪼개고, 사용자는 단순히 “리스트를 만들어줘”라고 요청하면 내부적으로 알아서 조립되도록 구조화합니다.

# ```python
# # 5단계: 역할 분담과 구조화

# # 1. 개별 아이템(li)을 만드는 작은 도구 함수
# def create_li_tag(content):
#     return f"<li>{content}</li>"

# # 2. 전체 목록(ul)을 조립하는 메인 함수
# def create_ul_component(data_list):
# 	    # 리스트가 비어있을 경우 예외 처리
#     if not data_list:
#         return ""

#     list_items = []
#     for data in data_list:
#         # 작은 도구 함수를 사용하여 조립
#         tag = create_li_tag(data)
#         list_items.append(tag)

#     # 리스트에 담긴 문자열들을 줄바꿈 문자(\n)로 예쁘게 연결
#     body = "\n".join(list_items)

#     return f"<ul>\n{body}\n</ul>"

# # 사용
# pokes = ["피카츄", "라이츄", "파이리"]
# final_html = create_ul_component(pokes)
# print(final_html)
# ```

# #### 기초 문법 해설

# - **f-string**: `f"<li>{content}</li>"`는 문자열 안에 변수를 직접 끼워 넣는 최신 방식입니다. `+` 기호보다 훨씬 읽기 쉽습니다.
# - **`join()`**: 리스트에 담긴 여러 글자 조각들을 특정 문자(여기서는 줄바꿈 `\n`)를 사이에 두고 하나로 합치는 강력한 접착제입니다.

# #### 논리적 설계 이유

# 이전 단계에서는 하나의 함수가 `<ul>`도 만들고 `<li>`도 만들었습니다. 5단계에서는 `<li>`를 만드는 로직을 별도로 분리했습니다. 만약 나중에 `<li>`에 클래스를 추가해야 한다면, `create_li_tag` 함수만 수정하면 됩니다. 전체 로직이 서로 영향을 덜 주게 됩니다.

# #### 현업 실무 관점

# - **관심사의 분리(Separation of Concerns)**: 각 함수가 하나의 역할에만 집중하게 합니다.
# - 또한, 빈 리스트가 들어왔을 때 빈 문자열을 반환하는 등의 **예외 처리**를 추가하여 코드가 실제 서비스에서 안전하게 돌아가도록(Robustness) 보강했습니다. 이것이 실제 라이브러리나 프레임워크가 동작하는 방식과 가장 유사합니다.'





