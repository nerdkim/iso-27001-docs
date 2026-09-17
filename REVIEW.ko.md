# 본문 전수 검토: 2026-09-17

> English: [REVIEW.md](REVIEW.md)

**93개 통제의 한영 문서 186개**를 모두 읽고 대조했습니다. **73개 통제, 146개 문서**를
수정했으며, 나머지 **20개 통제**에서는 이번 검토에서 실질적인 수정 사항을 발견하지 않았습니다.
이 수치는 통제 단위이며 개별 결함의 개수를 의미하지 않습니다.

## 1. 범위와 방법

모든 통제의 메타데이터와 6개 섹션을 대상으로 한영 의미, 기술적 정확성, 근거 없는 일괄 의무화,
문서 내부의 일관성, 보호조치와 증적/부적합 사례의 연결을 검토했습니다. 관련 통제 참조를 확인하고
출처/한계 고지를 유지했습니다. 자동 검사 통과로 본문 검토를 대신하지 않고, 전체 본문을 직접 읽은 뒤
한영 수정과 자동 검증을 수행했습니다.

주요 수정 분야는 인증정보, 삭제와 보존, 사고 보고, BYOD와 퇴직 처리, 물리적 안전, 복구 능력,
시험 데이터 및 배포 판단입니다. 특정 구현 하나를 보편적인 의무로 다루던 부분에는 적절한 대안과
책임 있는 예외 기준을 명시했습니다. 예외 승인이 적용 법규나 다른 구속력 있는 의무를 무효로 하지는
않습니다. 기존 Codex 설정과 검사 도구 수정은 유지했습니다.

라이선스된 ISO 원문을 이용한 정본 대조는 수행하지 않았습니다. 본문 조항, 공식 통제 속성,
2013 대응의 동등성과 ISMS-P 대응표의 충분성을 독립적으로 인증한 작업도 아닙니다. 대응표는
참고 자료이며, 수정 사항 미발견은 완전성이나 인증 적합성을 보장하지 않습니다. 설명은 계속해서
이 프로젝트의 원저작 자료로 관리합니다.

## 2. 검토 범위와 처리 결과

| 테마 | 검토 통제 | 수정 통제 | 실질적 수정 사항 미발견 |
|---|---|---|---|
| A.5 조직적 | 37 | 22 | 15 |
| A.6 인적 | 8 | 6 | 2 |
| A.7 물리적 | 14 | 14 | 0 |
| A.8 기술적 | 34 | 31 | 3 |
| 합계 | 93 | 73 | 20 |

