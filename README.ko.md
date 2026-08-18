# iso-27001-docs

> English: [README.md](README.md)

**ISO/IEC 27001:2022 Annex A**의 93개 통제를 통제 하나당 Markdown 파일 하나로 정리한 한국어/영어
이중 언어 실무 참고 자료집입니다.

이 저장소에는 문서만 있습니다. 애플리케이션도 빌드 산출물도 infra도 없습니다. 자료집을 쓰는 쪽은
[`extended/manifest.json`](extended/manifest.json)을 읽습니다. 그 파일이 공개 계약입니다.

## 저작권 경계, 먼저 읽으십시오

- 통제 **번호, 명칭, 4개 테마 분류**는 ISO/IEC 27001:2022 Annex A의 **공개 목록**에 근거합니다. 이
  목록은 사실 정보입니다.
- 각 문서의 **설명 본문은 본 자료집이 새로 작성한 원저작**입니다. 통제 목적, 주요 확인사항, 이행 지침,
  관련 통제, 증적 예시, 부적합 사례가 여기에 해당합니다. ISO/IEC 27001:2022 및 27002:2022의 규범
  텍스트가 **아니며**, 그 텍스트의 번역도 아닙니다.
- 표준의 규범 텍스트, 이행 지침, 속성 표, 제3자 해설은 이 repository에서 **원문 그대로 옮기지
  않습니다**.
- 정본 대조가 필요하면 **라이선스된 표준 원문**으로 확인하십시오. 모든 문서 하단에 이 고지가 있으며,
  누락된 문서가 있으면 CI가 실패합니다.

이 경계가 자료집의 갱신 방식도 결정합니다. 다시 맞출 상위 본문 자체가 없으므로, ISO 개정은 여기서
설명 문구가 아니라 **통제 목록**을 바꿉니다. 각 계층이 어느 판본에 고정돼 있고 어떻게 관리되는지는
[UPDATES.ko.md](UPDATES.ko.md)에 기록돼 있습니다.

## 구성

| 테마 | 언어별 통제 수 |
|---|---|
| A.5 조직적 통제(Organizational) | 37 |
| A.6 인적 통제(People) | 8 |
| A.7 물리적 통제(Physical) | 14 |
| A.8 기술적 통제(Technological) | 34 |
| **합계** | **언어별 93** (문서 186개) |

모든 통제 문서는 동일한 6개 섹션 구조를 지킵니다.

`통제 목적` → `주요 확인사항` → `이행 지침` → `관련 통제 및 속성` → `증적자료` → `부적합 사례`

## 디렉터리 구조

```
docs/
  ko/                            한국어 문서
    A.5-organizational/<no>.md   예: docs/ko/A.5-organizational/A.5.1.md
    A.6-people/<no>.md
    A.7-physical/<no>.md
    A.8-technological/<no>.md
    INDEX.md                     생성되는 목차
  en/                            영어 문서. 상대 경로가 한국어 쪽과 동일
extended/
  catalog/controls.json          Annex A 공개 통제 목록(번호, 명칭, 테마)
  manifest.json                  기계가독 색인(공개 계약)
  index/                         평탄 CSV 색인, 부적합 사례 룰북, 증적 사전
tools/
  build_index.py                 docs/에서 파생 색인 전체를 재생성
  check_corpus.py                읽기 전용 무결성 검사
harness/
  install-hooks.sh               clone에 git hook을 배선(최초 1회, 설치 절 참고)
  check-conventions.sh           문서 규약 검사기(playbook docs/16)
```

경로는 전부 ASCII라 소비자 쪽에서 URL 인코딩 문제가 생기지 않습니다.

## manifest 계약

`extended/manifest.json`(schema `corpus-manifest/v3`)이 쓰는 쪽에서 읽는 파일입니다. `nav` 값은
`themes`입니다. 읽는 쪽은 네 테마를 최상위 탐색으로 그립니다.

```json
{
  "schema": "corpus-manifest/v3",
  "standard": {
    "id": "iso-27001",
    "nav": "themes",
    "langs": ["ko", "en"],
    "sections": [{ "id": "organizational", "slug": "A.5-organizational", "no": "A.5",
                   "label": { "ko": "조직적 통제", "en": "Organizational controls" },
                   "count": { "ko": 37, "en": 37 } }],
    "provenance": { "ko": "...", "en": "..." },
    "itemSections": { "ko": ["통제 목적", "..."], "en": ["Control objective", "..."] }
  },
  "counts": { "ko": 93, "en": 93, "total": 186 },
  "items": [{
    "lang": "ko", "section": "organizational", "no": "A.5.1", "name": "정보보안 정책",
    "groupNo": "A.5", "group": "조직적 통제", "subgroupNo": "", "subgroup": "",
    "appliesTo": [], "path": "docs/ko/A.5-organizational/A.5.1.md",
    "counts": { "checkpoints": 4, "evidence": 4, "defects": 4, "hasLaws": false }
  }]
}
```

**절대 이름을 바꾸지 않는 고정 키**: 표준 id `iso-27001`, 테마 id `organizational` / `people` /
`physical` / `technological`, 그리고 통제 번호. 소비자가 이 값들을 키로 씁니다.

## 설치

이 repository에는 문서만 있어서 패키지 관리자도, git hook 배선을 걸어둘 install 단계도 없습니다.
`core.hooksPath`는 `.git/config`에 있고 이는 clone과 함께 따라오지 않는 로컬 상태이므로,
**clone마다 한 번씩** 다음을 실행하십시오.

```bash
bash harness/install-hooks.sh
```

여러 번 실행해도 안전하고, `.git/config` 밖에는 아무것도 쓰지 않습니다. `pre-commit`(문서 규약),
`commit-msg`(commit message 규칙), `pre-push`(master 직접 push 차단)를 활성화합니다. hook은 우회 가능한
편의 guardrail이고, 정본 게이트는 같은 검사기를 돌리는 CI(`.github/workflows/docs.yml`)입니다.

나머지는 Python 3(표준 라이브러리만)와 bash만 있으면 됩니다.

## 유지보수

```bash
python3 tools/build_index.py    # extended/와 docs/{ko,en}/INDEX.md 재생성
python3 tools/check_corpus.py   # 읽기 전용 무결성 검사
bash harness/check-conventions.sh
```

둘 다 결정적이고 재현 가능합니다. CI가 재생성한 뒤 diff가 있으면 실패시키므로, commit된 색인은 항상
자료집과 일치합니다.

통제를 추가/수정/삭제할 때는 **같은 commit에서 반대 언어 문서도 함께 고칩니다**. 대응 관계는 통제
번호로 잡힙니다. 한국어만 또는 영어만 고친 상태는 결함이며 CI가 막습니다.

통제를 추가하면 `extended/catalog/controls.json`에도 추가해야 합니다. 카탈로그와 문서가 어느 방향으로든
어긋나면 `check_corpus.py`가 실패합니다.

## 라이선스

- 코드와 도구: MIT. [LICENSE](LICENSE) 참고.
- 자료집(원저작 설명 본문과 `docs/` 편집, 구성): CC BY 4.0. [LICENSE-CONTENT](LICENSE-CONTENT)와
  [NOTICE](NOTICE) 참고.

위 라이선스는 본 프로젝트의 자체 저작물에만 적용됩니다. ISO/IEC 27001 표준 원문은 ISO와 IEC의 권리에
따르며 여기서 재라이선스하거나 복제하거나 번역하지 않습니다.
