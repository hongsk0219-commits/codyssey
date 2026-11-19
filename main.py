import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

EPSILON = 1e-9
REPEAT_COUNT = 10


def normalize_label(raw_label: Any) -> Optional[str]:
    """입력 라벨을 표준 라벨('Cross', 'X')로 정규화한다."""
    if not isinstance(raw_label, str):
        return None
    cleaned = raw_label.strip().lower()
    if cleaned in {"+", "cross"}:
        return "Cross"
    if cleaned == "x":
        return "X"
    return None


def is_valid_nxn_matrix(matrix: Any, size: int) -> bool:
    """2차원 숫자 배열이 size x size 형태인지 검증한다."""
    if not isinstance(matrix, list) or len(matrix) != size:
        return False
    for row in matrix:
        if not isinstance(row, list) or len(row) != size:
            return False
        for val in row:
            if isinstance(val, bool) or not isinstance(val, (int, float)):
                return False
    return True


def compute_mac(pattern: List[List[float]], kernel: List[List[float]]) -> float:
    """외부 라이브러리 없이 이중 반복문으로 MAC 연산 점수를 계산한다."""
    rows = len(pattern)
    cols = len(pattern[0]) if rows > 0 else 0
    total = 0.0
    for r in range(rows):
        for c in range(cols):
            total += float(pattern[r][c]) * float(kernel[r][c])
    return total


def measure_mac_avg_ms(
    pattern: List[List[float]],
    kernel_cross: List[List[float]],
    kernel_x: List[List[float]],
    repeats: int = REPEAT_COUNT,
) -> float:
    """I/O를 제외한 순수 MAC 연산 시간을 repeats회 반복 측정해 평균(ms)을 반환한다."""
    start = time.perf_counter()
    for _ in range(repeats):
        compute_mac(pattern, kernel_cross)
        compute_mac(pattern, kernel_x)
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000.0
    return elapsed_ms / repeats


def decide_two_filters(score_a: float, score_b: float, eps: float = EPSILON) -> str:
    """사용자 입력 모드(필터 A, B) 판정."""
    if abs(score_a - score_b) < eps:
        return "판정 불가"
    return "A" if score_a > score_b else "B"


def decide_cross_vs_x(
    cross_score: float,
    x_score: float,
    eps: float = EPSILON,
) -> str:
    """표준 라벨(Cross / X / UNDECIDED) 판정."""
    if abs(cross_score - x_score) < eps:
        return "UNDECIDED"
    return "Cross" if cross_score > x_score else "X"


def prompt_nxn_matrix(title: str, size: int) -> List[List[float]]:
    """size x size 2차원 배열을 한 줄씩 공백 구분으로 입력받고 검증한다."""
    while True:
        print(f"\n{title} ({size}줄 입력, 공백 구분)")
        matrix: List[List[float]] = []
        valid = True

        for _ in range(size):
            line = input().strip()
            parts = line.split()
            if len(parts) != size:
                print(f"입력 형식 오류: 각 줄에 {size}개의 숫자를 공백으로 구분해 입력하세요.")
                valid = False
                break
            try:
                row = [float(x) for x in parts]
            except ValueError:
                print(f"입력 형식 오류: 각 줄에 {size}개의 숫자를 공백으로 구분해 입력하세요.")
                valid = False
                break
            matrix.append(row)

        if valid:
            return matrix


def create_dummy_nxn(size: int, fill_value: float = 1.0) -> List[List[float]]:
    """성능 측정용 N x N 더미 배열 생성."""
    return [[fill_value for _ in range(size)] for _ in range(size)]


def print_performance_table(
    samples: Dict[int, Tuple[List[List[float]], List[List[float]], List[List[float]]]]
) -> None:
    """크기별 평균 연산 시간(ms)과 연산 횟수(N^2) 표를 출력한다."""
    print("\n#---------------------------------------")
    print(f"# 성능 분석 (평균/{REPEAT_COUNT}회)")
    print("#---------------------------------------")
    print(f"{'크기':<10} {'평균 시간(ms)':<16} {'연산 횟수'}")
    print("-" * 42)
    for size in sorted(samples.keys()):
        pattern, kernel_cross, kernel_x = samples[size]
        avg_ms = measure_mac_avg_ms(pattern, kernel_cross, kernel_x, REPEAT_COUNT)
        ops = size * size
        print(f"{size}×{size:<7} {avg_ms:<16.6f} {ops}")


def run_mode_1() -> None:
    """모드 1: 사용자 입력 (3x3)."""
    size = 3
    print("\n#---------------------------------------")
    print("# [1] 필터 입력")
    print("#---------------------------------------")
    filter_a = prompt_nxn_matrix("필터 A", size)
    filter_b = prompt_nxn_matrix("필터 B", size)
    print("필터 A, B 저장 완료.")

    print("\n#---------------------------------------")
    print("# [2] 패턴 입력")
    print("#---------------------------------------")
    pattern = prompt_nxn_matrix("패턴", size)

    score_a = compute_mac(pattern, filter_a)
    score_b = compute_mac(pattern, filter_b)
    avg_ms = measure_mac_avg_ms(pattern, filter_a, filter_b, REPEAT_COUNT)
    decision = decide_two_filters(score_a, score_b, EPSILON)

    print("\n#---------------------------------------")
    print("# [3] MAC 결과")
    print("#---------------------------------------")
    print(f"A 점수: {score_a}")
    print(f"B 점수: {score_b}")
    print(f"연산 시간(평균/{REPEAT_COUNT}회): {avg_ms:.6f} ms")
    print(f"판정: {decision}")

    print_performance_table({3: (pattern, filter_a, filter_b)})


