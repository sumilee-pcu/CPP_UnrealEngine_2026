# Pangaea UE 5.7.4 C++ 실습 프로젝트

이 저장소는 Unreal Engine 5.7.4에서 C++ 게임 프로젝트를 실습하기 위한 배포용 프로젝트입니다. 학생은 이 저장소를 내려받은 뒤 Visual Studio 프로젝트 파일을 생성하고, `PangaeaEditor`를 빌드한 다음 Unreal Editor에서 열어 실습을 진행합니다.

저장소 주소:

```text
https://github.com/sumilee-pcu/CPP_UnrealEngine_2026
```

## 1. 실습 환경

권장 환경은 다음과 같습니다.

- OS: Windows 10 또는 Windows 11
- Unreal Engine: 5.7.4
- IDE: Visual Studio 2022
- Git: Git for Windows
- 프로젝트 경로: 영문 경로 권장

예시 경로:

```text
F:\gameEngineering\Pangaea573
```

한글, 공백, 특수문자가 많은 경로에서는 Unreal Build Tool이나 Visual Studio 생성 과정에서 문제가 생길 수 있습니다. 수업 실습에서는 가능하면 `C:\UnrealProjects\Pangaea573` 또는 `F:\gameEngineering\Pangaea573`처럼 단순한 영문 경로를 사용하세요.

## 2. Unreal Engine 설치

이 프로젝트는 Unreal Engine 5.7.4 기준으로 검증되었습니다.

1. Epic Games Launcher를 실행합니다.
2. `Unreal Engine` 탭으로 이동합니다.
3. `Library`에서 Unreal Engine 5.7.4를 설치합니다.
4. 설치가 끝난 뒤 한 번 실행해서 정상적으로 열리는지 확인합니다.

프로젝트 파일인 `Pangaea.uproject`에는 다음 엔진 버전이 지정되어 있습니다.

```json
"EngineAssociation": "5.7"
```

Unreal Engine 5.7.x 계열에서 열리도록 구성되어 있지만, 수업에서는 반드시 5.7.4 사용을 권장합니다.

## 3. Visual Studio 2022 설치

Visual Studio Installer에서 다음 워크로드를 설치하세요.

- Desktop development with C++
- Game development with C++
- .NET desktop development

추가 구성 요소:

- MSVC v143 C++ build tools
- Windows 10 또는 Windows 11 SDK
- Unreal Engine installer / Unreal Engine IDE support 관련 구성 요소

이 저장소에는 `.vsconfig` 파일이 포함되어 있습니다. Visual Studio Installer에서 이 파일을 가져오면 필요한 구성 요소를 자동으로 선택하는 데 도움이 됩니다.

## 4. 프로젝트 다운로드

두 가지 방법 중 하나를 선택합니다.

### 방법 A: Git으로 받기

PowerShell 또는 Git Bash를 열고 원하는 작업 폴더로 이동합니다.

```powershell
cd F:\gameEngineering
git clone https://github.com/sumilee-pcu/CPP_UnrealEngine_2026.git Pangaea573
cd Pangaea573
```

### 방법 B: ZIP으로 받기

1. GitHub 저장소에 접속합니다.
2. `Code` 버튼을 누릅니다.
3. `Download ZIP`을 선택합니다.
4. ZIP 파일을 압축 해제합니다.
5. 압축 해제한 폴더명을 `Pangaea573`처럼 단순한 영문 이름으로 바꿉니다.

ZIP으로 받은 경우 Git 명령은 사용할 수 없지만, Unreal 프로젝트 실습은 가능합니다.

## 5. 폴더 구성

중요 폴더는 다음과 같습니다.

```text
Pangaea573
├─ Config
├─ Content
├─ Docs
├─ ImportAssets
├─ Scripts
├─ Source
├─ Pangaea.uproject
└─ README.md
```

각 폴더의 역할:

- `Config`: Unreal 프로젝트 설정 파일
- `Content`: Blueprint, Mesh, Texture, UI 등 Unreal 에셋
- `ImportAssets`: 원본 FBX, TGA, PNG 등 재임포트용 원본 파일
- `Scripts`: 프로젝트 파일 생성, 빌드, 에셋 설정용 PowerShell/Python 스크립트
- `Source`: C++ 소스 코드
- `Pangaea.uproject`: Unreal 프로젝트 파일

