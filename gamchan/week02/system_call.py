import subprocess


# macOS/Linux: clear 후 실행할 것
# cwd의 파일, 디렉토리 리스트 출력
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

print("stdout:", result.stdout)
print("stderr:", result.stderr)

# google.com 핑 테스트
proc = subprocess.Popen(['ping', '-c 4', 'google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = proc.communicate()

print("stdout:", stdout.decode())
print("stderr:", stderr.decode())