| 통제 | 결과 | 수정 주제 |
|---|---|---|
| [A.5.1](docs/ko/A.5-organizational/A.5.1.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.2](docs/ko/A.5-organizational/A.5.2.md) | 한영 수정 | 조직에 맞는 책임자와 법정 직위 적용 조건 |
| [A.5.3](docs/ko/A.5-organizational/A.5.3.md) | 한영 수정 | 개발/운영 겸직 시 보완통제 |
| [A.5.4](docs/ko/A.5-organizational/A.5.4.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.5](docs/ko/A.5-organizational/A.5.5.md) | 한영 수정 | 내부 심각도/승인과 법정 보고 요건 구분 |
| [A.5.6](docs/ko/A.5-organizational/A.5.6.md) | 한영 수정 | 승인된 취약점 조정 공개 |
| [A.5.7](docs/ko/A.5-organizational/A.5.7.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.8](docs/ko/A.5-organizational/A.5.8.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.9](docs/ko/A.5-organizational/A.5.9.md) | 한영 수정 | 반환/폐기 상태와 자산 이력 보존 |
| [A.5.10](docs/ko/A.5-organizational/A.5.10.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.11](docs/ko/A.5-organizational/A.5.11.md) | 한영 수정 | 자산 반환과 독립적인 접근 회수, BYOD 삭제 범위 |
| [A.5.12](docs/ko/A.5-organizational/A.5.12.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.13](docs/ko/A.5-organizational/A.5.13.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.14](docs/ko/A.5-organizational/A.5.14.md) | 한영 수정 | 프로토콜별 암호화, 종이 운송, 발송 회수 한계 |
| [A.5.15](docs/ko/A.5-organizational/A.5.15.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.16](docs/ko/A.5-organizational/A.5.16.md) | 한영 수정 | 계정과 주체 연결, 비밀정보 참조, 서비스 의존성 |
| [A.5.17](docs/ko/A.5-organizational/A.5.17.md) | 한영 수정 | 비밀번호 정책, 전용 해시, 비밀정보 유형 구분 |
| [A.5.18](docs/ko/A.5-organizational/A.5.18.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.19](docs/ko/A.5-organizational/A.5.19.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.20](docs/ko/A.5-organizational/A.5.20.md) | 한영 수정 | SOC 2 보고서 구분과 적용 통지 기한 |
| [A.5.21](docs/ko/A.5-organizational/A.5.21.md) | 한영 수정 | 서명/해시 기준값의 신뢰할 수 있는 출처 |
| [A.5.22](docs/ko/A.5-organizational/A.5.22.md) | 한영 수정 | 공급자 보고서 범위/기간/예외와 고객 책임 |
| [A.5.23](docs/ko/A.5-organizational/A.5.23.md) | 한영 수정 | 비공개 정보 노출과 승인된 공개 구분 |
| [A.5.24](docs/ko/A.5-organizational/A.5.24.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.25](docs/ko/A.5-organizational/A.5.25.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.26](docs/ko/A.5-organizational/A.5.26.md) | 한영 수정 | 사고 대응과 병행하는 통지/보고 |
| [A.5.27](docs/ko/A.5-organizational/A.5.27.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.28](docs/ko/A.5-organizational/A.5.28.md) | 한영 수정 | 증거 취득 한계, 무결성 기준과 원본 시계 보존 |
| [A.5.29](docs/ko/A.5-organizational/A.5.29.md) | 한영 수정 | 승인된 비상 보안 기준과 보완통제 |
| [A.5.30](docs/ko/A.5-organizational/A.5.30.md) | 한영 수정 | 실측 복구 시험과 도상훈련의 검증 범위 |
| [A.5.31](docs/ko/A.5-organizational/A.5.31.md) | 한영 수정 | 계약 종료 후 존속 의무 추적 |
| [A.5.32](docs/ko/A.5-organizational/A.5.32.md) | 한영 수정 | 라이선스 측정 단위와 조건별 오픈소스 의무 |
| [A.5.33](docs/ko/A.5-organizational/A.5.33.md) | 한영 수정 | 법적 보존, 백업 보존 및 복원 후 재삭제 |
| [A.5.34](docs/ko/A.5-organizational/A.5.34.md) | 한영 수정 | 적법한 처리 근거, 권리 행사 확인과 보존 예외 |
| [A.5.35](docs/ko/A.5-organizational/A.5.35.md) | 한영 수정 | 위험과 적용 의무에 따른 독립 검토 주기 |
| [A.5.36](docs/ko/A.5-organizational/A.5.36.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.5.37](docs/ko/A.5-organizational/A.5.37.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.6.1](docs/ko/A.6-people/A.6.1.md) | 한영 수정 | 채용 심사의 적법한 근거와 비례적인 재심사 |
| [A.6.2](docs/ko/A.6-people/A.6.2.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.6.3](docs/ko/A.6-people/A.6.3.md) | 한영 수정 | 근거 없는 사고 원인 순위 표현 제거 |
| [A.6.4](docs/ko/A.6-people/A.6.4.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.6.5](docs/ko/A.6-people/A.6.5.md) | 한영 수정 | 퇴직 확인 서명 불가 시 통지 증빙 |
| [A.6.6](docs/ko/A.6-people/A.6.6.md) | 한영 수정 | 적법한 공개 예외와 처리 근거/서약 구분 |
| [A.6.7](docs/ko/A.6-people/A.6.7.md) | 한영 수정 | 원격 접근 대안, 삭제 범위와 계속 필요한 권한 |
| [A.6.8](docs/ko/A.6-people/A.6.8.md) | 한영 수정 | 안전한 신고와 기밀성을 고려한 피드백 |
| [A.7.1](docs/ko/A.7-physical/A.7.1.md) | 한영 수정 | 방문자 통제 대안과 안전한 비상 대피 |
| [A.7.2](docs/ko/A.7-physical/A.7.2.md) | 한영 수정 | 출입권한과 장비 구분, 기계식 열쇠 분실 대응 |
| [A.7.3](docs/ko/A.7-physical/A.7.3.md) | 한영 수정 | 필수 안전 표지와 과도한 시설 정보 공개 구분 |
| [A.7.4](docs/ko/A.7-physical/A.7.4.md) | 한영 수정 | 위험에 맞는 감시와 적법한 영상 보존 |
| [A.7.5](docs/ko/A.7-physical/A.7.5.md) | 한영 수정 | 전문가의 소화설비 설계와 인명 보호 |
| [A.7.6](docs/ko/A.7-physical/A.7.6.md) | 한영 수정 | 보안/작업 안전에 비례하는 단독 작업 제한 |
| [A.7.7](docs/ko/A.7-physical/A.7.7.md) | 한영 수정 | 실제 화면 잠금과 재개 인증 |
| [A.7.8](docs/ko/A.7-physical/A.7.8.md) | 한영 수정 | 인증 출력 또는 통제된 즉시 회수 |
| [A.7.9](docs/ko/A.7-physical/A.7.9.md) | 한영 수정 | 원격 삭제 한계와 수리/폐기별 보호 |
| [A.7.10](docs/ko/A.7-physical/A.7.10.md) | 한영 수정 | 매체별 삭제 검증과 암호학적 삭제 조건 |
| [A.7.11](docs/ko/A.7-physical/A.7.11.md) | 한영 수정 | ATS 한계와 UPS/발전기 전원 경로 시험 |
| [A.7.12](docs/ko/A.7-physical/A.7.12.md) | 한영 수정 | 광케이블/차폐와 인증/암호화 구분 |
| [A.7.13](docs/ko/A.7-physical/A.7.13.md) | 한영 수정 | 복구용 백업과 유출 방지 구분 |
| [A.7.14](docs/ko/A.7-physical/A.7.14.md) | 한영 수정 | 삭제/파기 검증과 유효한 소프트웨어 사용권 |
| [A.8.1](docs/ko/A.8-technological/A.8.1.md) | 한영 수정 | 기기 소지와 접근 가능성 구분, 승인된 원격 삭제 |
| [A.8.2](docs/ko/A.8-technological/A.8.2.md) | 한영 수정 | 기본 비밀정보와 유형별 교체 |
| [A.8.3](docs/ko/A.8-technological/A.8.3.md) | 한영 수정 | 워터마크와 권한 검증/복사 방지 구분 |
| [A.8.4](docs/ko/A.8-technological/A.8.4.md) | 한영 수정 | 공개/실행용 소스, 저장소 보호와 SSO/MFA 구분 |
| [A.8.5](docs/ko/A.8-technological/A.8.5.md) | 한영 수정 | 유형별 자격증명 보호, 표시 선택과 피싱 저항성 |
| [A.8.6](docs/ko/A.8-technological/A.8.6.md) | 한영 수정 | 서비스에 맞는 경보와 자원 확장 선택 |
| [A.8.7](docs/ko/A.8-technological/A.8.7.md) | 한영 수정 | 플랫폼이 지원하는 악성코드 보호와 검증된 대안 |
| [A.8.8](docs/ko/A.8-technological/A.8.8.md) | 한영 수정 | 실제 악용을 반영한 우선순위와 승인된 점검 |
| [A.8.9](docs/ko/A.8-technological/A.8.9.md) | 한영 수정 | 구성 차이 조사 후 복원 또는 기준 승인 |
| [A.8.10](docs/ko/A.8-technological/A.8.10.md) | 한영 수정 | 기록/매체 삭제 구분, 클라우드 한계와 보존/만료 |
| [A.8.11](docs/ko/A.8-technological/A.8.11.md) | 한영 수정 | 재식별 위험, 마스킹 한계와 키/매핑 분리 |
| [A.8.12](docs/ko/A.8-technological/A.8.12.md) | 한영 수정 | 위험과 대응에 근거한 탐지 모드 운영 |
| [A.8.13](docs/ko/A.8-technological/A.8.13.md) | 한영 수정 | 랜섬웨어 격리와 복호화 키 복구 시험 |
| [A.8.14](docs/ko/A.8-technological/A.8.14.md) | 한영 수정 | RAID 수준, 복제/백업 구분과 안전한 장애 시험 |
| [A.8.15](docs/ko/A.8-technological/A.8.15.md) | 한영 수정 | 로그 비밀정보 제외와 무결성 기준값 보호 |
| [A.8.16](docs/ko/A.8-technological/A.8.16.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.8.17](docs/ko/A.8-technological/A.8.17.md) | 한영 수정 | 공통 시간 기준, 호스트 시계와 원본 시각 보존 |
| [A.8.18](docs/ko/A.8-technological/A.8.18.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.8.19](docs/ko/A.8-technological/A.8.19.md) | 한영 수정 | 신뢰할 수 있는 패키지 검증과 데이터 호환 복구 |
| [A.8.20](docs/ko/A.8-technological/A.8.20.md) | 한영 수정 | 기본 비밀정보와 연결 유형에 맞는 인증 |
| [A.8.21](docs/ko/A.8-technological/A.8.21.md) | 수정 사항 미발견 | 검토 후 유지 |
| [A.8.22](docs/ko/A.8-technological/A.8.22.md) | 한영 수정 | 특정 망 구성 대신 실제 논리적 경계 확인 |
| [A.8.23](docs/ko/A.8-technological/A.8.23.md) | 한영 수정 | DNS/URL 기능 구분과 조건부 HTTPS 검사 |
| [A.8.24](docs/ko/A.8-technological/A.8.24.md) | 한영 수정 | 키 사용 철회와 파기 구분, 자료 복구와 키 용도 |
| [A.8.25](docs/ko/A.8-technological/A.8.25.md) | 한영 수정 | 위험에 따른 배포 기준과 만료되는 예외 |
| [A.8.26](docs/ko/A.8-technological/A.8.26.md) | 한영 수정 | 거래별 행위 증명 요건과 타임스탬프 한계 |
| [A.8.27](docs/ko/A.8-technological/A.8.27.md) | 한영 수정 | 제로트러스트 구체화와 보안/안전을 고려한 장애 동작 |
| [A.8.28](docs/ko/A.8-technological/A.8.28.md) | 한영 수정 | CVE 적용 여부와 책임 있는 조치 결정 |
| [A.8.29](docs/ko/A.8-technological/A.8.29.md) | 한영 수정 | 통제된 시험 데이터와 배포 예외 |
| [A.8.30](docs/ko/A.8-technological/A.8.30.md) | 한영 수정 | 인수 기준, 실제 접근 회수와 보존 기록 |
| [A.8.31](docs/ko/A.8-technological/A.8.31.md) | 한영 수정 | 실효성 있는 환경 분리, 실행용 소스와 운영 접근 근거 |
| [A.8.32](docs/ko/A.8-technological/A.8.32.md) | 한영 수정 | 데이터/스키마 복구와 긴급 변경 권한 |
| [A.8.33](docs/ko/A.8-technological/A.8.33.md) | 한영 수정 | 가명/합성 데이터 한계와 정당한 보존 |
| [A.8.34](docs/ko/A.8-technological/A.8.34.md) | 한영 수정 | 승인된 운영 변경 시험과 증거 보존 |