다음 폴더는 자동 생성 산출물이므로 Git에 포함하지 않습니다.

- `Binaries`
- `Intermediate`
- `Saved`
- `DerivedDataCache`
- `.vs`

## 6. Visual Studio 프로젝트 파일 생성

처음 프로젝트를 받은 뒤에는 Visual Studio 솔루션 파일을 생성해야 합니다.

### 방법 A: 마우스 우클릭

1. `Pangaea.uproject` 파일을 찾습니다.
2. 파일을 우클릭합니다.
3. `Generate Visual Studio project files`를 선택합니다.
4. 생성이 끝나면 `Pangaea.sln` 파일이 생깁니다.

### 방법 B: 스크립트 실행

PowerShell을 프로젝트 폴더에서 실행합니다.

```powershell
cd F:\gameEngineering\Pangaea573
.\Scripts\GenerateProjectFiles.ps1
```

Unreal Engine 설치 경로가 기본값과 다르면 `-UnrealRoot` 옵션을 사용합니다.

```powershell
.\Scripts\GenerateProjectFiles.ps1 -UnrealRoot "C:\Program Files\Epic Games\UE_5.7"
```

수업 PC처럼 Unreal Engine이 `F:\gameEngineering\UE_5.7`에 설치되어 있다면 옵션 없이 실행해도 됩니다.

## 7. C++ 프로젝트 빌드

### 방법 A: Visual Studio에서 빌드

1. `Pangaea.sln`을 엽니다.
2. 상단 빌드 구성을 다음처럼 설정합니다.
   - Configuration: `Development Editor`
   - Platform: `Win64`
3. Solution Explorer에서 `Pangaea` 또는 솔루션을 우클릭합니다.
4. `Build`를 실행합니다.

빌드가 성공하면 Unreal Editor에서 프로젝트를 열 수 있습니다.

### 방법 B: 스크립트로 빌드

PowerShell에서 다음 명령을 실행합니다.

```powershell
cd F:\gameEngineering\Pangaea573
.\Scripts\BuildEditor.ps1
```

엔진 경로가 다르면 다음처럼 실행합니다.

```powershell
.\Scripts\BuildEditor.ps1 -UnrealRoot "C:\Program Files\Epic Games\UE_5.7"
```

빌드가 성공하면 `Binaries`와 `Intermediate` 폴더가 생성됩니다. 이 폴더들은 자동 생성물이므로 Git에 올리지 않습니다.

## 8. Unreal Editor에서 프로젝트 열기

1. `Pangaea.uproject`를 더블클릭합니다.
2. 모듈을 다시 빌드하겠다는 메시지가 나오면 `Yes`를 선택합니다.
3. Unreal Editor가 열릴 때까지 기다립니다.
4. Content Browser에서 `/Game/Pangaea` 폴더를 확인합니다.

프로젝트가 열리지 않고 C++ 빌드 오류가 나오면 Visual Studio에서 `PangaeaEditor`를 먼저 빌드한 뒤 다시 여세요.

## 9. 에셋 설정 스크립트 실행

이 저장소에는 이미 수업용 에셋이 포함되어 있습니다. 일반적으로 별도 작업 없이 바로 열 수 있습니다.

다만 에셋을 다시 생성하거나 원본 파일에서 재구성해야 하는 경우 다음 스크립트를 사용할 수 있습니다.

```powershell
cd F:\gameEngineering\Pangaea573
.\Scripts\RunAssetSetup.ps1
```

엔진 경로가 다르면 다음처럼 실행합니다.

```powershell
.\Scripts\RunAssetSetup.ps1 -UnrealRoot "C:\Program Files\Epic Games\UE_5.7"
```

주의:

- Unreal Editor가 이미 열려 있으면 먼저 닫고 실행하세요.
- 스크립트는 `ImportAssets/PangaeaAssets`의 FBX, TGA, PNG 파일을 기준으로 Content 에셋을 구성합니다.
- 기존 에셋이 있으면 중복 import를 피하도록 구성되어 있습니다.

## 10. 실습 시작 위치

주요 C++ 클래스는 `Source/Pangaea` 폴더에 있습니다.

