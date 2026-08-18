# docs/ : Annex A 통제 자료집

> English: [README.md](README.md)
>
> 저장소 소개: [../README.ko.md](../README.ko.md), 근거 판본: [../UPDATES.ko.md](../UPDATES.ko.md)

이 디렉터리가 자료집 본체입니다. ISO/IEC 27001:2022 Annex A의 정보보안 통제 93개를 담고 있습니다.
통제 하나가 Markdown 파일 하나이고 한국어와 영어로 있습니다. 이 저장소의 나머지는 전부 이 파일들에서
생성되거나 이 파일들을 지키기 위해 존재합니다.

## 이 문서들이 무엇이고 무엇이 아닌가

**표준 원문이 아닙니다.** 통제 번호, 명칭, 테마 분류는 Annex A 공개 통제 목록에서 가져왔습니다. 모든
문서의 설명 본문은 이 프로젝트가 실무 참조용으로 직접 쓴 **원저작물**입니다.

ISO/IEC 27001:2022의 규범 본문, 이행 지침, 속성 표는 여기서 복제하지도, 원문에 가깝게 바꿔 쓰지도,
번역하지도 않습니다. 각 문서 하단에 그 사실을 밝히는 출처와 한계 고지가 붙어 있습니다. 정본이 필요한
판단에는 라이선스를 갖춘 표준 원본을 사용하십시오.

이 경계는 문서를 고칠 때의 강한 규칙이며, 동시에 이 자료집의 갱신 모델이 상위 문서를 그대로 따라가는
방식과 다른 이유이기도 합니다. [../UPDATES.ko.md](../UPDATES.ko.md)를 보십시오.

## 읽기 전용

자료집을 **사용하는 동안에는** 이 디렉터리를 불변으로 취급하십시오. `tools/build_index.py`와
`tools/check_corpus.py`는 여기서 읽기만 하고, 자료집으로 답하는 agent는 `docs/` 아래의 무엇도 만들거나
고치거나 지우면 안 됩니다. 파생 산출물은 사용하는 쪽 작업 공간에 둡니다.

물론 유지보수하는 사람은 이 파일들을 고칩니다. 그것은 다른 활동이고 별도의 규칙을 따릅니다.
[../CLAUDE.md](../CLAUDE.md)와 아래의 언어 동기화 규칙을 보십시오.

## 디렉터리 구조

`docs/<lang>/<테마-slug>/<no>.md` 형태이며 `<lang>`은 `ko` 또는 `en`입니다. 두 언어는 **상대 경로가
완전히 동일**합니다. 경로는 전부 ASCII입니다.

```
docs/
  ko/
    A.5-organizational/A.5.1.md    통제 37개
    A.6-people/*.md                통제  8개
    A.7-physical/*.md              통제 14개
    A.8-technological/*.md         통제 34개
    INDEX.md                       생성되는 목차
  en/                              상대 경로 동일
    ...
    INDEX.md
```

언어별 93개 통제, 총 186개 문서입니다.

| 테마(고정 id) | slug | 통제 수 | 범위 | 목차 |
|---|---|:--:|:--:|---|
| `organizational` | `A.5-organizational` | 37 | A.5.1부터 A.5.37 | [ko](ko/INDEX.md) / [en](en/INDEX.md) |
| `people` | `A.6-people` | 8 | A.6.1부터 A.6.8 | 동일 |
| `physical` | `A.7-physical` | 14 | A.7.1부터 A.7.14 | 동일 |
| `technological` | `A.8-technological` | 34 | A.8.1부터 A.8.34 | 동일 |

어떤 통제가 존재해야 하는지는 [`../extended/catalog/controls.json`](../extended/catalog/controls.json)이
정의합니다. 카탈로그와 문서가 어느 방향으로든 어긋나면 `check_corpus.py`가 실패하므로, 카탈로그와 이
디렉터리가 조용히 어긋날 수는 없습니다.

## 문서 구조

모든 통제 문서는 상단 metadata 표, 순서가 같은 6개 섹션, 하단 출처와 한계 고지를 지킵니다.

`통제 목적` → `주요 확인사항` → `이행 지침` → `관련 통제 및 속성` → `증적자료` → `부적합 사례`

섹션이 빠지거나 순서가 어긋나면 `check_corpus.py`가 실패하므로, 이 구조는 믿고 의존해도 됩니다.

## 언어 대응 관계

ISMS-P 자료집과 달리, 여기서는 어느 언어도 다른 언어의 번역이 아니고 어느 쪽이 종속되지도 않습니다.
둘 다 이 프로젝트가 직접 쓴 것입니다. 그래도 두 쪽은 같은 내용을 말해야 하고 **같은 commit에서** 함께
바뀌어야 합니다. 한국어만 또는 영어만 고친 상태는 결함이며 CI가 막습니다. 대응 관계는 통제 번호로
잡힙니다.

## AI agent용: manifest를 거쳐서 접근

`docs/`를 무작정 grep하지 마십시오. [`../extended/manifest.json`](../extended/manifest.json)에서
시작합니다. 모든 문서의 `no`, `path`, 테마, 섹션별 개수가 색인돼 있습니다. 관련 통제 번호로 먼저
범위를 좁힌 다음, 그 파일들만 읽습니다. 목록만 필요하다면 문서 대신
`../extended/index/evidence-dictionary.json`이나 `../extended/index/nonconformity-rulebook.json`을
읽습니다.

전체 운영 규칙(읽기 전용 자료집, manifest 우선 접근, 인용 의무, 저작권 경계, 사람 승인 게이트)은
[../extended/README.ko.md](../extended/README.ko.md)에 있습니다.
