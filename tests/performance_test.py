from pathlib import Path
import subprocess
import sys
import time


CITY_COUNT = 200_000
ROAD_COUNT = 200_000


def build_input():
    """Cria uma cadeia conectada e adiciona uma estrada repetida válida."""
    data = bytearray(f"{CITY_COUNT} {ROAD_COUNT}\n".encode())

    for city in range(1, CITY_COUNT):
        data.extend(f"{city} {city + 1}\n".encode())

    # A cadeia usa N-1 estradas; esta repetição completa o total solicitado.
    data.extend(b"1 2\n")
    return bytes(data)


def main():
    project_root = Path(__file__).resolve().parents[1]
    solution_path = project_root / "src" / "main.py"
    input_data = build_input()

    start_time = time.perf_counter()
    result = subprocess.run(
        [sys.executable, str(solution_path)],
        input=input_data,
        capture_output=True,
        check=False,
    )
    elapsed = time.perf_counter() - start_time

    passed = result.returncode == 0 and result.stdout.strip() == b"0"
    print(f"Tempo de execução: {elapsed:.3f} segundos")
    print(f"Teste: {'APROVADO' if passed else 'REPROVADO'}")

    if not passed:
        if result.returncode != 0:
            print(f"Processo terminou com código {result.returncode}.")
        if result.stdout.strip() != b"0":
            print(f"Saída recebida: {result.stdout.decode(errors='replace').strip()!r}")
        if result.stderr:
            print(result.stderr.decode(errors="replace").strip())
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
