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
