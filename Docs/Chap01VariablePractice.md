# Chap01Variable 실습 코드

이 문서는 `시작해요 Unreal` 도입부에서 사용하는 변수 실습 코드입니다. 교재의 `Chap01_Variable` 예제를 현재 저장소의 `Pangaea` 프로젝트에 맞게 바꾼 버전입니다.

## 목표

- C++ Actor 클래스를 만든다.
- `int32`, `float`, `FString` 변수를 선언한다.
- `UPROPERTY`로 변수를 Unreal Editor의 Details 패널에 노출한다.
- `BeginPlay()`에서 게임 실행 시점에 값이 바뀌는 것을 확인한다.

## 생성 파일

```text
Source/Pangaea/Chap01Variable.h
Source/Pangaea/Chap01Variable.cpp
```

## Chap01Variable.h

```cpp
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Chap01Variable.generated.h"

UCLASS()
class PANGAEA_API AChap01Variable : public AActor
{
	GENERATED_BODY()

public:
	AChap01Variable();

protected:
	virtual void BeginPlay() override;

public:
	virtual void Tick(float DeltaTime) override;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Variable")
	int32 IntValue1 = 0;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Variable")
	float FloatValue1 = 0.0f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Variable")
	FString StringValue1 = TEXT("Default");
};
```

## Chap01Variable.cpp

```cpp
#include "Chap01Variable.h"
#include "Engine/Engine.h"

AChap01Variable::AChap01Variable()
{
	PrimaryActorTick.bCanEverTick = true;
}

void AChap01Variable::BeginPlay()
{
	Super::BeginPlay();

	IntValue1 = 1024;
	FloatValue1 = 3.14f;
	StringValue1 = TEXT("언리얼");

	UE_LOG(LogTemp, Warning,
		TEXT("Int: %d / Float: %.2f / String: %s"),
		IntValue1, FloatValue1, *StringValue1);

	if (GEngine)
	{
		GEngine->AddOnScreenDebugMessage(
			-1,
			5.0f,
			FColor::Yellow,
			FString::Printf(TEXT("Int: %d, Float: %.2f, String: %s"),
				IntValue1, FloatValue1, *StringValue1));
	}
}

void AChap01Variable::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
}
```

## Unreal Editor에서 확인하기

1. Visual Studio에서 `PangaeaEditor`를 `Development Editor | Win64`로 빌드합니다.
2. Unreal Editor를 엽니다.
3. `Chap01Variable` 클래스를 부모로 하는 Blueprint를 만듭니다.
4. Blueprint 이름을 `BP_Chap01Variable`로 지정합니다.
5. `BP_Chap01Variable`을 Level에 배치합니다.
6. Details 패널의 `Variable` 카테고리를 확인합니다.
7. `IntValue1`, `FloatValue1`, `StringValue1` 값을 바꿔 봅니다.
8. Play를 누르고 화면 메시지와 Output Log를 확인합니다.

## 핵심 개념

```cpp
UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Variable")
```

- `EditAnywhere`: 에디터 Details 패널에서 수정할 수 있습니다.
- `BlueprintReadWrite`: Blueprint에서 읽고 쓸 수 있습니다.
- `Category`: Details 패널에서 표시될 묶음 이름입니다.

```cpp
void AChap01Variable::BeginPlay()
```

- Actor가 게임 월드에서 시작될 때 한 번 호출됩니다.
- Play 버튼을 눌렀을 때 코드가 실행되는 시점을 보여주기에 좋습니다.

```cpp
TEXT("언리얼")
```

- Unreal 문자열 리터럴 표기입니다.
- `FString`에 한글 문자열을 넣을 때도 이 형식을 사용합니다.
