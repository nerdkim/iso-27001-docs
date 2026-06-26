# extended

> English: [README.md](README.md)

AI agent가 `docs/` 자료집 전체를 다시 읽지 않고도 **사용**할 수 있게 해 주는 계층이고, 그 사용을
정직하게 유지하는 운영 규약입니다. 이 readme 한 쌍을 빼면 전부 `docs/`와 `catalog/controls.json`에서
생성됩니다.

## 구성

```
catalog/controls.json               Annex A 공개 통제 목록: 번호, 테마, 한국어/영어 명칭. 사실
                                    정보이며, 어떤 통제가 존재해야 하는지의 기준입니다.
manifest.json                       모든 문서의 기계가독 색인(schema corpus-manifest/v3). 공개
                                    계약이며 웹 뷰어를 비롯한 소비자가 읽는 파일입니다.
index/control-index.csv             스프레드시트나 사람 검토용 평탄 색인
index/nonconformity-rulebook.json   93개 통제의 한국어 부적합 사례를 통제 번호로 색인. 셀프 진단과
                                    내부 심사 준비용 점검 규칙입니다.
index/evidence-dictionary.json      93개 통제의 한국어 증적자료를 통제 번호로 색인. 증적을 통제에
                                    mapping할 때 쓰는 참고 사전입니다.
```

repository 루트에서 `python3 tools/build_index.py`로 전부 재생성합니다. 빌드는 결정적이며, commit된
산출물이 `docs/`와 어긋나면 CI가 실패합니다.

## AI 사용 운영 규약

소비자 쪽 agent가 지켜야 하는 규칙입니다. 소비 환경의 `CLAUDE.md` 또는 `AGENTS.md`에 반영하십시오.

1. **`docs/`는 읽기 전용입니다.** 자료집을 사용하는 동안 `docs/` 아래의 무엇도 만들거나 고치거나
   지우지 않습니다. 파생 산출물은 소비자 쪽 작업 공간에 쓰고, 이 repository로 되돌려 쓰지 않습니다.
2. **manifest 우선 routing.** `manifest.json`을 먼저 읽습니다. 관련 통제 번호와 `path`로 범위를 좁힌
   뒤 해당 문서만 읽습니다. `docs/` 전체에 grep을 뿌리지 않습니다.
3. **모든 주장에 출처를 답니다.** 각 진술에 `docs/` 경로와 섹션명을
   `[출처: docs/ko/A.5-organizational/A.5.1.md > 주요 확인사항]` 형태로 붙입니다. 출처를 만들 수
   없으면
   단정하지 말고, 자료집이 다루지 않는 내용이라고 밝힙니다.
4. **자료집 범위를 벗어나지 않습니다.** 이 repository의 근거는 186개 `.md` 문서, `manifest.json`,
   `index/*`, `catalog/controls.json`입니다. 모델의 일반 지식으로 통제 요구사항이나 수치, 기준값을
   단정하지 않습니다.
5. **저작권 경계를 지킵니다.** 여기 설명 본문은 원저작이며 표준 원문이 아닙니다. 이를
   ISO/IEC 27001:2022의 규범 텍스트인 것처럼 제시하지 않고, 빈틈을 표준 문구 복원으로 메우지
   않습니다.
   정본이 필요한 답이면 라이선스된 표준 원문을 확인하도록 안내합니다.
6. **사람 승인 게이트.** 인증 준비 상태 판단, 최종 적합성 판정, 보완조치 완료 판정은 agent가 아니라
   사람이 결정합니다. 결과는 검토 대상 후보로 제시합니다.

## routing 예시

"접근통제가 운영되고 있음을 무엇으로 증명하는가"라는 질문은 이렇게 풀립니다.

1. `manifest.json`에서 `name`이 접근통제와 관련된 통제를 찾습니다(A.8.2에서 A.8.5 구간과 A.5.15).
2. 그 문서들만 읽어 `증적자료`와 `부적합 사례` 섹션을 뽑습니다. 목록만 필요하면
   `index/evidence-dictionary.json`과 `index/nonconformity-rulebook.json`에서 같은 내용을 바로
   읽어도
   됩니다.
3. 항목마다 출처를 달아 답하고, 자료집이 다루지 않는 부분은 미확인으로 표시합니다.