## 3. 사실 확인에 사용한 1차 자료

확인일은 2026-09-17입니다. 아래 자료는 해당 기술적 구분을 확인하는 근거이며, ISO 규범 문구의
출처나 이들 기관의 권고를 ISO 의무로 바꾸는 근거가 아닙니다. ICO와 OSHA 자료는 특정 관할의
조건을 보여주므로 실제 조직에 대한 적용 여부를 별도로 판단해야 합니다. 전체 편집 판단의 주제는
2절에 기록했습니다.

| 통제 | 사실 확인 주제 | 출처 |
|---|---|---|
| A.5.17, A.8.2, A.8.5 | 비밀번호 검증과 인증 | [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/) |
| A.7.10, A.7.14, A.8.10 | 매체 및 암호학적 삭제 한계 | [NIST SP 800-88 Rev. 2](https://csrc.nist.gov/pubs/sp/800/88/r2/final) |
| A.8.24 | 키 생명주기와 유출된 키 | [NIST SP 800-57 Part 1 Rev. 5, section 7.5](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-57pt1r5.pdf) |
| A.5.20, A.5.22 | SOC 보증 보고서 | [AICPA SOC services](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services) |
| A.5.14 | SSH를 사용하는 SFTP | [OpenSSH features](https://www.openssh.org/features.html) |
| A.5.33, A.5.34, A.8.10, A.8.33 | 삭제 예외와 백업 처리 | [ICO right to erasure](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/right-to-erasure/) |
| A.5.34, A.6.1, A.6.6 | 동의와 적법한 처리 근거 | [ICO consent guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/consent/when-is-consent-appropriate/) |
| A.8.11, A.8.29, A.8.31, A.8.33 | 가명화와 잔존 식별 위험 | [ICO pseudonymisation guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/pseudonymisation/) |
| A.7.11 | 전원 전환과 중단 가능성 | [Eaton ATS fundamentals](https://www.eaton.com/us/en-us/products/low-voltage-power-distribution-control-systems/automatic-transfer-switches/automatic-transfer-switch-fundamentals.html/) |
| A.7.1, A.7.3 | 비상 대피와 안전 표지 | [OSHA exit-route guidance](https://www.osha.gov/etools/evacuation-plans-procedures/emergency-standards/design-construction) |
| A.8.13, A.8.14 | 백업 격리와 복구 | [NCSC ransomware-resistant backups](https://www.ncsc.gov.uk/collection/ransomware-resistant-backups/principles-for-ransomware-resistant-on-premises-backups) |
| A.8.17 | Linux 컨테이너 시계 동작 | [Linux time_namespaces(7)](https://man7.org/linux/man-pages/man7/time_namespaces.7.html) |
| A.8.23 | TLS 검사 고려사항과 대안 | [NCSC ZTNA preparation](https://www.ncsc.gov.uk/collection/zero-trust/zero-trust-network-access-ztna/what-to-do-before-building-a-ztna-architecture) |
| A.8.27 | 제로트러스트와 암묵적 신뢰 | [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) |

## 4. 검증과 검토 시점 기록

186개 문서의 무결성 검사, Python 회귀 시험 9개, 문서 규약 검사기 시험 26개, 저장소 문서 규약 및
인프라 검사를 통과했습니다(인프라 파일 없음). 파생 색인을 재생성했으며 스키마와 항목 수는 유지됩니다.
언어별 통제 93개, 부적합 사례 540개, 증적 예시 556개입니다. 생성 결과의 재현성, 로컬 문서 링크와
공백 검사도 확인했습니다.

검토를 마친 통제 문서 묶음의 SHA-256은 `7b24f77d6d7a5872725fd9ed43734bcb7e90a85dce3e135fd4f612fc3e281fe3`입니다.
186개 통제 Markdown 파일의 `경로<TAB>파일-sha256<LF>` 기록을 정렬하여 UTF-8로 연결한
결과에 대한 해시입니다. 이 값은 검토한 파일을 식별하며 의미의 정확성을 증명하지는 않습니다.

요청한 본문 전수 검토는 이 기록으로 완료합니다. 별도의 playbook v0.2.0 이전은 저장소 소유자의
결정으로 현재 작업에서 제외했으며 [UPDATES.ko.md](UPDATES.ko.md)에 기록했습니다. 게시 이력은
Git과 master 반영 PR에서 확인합니다.