- `PangaeaCharacter`: 캐릭터 기본 동작과 체력 처리
- `PlayerAvatar`: 플레이어 캐릭터
- `Enemy`: 적 캐릭터
- `DefenseTower`: 방어 타워
- `Projectile`: 투사체
- `Weapon`: 무기
- `PangaeaGameMode`: 게임 모드
- `PangaeaGameState`: 게임 상태
- `HealthBarWidget`: 체력바 UI

주요 Blueprint 에셋은 다음 위치에 있습니다.

```text
Content/Pangaea/Blueprints
Content/Pangaea/UI
Content/Pangaea/Meshes
Content/Pangaea/Textures
Content/Pangaea/Animations
```

## 11. 정상 동작 확인 방법

배포 전 검증 기준은 다음과 같습니다.

```powershell
.\Scripts\GenerateProjectFiles.ps1
.\Scripts\BuildEditor.ps1
```

추가로 Blueprint 컴파일 검증을 할 수 있습니다.

```powershell
& "F:\gameEngineering\UE_5.7\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" `
  "F:\gameEngineering\Pangaea573\Pangaea.uproject" `
  -run=CompileAllBlueprints `
  -ProjectOnly `
  -Unattended `
  -NullRHI `
  -NoSound `
  -NoSplash
```

정상 결과 예시는 다음과 같습니다.

```text
Compiling Completed with 0 errors and 0 warnings and 0 blueprints that failed to load.
Success - 0 error(s), 0 warning(s)
```

## 12. 자주 발생하는 문제

### Pangaea.sln 파일이 없습니다

Visual Studio 프로젝트 파일을 아직 생성하지 않은 상태입니다.

해결:

```powershell
.\Scripts\GenerateProjectFiles.ps1
```

또는 `Pangaea.uproject`를 우클릭해서 `Generate Visual Studio project files`를 실행하세요.

### 프로젝트를 열 때 모듈을 빌드할 수 없다고 나옵니다

C++ 프로젝트 빌드가 필요합니다.

해결:

```powershell
.\Scripts\BuildEditor.ps1
```

또는 Visual Studio에서 `Development Editor | Win64`로 빌드하세요.

### Unreal Engine 버전이 다르다고 나옵니다

이 프로젝트는 Unreal Engine 5.7.4 기준입니다.

해결:

1. Unreal Engine 5.7.4를 설치합니다.
2. `Pangaea.uproject`를 우클릭합니다.
3. `Switch Unreal Engine version`을 선택합니다.
4. 설치된 Unreal Engine 5.7을 선택합니다.

### 경로 문제로 빌드가 실패합니다

경로에 한글, 공백, 특수문자가 있으면 일부 도구에서 문제가 생길 수 있습니다.

해결:

```text
C:\UnrealProjects\Pangaea573
F:\gameEngineering\Pangaea573
```

같은 단순한 영문 경로로 프로젝트를 옮긴 뒤 다시 프로젝트 파일을 생성하세요.

### UPawnSensingComponent deprecation 경고가 보입니다

UE 5.7.4에서 `UPawnSensingComponent`는 deprecated 상태입니다. 현재 수업 실습에서는 빌드가 가능하므로 경고로만 처리합니다.

향후 엔진 버전을 올릴 경우 AI Perception으로 교체하는 것이 좋습니다.

### Binaries, Intermediate, Saved 폴더가 생겼습니다

정상입니다. Unreal과 Visual Studio가 자동으로 만드는 빌드 산출물입니다.

이 폴더들은 Git에 올리지 않습니다.

## 13. Git 사용 시 주의사항

학생이 실습 내용을 Git으로 관리하는 경우 다음 파일과 폴더는 커밋하지 않습니다.

```text
Binaries/
DerivedDataCache/
Intermediate/
Saved/
.vs/
*.sln
*.VC.db
*.user
```

기본 `.gitignore`에 이미 반영되어 있습니다.

변경 내용을 확인하려면 다음 명령을 사용합니다.

```powershell
git status
```

## 14. 수업 배포 검증 상태

이 프로젝트는 다음 항목을 통과한 상태로 배포되었습니다.

- Visual Studio 프로젝트 파일 생성 성공
- `PangaeaEditor Win64 Development` 빌드 성공
- Blueprint 전체 컴파일 성공
- 에셋 설정 스크립트 재실행 성공

검증된 기준 버전:

```text
Unreal Engine 5.7.4
Visual Studio 2022
Windows 11
```