def parse_size_from_pattern_key(key: str) -> Optional[int]:
    """'size_{N}_{idx}' 형태 키에서 N을 추출한다."""
    parts = key.split("_")
    if len(parts) < 3 or parts[0] != "size":
        return None
    try:
        n = int(parts[1])
        return n if n > 0 else None
    except ValueError:
        return None


def run_mode_2(json_path: str = "data.json") -> None:
    """모드 2: data.json 분석."""
    path = Path(json_path)
    if not path.exists():
        print(f"오류: '{json_path}' 파일을 찾을 수 없습니다.")
        return

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    raw_filters = data.get("filters", {})
    raw_patterns = data.get("patterns", {})

    print("\n#---------------------------------------")
    print("# [1] 필터 로드")
    print("#---------------------------------------")
    loaded_filters: Dict[int, Dict[str, List[List[float]]]] = {}
    perf_samples: Dict[int, Tuple[List[List[float]], List[List[float]], List[List[float]]]] = {
        3: (create_dummy_nxn(3, 1.0), create_dummy_nxn(3, 1.0), create_dummy_nxn(3, 0.0))
    }

    for size in (5, 13, 25):
        size_key = f"size_{size}"
        f_group = raw_filters.get(size_key)
        if not isinstance(f_group, dict):
            print(f"! {size_key} 필터 그룹 누락 또는 형식 오류")
            continue

        norm_group: Dict[str, List[List[float]]] = {}
        for k, mat in f_group.items():
            norm_k = normalize_label(k)
            if norm_k in {"Cross", "X"} and is_valid_nxn_matrix(mat, size):
                norm_group[norm_k] = mat

        if "Cross" in norm_group and "X" in norm_group:
            loaded_filters[size] = norm_group
            perf_samples[size] = (norm_group["Cross"], norm_group["Cross"], norm_group["X"])
            print(f"✓ {size_key:<7} 필터 로드 완료 (Cross, X)")
        else:
            print(f"! {size_key:<7} 필터 로드 불완전 (Cross/X 확인 필요)")

    print("\n#---------------------------------------")
    print("# [2] 패턴 분석 (라벨 정규화 적용)")
    print("#---------------------------------------")
    total_tests = 0
    passed_tests = 0
    failures: List[Tuple[str, str]] = []

    for key, item in raw_patterns.items():
        total_tests += 1
        print(f"\n-- {key} ---")

        n = parse_size_from_pattern_key(key)
        if n is None:
            reason = "키 형식 오류(size_{N}_{idx} 형태가 아님)"
            print(f"판정: UNDECIDED | expected: UNKNOWN | FAIL ({reason})")
            failures.append((key, reason))
            continue

        if not isinstance(item, dict):
            reason = "패턴 항목 스키마 오류(dict가 아님)"
            print(f"판정: UNDECIDED | expected: UNKNOWN | FAIL ({reason})")
            failures.append((key, reason))
            continue

        expected_norm = normalize_label(item.get("expected"))
        expected_display = expected_norm if expected_norm else str(item.get("expected"))
        pattern_mat = item.get("input")

        if n not in loaded_filters:
            reason = f"size_{n} 필터 미로드"
            print(f"판정: UNDECIDED | expected: {expected_display} | FAIL ({reason})")
            failures.append((key, reason))
            continue

        if not is_valid_nxn_matrix(pattern_mat, n):
            reason = f"패턴 크기 불일치({n}x{n} 요구)"
            print(f"판정: UNDECIDED | expected: {expected_display} | FAIL ({reason})")
            failures.append((key, reason))
            continue

        cross_filter = loaded_filters[n]["Cross"]
        x_filter = loaded_filters[n]["X"]

        cross_score = compute_mac(pattern_mat, cross_filter)
        x_score = compute_mac(pattern_mat, x_filter)
        decision = decide_cross_vs_x(cross_score, x_score, EPSILON)

        print(f"Cross 점수: {cross_score}")
        print(f"X 점수: {x_score}")

        if expected_norm is None:
            reason = f"유효하지 않은 expected 값({item.get('expected')})"
            print(f"판정: {decision} | expected: {expected_display} | FAIL ({reason})")
            failures.append((key, reason))
            continue

        if decision == "UNDECIDED":
            reason = f"동점(|Cross-X| < {EPSILON})"
            print(f"판정: {decision} | expected: {expected_display} | FAIL ({reason})")
            failures.append((key, reason))
        elif decision == expected_norm:
            passed_tests += 1
            print(f"판정: {decision} | expected: {expected_display} | PASS")
        else:
            reason = f"판정({decision}) != expected({expected_norm})"
            print(f"판정: {decision} | expected: {expected_display} | FAIL ({reason})")
            failures.append((key, reason))

    print_performance_table(perf_samples)

    print("\n#---------------------------------------")
    print("# [4] 결과 요약")
    print("#---------------------------------------")
    failed_tests = total_tests - passed_tests
    print(f"총 테스트: {total_tests}개")
    print(f"통과: {passed_tests}개")
    print(f"실패: {failed_tests}개")

    if failures:
        print("\n실패 케이스:")
        for case_id, reason in failures:
            print(f"- {case_id}: {reason}")


def main() -> None:
    while True:
        print("\n=== Mini NPU Simulator ===")
        print("\n[모드 선택]")
        print("1. 사용자 입력 (3x3)")
        print("2. data.json 분석")
        choice = input("선택: ").strip()

        if choice == "1":
            run_mode_1()
            break
        elif choice == "2":
            run_mode_2("data.json")
            break
        else:
            print("잘못된 선택입니다. 1 또는 2를 입력하세요.")


if __name__ == "__main__":
    main()