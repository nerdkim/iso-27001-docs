# iso-27001-docs

> English: [README.md](README.md)

**ISO/IEC 27001:2022 Annex A**의 93개 통제를 통제 하나당 Markdown 파일 하나로 정리한 한국어/영어
이중 언어 실무 참고 자료집입니다.

이 저장소에는 문서만 있습니다. 애플리케이션도 빌드 산출물도 인프라도 없습니다. 자료집을 쓰는 쪽은
[`extended/manifest.json`](extended/manifest.json)을 읽습니다. 그 파일이 공개 계약입니다.

**범위: Annex A 한정.** 이 자료집은 Annex A 93개 통제만 다룹니다. ISMS 요구사항이 있는 본문 4장에서
10장, 곧 범위, 리더십, 위험 평가와 위험 처리, 6.1.3이 요구하는 적용가능성 명세서(Statement of
Applicability), 목표, 역량, 문서화된 정보, 운용, 성과 평가, 내부 심사, 경영 검토, 부적합과 시정조치는
다루지 않습니다. 각 통제 문서의 `ISO 27001 본문 연계` 줄은 본문을 가리키는 포인터이지 본문 요약이
아니므로, 그 요구사항이 필요하면 라이선스를 갖춘 표준 원본이 있어야 합니다. 적용가능성 명세서는
조직이 93개 통제 각각에 대한 판단을 기록하는 문서입니다. 이 자료집은 그 문서가 아니며 그것을 만들어
주지도 않습니다.

## 저작권 경계, 먼저 읽으십시오

- 통제 **번호, 명칭, 4개 테마 분류**는 ISO/IEC 27001:2022 Annex A의 **공개 목록**에 근거합니다. 이
  목록은 사실 정보입니다.
- 각 문서의 **설명 본문은 본 자료집이 새로 작성한 원저작**입니다. 통제 목적, 주요 확인사항, 이행 지침,
  관련 통제, 증적 예시, 부적합 사례가 여기에 해당합니다. ISO/IEC 27001:2022 및 27002:2022의 규범
  텍스트가 **아니며**, 그 텍스트의 번역도 아닙니다.
- 표준의 규범 텍스트, 이행 지침, 속성 표, 제3자 해설은 이 저장소에서 **원문 그대로 옮기지
  않습니다**.
- 정본 대조가 필요하면 **라이선스된 표준 원문**으로 확인하십시오. 모든 문서 하단에 이 고지가 있으며,
  누락된 문서가 있으면 CI가 실패합니다.

이 경계가 자료집의 갱신 방식도 결정합니다. 다시 맞출 상위 본문 자체가 없으므로, ISO 개정은 여기서
설명 문구가 아니라 **통제 목록**을 바꿉니다. 각 계층이 어느 판본에 고정돼 있고 어떻게 관리되는지는
[UPDATES.ko.md](UPDATES.ko.md)에 기록돼 있습니다.

[REVIEW.ko.md](REVIEW.ko.md)는 2026-09-17에 수행한 통제 문서 186개 전체의 본문 검토 기록입니다.
수정 내용, 통제별 검토 범위와 검증 한계를 담고 있습니다.

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
  README.md / README.ko.md       이 문서들이 무엇인지와 읽기 전용 규칙
  ko/                            한국어 문서
    A.5-organizational/<no>.md   예: docs/ko/A.5-organizational/A.5.1.md
    A.6-people/<no>.md
    A.7-physical/<no>.md
    A.8-technological/<no>.md
    INDEX.md                     생성되는 목차
  en/                            영어 문서. 상대 경로가 한국어 쪽과 동일
extended/
  README.md / README.ko.md       자료집을 AI가 사용할 때의 운영 규칙
  catalog/controls.json          Annex A 공개 통제 목록(번호, 명칭, 테마)
  manifest.json                  기계가독 색인(공개 계약)
  index/                         평탄 CSV 색인, 부적합 사례 룰북, 증적 사전
tools/
  build_index.py                 docs/에서 파생 색인 전체를 재생성
  check_corpus.py                읽기 전용 무결성 검사
  test_check_corpus.py           문서 경계 및 AGENTS.md 링크 회귀 시험
harness/
  install-hooks.sh               clone에 git hook을 배선(최초 1회, 설치 절 참고)
  check-conventions.sh           문서 규약 검사기(playbook docs/16)
  test-check-conventions.sh      위 검사기의 자체 시험. CI가 먼저 실행
  check-infra-conformance.sh     infra 규약 검사기(이 저장소에는 대상이 없음)
  githooks/                      pre-commit, commit-msg, pre-push
  gitmessage                     커밋 메시지 템플릿
