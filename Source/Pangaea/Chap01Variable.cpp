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
