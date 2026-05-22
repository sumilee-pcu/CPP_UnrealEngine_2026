#pragma once

#include "CoreMinimal.h"
#include "Components/ProgressBar.h"
#include "Blueprint/UserWidget.h"
#include "HealthBarWidget.generated.h"

UCLASS()
class PANGAEA_API UHealthBarWidget : public UUserWidget
{
	GENERATED_BODY()


public:
	UFUNCTION(BlueprintCallable)
	void SetHealthPercent(float Percent);

	UPROPERTY(VisibleAnywhere, BlueprintReadWrite, meta = (BindWidgetOptional))
		UProgressBar* HealthProgressBar;

protected:
	virtual void NativeConstruct() override;
};