skill/
  iso-27001-review/              Claude Code skill: 전달받은 내용을 이 자료집으로 Annex A에 대조
    SKILL.md                     절차(routing, 읽기, 판정, 보고 형식)
    topic-index.json             일상 용어를 통제 번호로 연결하는 routing 표
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
    "counts": { "checkpoints": 6, "evidence": 6, "defects": 6, "hasLaws": false }
  }]
}
```

**절대 이름을 바꾸지 않는 고정 키**: 표준 id `iso-27001`, 테마 id `organizational` / `people` /
`physical` / `technological`, 그리고 통제 번호. 소비자가 이 값들을 키로 씁니다.

## 설치

이 저장소에는 문서만 있어서 패키지 관리자도, git hook 배선을 걸어둘 설치 단계도 없습니다.
`core.hooksPath`는 `.git/config`에 있고 이는 clone과 함께 따라오지 않는 로컬 상태이므로,
**clone마다 한 번씩** 다음을 실행하십시오.

```bash
bash harness/install-hooks.sh
```

여러 번 실행해도 안전하고, hook 파일 세 개에 실행 권한을 주는 것 말고는 `.git/config` 밖에
아무것도 쓰지 않습니다. `pre-commit`(문서 규약), `commit-msg`(커밋 메시지 규칙),
`pre-push`(master 직접 푸시 차단)를 활성화합니다. hook은 우회 가능한
편의용 안전장치이고, 정본 게이트는 같은 검사기를 돌리는 CI(`.github/workflows/docs.yml`)입니다.

나머지는 Python 3(표준 라이브러리만)와 bash만 있으면 됩니다.

## Claude Code로 작업하기

이 저장소를 Claude Code에서 열면 유일한 지침 원본인 [CLAUDE.md](CLAUDE.md)를 읽습니다.
[AGENTS.md](AGENTS.md)는 이 파일을 가리키는 심볼릭 링크라서 `AGENTS.md`를 읽는 에이전트도 같은
규칙을 받습니다. 심볼릭 링크가 아니게 되면 `tools/check_corpus.py`가 실패합니다.

검토 스킬은 사용자별로 디렉터리를 `~/.claude/skills/`에 심볼릭 링크로 연결해 설치합니다. 자료집
최상위에서 한 번 실행하십시오. 기존 설치가 있으면 덮어쓰지 않습니다.

```bash
mkdir -p "$HOME/.claude/skills"
if [ ! -e "$HOME/.claude/skills/iso-27001-review" ] && [ ! -L "$HOME/.claude/skills/iso-27001-review" ]; then
  ln -s "$PWD/skill/iso-27001-review" "$HOME/.claude/skills/iso-27001-review"
fi
```

내용을 검토하려면 `/iso-27001-review` 뒤에 본문이나 파일 경로를 붙여 실행하십시오. 인자 없이
실행하면 대화에 앞서 붙여 넣은 내용을 검토합니다. 요청이 스킬 설명과 맞으면 Claude Code가 스스로
스킬을 고르기도 합니다. 스킬은 이 심볼릭 링크로 자료집 최상위를 찾으므로 어느 프로젝트에서도
동작합니다. 이 스킬은 자료집을 읽기만 합니다. 자료집 자체의 유지보수는 별도 작업이며 `CLAUDE.md`의
규칙을 따릅니다.

## 유지보수

```bash
python3 tools/build_index.py    # extended/와 docs/{ko,en}/INDEX.md 재생성
python3 tools/check_corpus.py   # 읽기 전용 무결성 검사
python3 -B -m unittest discover -s tools -p 'test_*.py'
bash harness/test-check-conventions.sh
bash harness/check-conventions.sh
bash harness/check-infra-conformance.sh
git diff --check
```

`build_index.py`는 결정적이고 재현 가능합니다. CI가 재생성한 뒤 diff가 있으면 실패시키므로, 커밋된
색인은 항상 자료집과 일치합니다.

통제를 추가/수정/삭제할 때는 **같은 커밋에서 반대 언어 문서도 함께 고칩니다**. 대응 관계는 통제
번호로 잡힙니다. 한국어만 또는 영어만 고친 상태는 결함입니다. `tools/check_corpus.py`는 한쪽
언어에만 통제가 있거나 두 언어의 섹션 항목 수가 다르면 실패합니다. 항목 수가 같은 채로 문장만 바꾼
경우는 CI가 아니라 리뷰에서 걸러집니다.

통제를 추가하면 `extended/catalog/controls.json`에도 추가해야 합니다. 카탈로그와 문서가 어느 방향으로든
어긋나면 `check_corpus.py`가 실패합니다.

확인 날짜와 검증 범위의 한계는 [UPDATES.ko.md](UPDATES.ko.md)에 기록합니다. 적용된 playbook
검사 도구의 기준 버전은 v0.1.6이며, v0.2.0 이전은 수행하지 않았습니다.
확인한 참조본 및 상위 저장소의 커밋은 `CLAUDE.md`에 기록되어 있습니다.

## 라이선스

- 코드와 도구: MIT. [LICENSE](LICENSE) 참고.
- 자료집(원저작 설명 본문, `docs/` 편집과 구성, `extended/`의 생성 데이터, 메타 문서의 본문):
  CC BY 4.0. [LICENSE-CONTENT](LICENSE-CONTENT)와 [NOTICE](NOTICE) 참고.

위 라이선스는 본 프로젝트의 자체 저작물에만 적용됩니다. ISO/IEC 27001 표준 원문은 ISO와 IEC의 권리에
따르며 여기서 재라이선스하거나 복제하거나 번역하지 않습니다.
